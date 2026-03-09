<template>
  <div id="volcengine-app" class="models-page">
    <NavBar />
    <main>
      <!-- Hero Banner -->
      <section class="page-hero">
        <div class="hero-glow hero-glow-1" />
        <div class="hero-glow hero-glow-2" />
        <div class="hero-glow hero-glow-3" />
        <div class="container" style="position: relative">
          <div class="hero-badge">
            <VolcIcon name="sparkles" :size="14" color="var(--color-brand)" />
            <span>豆包大模型生态</span>
          </div>
          <h1 class="page-title">豆包大模型</h1>
          <p class="page-subtitle">
            更强模型、更低价格、更易落地。体验字节跳动自研大模型的前沿能力，
            涵盖语言理解、视觉识别、语音交互、视频生成、图片创作等全模态能力。
          </p>
          <div class="hero-actions">
            <a href="#" class="btn-primary-lg">
              <VolcIcon name="sparkles" :size="16" />
              立即体验
            </a>
            <a href="#" class="btn-outline-lg">
              <VolcIcon name="book-open" :size="16" />
              技术文档
            </a>
          </div>
          <div class="hero-stats">
            <div class="stat-item">
              <span class="stat-num">1.6</span>
              <span class="stat-label">最新版本</span>
            </div>
            <div class="stat-divider" />
            <div class="stat-item">
              <span class="stat-num">50万+</span>
              <span class="stat-label">免费Tokens</span>
            </div>
            <div class="stat-divider" />
            <div class="stat-item">
              <span class="stat-num">6大</span>
              <span class="stat-label">模态能力</span>
            </div>
            <div class="stat-divider" />
            <div class="stat-item">
              <span class="stat-num">100+</span>
              <span class="stat-label">应用场景</span>
            </div>
          </div>
        </div>
      </section>

      <!-- Tab filter -->
      <section class="filter-section">
        <div class="container">
          <div class="filter-bar">
            <button
              v-for="tab in tabs"
              :key="tab.id"
              :class="['filter-tab', { active: activeTab === tab.id }]"
              @click="activeTab = tab.id"
            >
              <VolcIcon :name="tab.icon" :size="16" />
              {{ tab.label }}
            </button>
          </div>
        </div>
      </section>

      <!-- Models showcase -->
      <section class="models-showcase">
        <div class="container">
          <div v-if="activeTab === 'all' || activeTab === 'language'" class="featured-card">
            <div class="featured-grid">
              <div class="featured-content">
                <div class="flex items-center gap-3" style="margin-bottom: 8px">
                  <span class="featured-label">旗舰模型</span>
                  <span class="featured-tag">HOT</span>
                </div>
                <h2 class="featured-title">豆包大模型 1.6</h2>
                <p class="featured-desc">
                  全面升级的推理能力，强化多模态理解，支持GUI操作能力和前端页面编程能力。
                  在多项权威基准测试中达到业界领先水平，为企业和开发者提供更强大的AI基座。
                </p>
                <div class="featured-abilities">
                  <div class="ability-item">
                    <div class="ability-dot" style="background: var(--color-brand)" />
                    <span>超长上下文 128K</span>
                  </div>
                  <div class="ability-item">
                    <div class="ability-dot" style="background: var(--color-accent)" />
                    <span>复杂推理能力</span>
                  </div>
                  <div class="ability-item">
                    <div class="ability-dot" style="background: var(--color-yellow)" />
                    <span>代码生成与理解</span>
                  </div>
                  <div class="ability-item">
                    <div class="ability-dot" style="background: var(--color-green)" />
                    <span>多模态理解</span>
                  </div>
                </div>
                <div class="featured-btns">
                  <a href="#" class="btn-primary-lg">
                    开始使用
                    <VolcIcon name="arrow-right" :size="16" />
                  </a>
                  <a href="#" class="btn-outline-lg">查看定价</a>
                </div>
              </div>
              <div class="featured-visual">
                <div class="visual-orb">
                  <div class="orb-ring orb-ring-1" />
                  <div class="orb-ring orb-ring-2" />
                  <div class="orb-ring orb-ring-3" />
                  <div class="orb-core">
                    <VolcIcon name="brain" :size="48" color="var(--color-brand)" />
                  </div>
                </div>
              </div>
            </div>
          </div>

          <div class="models-grid-title">
            <h3>{{ activeTab === 'all' ? '全部模型' : currentTabLabel }}</h3>
            <span class="models-count">{{ filteredModels.length }} 款模型</span>
          </div>

          <div class="models-grid">
            <div
              v-for="(model, idx) in filteredModels"
              :key="idx"
              class="model-card"
            >
              <div class="model-card-header">
                <div class="model-icon" :style="{ background: model.bgColor }">
                  <VolcIcon :name="model.icon" :size="22" :color="model.color" />
                </div>
                <div class="model-meta">
                  <div class="flex items-center gap-2">
                    <h4 class="model-name">{{ model.name }}</h4>
                    <span
                      v-if="model.tag"
                      :class="['model-tag', model.tag === 'HOT' ? 'model-tag-hot' : 'model-tag-new']"
                    >
                      {{ model.tag }}
                    </span>
                  </div>
                  <span class="model-category">{{ model.category }}</span>
                </div>
              </div>
              <p class="model-desc">{{ model.description }}</p>
              <div class="model-highlights">
                <span v-for="(h, hi) in model.highlights" :key="hi" class="highlight-chip">{{ h }}</span>
              </div>
              <div v-if="model.pricing" class="model-pricing">
                <VolcIcon name="zap" :size="14" color="var(--color-yellow)" />
                <span>{{ model.pricing }}</span>
              </div>
              <div class="model-card-footer">
                <a href="#" class="model-link">
                  了解更多
                  <VolcIcon name="arrow-right" :size="14" />
                </a>
                <a href="#" class="model-try-btn">立即体验</a>
              </div>
            </div>
          </div>

          <div class="platform-section">
            <div class="platform-header">
              <div>
                <div class="flex items-center gap-3" style="margin-bottom: 8px">
                  <div
                    style="width: 4px; height: 24px; border-radius: 2px; background: var(--color-accent)"
                  />
                  <h3 class="platform-title">Agent 开发平台</h3>
                </div>
                <p class="platform-desc">从开发到部署，为你提供最便捷的 AI Agent 开发环境</p>
              </div>
            </div>
            <div class="platform-grid">
              <div
                v-for="(p, idx) in platforms"
                :key="idx"
                class="platform-card"
              >
                <div class="platform-card-top">
                  <div class="platform-icon" :style="{ background: p.bgColor }">
                    <VolcIcon :name="p.icon" :size="24" :color="p.color" />
                  </div>
                  <div class="platform-info">
                    <h4 class="platform-name">{{ p.name }}</h4>
                    <span class="platform-sub">{{ p.subtitle }}</span>
                  </div>
                </div>
                <p class="platform-card-desc">{{ p.description }}</p>
                <div class="platform-features">
                  <span v-for="(f, fi) in p.features" :key="fi" class="platform-feature-chip">{{ f }}</span>
                </div>
                <a href="#" class="platform-card-link">
                  立即体验
                  <VolcIcon name="arrow-right" :size="14" />
                </a>
              </div>
            </div>
          </div>

          <div class="cta-banner">
            <div class="cta-content">
              <h3 class="cta-title">开始使用豆包大模型</h3>
              <p class="cta-desc">
                每款豆包大语言模型提供 50 万 Tokens 免费额度，企业用户参与协作计划可获得 500 万 Tokens 免费额度
              </p>
            </div>
            <div class="cta-actions">
              <a href="#" class="btn-primary-lg">免费注册</a>
              <a href="#" class="btn-outline-lg">联系销售</a>
            </div>
          </div>
        </div>
      </section>
    </main>
    <FooterSection />
  </div>
