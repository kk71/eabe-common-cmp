<template>
  <section class="hero-section">
    <!-- Background glow -->
    <div
      class="glow"
      style="width: 600px; height: 600px; top: -100px; left: 15%; background: rgba(51, 112, 255, 0.06)"
    ></div>
    <div
      class="glow"
      style="width: 500px; height: 500px; bottom: -80px; right: 15%; background: rgba(20, 201, 201, 0.05)"
    ></div>

    <div class="container" style="position: relative">
      <!-- Tabs -->
      <div class="tab-bar" style="margin-bottom: 32px">
        <button
          v-for="tab in tabs"
          :key="tab.id"
          :class="['pill-tab', { active: activeTab === tab.id }]"
          @click="activeTab = tab.id"
        >
          {{ tab.label }}
        </button>
      </div>

      <!-- Main Grid -->
      <div class="hero-grid">
        <!-- Main Banner -->
        <div
          class="hero-banner card"
          style="
            padding: 48px;
            min-height: 380px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
          "
        >
          <div
            class="glow"
            style="
              width: 400px;
              height: 400px;
              top: -60px;
              right: -60px;
              background: rgba(51, 112, 255, 0.1);
            "
          ></div>
          <div
            class="glow"
            style="
              width: 300px;
              height: 300px;
              bottom: -40px;
              left: -40px;
              background: rgba(20, 201, 201, 0.08);
            "
          ></div>
          <div style="position: relative">
            <span class="hero-badge">
              <VolcIcon name="sparkles" :size="14" color="var(--color-brand)" />
              AI 创新巡展
            </span>
            <h1 class="hero-title">
              羿贝综合云服务平台<br />
              <span style="color: var(--color-brand)">云上增长新动力</span>
            </h1>
            <p class="hero-desc">
              聚焦前沿 AI 技术，探索行业实践，助力企业数字化转型与智能化升级
            </p>
          </div>
          <div class="flex gap-3" style="position: relative; flex-wrap: wrap">
            <a href="#" class="btn-primary">
              立即体验
              <VolcIcon name="arrow-right" :size="16" />
            </a>
            <a href="#" class="btn-secondary">查看详情</a>
          </div>
        </div>

        <!-- Right Column -->
        <div class="hero-right">
          <a
            v-for="(promo, idx) in promos"
            :key="idx"
            href="#"
            class="card promo-card"
          >
            <span :class="['tag', promo.tagClass]">
              {{ promo.tag }}
            </span>
            <span class="promo-title">
              {{ promo.title }}
            </span>
            <VolcIcon name="arrow-right" :size="16" color="var(--text-muted)" />
          </a>

          <!-- Quick Stats -->
          <div class="card stats-card">
            <p
              style="
                font-size: 12px;
                color: var(--text-muted);
                font-weight: 500;
                margin-bottom: 16px;
              "
            >
              核心优势
            </p>
            <div class="stats-grid">
              <div v-for="stat in stats" :key="stat.label" class="stat-item">
                <div
                  class="icon-box"
                  :style="{
                    width: '36px',
                    height: '36px',
                    background: stat.bgColor
                  }"
                >
                  <img :src="stat.icon" alt="" style="width: 24px; height: 24px" />
                </div>
                <div>
                  <p
                    style="
                      font-size: 14px;
                      font-weight: 600;
                      color: var(--text-primary);
                    "
                  >
                    {{ stat.label }}
                  </p>
                  <p style="font-size: 12px; color: var(--text-muted)">
                    {{ stat.sub }}
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VolcIcon from './SvgIcons.vue'
import IconBenefitAi from '@/assets/icons/svg/icon-benefit-ai.svg'
import IconBenefitTrial from '@/assets/icons/svg/icon-benefit-trial.svg'
import IconBenefitPrice from '@/assets/icons/svg/icon-benefit-price.svg'
import IconStream from '@/assets/icons/svg/icon-stream.svg'

export default {
  name: 'HeroSection',
  components: { VolcIcon },
  data() {
    return {
      activeTab: 'ai',
      tabs: [
        { id: 'ai', label: 'AI创新巡展' },
        { id: 'doubao', label: '豆包大模型' },
        { id: 'coze', label: '扣子' },
        { id: 'opensource', label: '开源' },
        { id: 'story', label: 'AI创变者说' }
      ],
      promos: [
        {
          tag: 'HOT',
          tagClass: 'tag-hot',
          title: '豆包最新模型 千万tokens 19.9元起'
        },
        {
          tag: 'NEW',
          tagClass: 'tag-new',
          title: 'ECS 热门机型首年29元起'
        },
        {
          tag: '促销',
          tagClass: 'tag-promo',
          title: '企业上云权益中心'
        }
      ],
      stats: [
        {
          icon: IconBenefitAi,
          label: 'AI 驱动',
          sub: '智能化升级',
          bgColor: 'rgba(51, 112, 255, 0.12)'
        },
        {
          icon: IconBenefitTrial,
          label: '极速体验',
          sub: '低延迟响应',
          bgColor: 'rgba(255, 122, 69, 0.12)'
        },
        {
          icon: IconBenefitPrice,
          label: '长效低价',
          sub: '组合优惠方案',
          bgColor: 'rgba(247, 186, 30, 0.14)'
        },
        {
          icon: IconStream,
          label: '灵活扩展',
          sub: '按需弹性资源',
          bgColor: 'rgba(65, 184, 131, 0.12)'
        }
      ]
    }
  }
}
</script>

<style scoped>
.hero-section {
  position: relative;
  padding: 96px 0 64px;
  overflow: hidden;
}
.hero-grid {
  display: grid;
  grid-template-columns: 2fr 1fr;
  gap: 24px;
}
.hero-banner {
  position: relative;
  overflow: hidden;
}
.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: rgba(51, 112, 255, 0.1);
  color: var(--color-brand);
  font-size: 12px;
  font-weight: 500;
  padding: 6px 14px;
  border-radius: 100px;
  margin-bottom: 24px;
}
.hero-title {
  font-size: 44px;
  font-weight: 700;
  line-height: 1.2;
  color: var(--text-primary);
  margin-bottom: 16px;
}
.hero-desc {
  font-size: 16px;
  color: var(--text-muted);
  max-width: 500px;
  line-height: 1.7;
  margin-bottom: 32px;
}
.hero-right {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.promo-card {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 18px 20px;
}
.promo-title {
  flex: 1;
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
}
.stats-card {
  padding: 20px;
  flex: 1;
}
.stats-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 16px;
}
.stat-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

@media (max-width: 768px) {
  .hero-grid {
    grid-template-columns: 1fr;
  }
  .hero-title {
    font-size: 30px;
  }
  .hero-banner {
    padding: 32px !important;
    min-height: auto !important;
  }
}
</style>

