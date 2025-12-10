<template>
  <div class="user-products-container">
    <div class="page-header">
      <h2>我的产品</h2>
      <p class="subtitle">当前登录用户购买的全部产品信息</p>
    </div>

    <el-row :gutter="20" v-loading="loading">
      <el-col :xs="24" :sm="12" :lg="8" v-for="product in data.products" :key="product.id" class="product-col">
        <el-card class="product-card" shadow="hover">
          <template #header>
            <div class="card-header">
              <div class="product-type-badge" :class="`badge-${product.type}`">
                <el-icon class="product-icon">
                  <component :is="getProductIcon(product.type)" />
                </el-icon>
                <span class="product-type-name">{{ product.typeName }}</span>
              </div>
              <el-tag :type="getStatusType(product.status)" size="small">
                {{ product.statusText }}
              </el-tag>
            </div>
          </template>

          <div class="product-content">
            <div class="product-info-item">
              <span class="label">产品名称：</span>
              <span class="value">{{ product.name }}</span>
            </div>
            <div class="product-info-item">
              <span class="label">资源编号：</span>
              <span class="value code">{{ product.resourceCode }}</span>
            </div>
            <div class="product-info-item">
              <span class="label">规格配置：</span>
              <span class="value">{{ product.spec }}</span>
            </div>
            <div class="product-info-item">
              <span class="label">购买时间：</span>
              <span class="value">{{ product.purchaseDate }}</span>
            </div>
            <div class="product-info-item">
              <span class="label">到期时间：</span>
              <span class="value" :class="{ 'expire-warning': product.isExpiringSoon }">
                {{ product.expireDate }}
              </span>
            </div>
            <div class="product-info-item">
              <span class="label">使用情况：</span>
              <div class="usage-bar">
                <el-progress :percentage="product.usagePercent" :color="getUsageColor(product.usagePercent)" :stroke-width="8" />
              </div>
            </div>
            <div class="product-info-item price-item">
              <span class="label">月费用：</span>
              <span class="value price">¥{{ product.monthlyPrice }}</span>
            </div>
          </div>

          <template #footer>
            <div class="card-footer">
              <el-button type="primary" size="small" @click="viewDetail(product)">
                <el-icon><View /></el-icon>
                查看详情
              </el-button>
              <el-button type="success" size="small" @click="renew(product)">
                <el-icon><Refresh /></el-icon>
                续费
              </el-button>
              <el-button type="info" size="small" @click="manage(product)">
                <el-icon><Setting /></el-icon>
                管理
              </el-button>
            </div>
          </template>
        </el-card>
      </el-col>
    </el-row>

    <!-- 统计概览 -->
    <div class="stats-overview">
      <h3>产品统计</h3>
      <el-row :gutter="20">
        <el-col :xs="24" :sm="12" :md="6">
          <el-statistic title="总产品数" :value="data.stats.totalProducts" class="stats-card">
            <template #prefix>
              <el-icon><Box /></el-icon>
            </template>
          </el-statistic>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6">
          <el-statistic title="运行中" :value="data.stats.runningProducts" class="stats-card">
            <template #prefix>
              <el-icon style="color: #67c23a"><CircleCheck /></el-icon>
            </template>
          </el-statistic>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6">
          <el-statistic title="即将到期" :value="data.stats.expiringSoon" class="stats-card">
            <template #prefix>
              <el-icon style="color: #e6a23c"><Warning /></el-icon>
            </template>
          </el-statistic>
        </el-col>
        <el-col :xs="24" :sm="12" :md="6">
          <el-statistic title="月总费用" :value="data.stats.totalMonthlyPrice" :precision="2" class="stats-card">
            <template #prefix>
              <span style="font-size: 14px">¥</span>
            </template>
          </el-statistic>
        </el-col>
      </el-row>
    </div>
  </div>
</template>

