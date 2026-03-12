<template>
  <div class="product-detail">
    <NavBar />
    <template v-if="product">
      <div class="breadcrumb-bar">
        <div class="container">
          <nav class="breadcrumb">
            <router-link to="/sell/home" class="bc-link">首页</router-link>
            <span class="bc-sep">/</span>
            <router-link to="/sell/home/products" class="bc-link">全部产品</router-link>
            <span class="bc-sep">/</span>
            <span class="bc-link bc-current" :style="{ color: category.color }">{{ category.name }}</span>
            <span class="bc-sep">/</span>
            <span class="bc-current">{{ product.name }}</span>
          </nav>
        </div>
      </div>

      <section class="detail-hero">
        <div class="hero-glow hero-glow-1" :style="{ background: glowColor }" />
        <div class="hero-glow hero-glow-2" />
        <div class="container hero-inner">
          <div class="hero-content">
            <div class="hero-badges">
              <span
                class="hero-cat-badge"
                :style="{ background: category.bgColor, color: category.color }"
              >
                <VolcIcon :name="category.icon" :size="14" :color="category.color" />
                {{ category.name }}
              </span>
              <span
                v-if="product.tag"
                :class="['hero-tag', product.tag === 'HOT' ? 'hero-tag-hot' : 'hero-tag-new']"
              >
                {{ product.tag }}
              </span>
            </div>
            <h1 class="hero-title">{{ product.name }}</h1>
            <p class="hero-banner-text">{{ product.detail.banner }}</p>
            <p class="hero-intro">{{ product.detail.intro }}</p>
            <div class="hero-actions">
              <a href="#" class="btn-primary">
                立即使用
                <VolcIcon name="arrow-right" :size="16" />
              </a>
              <a href="#" class="btn-secondary">
                <VolcIcon name="file-text" :size="16" />
                查看文档
              </a>
              <a href="#" class="btn-secondary">
                <VolcIcon name="headphones" :size="16" />
                咨询专家
              </a>
            </div>
          </div>
          <div class="hero-visual">
            <div class="visual-card">
              <div class="visual-icon-wrap" :style="{ background: product.bgColor }">
                <VolcIcon :name="product.icon" :size="48" :color="product.color" />
              </div>
              <div v-if="product.features" class="visual-features">
                <span
                  v-for="(f, fi) in product.features"
                  :key="fi"
                  class="visual-feature-chip"
                >
                  <VolcIcon name="check" :size="12" color="var(--color-accent)" />
                  {{ f }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <div class="sticky-nav" :class="{ 'sticky-nav-visible': showStickyNav }">
        <div class="container">
          <div class="sticky-nav-inner">
            <div class="sticky-tabs">
              <button
                v-for="tab in navTabs"
                :key="tab.id"
                class="sticky-tab"
                :class="{ active: activeTab === tab.id }"
                @click="scrollToSection(tab.id)"
              >
                {{ tab.label }}
              </button>
            </div>
            <a href="#" class="btn-primary-sm">立即使用</a>
          </div>
        </div>
      </div>

      <section ref="highlights" class="section" id="highlights">
        <div class="container">
          <div class="section-header">
            <div class="section-bar" :style="{ background: product.color }" />
            <div>
              <h2 class="section-title">核心优势</h2>
              <p class="section-subtitle">{{ product.name }} 的四大核心能力</p>
            </div>
          </div>
          <div class="highlights-grid">
            <div
              v-for="(h, idx) in product.detail.highlights"
              :key="idx"
              class="highlight-card"
            >
              <div class="highlight-num" :style="{ color: product.color }">
                {{ '0' + (idx + 1) }}
              </div>
              <h3 class="highlight-title">{{ h.title }}</h3>
              <p class="highlight-desc">{{ h.desc }}</p>
              <div class="highlight-line" :style="{ background: product.color }" />
            </div>
          </div>
        </div>
      </section>

      <section ref="specs" class="section section-alt" id="specs">
        <div class="container">
          <div class="section-header">
            <div class="section-bar" style="background: var(--color-accent)" />
            <div>
              <h2 class="section-title">产品规格</h2>
              <p class="section-subtitle">关键技术参数一览</p>
            </div>
          </div>
          <div class="specs-grid">
            <div
              v-for="(s, idx) in product.detail.specs"
              :key="idx"
              class="spec-card"
            >
              <div class="spec-icon-dot" :style="{ background: product.bgColor }">
                <VolcIcon name="check" :size="14" :color="product.color" />
              </div>
              <div class="spec-info">
                <span class="spec-label">{{ s.label }}</span>
                <span class="spec-value">{{ s.value }}</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section ref="scenarios" class="section" id="scenarios">
        <div class="container">
          <div class="section-header">
            <div class="section-bar" style="background: var(--color-yellow)" />
            <div>
              <h2 class="section-title">应用场景</h2>
              <p class="section-subtitle">探索 {{ product.name }} 的最佳实践场景</p>
            </div>
          </div>
          <div class="scenarios-grid">
            <div
              v-for="(sc, idx) in product.detail.scenarios"
              :key="idx"
              class="scenario-card"
            >
              <div class="scenario-num-bar">
                <div
                  class="scenario-num"
                  :style="{ background: scenarioColors[idx % 4] }"
                >
                  {{ '0' + (idx + 1) }}
                </div>
              </div>
              <h3 class="scenario-title">{{ sc.title }}</h3>
              <p class="scenario-desc">{{ sc.desc }}</p>
              <a href="#" class="scenario-link" :style="{ color: scenarioColors[idx % 4] }">
                了解方案
                <VolcIcon name="arrow-right" :size="14" />
              </a>
            </div>
          </div>
        </div>
      </section>

      <section ref="related" class="section section-alt" id="related">
        <div class="container">
          <div class="section-header">
            <div class="section-bar" style="background: var(--color-green)" />
            <div>
              <h2 class="section-title">相关产品</h2>
              <p class="section-subtitle">{{ category.name }} 分类下的其他产品</p>
            </div>
          </div>
          <div class="related-grid">
            <router-link
              v-for="r in relatedProducts"
              :key="r.slug"
              :to="'/sell/home/product/' + r.slug"
              class="related-card"
            >
              <div class="related-icon" :style="{ background: r.bgColor }">
                <VolcIcon :name="r.icon" :size="20" :color="r.color" />
              </div>
              <div class="related-info">
                <div class="flex items-center gap-2">
                  <span class="related-name">{{ r.name }}</span>
                  <span
                    v-if="r.tag"
                    :class="['related-tag', r.tag === 'HOT' ? 'tag-hot' : 'tag-new']"
                  >
                    {{ r.tag }}
                  </span>
                </div>
                <span class="related-desc">{{ r.desc }}</span>
              </div>
              <VolcIcon name="arrow-right" :size="16" class="related-arrow" />
            </router-link>
          </div>
        </div>
      </section>

      <section class="cta-section">
        <div class="cta-glow" />
        <div class="container cta-inner">
          <h2 class="cta-title">开始使用 {{ product.name }}</h2>
          <p class="cta-desc">{{ product.desc }}</p>
          <div class="cta-actions">
            <a href="#" class="btn-primary btn-lg">
              免费试用
              <VolcIcon name="arrow-right" :size="16" />
            </a>
            <a href="#" class="btn-secondary btn-lg">联系销售</a>
          </div>
        </div>
      </section>
    </template>

    <div v-else class="not-found">
      <div class="container not-found-inner">
        <VolcIcon name="search" :size="64" color="var(--text-muted)" />
        <h2 class="nf-title">产品未找到</h2>
        <p class="nf-desc">您访问的产品页面不存在，请检查链接是否正确</p>
        <router-link to="/sell/home/products" class="btn-primary">
          <VolcIcon name="arrow-right" :size="16" />
          返回产品列表
        </router-link>
      </div>
    </div>
    <FooterSection />
  </div>
</template>

<script>
import NavBar from '../../volc/NavBar.vue'
import FooterSection from '../../volc/FooterSection.vue'
import VolcIcon from '../../volc/SvgIcons.vue'
import { findProductBySlug } from '../../volc/data/products.js'

export default {
  name: 'ProductDetailPage',
  components: { NavBar, FooterSection, VolcIcon },
  props: {
    slug: {
      type: String,
      default: ''
    }
  },
  data() {
    return {
      product: null,
      category: null,
      relatedProducts: [],
      activeTab: 'highlights',
      showStickyNav: false,
      scenarioColors: [
        'var(--color-brand)',
        'var(--color-accent)',
        'var(--color-yellow)',
        'var(--color-green)'
      ],
      navTabs: [
        { id: 'highlights', label: '核心优势' },
        { id: 'specs', label: '产品规格' },
        { id: 'scenarios', label: '应用场景' },
        { id: 'related', label: '相关产品' }
      ]
    }
  },
  computed: {
    currentSlug() {
      return this.slug || this.$route.params.slug
    },
    glowColor() {
      if (!this.product) return 'rgba(51,112,255,0.1)'
      if (this.product.color.indexOf('brand') > -1) return 'rgba(51,112,255,0.12)'
      if (this.product.color.indexOf('accent') > -1) return 'rgba(20,201,201,0.12)'
      if (this.product.color.indexOf('yellow') > -1) return 'rgba(247,186,30,0.10)'
      if (this.product.color.indexOf('green') > -1) return 'rgba(159,219,29,0.10)'
      if (this.product.color.indexOf('red') > -1) return 'rgba(245,63,63,0.10)'
      return 'rgba(51,112,255,0.12)'
    }
  },
  watch: {
    currentSlug: {
      immediate: true,
      handler(slug) {
        this.loadProduct(slug)
      }
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    loadProduct(slug) {
      const result = findProductBySlug(slug)
      if (result) {
        this.product = result.product
        this.category = result.category
        this.relatedProducts = result.category.items.filter((item) => item.slug !== slug)
      } else {
        this.product = null
        this.category = null
        this.relatedProducts = []
      }
    },
    handleScroll() {
      this.showStickyNav = window.scrollY > 500
      const sections = ['related', 'scenarios', 'specs', 'highlights']
      for (let i = 0; i < sections.length; i++) {
        const el = this.$refs[sections[i]]
        if (el) {
          const rect = el.getBoundingClientRect()
          if (rect.top <= 180) {
            this.activeTab = sections[i]
            break
          }
        }
      }
    },
    scrollToSection(id) {
      const el = this.$refs[id]
      if (el) {
        const top = el.getBoundingClientRect().top + window.scrollY - 140
        window.scrollTo({ top, behavior: 'smooth' })
      }
    }
  }
}
</script>

<style src="../../volc/volc-main.css"></style>
<style scoped>
.product-detail {
  padding-top: 0;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.breadcrumb-bar {
  padding: 16px 0;
  border-bottom: 1px solid var(--border-color);
  background: var(--bg-secondary);
}

.breadcrumb {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--text-muted);
  flex-wrap: wrap;
}

.bc-link:hover {
  color: var(--text-primary);
}

.bc-sep {
  color: var(--border-color);
  font-size: 12px;
}

.bc-current {
  color: var(--text-secondary);
}

.detail-hero {
  position: relative;
  padding: 32px 0 36px;
  overflow: hidden;
  border-bottom: 1px solid var(--border-color);
}

.hero-glow {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(140px);
}

.hero-glow-1 {
  width: 700px;
  height: 700px;
  top: -300px;
  left: -200px;
}

.hero-glow-2 {
  width: 500px;
  height: 500px;
  top: -150px;
  right: -100px;
  background: rgba(20, 201, 201, 0.06);
}

.hero-inner {
  position: relative;
  display: flex;
  gap: 48px;
  align-items: center;
}

.hero-content {
  flex: 1;
  min-width: 0;
}

.hero-badges {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;
}

.hero-cat-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 4px 14px;
  border-radius: 100px;
  font-size: 12px;
  font-weight: 600;
}

.hero-tag {
  font-size: 11px;
  font-weight: 700;
  padding: 3px 10px;
  border-radius: 4px;
}

.hero-tag-hot {
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}

.hero-tag-new {
  background: rgba(20, 201, 201, 0.15);
  color: var(--color-accent);
}

.hero-title {
  font-size: 42px;
  font-weight: 800;
  color: var(--text-primary);
  line-height: 1.2;
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}

.hero-banner-text {
  font-size: 18px;
  font-weight: 600;
  color: var(--text-secondary);
  margin-bottom: 16px;
}

.hero-intro {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.8;
  margin-bottom: 24px;
  max-width: 600px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
}

.hero-visual {
  width: 340px;
  flex-shrink: 0;
}

.visual-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  padding: 36px 24px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
}