</template>

<script>
import NavBar from './volc/NavBar.vue'
import FooterSection from './volc/FooterSection.vue'
import VolcIcon from './volc/SvgIcons.vue'

export default {
  name: 'ModelsPage',
  components: { NavBar, FooterSection, VolcIcon },
  data() {
    return {
      activeTab: 'all',
      tabs: [
        { id: 'all', label: '全部', icon: 'sparkles' },
        { id: 'language', label: '语言模型', icon: 'brain' },
        { id: 'vision', label: '视觉理解', icon: 'eye' },
        { id: 'video', label: '视频生成', icon: 'video' },
        { id: 'voice', label: '语音交互', icon: 'mic' },
        { id: 'image', label: '图片生成', icon: 'image' }
      ],
      models: [
        {
          name: '豆包大模型 1.6',
          category: '语言模型',
          type: 'language',
          tag: 'HOT',
          description:
            '全面升级的推理能力，强化多模态理解，支持GUI操作和前端编程。在多项权威基准测试中达到业界领先水平。',
          icon: 'brain',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)',
          highlights: ['128K上下文', '复杂推理', '代码生成', '函数调用'],
          pricing: '低至 0.0008元/千Tokens'
        },
        {
          name: '豆包大模型 1.6 Pro',
          category: '语言模型',
          type: 'language',
          tag: 'NEW',
          description: '在1.6基础上进一步提升，更强的推理与长文本处理能力，适合专业级应用场景。',
          icon: 'brain',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)',
          highlights: ['256K上下文', '极致推理', '专业创作', '结构化输出'],
          pricing: '低至 0.005元/千Tokens'
        },
        {
          name: '豆包 · 视频生成模型',
          category: '视频生成',
          type: 'video',
          tag: 'NEW',
          description: '将文本、图像生成高质量视频，能够生成具备丰富细节层次的影视级视频，支持多种分辨率和时长。',
          icon: 'video',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)',
          highlights: ['影视级画质', '多分辨率', '文/图生视频', '运镜控制'],
          pricing: '按视频时长计费'
        },
        {
          name: '豆包 · 视觉理解模型',
          category: '视觉理解',
          type: 'vision',
          tag: 'NEW',
          description: '对视觉内容有更强的识别能力，更强理解和推理能力，以及更细腻的视觉描述能力。',
          icon: 'eye',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)',
          highlights: ['图片理解', 'OCR识别', '视觉推理', '多图对比'],
          pricing: '低至 0.003元/千Tokens'
        },
        {
          name: '豆包 · 实时语音模型',
          category: '语音交互',
          type: 'voice',
          description: '真正的端到端语音模型，通过自然语言进行多种高级指令控制，具备超拟人交互能力。',
          icon: 'mic',
          color: 'var(--color-green)',
          bgColor: 'rgba(159,219,29,0.1)',
          highlights: ['端到端', '超低延迟', '情感表达', '多语种'],
          pricing: '按通话时长计费'
        },
        {
          name: '豆包 · 文生图模型',
          category: '图片生成',
          type: 'image',
          description: '快速生成精美写真，支持50余种风格变换，并对图片实现扩图、重绘等创意延展。',
          icon: 'image',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)',
          highlights: ['50+风格', '高清生成', '图片编辑', '风格迁移'],
          pricing: '低至 0.04元/张'
        }
      ],
      platforms: [
        {
          name: '羿贝方舟',
          subtitle: '一站式大模型开发平台',
          icon: 'layers',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)',
          description:
            '体验超全模型，每款豆包大语言模型提供50万Tokens免费额度。支持模型推理、定制微调、Prompt优化等全链路能力。',
          features: ['智能广场', '模型推理', '模型定制', 'PromptPilot', '应用实验室']
        },
        {
          name: '扣子 (Coze)',
          subtitle: 'AI Agent 开发工具',
          icon: 'bot',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)',
          description:
            '提供各类最新大模型和工具、多种开发模式和框架，从开发到部署，为你提供最便捷的 Agent 开发环境。',
          features: ['工作流编排', '知识库管理', '插件市场', '一键部署', '效果评估']
        },
        {
          name: 'HiAgent',
          subtitle: '企业 AI 中台',
          icon: 'workflow',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)',
          description:
            '提供Agent全生命周期管理，支持接入各类模型服务，支持私有化安全集成，助力构建生产级高价值智能体。',
          features: ['Agent管理', '模型接入', '安全集成', '企业治理', '效能分析']
        }
      ]
    }
  },
  computed: {
    currentTabLabel() {
      const tab = this.tabs.find((t) => t.id === this.activeTab)
      return tab ? tab.label : ''
    },
    filteredModels() {
      if (this.activeTab === 'all') return this.models
      return this.models.filter((m) => m.type === this.activeTab)
    }
  }
}
</script>

