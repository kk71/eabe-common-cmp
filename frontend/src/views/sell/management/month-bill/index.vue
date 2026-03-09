<template>
  <div class="bill-overview-page">
    <!-- 顶部标题 -->
    <div class="bo-header">
      <div>
        <h2 class="bo-title">账单概览</h2>
        <p class="bo-subtitle">按月查看账单应付金额、历史欠费与产品费用构成</p>
      </div>
    </div>

    <!-- 顶部提示 -->
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
        <p>2. 本页面展示的是示意数据，后续可与后台账单汇总接口进行对接。</p>
      </div>
    </div>

    <!-- 过滤区 -->
    <div class="filter-bar">
      <el-form :model="filter" label-position="right" label-width="80px" class="filter-form">
        <el-row :gutter="16">
          <el-col :xs="24" :sm="12" :md="8">
            <el-form-item label="账务账期">
              <el-date-picker
                v-model="filter.period"
                type="month"
                placeholder="选择月份"
                style="width: 100%"
              />
            </el-form-item>
          </el-col>
          <el-col :xs="24" :sm="12" :md="8">
            <el-form-item label="Payer账号">
              <el-input v-model="filter.payer" placeholder="请输入" clearable />
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>

    <!-- 月账单卡片 + 趋势示意 -->
    <section class="section-block">
      <div class="bill-summary-grid">
        <!-- 左侧：月账单概览 -->
        <div class="card bill-card">
          <div class="bill-card-head">
            <span class="bill-period">{{ displayPeriod }}</span>
            <span class="bill-status billing">出账中</span>
          </div>
          <div class="bill-rows">
            <div class="bill-row">
              <span class="bill-row-label link-blue">应付金额</span>
              <span class="bill-row-value">¥ {{ summaryCard.payable }}</span>
            </div>
            <div class="bill-row">
              <span class="bill-row-label link-blue">已还款金额</span>
              <span class="bill-row-value">¥ {{ summaryCard.paid }}</span>
            </div>
            <div class="bill-row indent">
              <span class="bill-row-label muted">现金支付</span>
              <span class="bill-row-value muted">¥ {{ summaryCard.cashPay }}</span>
            </div>
            <div class="bill-row indent">
              <span class="bill-row-label muted">信控额度退款抵扣</span>
              <span class="bill-row-value muted">¥ {{ summaryCard.creditDeduct }}</span>
            </div>
            <div class="bill-row">
              <span class="bill-row-label">欠费金额</span>
              <span class="bill-row-value">
                <router-link to="/sell/management/wallet" class="link-blue">充值</router-link>
                ¥ {{ summaryCard.arrears }}
              </span>
            </div>
          </div>
          <div class="bill-card-footer">
            <div class="footer-left">
              <span class="footer-label">历史累计欠费金额 ¥ {{ summaryCard.historyArrears }}</span>
              <span class="footer-note">* 示例数据，实际以后台账单为准</span>
            </div>
            <router-link to="/sell/management/bill-detail" class="link-blue">查看账单详情 &gt;</router-link>
          </div>
        </div>

        <!-- 右侧：费用趋势 -->
        <div class="card trend-card">
          <div class="trend-head">
            <span class="trend-title">费用趋势</span>
            <a href="javascript:;" class="link-blue">费用分析 &gt;</a>
          </div>
          <div class="trend-chart-area">
            <svg class="trend-chart" viewBox="0 0 600 200" preserveAspectRatio="xMidYMid meet">
              <line x1="40" y1="10" x2="40" y2="170" stroke="#e5e6eb" stroke-width="1" />
              <line x1="40" y1="170" x2="580" y2="170" stroke="#e5e6eb" stroke-width="1" />
              <line x1="40" y1="40" x2="580" y2="40" stroke="#f2f3f5" stroke-width="1" stroke-dasharray="4" />
              <line x1="40" y1="90" x2="580" y2="90" stroke="#f2f3f5" stroke-width="1" stroke-dasharray="4" />
              <line x1="40" y1="140" x2="580" y2="140" stroke="#f2f3f5" stroke-width="1" stroke-dasharray="4" />
              <polyline fill="none" stroke="#3370ff" stroke-width="2" :points="trendPolylinePoints" />
              <circle v-for="(pt, idx) in trendPoints" :key="idx" :cx="pt.x" :cy="pt.y" r="3" fill="#3370ff" />
              <text x="35" y="172" text-anchor="end" fill="#86909c">¥ 0</text>
              <text
                v-for="(m, idx) in trendMonths"
                :key="`label-${m}`"
                :x="trendPoints[idx]?.x ?? (60 + idx * 80)"
                y="188"
                text-anchor="middle"
                fill="#86909c"
              >
                {{ m }}
              </text>
            </svg>
          </div>
        </div>
      </div>
    </section>

    <!-- 月账单列表（静态头 + 空态） -->
    <section class="section-block">
      <h3 class="section-title">月账单列表</h3>
      <div class="table-card">
        <div class="table-wrapper">
          <table class="data-table">
            <thead>
              <tr>
                <th>Payer账号</th>
                <th>账务账期</th>
                <th>应付金额</th>
                <th>现金支付</th>
                <th>欠费金额</th>
                <th>状态</th>
              </tr>
            </thead>
            <tbody>
              <tr v-if="loading"><td colspan="6" class="td-loading">加载中...</td></tr>
              <tr v-else-if="!monthBillList.length">
                <td colspan="6">
                  <div class="empty-state">
                    <div class="empty-icon-block">
                      <svg width="48" height="48" viewBox="0 0 64 64" fill="none">
                        <rect x="12" y="8" width="40" height="48" rx="4" fill="#f2f3f5" stroke="#d9dce1" stroke-width="2" />
                        <rect x="20" y="28" width="24" height="3" rx="1.5" fill="#d9dce1" />
                        <rect x="20" y="36" width="16" height="3" rx="1.5" fill="#d9dce1" />
                        <text x="46" y="24" font-size="10" fill="#86909c" font-weight="600">EMPTY</text>
                      </svg>
                    </div>
                    <span class="empty-text">暂无账单数据</span>
                  </div>
                </td>
              </tr>
              <tr v-else v-for="row in monthBillList" :key="row.payer + row.period">
                <td>{{ row.payer }}</td>
                <td>{{ row.period }}</td>
                <td>¥ {{ row.payAmount }}</td>
                <td>¥ {{ row.cashPay }}</td>
                <td>¥ {{ row.arrears }}</td>
                <td>{{ row.statusText }}</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { inject, watch } from 'vue';
  import { waitRequest } from '@/utils/http/tools';
  import { getMonthBillSummary, getCostFeeTrend } from '@/api/sell';

  const emits = defineEmits(['update-title']);
  const loading = inject('loading');

  const filter = reactive({
    period: '',
    payer: '',
  });

  const trendData = ref([]);
  const trendMonths = computed(() => trendData.value.map((x) => x.period));
  const trendAmounts = computed(() => trendData.value.map((x) => Number(x.amount || 0)));

  const trendPoints = computed(() => {
    const n = trendAmounts.value.length || 1;
    const x0 = 60;
    const x1 = 560;
    const yBottom = 168;
    const yTop = 20;
    const maxV = Math.max(0, ...trendAmounts.value);
    const denom = maxV > 0 ? maxV : 1;
    const step = n === 1 ? 0 : (x1 - x0) / (n - 1);
    return trendAmounts.value.map((v, i) => {
      const x = x0 + step * i;
      const y = yBottom - ((yBottom - yTop) * (v / denom));
      return { x, y };
    });
  });

  const trendPolylinePoints = computed(() => trendPoints.value.map((p) => `${p.x},${p.y}`).join(' '));

  const summaryCard = reactive({
    payable: '0.00',
    paid: '0.00',
    cashPay: '0.00',
    creditDeduct: '0.00',
    arrears: '0.00',
    historyArrears: '0.00',
  });

  const monthBillList = ref([]);

  const displayPeriod = computed(() => {
    const period = filter.period;
    if (!period) return '2026-03';
    try {
      const d = new Date(period);
      const m = `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}`;
      return m;
    } catch {
      return '2026-03';
    }
  });

  function fmtNum(n) {
    if (n == null || Number.isNaN(n)) return '0.00';
    return Number(n).toFixed(2);
  }

  async function loadSummary() {
    const [y, m] = displayPeriod.value.split('-').map(Number);
    const resp = await waitRequest(
      loading,
      getMonthBillSummary({ params: { year: y, month: m } })
    );
    const list = resp.data?.data ?? [];
    const total = list.reduce((s, x) => s + (x.total_amount || 0), 0);
    summaryCard.payable = fmtNum(total);
    summaryCard.paid = fmtNum(0);
    summaryCard.cashPay = fmtNum(total);
    summaryCard.creditDeduct = fmtNum(0);
    summaryCard.arrears = fmtNum(0);
    summaryCard.historyArrears = fmtNum(0);
    let rows = list.map((s) => ({
      payer: s.customer_code || s.customer_name || '-',
      period: `${s.year}-${String(s.month).padStart(2, '0')}`,
      payAmount: fmtNum(s.total_amount),
      cashPay: fmtNum(s.total_amount),
      arrears: fmtNum(0),
      statusText: '出账中',
    }));
    if (filter.payer && String(filter.payer).trim()) {
      const q = String(filter.payer).trim().toLowerCase();
      rows = rows.filter((r) => String(r.payer || '').toLowerCase().includes(q));
    }
    monthBillList.value = rows;
  }

  async function loadTrend() {
    const resp = await waitRequest(loading, getCostFeeTrend({ params: { months: 6 } }));
    trendData.value = resp.data?.data ?? [];
  }

  watch(
    () => [filter.period, filter.payer],
    () => loadSummary(),
    { immediate: false }
  );

  onMounted(async () => {
    emits('update-title', '账单概览');
    if (!filter.period) {
      const d = new Date();
      filter.period = new Date(d.getFullYear(), d.getMonth(), 1);
    }
    await loadSummary();
    await loadTrend();
  });
