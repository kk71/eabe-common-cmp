<template>
  <div class="billing-overview">
    <!-- 顶部标题 -->
    <div class="bo-header">
      <div>
        <h2 class="bo-title">账户总览</h2>
        <p class="bo-subtitle">查看当前账号的可用余额、近期账单与成本趋势</p>
      </div>
      <div class="bo-actions">
        <router-link class="bo-link" to="/sell/management/wallet">收支明细</router-link>
        <router-link class="bo-link" to="/sell/management/month-bill">账单概览</router-link>
      </div>
    </div>

    <!-- 余额卡片 -->
    <section class="card balance-card">
      <div class="balance-top">
        <div class="balance-info">
          <div class="balance-label">
            <span class="blue-dot" />
            可用余额
          </div>
          <div class="balance-row">
            <span class="balance-amount">{{ currencySymbol }}{{ availableBalanceText }}</span>
            <router-link to="/sell/management/wallet" class="link-blue">收支明细</router-link>
          </div>
          <div class="balance-detail">
            <span class="link-muted">现金余额</span>
            <span class="text-dark">: {{ currencySymbol }}{{ cashBalanceText }}</span>
            <span class="balance-sep">-</span>
            <span class="text-muted">欠费金额:</span>
            <span class="text-dark">{{ currencySymbol }}{{ debtAmountText }}</span>
          </div>
          <div class="balance-alert">
            可用余额预警
            <label class="toggle-switch">
              <input type="checkbox" />
              <span class="toggle-slider" />
            </label>
            <span class="balance-sep">|</span>
            <a href="javascript:;" class="link-blue">OpenAPI调试</a>
          </div>
        </div>
        <div class="balance-actions">
          <el-button type="primary" size="small">充值汇款</el-button>
          <el-button size="small">提现</el-button>
          <el-button size="small">汇款认领</el-button>
        </div>
      </div>
    </section>

    <!-- 近三月账单概览 -->
    <section class="card">
      <div class="card-header">
        <h3 class="card-title">近三月账单概览</h3>
        <router-link to="/sell/management/month-bill" class="link-blue">前往账单概览 &gt;</router-link>
      </div>
      <div class="bill-table-wrapper">
        <table class="bill-table">
          <thead>
            <tr>
              <th>Payer账号</th>
              <th>账务账期</th>
              <th>应付金额</th>
              <th>现金支付</th>
              <th>信控额度退款抵扣</th>
              <th>欠费金额</th>
              <th>状态</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="bill in bills" :key="bill.period">
              <td>demo</td>
              <td>{{ bill.period }}</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>-</td>
              <td>
                <span class="status-dot" :class="bill.statusClass" />
                {{ bill.status }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </section>

    <!-- 成本趋势 -->
    <section class="card">
      <div class="card-header">
        <div class="trend-header-left">
          <h3 class="card-title">成本趋势</h3>
          <span class="text-muted-sm">近 {{ trendMonths.length }} 月</span>
        </div>
        <a href="javascript:;" class="link-blue">前往费用分析 &gt;</a>
      </div>
      <div class="trend-filter">
        <span class="filter-label">报告名称</span>
        <div class="filter-select">
          <span>按产品汇总的月度费用</span>
        </div>
      </div>
      <div class="chart-container">
        <svg class="trend-chart" viewBox="0 0 900 200" preserveAspectRatio="xMidYMid meet">
          <line x1="0" y1="0" x2="900" y2="0" stroke="#f2f3f5" stroke-width="1" />
          <line x1="0" y1="66" x2="900" y2="66" stroke="#f2f3f5" stroke-width="1" />
          <line x1="0" y1="133" x2="900" y2="133" stroke="#f2f3f5" stroke-width="1" />
          <line x1="0" y1="199" x2="900" y2="199" stroke="#f2f3f5" stroke-width="1" />
          <text x="0" y="12" fill="#86909c">¥ {{ yAxisLabels[0] }}</text>
          <text x="0" y="78" fill="#86909c">¥ {{ yAxisLabels[1] }}</text>
          <text x="0" y="145" fill="#86909c">¥ {{ yAxisLabels[2] }}</text>
          <polyline
            fill="none"
            stroke="#3370ff"
            stroke-width="2"
            :points="trendPolylinePoints"
          />
          <g v-for="(m, i) in trendMonths" :key="m">
            <text :x="80 + i * 120" y="195" fill="#86909c" text-anchor="middle">
              {{ m }}
            </text>
          </g>
          <circle
            v-for="(pt, i) in trendPoints"
            :key="`${pt.x}-${pt.y}`"
            :cx="pt.x"
            :cy="pt.y"
            r="4"
            fill="#3370ff"
          />
        </svg>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { inject } from 'vue';
  import { waitRequest } from '@/utils/http/tools';
  import { getCostFeeTrend, getWalletAccounts } from '@/api/sell';

  const emits = defineEmits(['update-title']);
  const loading = inject('loading');

  const walletAccount = ref(null);

  const bills = ref([
    { period: '2026-03', status: '出账中', statusClass: 'dot-blue' },
    { period: '2026-02', status: '出账中', statusClass: 'dot-blue' },
    { period: '2026-01', status: '已结清', statusClass: 'dot-green' },
  ]);

  const currencySymbol = computed(() => '¥');
  const cashBalance = computed(() => Number(walletAccount.value?.balance ?? 0));
  const availableBalanceText = computed(() => cashBalance.value.toFixed(2));
  const cashBalanceText = computed(() => cashBalance.value.toFixed(2));
  // 后端目前未提供“欠费金额”字段，先以 0 展示，避免前端误算
  const debtAmountText = computed(() => '0.00');

  const trendData = ref([]);
  const trendMonths = computed(() => trendData.value.map((x) => x.period));
  const trendAmounts = computed(() => trendData.value.map((x) => Number(x.amount || 0)));

  const yAxisLabels = computed(() => {
    const maxV = Math.max(0, ...trendAmounts.value);
    const top = maxV <= 0 ? 0 : Math.ceil(maxV);
    const mid = top / 2;
    return [top.toFixed(0), mid.toFixed(0), '0'];
  });

  const trendPoints = computed(() => {
    const n = trendAmounts.value.length || 1;
    const x0 = 80;
    const x1 = 800;
    const yBottom = 199;
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

  async function loadTrend() {
    const resp = await waitRequest(loading, getCostFeeTrend({ params: { months: 6 } }));
    trendData.value = resp.data?.data ?? [];
  }

  async function loadWalletAccount() {
    const resp = await waitRequest(
      loading,
      getWalletAccounts({
        params: {
          page: 1,
          per_page: 1,
        },
      }),
    );
    walletAccount.value = resp.data?.data?.[0] ?? null;
  }

  onMounted(async () => {
    emits('update-title', '账户总览');
    await loadWalletAccount();
    await loadTrend();
  });
</script>

<style lang="less" scoped>
  .billing-overview {
    padding: 20px 24px;
    background: #f0f1f5;
    min-height: 100%;
    display: flex;
    flex-direction: column;
    gap: 16px;
  }

  .bo-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 12px;
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
  .bo-actions {
    display: flex;
    gap: 12px;
  }
  .bo-link {
    font-size: 13px;
    color: #3370ff;
    text-decoration: none;
  }
  .bo-link:hover {
    text-decoration: underline;
  }

  .card {
    background: #fff;
    border-radius: 8px;
    padding: 20px;
    border: 1px solid #e5e6eb;
  }
  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 16px;
  }
  .card-title {
    margin: 0;
    font-size: 15px;
    font-weight: 600;
    color: #1d2129;
  }

  .balance-card {
    display: flex;
    flex-direction: column;
  }
  .balance-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 24px;
  }
  .balance-info {
    flex: 1;
  }
  .balance-label {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    color: #4e5969;
    margin-bottom: 8px;
  }
  .blue-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #3370ff;
  }
  .balance-row {
    display: flex;
    align-items: baseline;
    gap: 16px;
    margin-bottom: 10px;
  }
  .balance-amount {
    font-size: 32px;
    font-weight: 700;
    color: #1d2129;
    line-height: 1;
  }
  .balance-detail {
    display: flex;
    align-items: center;
    flex-wrap: wrap;
    gap: 6px;
    font-size: 13px;
    color: #86909c;
    margin-bottom: 12px;
  }
  .text-dark {
    color: #1d2129;
  }
  .text-muted {
    color: #86909c;
  }
  .text-muted-sm {
    font-size: 12px;
    color: #86909c;
  }
  .balance-sep {
    color: #c9cdd4;
    margin: 0 4px;
  }
  .balance-alert {
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 13px;
    color: #4e5969;
  }
  .balance-actions {
    display: flex;
    gap: 8px;
    flex-shrink: 0;
  }

  .link-blue {
    font-size: 13px;
    color: #3370ff;
    text-decoration: none;
  }
  .link-blue:hover {
    color: #4080ff;
  }
  .link-muted {
    font-size: 13px;
    color: #3370ff;
    text-decoration: none;
    border-bottom: 1px dashed #3370ff;
  }

  .toggle-switch {
    position: relative;
    display: inline-block;
    width: 36px;
    height: 20px;
  }
  .toggle-switch input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .toggle-slider {
    position: absolute;
    cursor: pointer;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: #c9cdd4;
    border-radius: 10px;
    transition: background 0.2s;
  }
  .toggle-slider::before {
    content: '';
    position: absolute;
    width: 16px;
    height: 16px;
    left: 2px;
    bottom: 2px;
    background: #fff;
    border-radius: 50%;
    transition: transform 0.2s;
  }
  .toggle-switch input:checked + .toggle-slider {
    background: #3370ff;
  }
  .toggle-switch input:checked + .toggle-slider::before {
    transform: translateX(16px);
  }

  .bill-table-wrapper {
    overflow-x: auto;
  }
  .bill-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 13px;
  }
  .bill-table th {
    text-align: left;
    padding: 10px 12px;
    font-weight: 500;
    color: #86909c;
    background: #f7f8fa;
    border-bottom: 1px solid #e5e6eb;
    white-space: nowrap;
  }
  .bill-table td {
    padding: 12px;
    border-bottom: 1px solid #f2f3f5;
    color: #4e5969;
    white-space: nowrap;
  }
  .bill-table tbody tr:hover {
    background: #f7f8fa;
  }
  .status-dot {
    display: inline-block;
    width: 6px;
    height: 6px;
    border-radius: 50%;
    margin-right: 6px;
  }
  .dot-blue {
    background: #3370ff;
  }
  .dot-green {
    background: #00b42a;
  }

  .trend-header-left {
    display: flex;
    align-items: baseline;
    gap: 12px;
  }
  .trend-filter {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    margin-top: 8px;
  }
  .filter-label {
    font-size: 13px;
    color: #86909c;
  }
  .filter-select {
    display: flex;
    align-items: center;
    gap: 6px;
    padding: 6px 12px;
    border: 1px solid #e5e6eb;
    border-radius: 6px;
    font-size: 13px;
    color: #1d2129;
  }
  .chart-container {
    position: relative;
  }
  .trend-chart {
    width: 100%;
    height: 200px;
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

  @media (max-width: 960px) {
    .billing-overview {
      padding: 16px;
    }
    .balance-top {
      flex-direction: column;
    }
    .balance-actions {
      align-self: flex-start;
    }
  }
</style>
