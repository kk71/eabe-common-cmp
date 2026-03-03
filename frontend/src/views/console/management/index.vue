<template>
  <div class="management-home" v-loading="loading">
    <section class="hero-section">
      <div class="hero-bg"></div>
      <div class="hero-top-menu">
        <span class="menu-item active">大模型</span>
        <span class="menu-item">产品</span>
      </div>
      <div class="hero-content">
        <div class="hero-text">
          <div class="hero-tag">羿贝综合云服务平台</div>
          <h1 class="hero-title">你的企业级云与 AI 中台</h1>
          <p class="hero-subtitle">一站式管理账单、订单与钱包，实现从销售到结算的全链路数字化运营。</p>
          <div class="hero-actions">
            <el-button type="primary" size="large" @click="$router.push('/console/management/order')">
              进入订单中心
            </el-button>
            <el-button size="large" @click="$router.push('/console/management/wallet')">查看钱包与资金</el-button>
          </div>
          <div class="hero-meta">
            <span>实时销售与支付数据</span>
            <span>预充值钱包扣费闭环</span>
            <span>按月账单精细汇总</span>
          </div>
        </div>
        <div class="hero-cards">
          <el-card class="hero-card hero-card-main" shadow="hover">
            <div class="hero-card-header">
              <span>今日概览</span>
            </div>
            <div class="hero-card-body">
              <div class="hero-metric">
                <span class="label">累计销售额</span>
                <span class="value">¥{{ totalAmount.toFixed(2) }}</span>
              </div>
              <div class="hero-metric">
                <span class="label">订单总数</span>
                <span class="value">{{ totalCount }}</span>
              </div>
              <div class="hero-metric">
                <span class="label">已支付订单</span>
                <span class="value">{{ data.payment_stats.paid_count }}</span>
              </div>
            </div>
          </el-card>
          <el-card class="hero-card hero-card-side" shadow="hover">
            <div class="hero-card-body">
              <div class="hero-side-item">
                <div class="dot dot-green"></div>
                <span>已支付金额 ¥{{ data.payment_stats.paid_amount.toFixed(2) }}</span>
              </div>
              <div class="hero-side-item">
                <div class="dot dot-orange"></div>
                <span>待支付金额 ¥{{ data.payment_stats.processing_amount.toFixed(2) }}</span>
              </div>
              <div class="hero-side-item">
                <div class="dot dot-red"></div>
                <span>支付失败金额 ¥{{ data.payment_stats.failed_amount.toFixed(2) }}</span>
              </div>
            </div>
          </el-card>
        </div>
      </div>
    </section>

    <!-- 楼层一：综合统计（保留原内容） -->
    <section class="floor floor-summary">
      <div class="floor-header">
        <h2>综合统计</h2>
        <p>从产品维度快速了解整体销售量与销售额概况。</p>
      </div>
      <div class="floor-body">
        <el-row :gutter="20">
          <el-col :xs="24" :sm="12" :md="6">
            <el-card class="summary-card total-products" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><Box /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">产品种类</div>
                  <div class="summary-value">{{ data.overall_stats.length }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :xs="24" :sm="12" :md="6">
            <el-card class="summary-card total-sales" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><ShoppingCart /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">总销售量</div>
                  <div class="summary-value">{{ totalCount }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :xs="24" :sm="12" :md="6">
            <el-card class="summary-card total-revenue" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><Coin /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">总销售额</div>
                  <div class="summary-value">¥{{ totalAmount.toFixed(2) }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :xs="24" :sm="12" :md="6">
            <el-card class="summary-card avg-price" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><Wallet /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">平均单价</div>
                  <div class="summary-value">¥{{ avgPrice.toFixed(2) }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </section>

    <!-- 楼层二：支付结果统计（保留原内容） -->
    <section class="floor floor-payment">
      <div class="floor-header">
        <h2>支付结果统计</h2>
        <p>从支付视角透视订单履约效果，实时掌握资金回笼情况。</p>
      </div>
      <div class="floor-body">
        <el-row :gutter="20">
          <el-col :xs="24" :sm="12" :md="8">
            <el-card class="summary-card total-revenue" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><Coin /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">已支付金额</div>
                  <div class="summary-value">¥{{ data.payment_stats.paid_amount.toFixed(2) }}</div>
                  <div class="summary-label">已支付订单数：{{ data.payment_stats.paid_count }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :xs="24" :sm="12" :md="8">
            <el-card class="summary-card total-sales" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><Money /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">待支付金额</div>
                  <div class="summary-value">¥{{ data.payment_stats.processing_amount.toFixed(2) }}</div>
                  <div class="summary-label">待支付订单数：{{ data.payment_stats.processing_count }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
          <el-col :xs="24" :sm="12" :md="8">
            <el-card class="summary-card total-products" shadow="hover">
              <div class="summary-content">
                <div class="summary-icon">
                  <el-icon><ShoppingCart /></el-icon>
                </div>
                <div class="summary-info">
                  <div class="summary-label">支付失败金额</div>
                  <div class="summary-value">¥{{ data.payment_stats.failed_amount.toFixed(2) }}</div>
                  <div class="summary-label">支付失败订单数：{{ data.payment_stats.failed_count }}</div>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </section>

    <!-- 楼层三：销售量统计（保留原内容） -->
    <section class="floor floor-count">
      <div class="floor-header">
        <h2>销售量统计</h2>
        <p>按产品查看销量贡献，占比一目了然。</p>
      </div>
      <div class="floor-body">
        <el-row :gutter="20">
          <el-col :xs="24" :sm="12" :lg="8" v-for="(s, index) in data.overall_stats" :key="'count-' + index">
            <el-card class="product-stats-card" shadow="hover">
              <template #header>
                <div class="card-header">
                  <div class="product-badge" :style="{ background: getGradientColor(index) }">
                    <el-icon class="product-icon">
                      <component :is="getProductIcon(index)" />
                    </el-icon>
                    <span class="product-name">{{ s.product_name }}</span>
                  </div>
                </div>
              </template>
              <div class="stats-content">
                <el-statistic :value="s.count" class="stats-number">
                  <template #suffix>
                    <span class="stats-unit">件</span>
                  </template>
                </el-statistic>
                <div class="stats-footer">
                  <el-progress
                    :percentage="getPercentage(s.count, totalCount)"
                    :color="getProgressColor(index)"
                    :stroke-width="8"
                    :show-text="false"
                  />
                  <span class="percentage-text">占比 {{ getPercentage(s.count, totalCount) }}%</span>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </section>

    <!-- 楼层四：销售金额统计（保留原内容） -->
    <section class="floor floor-amount">
      <div class="floor-header">
        <h2>销售金额统计</h2>
        <p>按金额维度评估各产品线的营收价值。</p>
      </div>
      <div class="floor-body">
        <el-row :gutter="20">
          <el-col :xs="24" :sm="12" :lg="8" v-for="(s, index) in data.overall_stats" :key="'amount-' + index">
            <el-card class="product-stats-card amount-card" shadow="hover">
              <template #header>
                <div class="card-header">
                  <div class="product-badge" :style="{ background: getGradientColor(index) }">
                    <el-icon class="product-icon">
                      <component :is="getProductIcon(index)" />
                    </el-icon>
                    <span class="product-name">{{ s.product_name }}</span>
                  </div>
                </div>
              </template>
              <div class="stats-content">
                <el-statistic :value="s.amount" :precision="2" class="stats-number">
                  <template #prefix>
                    <span class="currency-symbol">¥</span>
                  </template>
                </el-statistic>
                <div class="stats-footer">
                  <el-progress
                    :percentage="getPercentage(s.amount, totalAmount)"
                    :color="getProgressColor(index)"
                    :stroke-width="8"
                    :show-text="false"
                  />
                  <span class="percentage-text">占比 {{ getPercentage(s.amount, totalAmount) }}%</span>
                </div>
                <div class="extra-info">
                  <span class="info-label">单价：</span>
                  <span class="info-value">¥{{ (s.amount / s.count).toFixed(2) }}</span>
                </div>
              </div>
            </el-card>
          </el-col>
        </el-row>
      </div>
    </section>
  </div>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { getOverallStats, getPaymentStats } from '@/api/console';
  import {
    DataAnalysis,
    TrendCharts,
    Box,
    ShoppingCart,
    Coin,
    Wallet,
    Histogram,
    Money,
    Platform,
    Cpu,
    Monitor,
    Upload,
    ChatDotRound,
    Service,
  } from '@element-plus/icons-vue';

  const emits = defineEmits(['update-title']);

  const loading = ref(false);

  const data = reactive({
    overall_stats: [],
    payment_stats: {
      paid_amount: 0,
      paid_count: 0,
      failed_amount: 0,
      failed_count: 0,
      processing_amount: 0,
      processing_count: 0,
    },
  });

  // 计算总销售量
  const totalCount = computed(() => {
    return data.overall_stats.reduce((sum, item) => sum + item.count, 0);
  });

  // 计算总销售额
  const totalAmount = computed(() => {
    return data.overall_stats.reduce((sum, item) => sum + item.amount, 0);
  });

  // 计算平均单价
  const avgPrice = computed(() => {
    if (totalCount.value === 0) return 0;
    return totalAmount.value / totalCount.value;
  });

  // 获取百分比
  const getPercentage = (value, total) => {
    if (total === 0) return 0;
    return Math.round((value / total) * 100);
  };

  // 获取渐变色
  const getGradientColor = (index) => {
    const gradients = [
      'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
      'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
      'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
      'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
      'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
      'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
      'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)',
    ];
    return gradients[index % gradients.length];
  };

  // 获取进度条颜色
  const getProgressColor = (index) => {
    const colors = ['#667eea', '#f5576c', '#00f2fe', '#38f9d7', '#fee140', '#330867', '#fed6e3', '#fecfef'];
    return colors[index % colors.length];
  };

  // 获取产品图标
  const getProductIcon = (index) => {
    const icons = [Platform, Cpu, Monitor, Upload, ChatDotRound, Service, Box, ShoppingCart];
    return icons[index % icons.length];
  };

  const onLoad = async () => {
    const overallResp = await waitRequest(
      loading,
      getOverallStats({
        params: {},
      }),
    );
    data.overall_stats = overallResp.data.data;

    const paymentResp = await waitRequest(
      loading,
      getPaymentStats({
        params: {},
      }),
    );
    data.payment_stats = paymentResp.data.data;
  };

  onMounted(async () => {
    emits('update-title', '羿贝综合云服务平台');
    await onLoad();
  });
</script>

<style lang="less" scoped>
  .management-home {
    min-height: 100vh;
    background: radial-gradient(circle at top left, #eef2ff 0%, #f7f8fa 50%, #ffffff 100%);
    color: #1d2129;
    padding-bottom: 40px;
  }

  .hero-section {
    position: relative;
    padding: 60px 40px 40px;
    overflow: hidden;
  }

  .hero-bg {
    position: absolute;
    inset: 0;
    background:
      radial-gradient(circle at 10% 20%, rgba(59, 130, 246, 0.35), transparent 55%),
      radial-gradient(circle at 80% 0%, rgba(129, 140, 248, 0.4), transparent 60%);
    opacity: 0.9;
    pointer-events: none;
  }

  .hero-top-menu {
    position: relative;
    max-width: 1200px;
    margin: 0 auto 16px;
    display: flex;
    gap: 16px;
    font-size: 13px;
    color: #4e5969;
  }

  .hero-top-menu .menu-item {
    cursor: pointer;
    padding-bottom: 6px;
    border-bottom: 2px solid transparent;
    opacity: 0.8;
  }

  .hero-top-menu .menu-item.active {
    border-color: #3370ff;
    opacity: 1;
  }

  .hero-content {
    position: relative;
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    gap: 24px;
  }

  .hero-text {
    flex: 1 1 480px;
    max-width: 640px;
  }

  .hero-tag {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: 999px;
    background: #e8f0ff;
    border: 1px solid #c6d4ff;
    font-size: 12px;
    color: #1d2129;
    margin-bottom: 16px;
  }

  .hero-title {
    font-size: 36px;
    font-weight: 700;
    line-height: 1.2;
    margin: 0 0 12px;
    color: #1d2129;
  }

  .hero-subtitle {
    font-size: 14px;
    color: #4e5969;
    max-width: 560px;
    margin-bottom: 24px;
  }

  .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-bottom: 16px;
  }

  .hero-meta {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    font-size: 12px;
    color: #4e5969;

    span {
      padding: 4px 10px;
      border-radius: 999px;
      background: rgba(255, 255, 255, 0.8);
      border: 1px solid #e5e6eb;
    }
  }

  .hero-cards {
    flex: 1 1 320px;
    max-width: 380px;
    display: flex;
    flex-direction: column;
    gap: 14px;
  }

  .hero-card {
    background: rgba(255, 255, 255, 0.92);
    border: 1px solid #e5e6eb;

    :deep(.el-card__body) {
      padding: 16px 18px;
    }
  }

  .hero-card-main .hero-card-header {
    font-size: 13px;
    color: #86909c;
    margin-bottom: 8px;
  }

  .hero-metric {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    margin-bottom: 6px;

    .label {
      font-size: 12px;
      color: #86909c;
    }

    .value {
      font-size: 18px;
      font-weight: 600;
      color: #1d2129;
    }
  }

  .hero-card-side .hero-side-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    color: #1d2129;
    margin-bottom: 6px;
  }

  .dot {
    width: 8px;
    height: 8px;
    border-radius: 999px;
  }
  .dot-green {
    background: #22c55e;
  }
  .dot-orange {
    background: #f97316;
  }
  .dot-red {
    background: #ef4444;
  }

  .floor {
    max-width: 1200px;
    margin: 0 auto;
    padding: 24px 24px 0;
  }

  .floor-header {
    margin-bottom: 18px;

    h2 {
      margin: 0 0 4px;
      font-size: 20px;
      font-weight: 600;
      color: #1d2129;
    }

    p {
      margin: 0;
      font-size: 13px;
      color: #4e5969;
    }
  }

  .floor-body {
    margin-bottom: 12px;
  }

  .summary-card {
    margin-bottom: 20px;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: none;

    &:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    :deep(.el-card__body) {
      padding: 24px;
    }
  }

  .summary-content {
    display: flex;
    align-items: center;
    gap: 20px;
  }

  .summary-icon {
    width: 64px;
    height: 64px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 32px;
    color: white;
  }

  .total-products .summary-icon {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }

  .total-sales .summary-icon {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  }

  .total-revenue .summary-icon {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  }

  .avg-price .summary-icon {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  }

  .summary-info {
    flex: 1;
  }

  .summary-label {
    font-size: 14px;
    color: #909399;
    margin-bottom: 8px;
    transition: color 0.3s ease;
  }

  .summary-value {
    font-size: 28px;
    font-weight: 600;
    color: #303133;
    transition: color 0.3s ease;
  }

  .product-stats-card {
    margin-bottom: 20px;
    border-radius: 12px;
    transition: all 0.3s ease;
    border: none;

    &:hover {
      transform: translateY(-4px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    }

    :deep(.el-card__header) {
      padding: 16px 20px;
      border-bottom: none;
    }

    :deep(.el-card__body) {
      padding: 24px;
    }
  }

  .card-header {
    .product-badge {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 8px 16px;
      border-radius: 8px;
      color: white;

      .product-icon {
        font-size: 24px;
      }

      .product-name {
        font-size: 16px;
        font-weight: 600;
      }
    }
  }

  .stats-content {
    .stats-number {
      margin-bottom: 20px;

      :deep(.el-statistic__content) {
        font-size: 36px;
        font-weight: 600;
        color: #303133;
      }

      .stats-unit {
        font-size: 16px;
        color: #909399;
        margin-left: 4px;
        transition: color 0.3s ease;
      }

      .currency-symbol {
        font-size: 20px;
        color: #909399;
        margin-right: 4px;
        transition: color 0.3s ease;
      }
    }

    .stats-footer {
      margin-bottom: 12px;

      .percentage-text {
        display: block;
        margin-top: 8px;
        font-size: 13px;
        color: #606266;
        transition: color 0.3s ease;
      }
    }

    .extra-info {
      padding-top: 12px;
      border-top: 1px solid #ebeef5;
      font-size: 14px;
      transition: border-color 0.3s ease;

      .info-label {
        color: #909399;
        transition: color 0.3s ease;
      }

      .info-value {
        color: #303133;
        font-weight: 600;
        margin-left: 4px;
        transition: color 0.3s ease;
      }
    }
  }

  .amount-card {
    .stats-number {
      :deep(.el-statistic__content) {
        color: #f5576c;
      }
    }
  }

</style>