</script>

<style lang="less" scoped>
  .bill-overview-page {
    min-height: 100%;
    background: #f0f1f5;
    padding: 20px 24px;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .bo-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .bo-title {
    margin: 0;
    font-size: 20px;
    font-weight: 600;
    color: #1d2129;
  }
  .bo-subtitle {
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

  .bill-summary-grid {
    display: grid;
    grid-template-columns: 1.1fr 1fr;
    gap: 16px;
  }
  .card {
    background: #fff;
    border-radius: 8px;
    border: 1px solid #e5e6eb;
  }

  .bill-card {
    display: flex;
    flex-direction: column;
  }
  .bill-card-head {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 20px 24px 0;
  }
  .bill-period {
    font-size: 22px;
    font-weight: 700;
    color: #1d2129;
  }
  .bill-status {
    font-size: 12px;
    padding: 2px 8px;
    border-radius: 4px;
    font-weight: 500;
  }
  .bill-status.billing {
    background: #e8f3ff;
    color: #3370ff;
  }
  .bill-rows {
    padding: 16px 24px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }
  .bill-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  .bill-row.indent {
    padding-left: 16px;
  }
  .bill-row-label {
    font-size: 13px;
    color: #4e5969;
  }
  .bill-row-label.link-blue {
    color: #3370ff;
  }
  .bill-row-label.muted {
    color: #86909c;
    font-size: 12px;
  }
  .bill-row-value {
    font-size: 14px;
    font-weight: 500;
    color: #1d2129;
  }
  .bill-row-value.muted {
    color: #86909c;
    font-size: 13px;
    font-weight: 400;
  }
  .bill-card-footer {
    padding: 14px 24px;
    border-top: 1px solid #f2f3f5;
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    background: #fafbfc;
    border-radius: 0 0 8px 8px;
  }
  .footer-left {
    display: flex;
    flex-direction: column;
    gap: 4px;
  }
  .footer-label {
    font-size: 13px;
    font-weight: 500;
    color: #1d2129;
  }
  .footer-note {
    font-size: 12px;
    color: #86909c;
  }
  .link-blue {
    color: #3370ff;
    text-decoration: none;
    font-size: 13px;
  }
  .link-blue:hover {
    text-decoration: underline;
  }

  .trend-card {
    display: flex;
    flex-direction: column;
  }
  .trend-head {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 20px 24px 12px;
  }
  .trend-title {
    font-size: 14px;
    font-weight: 600;
    color: #1d2129;
  }
  .trend-chart-area {
    flex: 1;
    padding: 0 16px 16px;
  }
  .trend-chart {
    width: 100%;
    min-height: 160px;
    font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', 'Microsoft YaHei', Arial, sans-serif;
  }
  .trend-chart text {
    font-family: inherit;
    font-variant-numeric: tabular-nums;
    font-size: 12px;
    font-weight: 400;
    letter-spacing: 0;
    text-rendering: geometricPrecision;
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
  .td-loading {
    padding: 24px;
    text-align: center;
    color: #86909c;
  }

  @media (max-width: 1100px) {
    .bill-summary-grid {
      grid-template-columns: 1fr;
    }
  }
  @media (max-width: 960px) {
    .bill-overview-page {
      padding: 16px;
    }
  }
</style>