<script setup>
  import {
    Platform,
    Cpu,
    Coin,
    Monitor,
    Upload,
    ChatDotRound,
    View,
    Refresh,
    Setting,
    Box,
    CircleCheck,
    Warning,
  } from '@element-plus/icons-vue';
  import { ElMessage } from 'element-plus';

  const emits = defineEmits(['update-title']);

  const loading = ref(false);

  // 模拟数据
  const data = reactive({
    products: [
      {
        id: 1,
        type: 'stream',
        typeName: '流量',
        name: 'CDN加速服务-标准版',
        resourceCode: 'CDN-2024-001-XJ8K9',
        spec: '1TB/月 带宽峰值100Mbps',
        purchaseDate: '2024-01-15',
        expireDate: '2025-01-15',
        status: 'running',
        statusText: '运行中',
        usagePercent: 65,
        monthlyPrice: 299.0,
        isExpiringSoon: false,
      },
      {
        id: 2,
        type: 'sms',
        typeName: '短信',
        name: '短信服务包-企业版',
        resourceCode: 'SMS-2024-002-PL3M7',
        spec: '10万条/月 三网合一',
        purchaseDate: '2024-02-20',
        expireDate: '2024-12-20',
        status: 'running',
        statusText: '运行中',
        usagePercent: 82,
        monthlyPrice: 450.0,
        isExpiringSoon: true,
      },
      {
        id: 3,
        type: 'gpu',
        typeName: 'GPU',
        name: 'GPU计算实例-V100',
        resourceCode: 'GPU-2024-003-RT6N2',
        spec: 'NVIDIA V100 16GB 8核32GB内存',
        purchaseDate: '2024-03-10',
        expireDate: '2025-03-10',
        status: 'running',
        statusText: '运行中',
        usagePercent: 45,
        monthlyPrice: 3200.0,
        isExpiringSoon: false,
      },
      {
        id: 4,
        type: 'ecs',
        typeName: 'ECS',
        name: '云服务器-计算优化型',
        resourceCode: 'ECS-2024-004-WQ5H8',
        spec: '16核64GB 500GB SSD',
        purchaseDate: '2024-04-05',
        expireDate: '2025-04-05',
        status: 'running',
        statusText: '运行中',
        usagePercent: 58,
        monthlyPrice: 1280.0,
        isExpiringSoon: false,
      },
      {
        id: 5,
        type: 'bare_metal',
        typeName: '裸金属服务器',
        name: '裸金属服务器-高性能型',
        resourceCode: 'BM-2024-005-ZX9K4',
        spec: '双路至强 128GB 2TB NVMe',
        purchaseDate: '2024-05-12',
        expireDate: '2025-05-12',
        status: 'stopped',
        statusText: '已停止',
        usagePercent: 0,
        monthlyPrice: 5600.0,
        isExpiringSoon: false,
      },
      {
        id: 6,
        type: 'cloud_computer',
        typeName: '云电脑',
        name: '云桌面-设计师专用版',
        resourceCode: 'CC-2024-006-LM2P9',
        spec: '8核16GB RTX3060 256GB SSD',
        purchaseDate: '2024-06-18',
        expireDate: '2024-12-18',
        status: 'running',
        statusText: '运行中',
        usagePercent: 72,
        monthlyPrice: 890.0,
        isExpiringSoon: true,
      },
    ],
    stats: {
      totalProducts: 6,
      runningProducts: 5,
      expiringSoon: 2,
      totalMonthlyPrice: 11719.0,
    },
  });

  // 获取产品图标
  const getProductIcon = (type) => {
    const iconMap = {
      stream: Upload,
      sms: ChatDotRound,
      gpu: Cpu,
      ecs: Platform,
      bare_metal: Coin,
      cloud_computer: Monitor,
    };
    return iconMap[type] || Platform;
  };

  // 获取状态类型
  const getStatusType = (status) => {
    const typeMap = {
      running: 'success',
      stopped: 'info',
      expired: 'danger',
      pending: 'warning',
    };
    return typeMap[status] || 'info';
  };

  // 获取使用率颜色
  const getUsageColor = (percent) => {
    if (percent < 50) return '#67c23a';
    if (percent < 80) return '#e6a23c';
    return '#f56c6c';
  };

  // 查看详情
  const viewDetail = (product) => {
    ElMessage.info(`查看产品详情: ${product.name}`);
  };

  // 续费
  const renew = (product) => {
    ElMessage.success(`续费产品: ${product.name}`);
  };

  // 管理
  const manage = (product) => {
    ElMessage.info(`管理产品: ${product.name}`);
  };

  onMounted(async () => {
    emits('update-title', '羿贝综合云服务平台 - 我的产品');
    // 模拟加载
    loading.value = true;
    setTimeout(() => {
      loading.value = false;
    }, 500);
  });
</script>

