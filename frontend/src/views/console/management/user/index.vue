<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <user-dialog ref="userDialog" />

    <user-password-dialog ref="userPasswordDialog" />

    <el-form ref="form" :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="搜索">
            <plain-text v-model="data.filterData.keyword" clearable placeholder="用户名/昵称" />
          </el-form-item>
        </el-col>
      </el-row>
      <el-row class="button-bar">
        <el-button plain type="primary" @click="gotoAdd">创建</el-button>
        <el-button plain type="danger" @click="gotoDelete" :disabled="data.bulkDeletionDisabled">批量删除</el-button>
      </el-row>
    </el-form>

    <el-table
      ref="listTable"
      :data="data.data"
      stripe
      v-loading="loading"
      @selection-change="
        () => {
          data.bulkDeletionDisabled = listTable.getSelectionRows().length == 0;
        }
      "
    >
      <el-table-column type="selection" />
      <el-table-column prop="avatar_thumb" label="头像" width="80">
        <template #default="{ row }">
          <el-avatar :src="row.avatar" :size="40" />
        </template>
      </el-table-column>
      <el-table-column prop="name" label="昵称" min-width="200" />
      <el-table-column prop="login_name" label="密码登录名" min-width="100" />
      <el-table-column label="角色" min-width="100">
        <template #default="{ row }">
          <role-selector v-model="row.role_ids" multiple :editable="false" />
        </template>
      </el-table-column>
      <table-column-boolean prop="is_admin" label="管理员" width="100" />
      <table-column-boolean prop="disabled" label="禁用" width="100" />
      <el-table-column label="操作" width="220" fixed="right">
        <template #default="{ row }">
          <el-tooltip content="编辑" placement="top" effect="light">
            <el-button type="success" :icon="Edit" size="small" @click="gotoDetail(row)" />
          </el-tooltip>
          <el-button type="warning" size="small" @click="gotoChangePassword(row)">修改密码</el-button>
          <el-tooltip content="删除" placement="top" effect="light">
            <el-button type="danger" :icon="Delete" size="small" @click="gotoDelete(row)" />
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
  </filterable-list-frame>
</template>

<script setup>
  import { Edit, Delete } from '@element-plus/icons-vue';
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { confirmBox } from '@/utils/msgbox';
  import { getUser, deleteUser } from '@/api/system'; // 需要创建对应的API
  import UserDialog from './components/user-dialog.vue';
  import UserPasswordDialog from './components/user-password-dialog.vue';
  import RoleSelector from '@/views/console/management/role/components/role-selector.vue';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const userDialog = useTemplateRef('userDialog');

  const userPasswordDialog = useTemplateRef('userPasswordDialog');

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      keyword: '',
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
      keyword: String,
    }),
    data: [],
    bulkDeletionDisabled: true,
  });

  const onLoad = async () => {
    const resp = await waitRequest(
      loading,
      getUser({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  };

  const selectedIds = computed(() => {
    return listTable.value.getSelectionRows().map((i) => i.id);
  });

  const gotoAdd = async () => {
    await userDialog.value.showAdd();
    data.p.page = 1;
    await onLoad();
  };

  const gotoDetail = async (user) => {
    await userDialog.value.show(user.id);
    await onLoad();
  };

  const gotoChangePassword = async (user) => {
    await userPasswordDialog.value.show(user.id);
  };

  const gotoDelete = async (user) => {
    if (await confirmBox('确认删除吗？')) {
      if (!user.id) {
        await deleteUser({ params: { id__in: selectedIds.value.toString() } });
      } else {
        await deleteUser({ params: { id: user.id } });
      }
      await onLoad();
    }
  };

  onMounted(async () => {
    emits('update-title', '用户');
    await onLoad();
  });
</script>
