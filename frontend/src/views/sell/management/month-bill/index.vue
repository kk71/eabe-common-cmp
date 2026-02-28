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
          <el-form-item label="年份">
            <el-input-number v-model="data.filterData.year" :min="2000" :max="2100" controls-position="right" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="月份">
            <el-input-number v-model="data.filterData.month" :min="1" :max="12" controls-position="right" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="year" label="年" width="80" />
      <el-table-column prop="month" label="月" width="50" />
      <el-table-column prop="customer_code" label="客户编码" min-width="160" />
      <el-table-column prop="customer_name" label="客户名称" min-width="200" />
      <el-table-column prop="rent_amount" label="月租费" min-width="120" sortable />
      <el-table-column prop="token_amount" label="Token使用费" min-width="140" sortable />
      <el-table-column prop="other_amount" label="其他一次性费用" min-width="160" sortable />
      <el-table-column prop="total_amount" label="当月总费用" min-width="150" sortable />

      <el-table-column label="操作" width="140" fixed="right">
        <template #default="{ row }">
          <el-button type="primary" link size="small" @click="openDetail(row)">查看明细</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="detailDialog.visible" :title="`账单明细 - ${detailDialog.title}`" width="900px">
      <el-table :data="detailDialog.items" stripe>
        <el-table-column prop="product_name" label="商品名" min-width="200" />
        <el-table-column prop="account_code" label="订购帐号名" min-width="120" />
        <table-column-smv label="产品系列" prop="product_type" flag="product-type" min-width="140" />
        <el-table-column prop="resource_code" label="资源编号" min-width="200" />
        <el-table-column prop="amount" label="用量" min-width="100" />
        <table-column-smv label="出账类型" prop="settlement_type" flag="bill-settlement-type" min-width="100" />
        <el-table-column prop="homepage_price" label="官网价" min-width="120" />
        <el-table-column prop="discount_price" label="折扣价" min-width="100" />
        <el-table-column prop="total_paid" label="实付金额" min-width="120" />
      </el-table>
      <template #footer>
        <el-button @click="detailDialog.visible = false">关闭</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getMonthBillSummary } from '@/api/sell';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const router = useRouter();

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      year: null,
      month: null,
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
    }),
    data: [],
  });

  const detailDialog = reactive({
    visible: false,
    title: '',
    items: [],
  });

  async function onLoad() {
    let resp = await waitRequest(
      loading,
      getMonthBillSummary({
        params: {
          ...data.filterData,
        },
      }),
    );
    data.data = resp.data.data;
  }

  const openDetail = (row) => {
    detailDialog.title = `${row.year}-${String(row.month).padStart(2, '0')} / ${row.customer_name || row.customer_code}`;
    detailDialog.items = row.items || [];
    detailDialog.visible = true;
  };

  onMounted(async () => {
    emits('update-title', '月度账单');
    await onLoad();
  });
</script>