.visual-icon-wrap {
  width: 100px;
  height: 100px;
  border-radius: 28px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.visual-features {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 8px;
}

.visual-feature-chip {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 14px;
  border-radius: 100px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
}

.sticky-nav {
  position: sticky;
  top: 64px;
  z-index: 50;
  background: var(--bg-primary);
  border-bottom: 1px solid var(--border-color);
  transform: translateY(-100%);
  opacity: 0;
  pointer-events: none;
  transition: all 0.3s ease;
}

.sticky-nav-visible {
  transform: translateY(0);
  opacity: 1;
  pointer-events: auto;
}

.sticky-nav-inner {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 52px;
}

.sticky-tabs {
  display: flex;
  gap: 4px;
}

.sticky-tab {
  padding: 8px 18px;
  font-size: 13px;
  font-weight: 500;
  color: var(--text-muted);
  border-radius: 6px;
  transition: all 0.2s;
  background: none;
  font-family: inherit;
  border: none;
  cursor: pointer;
}

.sticky-tab:hover {
  color: var(--text-secondary);
}

.sticky-tab.active {
  color: var(--color-brand);
  background: rgba(51, 112, 255, 0.08);
}

.btn-primary-sm {
  display: inline-flex;
  align-items: center;
  padding: 6px 18px;
  font-size: 13px;
  background: var(--color-brand);
  color: #fff;
  border-radius: 6px;
  font-weight: 500;
  transition: background 0.2s;
}

.btn-primary-sm:hover {
  background: var(--color-brand-hover);
}

.section {
  padding: 32px 0;
}

.section-alt {
  background: var(--bg-secondary);
}

.section-bar {
  width: 4px;
  height: 32px;
  border-radius: 2px;
  flex-shrink: 0;
}

.section-header {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 32px;
}

.section-title {
  font-size: 28px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 6px;
}

.section-subtitle {
  font-size: 14px;
  color: var(--text-muted);
}

.highlights-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}

