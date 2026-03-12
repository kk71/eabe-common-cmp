<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <el-form ref="form" :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
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
      <el-table-column prop="name" label="名称" min-width="200" />
      <el-table-column label="操作" width="220" fixed="right">
        <template #default="{ row }">
          <el-tooltip content="编辑" placement="top" effect="light">
            <el-button type="success" :icon="Edit" size="small" @click="gotoDetail(row)" />
          </el-tooltip>
          <el-tooltip content="删除" placement="top" effect="light">
            <el-button type="danger" :icon="Delete" size="small" @click="gotoDelete(row)" />
          </el-tooltip>
        </template>
      </el-table-column>
    </el-table>
    <role-drawer ref="roleDrawer" />
  </filterable-list-frame>
</template>

<script setup>
  import { Edit, Delete } from '@element-plus/icons-vue';
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { confirmBox } from '@/utils/msgbox';
  import { getRole, deleteRole } from '@/api/system';
  import RoleDrawer from './components/role-drawer.vue';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = useTemplateRef('listTable');

  const roleDrawer = useTemplateRef('roleDrawer');

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0, total: 0 },
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
      getRole({
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
    await roleDrawer.value.showAdd();
    await onLoad();
  };

  const gotoDetail = async (role) => {
    await roleDrawer.value.show(role.id);
    await onLoad();
  };

  const gotoDelete = async (user) => {
    if (await confirmBox('确认删除吗？')) {
      if (!user.id) {
        await deleteRole({ params: { id__in: selectedIds.value.toString() } });
      } else {
        await deleteRole({ params: { id: user.id } });
      }
      await onLoad();
    }
  };

  onMounted(async () => {
    emits('update-title', '角色');
    await onLoad();
  });
</script>
