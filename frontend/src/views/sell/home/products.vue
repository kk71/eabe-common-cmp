<template>
  <div id="volcengine-app" class="products-page">
    <NavBar />
    <main>
      <!-- Hero Banner -->
      <section class="page-hero">
        <div class="hero-glow hero-glow-1" />
        <div class="hero-glow hero-glow-2" />
        <div class="container" style="position: relative">
          <h1 class="page-title">全栈云产品</h1>
          <p class="page-subtitle">
            从计算、存储、网络到数据库、大数据、安全，羿贝引擎提供全栈基础云服务，为业务增长保驾护航
          </p>
          <div class="search-bar">
            <VolcIcon name="search" :size="18" color="var(--text-muted)" />
            <input
              v-model="searchQuery"
              type="text"
              placeholder="搜索产品名称或关键词..."
              class="search-input"
            />
            <span v-if="searchQuery" class="search-clear" @click="searchQuery = ''">
              <VolcIcon name="x" :size="16" />
            </span>
          </div>
        </div>
      </section>

      <!-- Category Sidebar + Products Grid -->
      <section class="products-body">
        <div class="container">
          <div class="products-layout">
            <aside class="sidebar">
              <div
                v-for="cat in categories"
                :key="cat.id"
                class="sidebar-item"
                :class="{ active: activeCat === cat.id }"
                @click="scrollToCategory(cat.id)"
              >
                <div class="sidebar-icon" :style="{ background: cat.bgColor }">
                  <VolcIcon :name="cat.icon" :size="16" :color="cat.color" />
                </div>
                <div class="sidebar-info">
                  <span class="sidebar-name">{{ cat.name }}</span>
                  <span class="sidebar-count">{{ cat.items.length }} 款产品</span>
                </div>
              </div>
            </aside>

            <div class="products-content">
              <div
                v-for="cat in filteredCategories"
                :key="cat.id"
                :ref="(el) => setCatRef(cat.id, el)"
                class="cat-section"
              >
                <div class="cat-header">
                  <div class="cat-header-left">
                    <div class="cat-bar" :style="{ background: cat.color }" />
                    <h2 class="cat-title">{{ cat.name }}</h2>
                    <span class="cat-count">{{ cat.items.length }}</span>
                  </div>
                  <span class="cat-desc">{{ cat.desc }}</span>
                </div>
                <div class="cat-grid">
                  <div
                    v-for="(item, idx) in cat.items"
                    :key="idx"
                    class="product-card"
                  >
                    <div class="product-card-top">
                      <div class="product-icon" :style="{ background: item.bgColor }">
                        <VolcIcon :name="item.icon" :size="20" :color="item.color" />
                      </div>
                      <div class="product-info">
                        <div class="flex items-center gap-2">
                          <h3 class="product-name">{{ item.name }}</h3>
                          <span
                            v-if="item.tag"
                            :class="[
                              'product-tag',
                              item.tag === 'HOT' ? 'product-tag-hot' : 'product-tag-new'
                            ]"
                          >
                            {{ item.tag }}
                          </span>
                        </div>
                        <p class="product-desc">{{ item.desc }}</p>
                      </div>
                    </div>
                    <div v-if="item.features" class="product-features">
                      <span v-for="(f, fi) in item.features" :key="fi" class="feature-chip">{{ f }}</span>
                    </div>
                    <div class="product-actions">
                      <router-link :to="'/sell/home/product/' + item.slug" class="product-link">
                        了解详情
                        <VolcIcon name="arrow-right" :size="14" />
                      </router-link>
                      <router-link :to="'/sell/home/product/' + item.slug" class="product-try">
                        立即使用
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
              <div v-if="filteredCategories.length === 0" class="empty-state">
                <VolcIcon name="search" :size="48" color="var(--text-muted)" />
                <p>未找到匹配的产品</p>
                <button class="reset-btn" @click="searchQuery = ''">清除搜索</button>
              </div>
            </div>
          </div>
        </div>
      </section>
    </main>
    <FooterSection />
  </div>
</template>

<script>
import NavBar from '../volc/NavBar.vue'
import FooterSection from '../volc/FooterSection.vue'
import VolcIcon from '../volc/SvgIcons.vue'
import { productsData } from '../volc/data/products.js'

export default {
  name: 'ProductsPage',
  components: { NavBar, FooterSection, VolcIcon },
  data() {
    return {
      searchQuery: '',
      activeCat: 'compute',
      categories: productsData,
      catRefs: {}
    }
  },
  computed: {
    filteredCategories() {
      const query = this.searchQuery.toLowerCase().trim()
      if (!query) return this.categories
      return this.categories
        .map((cat) => {
          const filtered = cat.items.filter(
            (item) =>
              item.name.toLowerCase().indexOf(query) !== -1 ||
              item.desc.toLowerCase().indexOf(query) !== -1
          )
          if (filtered.length === 0) return null
          return { ...cat, items: filtered }
        })
        .filter(Boolean)
    }
  },
  methods: {
    setCatRef(id, el) {
      if (el) {
        this.catRefs[id] = el
      }
    },
    scrollToCategory(id) {
      this.activeCat = id
      const el = this.catRefs[id]
      if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' })
      }
    }
  }
}
</script>