.highlight-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 24px;
  transition: all 0.3s;
  position: relative;
  overflow: hidden;
}

.highlight-card:hover {
  border-color: var(--border-hover);
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(0, 0, 0, 0.08);
}

.highlight-num {
  font-size: 36px;
  font-weight: 900;
  opacity: 0.15;
  line-height: 1;
  margin-bottom: 16px;
  font-variant-numeric: tabular-nums;
}

.highlight-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.highlight-desc {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.7;
}

.highlight-line {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  opacity: 0;
  transition: opacity 0.3s;
}

.highlight-card:hover .highlight-line {
  opacity: 1;
}

.specs-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.spec-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 18px;
  transition: all 0.2s;
}

.spec-card:hover {
  border-color: var(--border-hover);
}

.spec-icon-dot {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.spec-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.spec-label {
  font-size: 12px;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.spec-value {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
}

.scenarios-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 16px;
}

.scenario-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 20px;
  display: flex;
  flex-direction: column;
  transition: all 0.3s;
}

.scenario-card:hover {
  border-color: var(--border-hover);
  transform: translateY(-2px);
}

.scenario-num-bar {
  margin-bottom: 14px;
}

.scenario-num {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 10px;
  font-size: 13px;
  font-weight: 800;
  color: #fff;
}

.scenario-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 10px;
}

