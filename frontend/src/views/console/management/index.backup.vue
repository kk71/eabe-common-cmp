<template>
  <div class="management-dashboard" v-loading="loading">
    <!-- 页面头部 -->
    <div class="page-header">
      <h2>
        <el-icon class="header-icon"><DataAnalysis /></el-icon>
        销售数据总览
      </h2>
      <p class="subtitle">实时查看各产品的销售量和销售金额统计</p>
    </div>

    <!-- 总体统计卡片 -->
    <div class="summary-section">
      <h3 class="section-title">
        <el-icon><TrendCharts /></el-icon>
        综合统计
      </h3>
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

    <!-- 支付结果统计卡片 -->
    <div class="summary-section">
      <h3 class="section-title">
        <el-icon><Wallet /></el-icon>
        支付结果统计
      </h3>
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

    <!-- 销售量统计 -->
    <div class="stats-section">
      <h3 class="section-title">
        <el-icon><Histogram /></el-icon>
        销售量统计
      </h3>
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

    <!-- 销售金额统计 -->
    <div class="stats-section">
      <h3 class="section-title">
        <el-icon><Money /></el-icon>
        销售金额统计
      </h3>
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

  const totalCount = computed(() => {
    return data.overall_stats.reduce((sum, item) => sum + item.count, 0);
  });

  const totalAmount = computed(() => {
    return data.overall_stats.reduce((sum, item) => sum + item.amount, 0);
  });

  const avgPrice = computed(() => {
    if (totalCount.value === 0) return 0;
    return totalAmount.value / totalCount.value;
  });

  const getPercentage = (value, total) => {
    if (total === 0) return 0;
    return Math.round((value / total) * 100);
  };

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

  const getProgressColor = (index) => {
    const colors = ['#667eea', '#f5576c', '#00f2fe', '#38f9d7', '#fee140', '#330867', '#fed6e3', '#fecfef'];
    return colors[index % colors.length];
  };

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
  /* 保留原样式做备份 */
  .management-dashboard {
    padding: 20px;
    background: #f5f7fa;
    min-height: 100vh;
  }
</style>

