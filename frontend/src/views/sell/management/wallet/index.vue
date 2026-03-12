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
          <el-form-item label="客户编码">
            <plain-text v-model="data.filterData.customer_code" clearable placeholder="" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="customer_code" label="客户编码" min-width="160" />
      <el-table-column prop="customer_name" label="客户名称" min-width="160" />
      <el-table-column prop="balance" label="可用余额" min-width="120" sortable />
      <el-table-column prop="frozen_balance" label="冻结余额" min-width="120" sortable />
      <el-table-column prop="total_recharge" label="累计充值" min-width="150" sortable />
      <el-table-column prop="currency" label="币种" width="80" />
      <el-table-column prop="create_time" label="创建时间" min-width="180" />
      <el-table-column label="操作" width="140" fixed="right">
        <template #default="{ row }">
          <el-button type="primary" link size="small" @click="openTxDialog(row)">查看流水</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-dialog v-model="txDialog.visible" :title="`钱包流水 - ${txDialog.customerLabel}`" width="800px">
      <el-table :data="txDialog.data" v-loading="loading" stripe>
        <el-table-column prop="tx_id" label="流水编号" min-width="200" />
        <el-table-column prop="tx_type" label="类型" min-width="80" />
        <el-table-column prop="change_amount" label="变动金额" min-width="120" />
        <el-table-column prop="balance_after" label="变动后余额" min-width="120" />
        <el-table-column prop="related_order_id" label="订单号" min-width="150" />
        <el-table-column prop="remark" label="备注" min-width="180" />
        <el-table-column prop="create_time" label="时间" min-width="180" />
      </el-table>
      <template #footer>
        <el-button @click="txDialog.visible = false">关闭</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getWalletAccounts, getWalletTransactions } from '@/api/sell';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      customer_code: '',
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
    }),
    data: [],
  });

  const txDialog = reactive({
    visible: false,
    customerLabel: '',
    customer_code: '',
    data: [],
  });

  const openTxDialog = async (row) => {
    txDialog.customer_code = row.customer_code;
    txDialog.customerLabel = row.customer_name || row.customer_code;
    txDialog.visible = true;
    await loadTransactions();
  };

  async function onLoad() {
    const resp = await waitRequest(
      loading,
      getWalletAccounts({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  }

  async function loadTransactions() {
    if (!txDialog.customer_code) return;
    const resp = await waitRequest(
      loading,
      getWalletTransactions({
        params: {
          customer_code: txDialog.customer_code,
          page: 1,
          per_page: 50,
        },
      }),
    );
    txDialog.data = resp.data.data;
  }

  onMounted(async () => {
    emits('update-title', '钱包中心');
    await onLoad();
  });
</script>