.scenario-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.7;
  flex: 1;
  margin-bottom: 14px;
}

.scenario-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  transition: gap 0.2s;
}

.scenario-link:hover {
  gap: 10px;
}

.related-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.related-card {
  display: flex;
  align-items: center;
  gap: 16px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 16px 18px;
  transition: all 0.2s;
}

.related-card:hover {
  border-color: var(--border-hover);
  background: var(--bg-card-hover);
}

.related-card:hover .related-arrow {
  color: var(--color-brand);
  transform: translateX(4px);
}

.related-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.related-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.related-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
}

.related-desc {
  font-size: 13px;
  color: var(--text-muted);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.related-tag {
  font-size: 10px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 3px;
  flex-shrink: 0;
}

.tag-hot {
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}

.tag-new {
  background: rgba(20, 201, 201, 0.15);
  color: var(--color-accent);
}

.related-arrow {
  color: var(--text-muted);
  flex-shrink: 0;
  transition: all 0.2s;
}

.cta-section {
  position: relative;
  padding: 32px 0;
  overflow: hidden;
  text-align: center;
  border-top: 1px solid var(--border-color);
}

.cta-glow {
  position: absolute;
  width: 600px;
  height: 600px;
  border-radius: 50%;
  top: -200px;
  left: 50%;
  transform: translateX(-50%);
  background: rgba(51, 112, 255, 0.08);
  filter: blur(120px);
  pointer-events: none;
}

.cta-inner {
  position: relative;
}

.cta-title {
  font-size: 32px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 12px;
}

.cta-desc {
  font-size: 15px;
  color: var(--text-muted);
  margin-bottom: 24px;
  max-width: 520px;
  margin-left: auto;
  margin-right: auto;
  line-height: 1.7;
}

.cta-actions {
  display: flex;
  justify-content: center;
  gap: 12px;
}

.btn-lg {
  padding: 12px 32px;
  font-size: 15px;
}

.not-found {
  padding-top: 64px;
  padding-bottom: 80px;
}

.not-found-inner {
  text-align: center;
  padding: 120px 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.nf-title {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
}

.nf-desc {
  font-size: 14px;
  color: var(--text-muted);
}

@media (max-width: 1024px) {
  .hero-visual {
    display: none;
  }
  .scenarios-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .specs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .hero-title {
    font-size: 28px;
  }
  .hero-banner-text {
    font-size: 16px;
  }
  .highlights-grid {
    grid-template-columns: 1fr;
  }
  .scenarios-grid {
    grid-template-columns: 1fr;
  }
  .specs-grid {
    grid-template-columns: 1fr;
  }
  .related-grid {
    grid-template-columns: 1fr;
  }
  .section {
    padding: 20px 0;
  }
  .detail-hero {
    padding: 18px 0 24px;
  }
  .cta-section {
    padding: 24px 0;
  }
  .section-title {
    font-size: 22px;
  }
  .cta-title {
    font-size: 24px;
  }
  .sticky-tabs {
    overflow-x: auto;
  }
}
</style>