<style src="./volc/volc-main.css"></style>
<style scoped>
.models-page {
  padding-top: 0;
  background-color: var(--bg-primary);
  color: var(--text-primary);
  min-height: 100vh;
}

.page-hero {
  position: relative;
  padding: 72px 0 48px;
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
  left: 10%;
  background: rgba(51, 112, 255, 0.1);
}

.hero-glow-2 {
  width: 400px;
  height: 400px;
  top: -50px;
  right: 10%;
  background: rgba(20, 201, 201, 0.08);
}

.hero-glow-3 {
  width: 300px;
  height: 300px;
  bottom: -100px;
  left: 40%;
  background: rgba(247, 186, 30, 0.05);
}

.hero-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 16px;
  background: rgba(51, 112, 255, 0.08);
  border: 1px solid rgba(51, 112, 255, 0.2);
  border-radius: 100px;
  font-size: 13px;
  color: var(--color-brand);
  font-weight: 500;
  margin-bottom: 24px;
}

.page-title {
  font-size: 48px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 16px;
  letter-spacing: -1px;
}

.page-subtitle {
  font-size: 16px;
  color: var(--text-muted);
  line-height: 1.8;
  max-width: 680px;
  margin-bottom: 32px;
}

.hero-actions {
  display: flex;
  gap: 12px;
  margin-bottom: 40px;
}