<style src="../volc/volc-main.css"></style>
<style scoped>
.products-page {
  padding-top: 0;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.page-hero {
  position: relative;
  padding: 64px 0 32px;
  overflow: hidden;
  border-bottom: 1px solid var(--border-color);
}

.hero-glow {
  position: absolute;
  border-radius: 50%;
  pointer-events: none;
  filter: blur(120px);
}

.hero-glow-1 {
  width: 600px;
  height: 600px;
  top: -200px;
  left: -100px;
  background: rgba(51, 112, 255, 0.08);
}

.hero-glow-2 {
  width: 400px;
  height: 400px;
  top: -100px;
  right: -50px;
  background: rgba(20, 201, 201, 0.06);
}

.page-title {
  font-size: 40px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}

.page-subtitle {
  font-size: 16px;
  color: var(--text-muted);
  line-height: 1.7;
  max-width: 640px;
  margin-bottom: 32px;
}

.search-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-md);
  padding: 12px 20px;
  max-width: 480px;
  transition: border-color 0.2s;
}

.search-bar:focus-within {
  border-color: var(--color-brand);
}

.search-input {
  flex: 1;
  background: none;
  border: none;
  outline: none;
  color: var(--text-primary);
  font-size: 14px;
  font-family: inherit;
}

.search-input::placeholder {
  color: var(--text-muted);
}

.search-clear {
  cursor: pointer;
  color: var(--text-muted);
  transition: color 0.2s;
  display: flex;
}

.search-clear:hover {
  color: var(--text-primary);
}

.products-body {
  padding: 28px 0 56px;
}

.products-layout {
  display: flex;
  gap: 32px;
}

.sidebar {
  width: 240px;
  flex-shrink: 0;
  position: sticky;
  top: 104px;
  align-self: flex-start;
  display: flex;
  flex-direction: column;
  gap: 4px;
  max-height: calc(100vh - 120px);
  overflow-y: auto;
}

.sidebar-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 8px 12px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
}

.sidebar-item:hover {
  background: rgba(255, 255, 255, 0.5);
}

.sidebar-item.active {
  background: rgba(51, 112, 255, 0.08);
}

.sidebar-item.active .sidebar-name {
  color: var(--color-brand);
  font-weight: 600;
}

.sidebar-icon {
  width: 32px;
  height: 32px;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.sidebar-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.sidebar-name {
  font-size: 14px;
  font-weight: 500;
  color: var(--text-secondary);
  transition: color 0.2s;
}

.sidebar-count {
  font-size: 12px;
  color: var(--text-muted);
}

.products-content {
  flex: 1;
  min-width: 0;
}

.cat-section {
  margin-bottom: 40px;
  scroll-margin-top: 104px;
}

.cat-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid var(--border-color);
}

.cat-header-left {
  display: flex;
  align-items: center;
  gap: 12px;
}

.cat-bar {
  width: 4px;
  height: 24px;
  border-radius: 2px;
  flex-shrink: 0;
}

.cat-title {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
}

.cat-count {
  font-size: 12px;
  color: var(--text-muted);
  background: var(--bg-card);
  padding: 2px 8px;
  border-radius: 100px;
}

.cat-desc {
  font-size: 13px;
  color: var(--text-muted);
}

.cat-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}

.product-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 18px;
  transition: all 0.25s;
  display: flex;
  flex-direction: column;
}

.product-card:hover {
  border-color: rgba(51, 112, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.08);
}

.product-card-top {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  margin-bottom: 12px;
}

.product-icon {
  width: 44px;
  height: 44px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.product-info {
  flex: 1;
  min-width: 0;
}

.product-name {
  font-size: 15px;
  font-weight: 600;
  color: var(--text-primary);
}

.product-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-top: 6px;
}

.product-tag {
  font-size: 10px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 4px;
  white-space: nowrap;
  flex-shrink: 0;
  line-height: 1.4;
}

.product-tag-hot {
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}

.product-tag-new {
  background: rgba(20, 201, 201, 0.15);
  color: var(--color-accent);
}

.product-features {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 12px;
}

.feature-chip {
  font-size: 11px;
  color: var(--text-muted);
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid var(--border-color);
  padding: 3px 10px;
  border-radius: 100px;
}

.product-actions {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-top: auto;
  padding-top: 12px;
  border-top: 1px solid var(--border-color);
}

.product-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-brand);
  transition: gap 0.2s;
}

.product-link:hover {
  gap: 10px;
}

.product-try {
  font-size: 12px;
  color: var(--text-muted);
  padding: 4px 12px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  transition: all 0.2s;
}

.product-try:hover {
  border-color: var(--color-brand);
  color: var(--color-brand);
}

.empty-state {
  text-align: center;
  padding: 80px 0;
  color: var(--text-muted);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
}

.empty-state p {
  font-size: 16px;
}

.reset-btn {
  font-size: 14px;
  color: var(--color-brand);
  background: none;
  border: 1px solid var(--color-brand);
  border-radius: 8px;
  padding: 8px 20px;
  cursor: pointer;
  transition: all 0.2s;
  font-family: inherit;
}

.reset-btn:hover {
  background: rgba(51, 112, 255, 0.1);
}

@media (max-width: 1024px) {
  .sidebar {
    display: none;
  }
  .products-layout {
    flex-direction: column;
  }
}

@media (max-width: 768px) {
  .page-title {
    font-size: 28px;
  }
  .cat-grid {
    grid-template-columns: 1fr;
  }
  .cat-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  .page-hero {
    padding: 56px 0 32px;
  }
}
</style>
