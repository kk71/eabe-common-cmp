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
            <plain-text v-model="data.filterData.keyword" clearable placeholder="客户编码 / 名称" />
          </el-form-item>
        </el-col>
        <el-col :xs="24" :sm="12" :md="12" :lg="8" :xl="4">
          <el-form-item label="客户编码">
            <plain-text v-model="data.filterData.customer_code" clearable placeholder="" />
          </el-form-item>
        </el-col>
      </el-row>
    </el-form>

    <el-space style="margin-bottom: 10px">
      <el-button type="primary" @click="openRechargeDialog">充值</el-button>
      <el-button @click="openSetBalanceDialog">设置余额</el-button>
      <el-button @click="importDialog.visible = true">导入扣费记录</el-button>
    </el-space>

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

    <el-dialog v-model="rechargeDialog.visible" title="钱包充值" width="400px">
      <el-form ref="rechargeFormRef" :model="rechargeDialog.form" :rules="rechargeDialog.rules" label-width="80px">
        <el-form-item label="客户" prop="customer_code">
          <customer-selector v-model="rechargeDialog.form.customer_code" v-model:customerName="rechargeDialog.form.customer_name" />
        </el-form-item>
        <el-form-item label="金额" prop="amount">
          <el-input-number v-model="rechargeDialog.form.amount" :min="0.01" :step="0.01" :precision="2" />
        </el-form-item>
        <el-form-item label="备注">
          <plain-text v-model="rechargeDialog.form.remark" type="textarea" clearable />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="rechargeDialog.visible = false">取消</el-button>
        <el-button type="primary" @click="doRecharge">确定</el-button>
      </template>
    </el-dialog>

    <el-dialog v-model="setBalanceDialog.visible" title="设置钱包余额" width="420px">
      <el-alert type="warning" show-icon :closable="false" style="margin-bottom: 10px">
        <template #title>该操作会自动生成一条“充值/调整”流水用于对账</template>
      </el-alert>
      <el-form ref="setBalanceFormRef" :model="setBalanceDialog.form" :rules="setBalanceDialog.rules" label-width="90px">
        <el-form-item label="客户" prop="customer_code">
          <customer-selector v-model="setBalanceDialog.form.customer_code" v-model:customerName="setBalanceDialog.form.customer_name" />
        </el-form-item>
        <el-form-item label="目标余额" prop="balance">
          <el-input-number v-model="setBalanceDialog.form.balance" :min="0" :step="0.01" :precision="2" />
        </el-form-item>
        <el-form-item label="备注">
          <plain-text v-model="setBalanceDialog.form.remark" type="textarea" clearable />
        </el-form-item>
      </el-form>
      <template #footer>
        <el-button @click="setBalanceDialog.visible = false">取消</el-button>
        <el-button type="primary" @click="doSetBalance">确定</el-button>
      </template>
    </el-dialog>

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

    <el-dialog v-model="importDialog.visible" title="导入扣费记录（CSV / Excel）" width="760px">
      <el-alert type="info" show-icon :closable="false" style="margin-bottom: 10px">
        <template #title>
          支持流量/短信/token 费用扣费记录导入。建议字段顺序：time, customer_code, customer_name, cost_type, amount, remark
        </template>
      </el-alert>
      <el-form :model="importDialog.form" label-width="140px" style="margin-bottom: 10px">
        <el-form-item label="同步更新钱包余额">
          <el-switch v-model="importDialog.form.apply_to_balance" />
        </el-form-item>
        <el-form-item v-if="importDialog.form.apply_to_balance" label="允许余额为负">
          <el-switch v-model="importDialog.form.allow_negative_balance" />
        </el-form-item>
      </el-form>
      <el-upload
        drag
        :auto-upload="false"
        :limit="1"
        accept=".csv,.xlsx"
        :on-change="onImportFileChange"
        :on-remove="onImportFileRemove"
      >
        <el-icon class="el-icon--upload"><upload-filled /></el-icon>
        <div class="el-upload__text">拖拽文件到此处，或 <em>点击选择</em></div>
        <template #tip>
          <div class="el-upload__tip">支持 .csv / .xlsx，首行表头会自动跳过</div>
        </template>
      </el-upload>
      <template #footer>
        <el-button @click="importDialog.visible = false">取消</el-button>
        <el-button type="primary" :disabled="!importDialog.file" @click="doImportTx">导入</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getWalletAccounts, getWalletTransactions, rechargeWallet, setWalletBalance, importWalletTransactionsFile } from '@/api/console';
  import { UploadFilled } from '@element-plus/icons-vue';
  import CustomerSelector from '@/views/console/components/customer-selector.vue';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);
  const rechargeFormRef = ref(null);
  const setBalanceFormRef = ref(null);

  const data = reactive({
    p: { page: 1, per_page: 20, pages: 0 },
    filterData: {
      keyword: '',
      customer_code: '',
    },
    filterDataTyping: new QSValidator({
      page: Number,
      per_page: Number,
    }),
    data: [],
  });

  const rechargeDialog = reactive({
    visible: false,
    form: {
      customer_code: '',
      customer_name: '',
      amount: 0,
      remark: '',
    },
    rules: {
      customer_code: [{ required: true, message: '请选择客户', trigger: 'change' }],
      amount: [{ required: true, message: '请输入金额', trigger: 'change' }],
    },
  });

  const setBalanceDialog = reactive({
    visible: false,
    form: {
      customer_code: '',
      customer_name: '',
      balance: 0,
      remark: '',
    },
    rules: {
      customer_code: [{ required: true, message: '请选择客户', trigger: 'change' }],
      balance: [{ required: true, message: '请输入目标余额', trigger: 'change' }],
    },
  });

  const txDialog = reactive({
    visible: false,
    customerLabel: '',
    customer_code: '',
    data: [],
  });

  const importDialog = reactive({
    visible: false,
    file: null,
    form: {
      apply_to_balance: false,
      allow_negative_balance: true,
    },
  });

  const openRechargeDialog = () => {
    const selection = listTable.value?.getSelectionRows?.() || [];
    if (selection.length === 1) {
      rechargeDialog.form.customer_code = selection[0].customer_code;
      rechargeDialog.form.customer_name = selection[0].customer_name || '';
    }
    rechargeDialog.visible = true;
  };

  const openSetBalanceDialog = () => {
    const selection = listTable.value?.getSelectionRows?.() || [];
    if (selection.length === 1) {
      setBalanceDialog.form.customer_code = selection[0].customer_code;
      setBalanceDialog.form.customer_name = selection[0].customer_name || '';
      setBalanceDialog.form.balance = Number(selection[0].balance || 0);
    }
    setBalanceDialog.visible = true;
  };

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

  const doRecharge = async () => {
    const ok = await rechargeFormRef.value?.validate?.().catch(() => false);
    if (!ok) return;
    await waitRequest(
      loading,
      rechargeWallet({
        data: {
          ...rechargeDialog.form,
        },
      }),
    );
    rechargeDialog.visible = false;
    await onLoad();
  };

  const doSetBalance = async () => {
    const ok = await setBalanceFormRef.value?.validate?.().catch(() => false);
    if (!ok) return;
    await waitRequest(
      loading,
      setWalletBalance({
        data: {
          ...setBalanceDialog.form,
        },
      }),
    );
    setBalanceDialog.visible = false;
    await onLoad();
  };

  const doImportTx = async () => {
    if (!importDialog.file) return;
    const fd = new FormData();
    fd.append('file', importDialog.file);
    fd.append('skip_header', 'true');
    fd.append('apply_to_balance', String(importDialog.form.apply_to_balance));
    fd.append('allow_negative_balance', String(importDialog.form.allow_negative_balance));
    await waitRequest(
      loading,
      importWalletTransactionsFile({
        data: fd,
        headers: { 'Content-Type': 'multipart/form-data' },
      }),
    );
    importDialog.visible = false;
    importDialog.file = null;
    await onLoad();
  };

  const onImportFileChange = (uploadFile) => {
    importDialog.file = uploadFile?.raw || null;
  };
  const onImportFileRemove = () => {
    importDialog.file = null;
  };

  onMounted(async () => {
    emits('update-title', '财务资金管理');
    await onLoad();
  });
</script>

