<template>
  <div class="bill-page" v-loading="loading">
    <section class="bill-hero">
      <div class="bill-hero-bg"></div>
      <div class="bill-hero-content">
        <div class="bill-hero-text">
          <div class="bill-hero-tag">账单中心 · 管理控制台</div>
          <h1 class="bill-hero-title">按月总览您的云上费用</h1>
          <p class="bill-hero-subtitle">
            按客户与月份聚合展示月租费、Token 使用费与一次性费用，并与钱包扣费自动对齐，支撑对账与核销。
          </p>
        </div>
        <div class="bill-hero-side">
          <el-card class="bill-hero-card" shadow="hover">
            <div class="bill-hero-card-title">筛选账单周期</div>
            <div class="bill-hero-card-body">
              <el-form :model="data.filterData" label-width="56px" label-position="left" class="bill-hero-form">
                <el-form-item label="年份">
                  <el-input-number
                    v-model="data.filterData.year"
                    :min="2000"
                    :max="2100"
                    controls-position="right"
                    size="small"
                  />
                </el-form-item>
                <el-form-item label="月份">
                  <el-input-number
                    v-model="data.filterData.month"
                    :min="1"
                    :max="12"
                    controls-position="right"
                    size="small"
                  />
                </el-form-item>
                <el-form-item label="客户">
                  <plain-text v-model="data.filterData.customer_code" clearable placeholder="客户编码" />
                </el-form-item>
              </el-form>
              <div class="bill-hero-actions">
                <el-button type="primary" size="small" @click="onLoad">查询账单</el-button>
                <el-button size="small" @click="exportSummaryCsv">导出汇总</el-button>
                <el-button size="small" @click="importDialog.visible = true">导入账单</el-button>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </section>

    <section class="bill-section">
      <div class="bill-section-header">
        <h2>月度账单汇总</h2>
        <p>一行即一张月度账单，汇总展示不同费用构成与账单总额。</p>
      </div>

      <filterable-list-frame
        v-model:filterData="data.filterData"
        v-model:pagination="data.p"
        :filter-data-typing="data.filterDataTyping"
        @filter-changed="onLoad"
      >
        <el-table ref="listTable" :data="data.data" stripe v-loading="loading" class="bill-table">
          <el-table-column type="selection" width="50" />
          <el-table-column prop="year" label="年" width="80" />
          <el-table-column prop="month" label="月" width="60" />
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
      </filterable-list-frame>
    </section>

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
        <template #title>选择 CSV 或 Excel(xlsx) 上传，用于生成账单与后续按月扣费</template>
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
  </div>
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

  onMounted(async () => {
    emits('update-title', '月度账单');
    await onLoad();
  });
</script>

<style scoped>
  .bill-page {
    min-height: 100vh;
    background: radial-gradient(circle at top left, #eef2ff 0%, #f7f8fa 50%, #ffffff 100%);
    padding: 24px 32px 40px;
    box-sizing: border-box;
  }

  .bill-hero {
    position: relative;
    margin-bottom: 24px;
    overflow: hidden;
    border-radius: 16px;
  }

  .bill-hero-bg {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(circle at 10% 10%, rgba(59, 130, 246, 0.3), transparent 55%),
      radial-gradient(circle at 80% 0%, rgba(129, 140, 248, 0.4), transparent 60%);
    opacity: 0.9;
    pointer-events: none;
  }

  .bill-hero-content {
    position: relative;
    display: flex;
    flex-wrap: wrap;
    gap: 24px;
    padding: 24px 28px;
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #e5e6eb;
  }

  .bill-hero-text {
    flex: 1 1 420px;
  }

  .bill-hero-tag {
    display: inline-flex;
    padding: 4px 12px;
    border-radius: 999px;
    border: 1px solid #c6d4ff;
    font-size: 12px;
    color: #1d2129;
    background: #e8f0ff;
    margin-bottom: 8px;
  }

  .bill-hero-title {
    margin: 0 0 8px;
    font-size: 24px;
    font-weight: 600;
    color: #1d2129;
  }

  .bill-hero-subtitle {
    margin: 0;
    font-size: 13px;
    color: #4e5969;
    max-width: 520px;
  }

  .bill-hero-side {
    flex: 1 1 320px;
    max-width: 360px;
  }

  .bill-hero-card {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #e5e6eb;

    :deep(.el-card__body) {
      padding: 14px 16px;
    }
  }

  .bill-hero-card-title {
    font-size: 13px;
    color: #1d2129;
    margin-bottom: 8px;
  }

  .bill-hero-form {
    :deep(.el-form-item__label) {
      color: #4e5969;
      font-size: 12px;
    }
  }

  .bill-hero-actions {
    display: flex;
    gap: 8px;
    margin-top: 8px;
  }

  .bill-section {
    max-width: 1200px;
    margin: 0 auto;
  }

  .bill-section-header {
    margin: 8px 0 16px;

    h2 {
      margin: 0 0 4px;
      font-size: 18px;
      font-weight: 600;
      color: #1d2129;
    }

    p {
      margin: 0;
      font-size: 13px;
      color: #4e5969;
    }
  }

  .bill-table {
    background: #ffffff;

    :deep(.el-table__header-wrapper th) {
      background: #f7f8fa;
      color: #4e5969;
      border-bottom-color: #e5e6eb;
    }

    :deep(.el-table__row) td {
      background: #ffffff;
      border-bottom-color: #f2f3f5;
      color: #1d2129;
    }
  }

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
