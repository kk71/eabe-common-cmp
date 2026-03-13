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

    <el-space style="margin-bottom: 10px">
      <el-button type="primary" @click="onLoad">查询账单</el-button>
      <el-button @click="exportSummaryCsv">导出汇总</el-button>
      <el-button @click="importDialog.visible = true">导入账单</el-button>
      <el-button @click="downloadImportTemplate">下载模板</el-button>
    </el-space>

    <el-table ref="listTable" :data="data.data" stripe v-loading="loading">
      <el-table-column type="selection" width="50" />
      <el-table-column prop="year" label="年" width="80" />
      <el-table-column prop="month" label="月" width="60" />
      <el-table-column label="客户名称" min-width="160">
        <template #default="{ row }">
          <el-tooltip
            v-if="(row.customer_code || '').trim()"
            effect="dark"
            :content="`客户编码：${(row.customer_code || '').trim()}`"
            placement="top"
          >
            <span>{{ row.customer_name || '-' }}</span>
          </el-tooltip>
          <span v-else>{{ row.customer_name || '-' }}</span>
        </template>
      </el-table-column>
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
      <div class="detail-header">
        <div class="detail-summary">
          <span>当月总费用：¥{{ detailDialog.total_amount.toFixed(2) }}</span>
          <span>钱包扣费金额：¥{{ detailDialog.wallet_paid_amount.toFixed(2) }}</span>
          <span>差额：¥{{ (detailDialog.wallet_paid_amount - detailDialog.total_amount).toFixed(2) }}</span>
        </div>
        <el-button size="small" @click="exportDetailCsv">导出明细CSV</el-button>
      </div>
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

      <el-dialog v-model="importDialog.visible" title="导入月度账单（CSV / Excel）" width="820px">
      <el-alert type="info" show-icon :closable="false" style="margin-bottom: 10px">
      <template #title>
          选择 CSV 或 Excel(xlsx) 上传，用于生成账单与后续按月扣费。字段顺序：
          账期(YYYYMM)、商品名称、客户编码、订购账号名称、产品系列、资源编号、用量、出账类型、官网价格、优惠价格、实付金额
        </template>
      </el-alert>
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
        <el-button type="primary" :disabled="!importDialog.file" @click="doImportMonthBills">导入</el-button>
      </template>
    </el-dialog>
  </filterable-list-frame>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { QSValidator } from '@/utils/router';
  import { getMonthBillSummary, getWalletTransactions, importMonthBillsFile } from '@/api/console';
  import { UploadFilled } from '@element-plus/icons-vue';

  const emits = defineEmits(['update-title']);

  const loading = inject('loading');

  const listTable = ref(null);

  const router = useRouter();

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

  const detailDialog = reactive({
    visible: false,
    title: '',
    items: [],
    total_amount: 0,
    wallet_paid_amount: 0,
  });

  const importDialog = reactive({
    visible: false,
    file: null,
  });

  async function onLoad() {
    const resp = await waitRequest(
      loading,
      getMonthBillSummary({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.p = resp.data.pagination;
    data.data = resp.data.data;
  }

  const doImportMonthBills = async () => {
    if (!importDialog.file) return;
    const fd = new FormData();
    fd.append('file', importDialog.file);
    fd.append('skip_header', 'true');
    await waitRequest(
      loading,
      importMonthBillsFile({
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

  const openDetail = async (row) => {
    detailDialog.title = `${row.year}-${String(row.month).padStart(2, '0')} / ${row.customer_name || row.customer_code}`;
    detailDialog.items = row.items || [];
    detailDialog.total_amount = row.total_amount || 0;
    await loadWalletForBill(row);
    detailDialog.visible = true;
  };

  const loadWalletForBill = async (row) => {
    const resp = await waitRequest(
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
    detailDialog.wallet_paid_amount = Math.abs(paid);
  };

  const exportSummaryCsv = () => {
    const headers = ['year', 'month', 'customer_code', 'customer_name', 'rent_amount', 'token_amount', 'other_amount', 'total_amount'];
    const rows = data.data.map((r) =>
      [r.year, r.month, r.customer_code, r.customer_name, r.rent_amount, r.token_amount, r.other_amount, r.total_amount].join(','),
    );
    downloadCsv('month-bill-summary.csv', [headers.join(','), ...rows].join('\n'));
  };

  const exportDetailCsv = () => {
    const headers = [
      'product_name',
      'account_code',
      'product_type',
      'resource_code',
      'amount',
      'settlement_type',
      'homepage_price',
      'discount_price',
      'total_paid',
    ];
    const rows = detailDialog.items.map((i) =>
      [
        i.product_name,
        i.account_code,
        i.product_type,
        i.resource_code,
        i.amount,
        i.settlement_type,
        i.homepage_price,
        i.discount_price,
        i.total_paid,
      ].join(','),
    );
    downloadCsv('month-bill-detail.csv', [headers.join(','), ...rows].join('\n'));
  };

  const downloadCsv = (filename, content) => {
    const blob = new Blob(['\ufeff' + content], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.setAttribute('download', filename);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url);
  };

  const downloadImportTemplate = () => {
    const base = import.meta.env.BASE_URL || '/';
    const url = `${base.replace(/\/+$/, '/')}templates/month_bill_import_template.xlsx`;
    const a = document.createElement('a');
    a.href = url;
    a.download = 'month_bill_import_template.xlsx';
    document.body.appendChild(a);
    a.click();
    a.remove();
  };

  onMounted(async () => {
    emits('update-title', '月度账单');
    await onLoad();
  });
</script>

<style scoped>
  .detail-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 10px;
  }

  .detail-summary span {
    margin-right: 16px;
    font-size: 13px;
  }
</style>
