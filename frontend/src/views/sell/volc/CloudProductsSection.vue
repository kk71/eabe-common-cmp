<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 600px;
        height: 600px;
        bottom: -100px;
        left: 30%;
        background: rgba(51, 112, 255, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Header -->
      <div class="flex items-center justify-between" style="margin-bottom: 48px">
        <div>
          <div class="flex items-center gap-3" style="margin-bottom: 16px">
            <div class="section-bar" style="background: var(--color-yellow)"></div>
            <h2 class="section-title">AI 云原生</h2>
          </div>
          <p style="font-size: 16px; color: var(--text-muted)">
            以 Agent 为中心的基础架构新范式
          </p>
        </div>
        <a href="#" class="link-arrow md-hide">
          探索更多云产品
          <SvgIcon name="arrow-right" :size="16" />
        </a>
      </div>

      <!-- Category Tabs -->
      <div class="tab-bar" style="margin-bottom: 32px">
        <button
          v-for="cat in categories"
          :key="cat.id"
          :class="['cat-tab', { active: activeCategory === cat.id }]"
          @click="activeCategory = cat.id"
        >
          {{ cat.label }}
        </button>
      </div>

      <!-- Products Grid -->
      <div class="products-grid">
        <a
          v-for="(product, idx) in products"
          :key="idx"
          href="#"
          class="card product-card"
        >
          <div class="flex items-center gap-3" style="margin-bottom: 12px">
            <div
              class="icon-box"
              :style="{
                width: '36px',
                height: '36px',
                borderRadius: '10px',
                background: product.bgColor,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center'
              }"
            >
              <img :src="product.icon" alt="" style="width: 18px; height: 18px" />
            </div>
            <div class="flex items-center gap-2 min-w-0">
              <h4 class="product-name truncate">
                {{ product.name }}
              </h4>
              <span
                v-if="product.tag"
                :class="['ptag', product.tag === 'HOT' ? 'ptag-hot' : 'ptag-new']"
              >
                {{ product.tag }}
              </span>
            </div>
          </div>
          <p style="font-size: 12px; color: var(--text-muted); line-height: 1.6">
            {{ product.description }}
          </p>
          <div
            class="hover-reveal"
            style="
              margin-top: 12px;
              display: flex;
              align-items: center;
              gap: 4px;
              color: var(--color-brand);
              font-size: 12px;
              font-weight: 500;
            "
          >
            了解详情
            <SvgIcon name="arrow-right" :size="12" />
          </div>
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import SvgIcon from './SvgIcons.vue'
import IconGpu from '@/assets/icons/svg/icon-gpu.svg'
import IconEcs from '@/assets/icons/svg/icon-ecs.svg'
import IconBareMetal from '@/assets/icons/svg/icon-bare-metal.svg'
import IconCloudPc from '@/assets/icons/svg/icon-cloud-pc.svg'
import IconStream from '@/assets/icons/svg/icon-stream.svg'
import IconPost from '@/assets/icons/svg/icon-post.svg'
import Icon7Day from '@/assets/icons/svg/icon-7day.svg'
import Icon15Day from '@/assets/icons/svg/icon-15day.svg'
import IconBenefitAi from '@/assets/icons/svg/icon-benefit-ai.svg'
import IconFeatureSecure from '@/assets/icons/svg/icon-feature-secure.svg'

export default {
  name: 'CloudProductsSection',
  components: { SvgIcon },
  data() {
    return {
      activeCategory: 'featured',
      categories: [
        { id: 'featured', label: '精选产品' },
        { id: 'ai', label: '人工智能与机器学习' },
        { id: 'compute', label: '计算与网络' },
        { id: 'storage', label: '存储与数据库' },
        { id: 'container', label: '容器与中间件' },
        { id: 'bigdata', label: '大数据' },
        { id: 'cdn', label: 'CDN与边缘' },
        { id: 'video', label: '视频云' },
        { id: 'security', label: '安全' },
        { id: 'enterprise', label: '企业服务与云通信' }
      ],
      products: [
        {
          icon: IconGpu,
          name: 'GPU云服务器',
          tag: 'HOT',
          description: '高并行、高精度计算的GPU算力',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: IconEcs,
          name: '容器服务',
          tag: 'HOT',
          description: '高性能Kubernetes容器集群管理',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)'
        },
        {
          icon: IconBareMetal,
          name: '函数服务',
          tag: '',
          description: '无服务器函数托管计算平台',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)'
        },
        {
          icon: IconCloudPc,
          name: '公网IP',
          tag: 'HOT',
          description: '弹性、灵活、安全可靠的公网服务',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: IconStream,
          name: '云搜索服务',
          tag: 'HOT',
          description: '全托管AI信息检索和分析平台',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)'
        },
        {
          icon: IconPost,
          name: '对象存储',
          tag: '',
          description: '10EB级数据规模，高可用的对象存储服务',
          color: 'var(--color-green)',
          bgColor: 'rgba(159,219,29,0.1)'
        },
        {
          icon: Icon7Day,
          name: '云数据库 MySQL 版',
          tag: 'HOT',
          description: '即开即用稳定可靠的弹性MySQL服务',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)'
        },
        {
          icon: Icon15Day,
          name: '缓存数据库 Redis 版',
          tag: '',
          description: '兼具缓存的高性能与存储的持久化',
          color: 'var(--color-red)',
          bgColor: 'rgba(245,63,63,0.1)'
        },
        {
          icon: IconBenefitAi,
          name: 'AI数据湖服务',
          tag: '',
          description: '大模型时代 AI 数据基建',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: IconFeatureSecure,
          name: '大模型应用防火墙',
          tag: 'NEW',
          description: '针对大语言模型推理服务的安全防护产品',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)'
        }
      ]
    }
  }
}
</script>

<style scoped>
.section {
  padding: 80px 0;
  position: relative;
  overflow: hidden;
}
.section-title {
  font-size: 28px;
  font-weight: 700;
  color: var(--text-primary);
}
.link-arrow {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  color: var(--color-brand);
  font-size: 14px;
  font-weight: 500;
  transition: gap 0.2s;
}
.link-arrow:hover {
  gap: 10px;
}
.products-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}
.product-card {
  padding: 20px;
}
.product-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}
.ptag {
  font-size: 10px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 4px;
  white-space: nowrap;
  flex-shrink: 0;
}
.ptag-hot {
  background: rgba(245, 63, 63, 0.1);
  color: var(--color-red);
}
.ptag-new {
  background: rgba(20, 201, 201, 0.1);
  color: var(--color-accent);
}

@media (max-width: 1024px) {
  .products-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 768px) {
  .products-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

