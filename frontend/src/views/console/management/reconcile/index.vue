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
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="客户编码">
            <plain-text v-model="data.filterData.customer_code" clearable placeholder="" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <div class="toolbar">
      <el-button size="small" :loading="reconciling" @click="reconcileAll">计算对账</el-button>
    </div>

    <el-table :data="data.data" stripe v-loading="loading">
      <el-table-column prop="year" label="年" width="80" />
      <el-table-column prop="month" label="月" width="50" />
      <el-table-column prop="customer_code" label="客户编码" min-width="160" />
      <el-table-column prop="customer_name" label="客户名称" min-width="200" />
      <el-table-column prop="total_amount" label="账单金额" min-width="140" sortable />
      <el-table-column prop="wallet_paid_amount" label="钱包扣费" min-width="140" sortable />
      <el-table-column label="差额" min-width="120" sortable>
        <template #default="{ row }">
          <span :style="{ color: getDiffColor(row.diff) }">¥{{ row.diff.toFixed(2) }}</span>
        </template>
      </el-table-column>
    </el-table>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getMonthBillSummary, getWalletTransactions } from '@/api/console';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      year: null,
      month: null,
      customer_code: '',
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
    }),
    data: [],
  });

  const reconciling = ref(false);

  async function onLoad() {
    let resp = await waitRequest(
      loading,
      getMonthBillSummary({
        params: {
          ...data.filterData,
        },
      }),
    );
    data.data = (resp.data.data || []).map((r) => ({
      ...r,
      wallet_paid_amount: 0,
      diff: 0,
    }));
  }

  const reconcileAll = async () => {
    reconciling.value = true;
    try {
      for (const row of data.data) {
        await reconcileRow(row);
      }
    } finally {
      reconciling.value = false;
    }
  };

  const reconcileRow = async (row) => {
    let resp = await waitRequest(
      loading,
      getWalletTransactions({
        params: {
          customer_code: row.customer_code,
          page: 1,
          per_page: 200,
        },
      }),
    );
    const year = row.year;
    const month = row.month;
    const txs = resp.data.data || [];
    const paid = txs
      .filter((tx) => {
        if (tx.tx_type !== 'consume') return false;
        const dt = new Date(tx.create_time);
        return dt.getFullYear() === year && dt.getMonth() + 1 === month;
      })
      .reduce((sum, tx) => sum + Number(tx.change_amount || 0), 0);
    row.wallet_paid_amount = Math.abs(paid);
    row.diff = row.wallet_paid_amount - row.total_amount;
  };

  const getDiffColor = (diff) => {
    if (diff === 0) return '#16a34a';
    if (diff > 0) return '#eab308';
    return '#dc2626';
  };

  onMounted(async () => {
    emits('update-title', '对账中心');
    await onLoad();
  });
</script>

<style scoped>
  .toolbar {
    margin: 0 0 10px;
    text-align: right;
  }
</style>

