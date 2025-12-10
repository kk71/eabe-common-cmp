<template>
  <filterable-list-frame
    v-model:filterData="data.filterData"
    v-model:pagination="data.p"
    :filter-data-typing="data.filterDataTyping"
    @filter-changed="onLoad"
  >
    <el-form ref="form" :model="data.filterData" class="filter-box" label-position="right" label-width="70px">
      <el-row :gutter="10">
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="搜索">
            <plain-text v-model="data.filterData.keyword" clearable placeholder="" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="产品类型">
            <csm v-model="data.filterData.product_type" flag="product-type" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="订单状态">
            <csm v-model="data.filterData.status" flag="order-status" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="区域">
            <csm v-model="data.filterData.origin" flag="order-origin" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="order_id" label="订单编号" min-width="200" />
      <el-table-column prop="batch_code" label="批次" min-width="200" />
      <el-table-column label="产品" prop="product_name" min-width="160" />
      <el-table-column prop="resource_code" label="资源编号" min-width="200" />
      <el-table-column prop="order_guanxi_id" label="订购关系ID" min-width="120" />
      <table-column-smv label="区域" prop="origin" flag="order-origin" min-width="140" />
      <table-column-smv label="订单类型" prop="product_type" flag="product-type" min-width="140" />
      <table-column-dt prop="order_date" label="下单日期" min-width="120" type="date" />
      <table-column-smv label="状态" prop="status" flag="order-status" min-width="140" />
      <el-table-column prop="total_price" label="总金额" min-width="150" sortable />

      <el-table-column v-if="false" label="操作" width="120" fixed="right">
        <template #default="{ row }">
          <el-button type="primary" size="small" @click="gotoDetail(row)">详情</el-button>
        </template>
      </el-table-column>
    </el-table>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getOrders } from '@/api/console';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      keyword: '',
      product_type: null,
      order_type: null,
      status: null,
      origin: null,
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
      keyword: String,
    }),
    data: [],
  });

  async function onLoad() {
    let resp = await waitRequest(
      loading,
      getOrders({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  }

  onMounted(async () => {
    emits('update-title', '订单管理');
    await onLoad();
  });
</script>
