<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <el-drawer v-model="data.showErrorDrawer" size="40%" append-to-body title="错误信息">
      <el-form label-position="right" label-width="70px">
        <el-form-item label="类型">
          <div class="row-center gap">
            <plain-text v-model="data.targetShowError.task_type" :editable="false" />
            <csm v-model="data.targetShowError.status" flag="celery-task-status" :editable="false" />
          </div>
        </el-form-item>
        <el-form-item label="描述">
          <plain-text v-model="data.targetShowError.task_description" :editable="false" />
        </el-form-item>
        <el-form-item label="错误信息" label-position="top">
          <el-scrollbar>
            <pre>{{ data.targetShowError.error_info }}</pre>
          </el-scrollbar>
        </el-form-item>
      </el-form>
    </el-drawer>

    <el-form ref="form" :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="搜索">
            <plain-text v-model="data.filterData.keyword" clearable placeholder="" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="状态">
            <csm v-model="data.filterData.status" flag="celery-task-status" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <table-column-smv flag="celery-task-status" prop="status" label="状态" width="100" />
      <el-table-column prop="task_type" label="任务类型" min-width="200" />
      <el-table-column prop="task_description" label="描述" min-width="300" />
      <table-column-dt prop="start_time" label="开始时间" width="200" />
      <table-column-dt prop="end_time" label="终止时间" width="200" />
      <el-table-column prop="error_info" label="错误信息" width="100">
        <template #default="{ row }">
          <el-button v-if="row.error_info" type="primary" size="small" @click="showError(row)">详情</el-button>
          <span v-else>-</span>
        </template>
      </el-table-column>
    </el-table>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getCeleryTaskRecord } from '@/api/system';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const router = useRouter();

  const listTable = ref(null);

  const data = reactive({
    p: { page: 1, per_page: 10, pages: 0 },
    filterData: {
      keyword: '',
      status: null,
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
      keyword: String,
    }),
    data: [],
    // 当前用于展示错误信息抽屉的任务
    targetShowError: null,
    // 是否展示错误信息抽屉
    showErrorDrawer: false,
  });

  const showError = (row) => {
    data.targetShowError = row;
    data.showErrorDrawer = true;
  };

  const onLoad = async () => {
    let resp = await waitRequest(
      loading,
      getCeleryTaskRecord({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  };

  onMounted(async () => {
    emits('update-title', '异步任务日志');
    await onLoad();
  });
</script>
