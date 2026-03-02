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
                <tr v-for="row in monthBills" :key="row.period">
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

      <!-- 汇总示意（空态） -->
      <section class="section-block">
        <div class="section-head-row">
          <div class="section-title-row">
            <h3 class="section-title">产品汇总（示意）</h3>
            <span class="muted-text">2026-03</span>
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
                <tr>
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
                      <span class="empty-text">暂无内容，后续可接入真实产品汇总数据</span>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </template>

    <!-- Tab: 账单 -->
    <template v-if="activeMainTab === 'bills'">
      <div class="empty-tab-state">
        <div class="empty-icon-block">
          <svg width="64" height="64" viewBox="0 0 64 64" fill="none">
            <rect x="12" y="8" width="40" height="48" rx="4" fill="#f2f3f5" stroke="#d9dce1" stroke-width="2" />
            <rect x="20" y="28" width="24" height="3" rx="1.5" fill="#d9dce1" />
            <rect x="20" y="36" width="16" height="3" rx="1.5" fill="#d9dce1" />
            <text x="46" y="24" font-size="10" fill="#86909c" font-weight="600">EMPTY</text>
          </svg>
        </div>
        <span class="empty-text">暂无账单数据，可根据业务需要对接账单列表接口</span>
      </div>
    </template>

    <!-- Tab: 账单明细 -->
    <template v-if="activeMainTab === 'detail'">
      <div class="empty-tab-state">
        <div class="empty-icon-block">
          <svg width="64" height="64" viewBox="0 0 64 64" fill="none">
            <rect x="12" y="8" width="40" height="48" rx="4" fill="#f2f3f5" stroke="#d9dce1" stroke-width="2" />
            <rect x="20" y="28" width="24" height="3" rx="1.5" fill="#d9dce1" />
            <rect x="20" y="36" width="16" height="3" rx="1.5" fill="#d9dce1" />
            <text x="46" y="24" font-size="10" fill="#86909c" font-weight="600">EMPTY</text>
          </svg>
        </div>
        <span class="empty-text">暂无账单明细数据，可对接详细明细接口并在此展示</span>
      </div>
    </template>
  </div>
</template>

<script setup>
  const emits = defineEmits(['update-title']);

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

  const monthBills = ref([
    { payer: 'demo', period: '2026-03', payAmount: '-', cashPay: '-', creditDeduct: '-', arrears: '-', statusText: '出账中', statusClass: 'billing', dueDate: '-' },
    { payer: 'demo', period: '2026-02', payAmount: '-', cashPay: '-', creditDeduct: '-', arrears: '-', statusText: '出账中', statusClass: 'billing', dueDate: '-' },
    { payer: 'demo', period: '2026-01', payAmount: '-', cashPay: '-', creditDeduct: '-', arrears: '-', statusText: '已结清', statusClass: 'settled', dueDate: '-' },
  ]);

  onMounted(() => {
    emits('update-title', '账单详情');
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

  @media (max-width: 960px) {
    .bill-detail-page {
      padding: 16px;
    }
  }
</style>

