<template>
  <div class="bill-detail-page">
    <!-- 顶部标题 -->
    <div class="bd-header">
      <div>
        <h2 class="bd-title">账单详情</h2>
        <p class="bd-subtitle">按月查看账单总览、账单列表及明细，支持后续与真实账单接口对接</p>
      </div>
    </div>

    <!-- 提示信息 -->
    <div class="info-banner">
      <div class="info-icon">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#3370ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="10" />
          <line x1="12" y1="16" x2="12" y2="12" />
          <line x1="12" y1="8" x2="12.01" y2="8" />
        </svg>
      </div>
      <div class="info-text">
        <p>1. 请于每月第 2 个自然日 12 点后查看上月账单数据，当月数据存在一定延迟。</p>
        <p>2. 本页面目前使用示意数据，实际应付金额、折扣信息等可与后台账单明细接口进行对接。</p>
      </div>
    </div>

    <!-- 顶部标签页 -->
    <div class="main-tabs">
      <span
        v-for="tab in mainTabs"
        :key="tab.id"
        class="main-tab"
        :class="{ active: activeMainTab === tab.id }"
        @click="activeMainTab = tab.id"
      >
        {{ tab.name }}
      </span>
    </div>

    <!-- Tab: 账单总览 -->
    <template v-if="activeMainTab === 'summary'">
      <!-- 过滤区 -->
      <div class="filter-bar">
        <el-form :model="summaryFilter" label-position="right" label-width="80px" class="filter-form">
          <el-row :gutter="16">
            <el-col :xs="24" :sm="12" :md="8">
              <el-form-item label="账务账期">
                <el-date-picker
                  v-model="summaryFilter.range"
                  type="monthrange"
                  start-placeholder="开始月份"
                  end-placeholder="结束月份"
                  range-separator="-"
                  style="width: 100%"
                />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="8">
              <el-form-item label="Payer账号">
                <el-input v-model="summaryFilter.payer" placeholder="请输入" clearable />
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </div>

      <!-- 月账单表格（示意） -->
      <section class="section-block">
        <h3 class="section-title">月账单总览</h3>
        <div class="table-card">
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Payer账号</th>
                  <th>账务账期</th>
                  <th class="th-highlight">应付金额</th>
                  <th>现金支付</th>
                  <th>信控额度退款抵扣</th>
                  <th>欠费金额</th>
                  <th>状态</th>
                  <th>还款到期日</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="loading"><td colspan="8" class="td-loading">加载中...</td></tr>
                <tr v-else-if="!monthBills.length">
                  <td colspan="8">
                    <div class="empty-state">
                      <span class="empty-text">暂无月账单数据</span>
                    </div>
                  </td>
                </tr>
                <tr v-else v-for="row in monthBills" :key="row.payer + row.period">
                  <td>{{ row.payer }}</td>
                  <td>{{ row.period }}</td>
                  <td>{{ row.payAmount }}</td>
                  <td>{{ row.cashPay }}</td>
                  <td>{{ row.creditDeduct }}</td>
                  <td>{{ row.arrears }}</td>
                  <td>
                    <span class="status-dot" :class="row.statusClass" />
                    {{ row.statusText }}
                  </td>
                  <td>{{ row.dueDate }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- 产品汇总 -->
      <section class="section-block">
        <div class="section-head-row">
          <div class="section-title-row">
            <h3 class="section-title">产品汇总</h3>
            <span class="muted-text">{{ productSummaryPeriod }}</span>
          </div>
        </div>
        <div class="table-card">
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>产品</th>
                  <th>账务账期</th>
                  <th>原价</th>
                  <th>折后价</th>
                  <th>代金券抵扣</th>
                  <th class="th-highlight">应付金额</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="!productSummaryRows.length">
                  <td colspan="6">
                    <div class="empty-state">
                      <span class="empty-text">暂无产品汇总数据</span>
                    </div>
                  </td>
                </tr>
                <tr v-else v-for="(item, idx) in productSummaryRows" :key="idx">
                  <td>{{ item.product }}</td>
                  <td>{{ item.period }}</td>
                  <td>¥ {{ item.originalPrice }}</td>
                  <td>¥ {{ item.discountPrice }}</td>
                  <td>¥ {{ item.voucherDeduct }}</td>
                  <td>¥ {{ item.payAmount }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </template>

    <!-- Tab: 账单 -->
    <template v-if="activeMainTab === 'bills'">
      <div class="filter-bar">
        <el-form :model="billsFilter" label-position="right" label-width="80px" class="filter-form">
          <el-row :gutter="16">
            <el-col :xs="24" :sm="12" :md="8">
              <el-form-item label="账务账期">
                <el-date-picker
                  v-model="billsFilter.period"
                  type="month"
                  placeholder="选择月份"
                  style="width: 100%"
                />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="8">
              <el-form-item label="Payer账号">
                <el-input v-model="billsFilter.payer" placeholder="请输入" clearable />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="8">
              <el-form-item>
                <el-button type="primary" @click="loadBills">查询</el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </div>
      <section class="section-block">
        <div class="table-card">
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>Payer账号</th>
                  <th>账务账期</th>
                  <th class="th-highlight">应付金额</th>
                  <th>现金支付</th>
                  <th>欠费金额</th>
                  <th>状态</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="billsLoading"><td colspan="6" class="td-loading">加载中...</td></tr>
                <tr v-else-if="!billsList.length">
                  <td colspan="6">
                    <div class="empty-state"><span class="empty-text">暂无账单数据</span></div>
                  </td>
                </tr>
                <tr v-else v-for="row in billsList" :key="row.payer + row.period">
                  <td>{{ row.payer }}</td>
                  <td>{{ row.period }}</td>
                  <td>¥ {{ row.payAmount }}</td>
                  <td>¥ {{ row.cashPay }}</td>
                  <td>¥ {{ row.arrears }}</td>
                  <td>
                    <span class="status-dot" :class="row.statusClass" />
                    {{ row.statusText }}
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </template>

    <!-- Tab: 账单明细 -->
    <template v-if="activeMainTab === 'detail'">
      <div class="filter-bar">
        <el-form :model="detailFilter" label-position="right" label-width="80px" class="filter-form">
          <el-row :gutter="16">
            <el-col :xs="24" :sm="12" :md="6">
              <el-form-item label="账务账期">
                <el-date-picker
                  v-model="detailFilter.period"
                  type="month"
                  placeholder="选择月份"
                  style="width: 100%"
                />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
              <el-form-item label="Payer账号">
                <el-input v-model="detailFilter.payer" placeholder="请输入" clearable />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
              <el-form-item label="产品/资源">
                <el-input v-model="detailFilter.keyword" placeholder="产品名/资源编号" clearable />
              </el-form-item>
            </el-col>
            <el-col :xs="24" :sm="12" :md="6">
              <el-form-item>
                <el-button type="primary" @click="() => { detailPagination.page = 1; loadDetail(); }">查询</el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-form>
      </div>
      <section class="section-block">
        <div class="table-card">
          <div class="table-wrapper">
            <table class="data-table">
              <thead>
                <tr>
                  <th>账务账期</th>
                  <th>产品</th>
                  <th>资源编号</th>
                  <th>用量</th>
                  <th>官网价</th>
                  <th>优惠价</th>
                  <th class="th-highlight">实付金额</th>
                </tr>
              </thead>
              <tbody>
                <tr v-if="detailLoading"><td colspan="7" class="td-loading">加载中...</td></tr>
                <tr v-else-if="!detailList.length">
                  <td colspan="7">
                    <div class="empty-state"><span class="empty-text">暂无账单明细数据</span></div>
                  </td>
                </tr>
                <tr v-else v-for="row in detailList" :key="row.id">
                  <td>{{ row.period }}</td>
                  <td>{{ row.product_name }}</td>
                  <td>{{ row.resource_code }}</td>
                  <td>{{ row.amount ?? '-' }}</td>
                  <td>¥ {{ row.homepage_price }}</td>
                  <td>¥ {{ row.discount_price }}</td>
                  <td>¥ {{ row.total_paid }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
        <div v-if="detailPagination.pages > 1" class="pagination-wrap">
          <el-pagination
            v-model:current-page="detailPagination.page"
            :page-size="detailPagination.per_page"
            :total="detailPagination.total"
            layout="prev, pager, next"
            @current-change="loadDetail"
          />
        </div>
      </section>
    </template>
  </div>
</template>

<script setup>
  import { inject, watch } from 'vue';
  import { waitRequest } from '@/utils/http/tools';
  import { getMonthBillSummary, getMonthBills } from '@/api/sell';

  const emits = defineEmits(['update-title']);
  const loading = inject('loading');

  const mainTabs = [
    { id: 'summary', name: '账单总览' },
    { id: 'bills', name: '账单' },
    { id: 'detail', name: '账单明细' },
  ];
  const activeMainTab = ref('summary');

  const summaryFilter = reactive({
    range: [],
    payer: '',
  });

  const monthBills = ref([]);
  const productSummaryRows = ref([]);
  const productSummaryPeriod = ref('');

  const billsFilter = reactive({ period: null, payer: '' });
  const billsList = ref([]);
  const billsLoading = ref(false);

  const detailFilter = reactive({ period: null, payer: '', keyword: '' });
  const detailList = ref([]);
  const detailLoading = ref(false);
  const detailPagination = reactive({ page: 1, per_page: 20, total: 0, pages: 0 });

  function fmtNum(n) {
    if (n == null || Number.isNaN(n)) return '0.00';
    return Number(n).toFixed(2);
  }

  async function loadSummary() {
    const range = summaryFilter.range;
    let years = [];
    let months = [];
    if (range && range.length === 2) {
      const [s, e] = range;
      const d1 = new Date(s);
      const d2 = new Date(e);
      for (let y = d1.getFullYear(); y <= d2.getFullYear(); y++) {
        for (let m = y === d1.getFullYear() ? d1.getMonth() + 1 : 1; m <= (y === d2.getFullYear() ? d2.getMonth() + 1 : 12); m++) {
          years.push(y);
          months.push(m);
        }
      }
    }
    if (!years.length) {
      const d = new Date();
      years = [d.getFullYear()];
      months = [d.getMonth() + 1];
    }
    const all = [];
    for (let i = 0; i < years.length; i++) {
      const resp = await waitRequest(
        loading,
        getMonthBillSummary({ params: { year: years[i], month: months[i] } })
      );
      const list = resp.data?.data ?? [];
      all.push(...list);
    }
    const now = new Date();
    const yNow = now.getFullYear();
    const mNow = now.getMonth() + 1;
    monthBills.value = all.map((s) => {
      const isCurrentOrFuture = s.year > yNow || (s.year === yNow && s.month >= mNow);
      return {
        payer: s.customer_code || s.customer_name || '-',
        period: `${s.year}-${String(s.month).padStart(2, '0')}`,
        payAmount: fmtNum(s.total_amount),
        cashPay: fmtNum(s.total_amount),
        creditDeduct: fmtNum(0),
        arrears: fmtNum(0),
        statusText: isCurrentOrFuture ? '出账中' : '已结清',
        statusClass: isCurrentOrFuture ? 'billing' : 'settled',
        dueDate: `${s.year}-${String(s.month).padStart(2, '0')}-15`,
      };
    });
    if (summaryFilter.payer && String(summaryFilter.payer).trim()) {
      const q = String(summaryFilter.payer).trim().toLowerCase();
      monthBills.value = monthBills.value.filter((r) => String(r.payer || '').toLowerCase().includes(q));
    }
    const first = all[0];
    productSummaryPeriod.value = first ? `${first.year}-${String(first.month).padStart(2, '0')}` : '';
    const itemRows = [];
    for (const s of all) {
      for (const it of s.items || []) {
        itemRows.push({
          product: it.product_name || '-',
          period: `${it.year}-${String(it.month).padStart(2, '0')}`,
          originalPrice: fmtNum(it.homepage_price),
          discountPrice: fmtNum(it.discount_price),
          voucherDeduct: fmtNum(0),
          payAmount: fmtNum(it.total_paid),
        });
      }
    }
    productSummaryRows.value = itemRows;
  }

  watch(
    () => [summaryFilter.range, summaryFilter.payer],
    () => loadSummary(),
    { deep: true }
  );

  async function loadBills() {
    let y, m;
    if (billsFilter.period) {
      const d = new Date(billsFilter.period);
      y = d.getFullYear();
      m = d.getMonth() + 1;
    } else {
      const d = new Date();
      y = d.getFullYear();
      m = d.getMonth() + 1;
    }
    billsLoading.value = true;
    try {
      const resp = await waitRequest(
        loading,
        getMonthBillSummary({
          params: { year: y, month: m, ...(billsFilter.payer ? { customer_code: billsFilter.payer } : {}) },
        })
      );
      const list = resp.data?.data ?? [];
      const now = new Date();
      const yNow = now.getFullYear();
      const mNow = now.getMonth() + 1;
      billsList.value = list.map((s) => {
        const isCurrentOrFuture = s.year > yNow || (s.year === yNow && s.month >= mNow);
        return {
          payer: s.customer_code || s.customer_name || '-',
          period: `${s.year}-${String(s.month).padStart(2, '0')}`,
          payAmount: fmtNum(s.total_amount),
          cashPay: fmtNum(s.total_amount),
          arrears: fmtNum(0),
          statusText: isCurrentOrFuture ? '出账中' : '已结清',
          statusClass: isCurrentOrFuture ? 'billing' : 'settled',
        };
      });
    } finally {
      billsLoading.value = false;
    }
  }

  async function loadDetail() {
    let y, m;
    if (detailFilter.period) {
      const d = new Date(detailFilter.period);
      y = d.getFullYear();
      m = d.getMonth() + 1;
    } else {
      const d = new Date();
      y = d.getFullYear();
      m = d.getMonth() + 1;
    }
    detailLoading.value = true;
    try {
      const resp = await waitRequest(
        loading,
        getMonthBills({
          params: {
            year: y,
            month: m,
            page: detailPagination.page,
            per_page: detailPagination.per_page,
            ...(detailFilter.payer ? { customer_code: detailFilter.payer } : {}),
            ...(detailFilter.keyword ? { keyword: detailFilter.keyword } : {}),
          },
        })
      );
      const data = resp.data?.data ?? [];
      const pag = resp.data?.pagination ?? {};
      detailList.value = data.map((r) => ({
        id: r.id,
        period: `${r.year}-${String(r.month).padStart(2, '0')}`,
        product_name: r.product_name ?? '-',
        resource_code: r.resource_code ?? '-',
        amount: r.amount,
        homepage_price: fmtNum(r.homepage_price),
        discount_price: fmtNum(r.discount_price),
        total_paid: fmtNum(r.total_paid),
      }));
      detailPagination.total = pag.total ?? 0;
      detailPagination.pages = pag.per_page ? Math.ceil((pag.total ?? 0) / pag.per_page) : 0;
    } finally {
      detailLoading.value = false;
    }
  }

  watch(activeMainTab, (tab) => {
    if (tab === 'bills') loadBills();
    if (tab === 'detail') loadDetail();
  });

  onMounted(async () => {
    emits('update-title', '账单详情');
    await loadSummary();
    if (activeMainTab.value === 'bills') await loadBills();
    if (activeMainTab.value === 'detail') await loadDetail();
  });
</script>

<style lang="less" scoped>
  .bill-detail-page {
    min-height: 100%;
    background: #f0f1f5;
    padding: 20px 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .bd-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .bd-title {
    margin: 0;
    font-size: 20px;
    font-weight: 600;
    color: #1d2129;
  }
  .bd-subtitle {
    margin: 4px 0 0;
    font-size: 13px;
    color: #86909c;
  }

  .info-banner {
    display: flex;
    gap: 10px;
    padding: 12px 16px;
    background: #e8f3ff;
    border-radius: 8px;
    border: 1px solid #bedaff;
  }
  .info-icon {
    flex-shrink: 0;
    margin-top: 2px;
  }
  .info-text {
    font-size: 13px;
    color: #4e5969;
    line-height: 1.8;
  }
  .info-text p {
    margin: 0;
  }

  .main-tabs {
    display: flex;
    align-items: center;
    border-bottom: 1px solid #e5e6eb;
    gap: 0;
  }
  .main-tab {
    font-size: 14px;
    color: #4e5969;
    padding: 10px 20px;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.15s;
    white-space: nowrap;
  }
  .main-tab:hover {
    color: #3370ff;
  }
  .main-tab.active {
    color: #3370ff;
    font-weight: 500;
    border-bottom-color: #3370ff;
  }

  .filter-bar {
    background: #fff;
    border-radius: 8px;
    padding: 14px 20px;
    border: 1px solid #e5e6eb;
  }

  .section-block {
    display: flex;
    flex-direction: column;
    gap: 14px;
  }
  .section-title {
    font-size: 15px;
    font-weight: 600;
    color: #1d2129;
    margin: 0;
  }
  .section-head-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .section-title-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }
  .muted-text {
    font-size: 13px;
    color: #86909c;
  }

  .table-card {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e5e6eb;
    overflow: hidden;
  }
  .table-wrapper {
    overflow-x: auto;
  }
  .data-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }
  .data-table th {
    text-align: left;
    padding: 12px 16px;
    font-weight: 500;
    color: #86909c;
    background: #f7f8fa;
    border-bottom: 1px solid #e5e6eb;
    white-space: nowrap;
  }
  .data-table td {
    padding: 14px 16px;
    border-bottom: 1px solid #f2f3f5;
    color: #4e5969;
    white-space: nowrap;
  }
  .data-table tbody tr:hover {
    background: #f7f8fa;
  }
  .th-highlight {
    color: #3370ff;
  }

  .status-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    margin-right: 6px;
  }
  .status-dot.billing {
    background: #3370ff;
  }
  .status-dot.settled {
    background: #00b42a;
  }

  .empty-state {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px 0;
    gap: 8px;
  }
  .empty-icon-block {
    opacity: 0.7;
  }
  .empty-text {
    font-size: 13px;
    color: #86909c;
  }
  .empty-tab-state {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e5e6eb;
    padding: 80px 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 12px;
  }
  .td-loading {
    padding: 24px;
    text-align: center;
    color: #86909c;
  }
  .pagination-wrap {
    margin-top: 16px;
    display: flex;
    justify-content: flex-end;
  }

  @media (max-width: 960px) {
    .bill-detail-page {
      padding: 16px;
    }
  }
</style>

