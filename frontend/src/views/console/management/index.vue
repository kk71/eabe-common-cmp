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
  import { getOverallStats } from '@/api/console';
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
    let resp = await waitRequest(
      loading,
      getOverallStats({
        params: {
          ...data.filterData,
          ...data.p,
        },
      }),
    );
    data.overall_stats = resp.data.data;
  };

  onMounted(async () => {
    emits('update-title', '羿贝综合云服务平台');
    await onLoad();
  });
</script>

<style lang="less" scoped>
  .management-dashboard {
    padding: 20px;
    background: #f5f7fa;
    min-height: 100vh;
    transition: background-color 0.3s ease;
  }

  .page-header {
    margin-bottom: 30px;
    padding: 24px;
    background: white;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);
    transition: all 0.3s ease;

    h2 {
      margin: 0 0 8px 0;
      font-size: 28px;
      color: #303133;
      font-weight: 600;
      display: flex;
      align-items: center;
      gap: 12px;
      transition: color 0.3s ease;

      .header-icon {
        font-size: 32px;
        color: #667eea;
        transition: color 0.3s ease;
      }
    }

    .subtitle {
      margin: 0;
      font-size: 14px;
      color: #909399;
      padding-left: 44px;
      transition: color 0.3s ease;
    }
  }

  .summary-section {
    margin-bottom: 30px;
  }

  .section-title {
    margin: 0 0 20px 0;
    font-size: 20px;
    color: #303133;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 8px;
    transition: color 0.3s ease;

    .el-icon {
      font-size: 24px;
      color: #667eea;
      transition: color 0.3s ease;
    }
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

  .stats-section {
    margin-bottom: 30px;
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

  // 暗色模式适配
  html.dark {
    .management-dashboard {
      background: #141414;
    }

    .page-header {
      background: #2d2d2d;
      box-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);

      h2 {
        color: #e5e5e5;

        .header-icon {
          color: #8b9cff;
        }
      }

      .subtitle {
        color: #a8a8a8;
      }
    }

    .section-title {
      color: #e5e5e5;

      .el-icon {
        color: #8b9cff;
      }
    }

    .summary-label {
      color: #a8a8a8;
    }

    .summary-value {
      color: #e5e5e5;
    }

    .stats-content {
      .stats-number {
        :deep(.el-statistic__content) {
          color: #e5e5e5;
        }

        .stats-unit {
          color: #a8a8a8;
        }

        .currency-symbol {
          color: #a8a8a8;
        }
      }

      .stats-footer {
        .percentage-text {
          color: #b8b8b8;
        }
      }

      .extra-info {
        border-top-color: #3a3a3a;

        .info-label {
          color: #a8a8a8;
        }

        .info-value {
          color: #e5e5e5;
        }
      }
    }

    .amount-card {
      .stats-number {
        :deep(.el-statistic__content) {
          color: #ff7a8a;
        }
      }
    }
  }
</style>