.btn-primary-lg {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: var(--color-brand);
  color: #fff;
  padding: 12px 28px;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 600;
  transition: background 0.2s;
}

.btn-primary-lg:hover {
  background: var(--color-brand-hover);
}

.btn-outline-lg {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  background: transparent;
  color: var(--text-secondary);
  padding: 12px 28px;
  border-radius: var(--radius-md);
  font-size: 15px;
  font-weight: 500;
  border: 1px solid var(--border-color);
  transition: all 0.2s;
}

.btn-outline-lg:hover {
  border-color: var(--color-brand);
  color: var(--color-brand);
}

.hero-stats {
  display: flex;
  gap: 40px;
  align-items: center;
}

.stat-item {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.stat-num {
  font-size: 28px;
  font-weight: 800;
  color: var(--text-primary);
}

.stat-label {
  font-size: 13px;
  color: var(--text-muted);
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: var(--border-color);
}

.filter-section {
  padding: 16px 0;
  border-bottom: 1px solid var(--border-color);
  position: sticky;
  top: 64px;
  background: var(--bg-primary);
  z-index: 50;
}

.filter-bar {
  display: flex;
  gap: 8px;
  overflow-x: auto;
  scrollbar-width: none;
}

.filter-bar::-webkit-scrollbar {
  display: none;
}

.filter-tab {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 20px;
  border-radius: 100px;
  font-size: 14px;
  font-weight: 500;
  white-space: nowrap;
  transition: all 0.2s;
  border: 1px solid transparent;
  cursor: pointer;
  font-family: inherit;
  color: var(--text-muted);
  background: var(--bg-secondary);
}

.filter-tab:hover {
  color: var(--text-secondary);
  background: var(--bg-card);
}

.filter-tab.active {
  background: var(--color-brand);
  color: #fff;
  border-color: var(--color-brand);
}

.models-showcase {
  padding: 40px 0 64px;
}

.featured-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  padding: 40px;
  margin-bottom: 36px;
  overflow: hidden;
  position: relative;
}

.featured-grid {
  display: flex;
  gap: 40px;
  align-items: center;
}

.featured-content {
  flex: 1;
  min-width: 0;
}

.featured-label {
  font-size: 12px;
  font-weight: 600;
  color: var(--color-brand);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.featured-tag {
  font-size: 10px;
  font-weight: 700;
  padding: 2px 8px;
  border-radius: 4px;
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}

.featured-title {
  font-size: 32px;
  font-weight: 800;
  color: var(--text-primary);
  margin-bottom: 16px;
}

.featured-desc {
  font-size: 15px;
  color: var(--text-muted);
  line-height: 1.8;
  margin-bottom: 24px;
}

.featured-abilities {
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 24px;
}

.ability-item {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: var(--text-secondary);
}

.ability-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  flex-shrink: 0;
}

.featured-btns {
  display: flex;
  gap: 12px;
}

.featured-visual {
  width: 320px;
  height: 320px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
}

.visual-orb {
  width: 240px;
  height: 240px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.orb-ring {
  position: absolute;
  border-radius: 50%;
  border: 1px solid;
  animation: orbPulse 4s ease-in-out infinite;
}

.orb-ring-1 {
  width: 100%;
  height: 100%;
  border-color: rgba(51, 112, 255, 0.15);
}

.orb-ring-2 {
  width: 75%;
  height: 75%;
  border-color: rgba(51, 112, 255, 0.25);
  animation-delay: 0.5s;
}

.orb-ring-3 {
  width: 50%;
  height: 50%;
  border-color: rgba(51, 112, 255, 0.35);
  animation-delay: 1s;
}

.orb-core {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: rgba(51, 112, 255, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1;
}

@keyframes orbPulse {
  0%,
  100% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(1.05);
    opacity: 0.6;
  }
}

.models-grid-title {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 20px;
}

.models-grid-title h3 {
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
}

.models-count {
  font-size: 12px;
  color: var(--text-muted);
  background: var(--bg-card);
  padding: 2px 10px;
  border-radius: 100px;
}

.models-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 48px;
}

