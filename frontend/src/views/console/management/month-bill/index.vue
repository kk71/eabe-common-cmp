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
          <el-form-item label="出账类型">
            <csm v-model="data.filterData.settlement_type" flag="bill-settlement-type" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="year" label="年" width="80" />
      <el-table-column prop="month" label="月" width="50" />
      <el-table-column prop="product_name" label="商品名" min-width="200" />
      <el-table-column prop="customer_code" label="客户编码" min-width="200" />
      <el-table-column prop="customer_name" label="客户名称" min-width="200" />
      <el-table-column prop="account_code" label="订购帐号名" min-width="120" />
      <table-column-smv label="产品系列" prop="product_type" flag="product-type" min-width="140" />
      <el-table-column prop="resource_code" label="资源编号" min-width="200" />
      <el-table-column prop="amount" label="用量" min-width="120" />
      <table-column-smv label="出账类型" prop="settlement_type" flag="bill-settlement-type" min-width="100" />
      <el-table-column prop="homepage_price" label="官网价" min-width="150" sortable />
      <el-table-column prop="discount_price" label="折扣价" min-width="100" sortable />
      <el-table-column prop="total_paid" label="实付金额" min-width="150" sortable />

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
  import { getMonthBills } from '@/api/console';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      keyword: '',
      product_type: null,
      settlement_type: null,
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
    }),
    data: [],
  });

  async function onLoad() {
    let resp = await waitRequest(
      loading,
      getMonthBills({
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
    emits('update-title', '月度账单');
    await onLoad();
  });
</script>