<style lang="less" scoped>
  .user-products-container {
    padding: 20px;
    background: #f5f7fa;
    min-height: 100vh;
    transition: background-color 0.3s ease;
  }

  .page-header {
    margin-bottom: 30px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;

    h2 {
      margin: 0 0 8px 0;
      font-size: 28px;
      color: #303133;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    .subtitle {
      margin: 0;
      color: #909399;
      font-size: 14px;
      transition: color 0.3s ease;
    }
  }

  .product-col {
    margin-bottom: 20px;
  }

  .product-card {
    height: 100%;
    transition: all 0.3s ease;
    border-radius: 8px;

    &:hover {
      transform: translateY(-4px);
    }

    :deep(.el-card__header) {
      padding: 16px 20px;
      background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
      border-bottom: none;
    }

    :deep(.el-card__body) {
      padding: 20px;
    }

    :deep(.el-card__footer) {
      padding: 12px 20px;
      background: #fafafa;
      border-top: 1px solid #ebeef5;
      transition: all 0.3s ease;
    }
  }

  .card-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .product-type-badge {
    display: flex;
    align-items: center;
    gap: 8px;
    color: white;

    .product-icon {
      font-size: 20px;
    }

    .product-type-name {
      font-size: 16px;
      font-weight: 600;
    }
  }

  .product-content {
    .product-info-item {
      margin-bottom: 12px;
      display: flex;
      align-items: flex-start;
      font-size: 14px;

      &:last-child {
        margin-bottom: 0;
      }

      .label {
        color: #909399;
        min-width: 80px;
        flex-shrink: 0;
        transition: color 0.3s ease;
      }

      .value {
        color: #303133;
        flex: 1;
        word-break: break-all;
        transition: color 0.3s ease;

        &.code {
          font-family: 'Courier New', monospace;
          font-size: 13px;
          color: #409eff;
        }

        &.price {
          font-size: 18px;
          font-weight: 600;
          color: #f56c6c;
        }

        &.expire-warning {
          color: #e6a23c;
          font-weight: 600;
        }
      }

      &.price-item {
        margin-top: 16px;
        padding-top: 16px;
        border-top: 1px dashed #ebeef5;
        transition: border-color 0.3s ease;
      }
    }

    .usage-bar {
      flex: 1;
      padding-top: 4px;
    }
  }

  .card-footer {
    display: flex;
    gap: 8px;
    justify-content: space-between;

    .el-button {
      flex: 1;
    }
  }

  .stats-overview {
    margin-top: 40px;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;

    h3 {
      margin: 0 0 20px 0;
      font-size: 20px;
      color: #303133;
      font-weight: 600;
      transition: color 0.3s ease;
    }

    .stats-card {
      padding: 20px;
      background: #f9fafc;
      border-radius: 8px;
      text-align: center;
      transition: background-color 0.3s ease;

      :deep(.el-statistic__head) {
        font-size: 14px;
        color: #909399;
        margin-bottom: 8px;
      }

      :deep(.el-statistic__content) {
        font-size: 28px;
        font-weight: 600;
        color: #303133;
      }
    }
  }

  // 不同产品类型的渐变色
  .badge-stream {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  }

  .badge-sms {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
  }

  .badge-gpu {
    background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
  }

  .badge-ecs {
    background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
  }

  .badge-bare_metal {
    background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
  }

  .badge-cloud_computer {
    background: linear-gradient(135deg, #30cfd0 0%, #330867 100%);
  }

  // 暗色模式适配
  html.dark {
    .user-products-container {
      background: #1a1a1a;
    }

    .page-header {
      background: #2d2d2d;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);

      h2 {
        color: #e5e5e5;
      }

      .subtitle {
        color: #a8a8a8;
      }
    }

    .product-card {
      :deep(.el-card__footer) {
        background: #252525;
        border-top-color: #3a3a3a;
      }
    }

    .product-content {
      .product-info-item {
        .label {
          color: #a8a8a8;
        }

        .value {
          color: #e5e5e5;

          &.code {
            color: #66b1ff;
          }
        }

        &.price-item {
          border-top-color: #3a3a3a;
        }
      }
    }

    .stats-overview {
      background: #2d2d2d;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);

      h3 {
        color: #e5e5e5;
      }

      .stats-card {
        background: #252525;

        :deep(.el-statistic__head) {
          color: #a8a8a8;
        }

        :deep(.el-statistic__content) {
          color: #e5e5e5;
        }
      }
    }
  }

  // 响应式调整
  @media (max-width: 768px) {
    .user-products-container {
      padding: 10px;
    }

    .page-header {
      padding: 15px;

      h2 {
        font-size: 22px;
      }
    }

    .card-footer {
      flex-direction: column;

      .el-button {
        width: 100%;
      }
    }
  }
</style>