.model-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 20px;
  transition: all 0.25s;
  display: flex;
  flex-direction: column;
}

.model-card:hover {
  border-color: rgba(51, 112, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.model-card-header {
  display: flex;
  align-items: flex-start;
  gap: 14px;
  margin-bottom: 14px;
}

.model-icon {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.model-meta {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.model-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
}

.model-category {
  font-size: 12px;
  color: var(--text-muted);
}

.model-tag {
  font-size: 10px;
  font-weight: 600;
  padding: 2px 6px;
  border-radius: 4px;
  white-space: nowrap;
  flex-shrink: 0;
  line-height: 1.4;
}

.model-tag-hot {
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}

.model-tag-new {
  background: rgba(20, 201, 201, 0.15);
  color: var(--color-accent);
}

.model-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 14px;
}

.model-highlights {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 14px;
}

.highlight-chip {
  font-size: 11px;
  color: var(--text-secondary);
  background: rgba(255, 255, 255, 0.5);
  border: 1px solid var(--border-color);
  padding: 3px 10px;
  border-radius: 100px;
}

.model-pricing {
  display: flex;
  align-items: center;
  gap: 6px;
  font-size: 12px;
  color: var(--color-yellow);
  margin-bottom: 14px;
  padding: 8px 12px;
  background: rgba(247, 186, 30, 0.08);
  border-radius: 8px;
}

.model-card-footer {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 14px;
  border-top: 1px solid var(--border-color);
  margin-top: auto;
}

.model-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-brand);
  transition: gap 0.2s;
}

.model-link:hover {
  gap: 10px;
}

.model-try-btn {
  font-size: 12px;
  color: var(--text-muted);
  padding: 4px 14px;
  border: 1px solid var(--border-color);
  border-radius: 6px;
  transition: all 0.2s;
}

.model-try-btn:hover {
  border-color: var(--color-brand);
  color: var(--color-brand);
}

.platform-section {
  margin-bottom: 48px;
}

.platform-header {
  margin-bottom: 20px;
}

.platform-title {
  font-size: 22px;
  font-weight: 700;
  color: var(--text-primary);
}

.platform-desc {
  font-size: 14px;
  color: var(--text-muted);
  margin-top: 4px;
}

.platform-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

.platform-card {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-lg);
  padding: 24px;
  transition: all 0.25s;
}

.platform-card:hover {
  border-color: rgba(51, 112, 255, 0.3);
}

.platform-card-top {
  display: flex;
  align-items: center;
  gap: 14px;
  margin-bottom: 14px;
}

.platform-icon {
  width: 48px;
  height: 48px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.platform-info {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.platform-name {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
}

.platform-sub {
  font-size: 12px;
  color: var(--text-muted);
}

.platform-card-desc {
  font-size: 13px;
  color: var(--text-muted);
  line-height: 1.7;
  margin-bottom: 16px;
}

.platform-features {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 16px;
}

.platform-feature-chip {
  font-size: 11px;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  border: 1px solid var(--border-color);
  padding: 4px 10px;
  border-radius: 6px;
}

.platform-card-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-brand);
  transition: gap 0.2s;
}

.platform-card-link:hover {
  gap: 10px;
}

.cta-banner {
  background: var(--bg-card);
  border: 1px solid var(--border-color);
  border-radius: var(--radius-xl);
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  position: relative;
  overflow: hidden;
}

.cta-content {
  position: relative;
}

.cta-title {
  font-size: 24px;
  font-weight: 700;
  color: var(--text-primary);
  margin-bottom: 8px;
}

.cta-desc {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.6;
  max-width: 560px;
}

.cta-actions {
  display: flex;
  gap: 12px;
  flex-shrink: 0;
  position: relative;
}

@media (max-width: 1024px) {
  .models-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .platform-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .featured-visual {
    display: none;
  }
}

@media (max-width: 768px) {
  .page-title {
    font-size: 32px;
  }
  .models-grid {
    grid-template-columns: 1fr;
  }
  .platform-grid {
    grid-template-columns: 1fr;
  }
  .featured-card {
    padding: 20px;
  }
  .featured-title {
    font-size: 24px;
  }
  .hero-stats {
    flex-wrap: wrap;
    gap: 24px;
  }
  .stat-divider {
    display: none;
  }
  .cta-banner {
    flex-direction: column;
    padding: 28px;
    align-items: flex-start;
  }
  .hero-actions {
    flex-direction: column;
  }
  .page-hero {
    padding: 52px 0 32px;
  }
  .filter-section {
    top: 0;
  }
}
</style>
