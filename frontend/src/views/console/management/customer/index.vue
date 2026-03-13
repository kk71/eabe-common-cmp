<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <el-form :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="搜索">
            <plain-text v-model="data.filterData.keyword" clearable placeholder="客户名/电话/负责人" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row class="button-bar">
        <el-button plain type="primary" @click="openAdd">创建</el-button>
      </el-row>
    </el-form>

    <el-table :data="data.data" stripe v-loading="loading">
      <el-table-column prop="id" label="ID" width="90" />
      <el-table-column prop="code" label="客户编号" min-width="140" />
      <el-table-column prop="name" label="客户名" min-width="180" />
      <el-table-column prop="contact_phone" label="联系电话" min-width="140" />
      <el-table-column prop="principal" label="主要负责人" min-width="140" />
      <el-table-column label="关联用户" min-width="240">
        <template #default="{ row }">
          <el-popover
            v-for="uid in row.user_ids || []"
            :key="uid"
            placement="top"
            trigger="hover"
            :width="260"
          >
            <div style="line-height: 20px">
              <div><span style="color: #86909c">用户ID：</span>{{ uid }}</div>
              <div><span style="color: #86909c">昵称：</span>{{ userMap[uid]?.name || '-' }}</div>
            </div>
            <template #reference>
              <el-tag style="margin-right: 6px" type="info">
                {{ userMap[uid]?.login_name || uid }}
              </el-tag>
            </template>
          </el-popover>
        </template>
      </el-table-column>
      <table-column-dt prop="create_time" label="创建时间" min-width="180" />
      <el-table-column label="操作" width="180" fixed="right">
        <template #default="{ row }">
          <el-tooltip content="编辑" placement="top" effect="light">
            <el-button type="success" :icon="Edit" size="small" @click="openEdit(row)" />
          </el-tooltip>
          <el-tooltip content="删除" placement="top" effect="light">
            <el-button type="danger" :icon="Delete" size="small" @click="doDelete(row)" />
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="dialog.visible" :title="dialog.isEdit ? '编辑客户' : '创建客户'" width="520px">
      <el-form ref="dialogFormRef" :model="dialog.form" :rules="dialog.rules" label-width="90px">
        <el-form-item label="客户编号" prop="code">
          <plain-text v-model="dialog.form.code" clearable placeholder="用于导入数据的唯一标识" />
        </el-form-item>
        <el-form-item label="客户名" prop="name">
          <plain-text v-model="dialog.form.name" clearable />
        </el-form-item>
        <el-form-item label="联系电话">
          <plain-text v-model="dialog.form.contact_phone" clearable />
        </el-form-item>
        <el-form-item label="主要负责人">
          <plain-text v-model="dialog.form.principal" clearable />
        </el-form-item>
        <el-form-item label="备注">
          <plain-text v-model="dialog.form.remark" type="textarea" clearable />
        </el-form-item>
        <el-form-item label="关联用户" prop="user_ids">
          <user-selector v-model="dialog.form.user_ids" multiple />
          <div style="margin-top: 6px; color: #86909c; font-size: 12px">仅允许绑定非管理员用户</div>
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="dialog.visible = false">取消</el-button>
        <el-button type="primary" @click="doSave">确定</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup lang="ts">
  import { Edit, Delete } from '@element-plus/icons-vue';
  import { inject, nextTick, onMounted, reactive, ref } from 'vue';
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { confirmBox } from '@/utils/msgbox';
  import { getCustomers, createCustomer, updateCustomer, deleteCustomer, getCustomerDetail } from '@/api/console';
  import { getUser } from '@/api/system';
  import UserSelector from '@/views/console/components/user-selector.vue';

  const emits = defineEmits(['update-title']);
  const loading: any = inject('loading');
  const dialogFormRef = ref<any>(null);

  const userLoading = ref(false);
  const userMap = reactive<Record<string, { id: string; name?: string | null; login_name?: string | null }>>({});

  const data = reactive<any>({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: { keyword: '' },
    filterDataTyping: new QSValidator({ page: Number, per_page: Number, keyword: String }),
    data: [],
  });

  const ensureUsersLoaded = async (ids: string[]) => {
    const uniq = Array.from(new Set((ids || []).filter((i) => !!i)));
    const missing = uniq.filter((id) => !userMap[id]);
    if (!missing.length) return;
    for (const id of missing) {
      const resp = await waitRequest(
        userLoading,
        getUser({
          params: {
            id,
            include_disabled: true,
            per_page: 1,
          },
        }),
      );
      const u = (resp.data.data || [])[0];
      if (u) {
        userMap[id] = { id: u.id, name: u.name, login_name: u.login_name };
      } else {
        userMap[id] = { id };
      }
    }
  };

  const dialog = reactive<any>({
    visible: false,
    isEdit: false,
    id: null,
    form: {
      code: '',
      name: '',
      contact_phone: '',
      principal: '',
      remark: '',
      user_ids: [],
    },
    rules: {
      code: [
        { required: true, message: '请输入客户编号', trigger: ['blur', 'change'] },
        {
          validator: (_: any, v: any, cb: any) => {
            const s = String(v ?? '').trim();
            if (!s) return cb(new Error('请输入客户编号'));
            cb();
          },
          trigger: ['blur', 'change'],
        },
      ],
      name: [
        { required: true, message: '请输入客户名', trigger: ['blur', 'change'] },
        {
          validator: (_: any, v: any, cb: any) => {
            const s = String(v ?? '').trim();
            if (!s) return cb(new Error('请输入客户名'));
            cb();
          },
          trigger: ['blur', 'change'],
        },
      ],
      user_ids: [
        {
          validator: (_: any, v: any, cb: any) => {
            const arr = Array.isArray(v) ? v : [];
            if (arr.length < 1) return cb(new Error('请至少选择 1 个关联用户'));
            cb();
          },
          trigger: 'change',
        },
      ],
    },
  });

  async function onLoad() {
    const resp = await waitRequest(
      loading,
      getCustomers({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    const r: any = resp.data as any;
    data.p = r.pagination;
    data.data = r.data;
    const allUserIds = (data.data || []).flatMap((c: any) => c?.user_ids || []);
    await ensureUsersLoaded(allUserIds);
  }

  const openAdd = () => {
    dialog.visible = true;
    dialog.isEdit = false;
    dialog.id = null;
    dialog.form = { code: '', name: '', contact_phone: '', principal: '', remark: '', user_ids: [] };
    dialogFormRef.value?.clearValidate?.();
  };

  const openEdit = async (row: any) => {
    const resp = await waitRequest(loading, getCustomerDetail({ params: { id: row.id } }));
    const c = resp.data.data;
    dialog.visible = true;
    dialog.isEdit = true;
    dialog.id = c.id;
    dialog.form = {
      code: c.code || '',
      name: c.name || '',
      contact_phone: c.contact_phone || '',
      principal: c.principal || '',
      remark: c.remark || '',
      user_ids: c.user_ids || [],
    };
    await nextTick();
    dialogFormRef.value?.clearValidate?.();
  };

  const doSave = async () => {
    const ok = await dialogFormRef.value?.validate?.().catch(() => false);
    if (!ok) return;
    const payload = {
      code: String(dialog.form.code || '').trim(),
      name: String(dialog.form.name || '').trim(),
      contact_phone: dialog.form.contact_phone || null,
      principal: dialog.form.principal || null,
      remark: dialog.form.remark || null,
      user_ids: dialog.form.user_ids || [],
    };
    if (dialog.isEdit) {
      await waitRequest(loading, updateCustomer({ params: { id: dialog.id }, data: payload }));
    } else {
      await waitRequest(loading, createCustomer({ data: payload }));
    }
    dialog.visible = false;
    await onLoad();
  };

  const doDelete = async (row: any) => {
    if (await confirmBox('确认删除该客户吗？（会自动解绑关联用户，并将关联用户标记为禁用）')) {
      await waitRequest(loading, deleteCustomer({ params: { id: row.id } }));
      await onLoad();
    }
  };

  onMounted(async () => {
    emits('update-title', '客户');
    await onLoad();
  });
</script>

