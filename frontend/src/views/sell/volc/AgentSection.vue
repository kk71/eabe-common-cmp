<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 500px;
        height: 500px;
        top: 0;
        right: -100px;
        background: rgba(20, 201, 201, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Header -->
      <div style="margin-bottom: 48px">
        <div class="flex items-center gap-3" style="margin-bottom: 16px">
          <div class="section-bar" style="background: var(--color-accent)"></div>
          <h2 class="section-title">Agent 开发平台与精选 AI 应用</h2>
        </div>
      </div>

      <!-- Platform Tabs -->
      <div class="tab-bar" style="margin-bottom: 32px">
        <button
          v-for="p in platforms"
          :key="p.id"
          :class="['tab-item', { active: activePlatform === p.id }]"
          @click="activePlatform = p.id"
        >
          {{ p.name }}
        </button>
      </div>

      <!-- Platform Content -->
      <div class="card platform-content" style="margin-bottom: 32px">
        <div class="platform-grid">
          <div class="flex-1">
            <div class="flex items-center gap-3" style="margin-bottom: 8px">
              <h3
                style="
                  font-size: 20px;
                  font-weight: 700;
                  color: var(--text-primary);
                "
              >
                {{ currentPlatform.name }}
              </h3>
              <span class="platform-badge">
                {{ currentPlatform.subtitle }}
              </span>
            </div>
            <p
              style="
                font-size: 14px;
                color: var(--text-muted);
                line-height: 1.7;
                margin-bottom: 24px;
                max-width: 540px;
              "
            >
              {{ currentPlatform.description }}
            </p>
            <div class="flex flex-wrap gap-2" style="margin-bottom: 32px">
              <span
                v-for="(f, i) in currentPlatform.features"
                :key="i"
                class="feature-tag"
              >
                {{ f }}
              </span>
            </div>
            <a href="#" class="btn-primary">
              立即体验
              <SvgIcon name="arrow-right" :size="16" />
            </a>
          </div>
          <div class="platform-preview">
            <div style="text-align: center">
              <div
                class="icon-box"
                :style="{
                  width: '64px',
                  height: '64px',
                  borderRadius: '16px',
                  margin: '0 auto 16px',
                  background:
                    currentPlatform.id === 'ark'
                      ? 'rgba(51,112,255,0.1)'
                      : currentPlatform.id === 'coze'
                      ? 'rgba(20,201,201,0.1)'
                      : 'rgba(247,186,30,0.1)'
                }"
              >
                <SvgIcon
                  name="layers"
                  :size="32"
                  :color="
                    currentPlatform.id === 'ark'
                      ? 'var(--color-brand)'
                      : currentPlatform.id === 'coze'
                      ? 'var(--color-accent)'
                      : 'var(--color-yellow)'
                  "
                />
              </div>
              <p
                style="
                  font-size: 18px;
                  font-weight: 600;
                  color: var(--text-primary);
                "
              >
                {{ currentPlatform.name }}
              </p>
              <p
                style="
                  font-size: 14px;
                  color: var(--text-muted);
                  margin-top: 4px;
                "
              >
                {{ currentPlatform.subtitle }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Agent Cards -->
      <div class="agents-grid">
        <a
          v-for="(agent, idx) in agents"
          :key="idx"
          href="#"
          class="card agent-card"
        >
          <div
            class="icon-box"
            :style="{
              width: '40px',
              height: '40px',
              borderRadius: '10px',
              marginBottom: '16px',
              background: agent.bgColor
            }"
          >
            <SvgIcon :name="agent.icon" :size="20" :color="agent.color" />
          </div>
          <h4
            style="
              font-size: 14px;
              font-weight: 600;
              color: var(--text-primary);
              margin-bottom: 8px;
            "
          >
            {{ agent.name }}
          </h4>
          <p
            style="font-size: 12px; color: var(--text-muted); line-height: 1.6"
            class="line-clamp-3"
          >
            {{ agent.description }}
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
            立即体验
            <SvgIcon name="arrow-right" :size="12" />
          </div>
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import SvgIcon from './SvgIcons.vue'

export default {
  name: 'AgentSection',
  components: { SvgIcon },
  data() {
    return {
      activePlatform: 'ark',
      platforms: [
        {
          id: 'ark',
          name: '火山方舟',
          subtitle: '一站式大模型开发平台',
          description:
            '体验超全模型，每款豆包大语言模型提供50万Tokens免费额度，企业用户参与协作计划可获得500万Tokens免费额度。',
          features: [
            '智能广场',
            '模型推理',
            '模型定制',
            'PromptPilot',
            '应用实验室',
            '系统管理'
          ]
        },
        {
          id: 'coze',
          name: '扣子',
          subtitle: '一站式 AI Agent 开发工具',
          description:
            '提供各类最新大模型和工具、多种开发模式和框架，从开发到部署，为你提供最便捷的 AI Agent 开发环境。',
          features: [
            '大模型接入',
            '工作流编排',
            '知识库管理',
            '插件市场',
            '一键部署',
            '效果评估'
          ]
        },
        {
          id: 'hiagent',
          name: 'HiAgent',
          subtitle: '企业 AI 中台',
          description:
            '提供Agent全生命周期管理，支持接入各类模型服务，支持私有化安全集成，助力构建生产级高价值智能体。',
          features: ['Agent管理', '模型接入', '安全集成', '企业治理', '数据管理', '效能分析']
        }
      ],
      agents: [
        {
          icon: 'bot',
          name: 'AgentKit',
          description:
            '模拟各类OS环境中完成开放式任务的通用Agent解决方案，助力打造专属通用Agent',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: 'layers',
          name: 'Data Agent',
          description:
            '新一代企业级AI数字专家，深度理解和运用企业数据资产，持续释放数据价值',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)'
        },
        {
          icon: 'shield',
          name: '安全智能体',
          description:
            '7x24小时全自动威胁研判，AI智能处理全量告警，精准挖掘隐匿攻击',
          color: 'var(--color-red)',
          bgColor: 'rgba(245,63,63,0.1)'
        },
        {
          icon: 'book-open',
          name: 'AI 知识管理',
          description:
            '多模态内容理解、可交互推理过程、个性化探索指南，你的知识管理专家',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)'
        },
        {
          icon: 'languages',
          name: 'AI 视频翻译',
          description:
            '视频点播多模态翻译解决方案，一键实现字幕、配音、人物口型翻译',
          color: 'var(--color-green)',
          bgColor: 'rgba(159,219,29,0.1)'
        }
      ]
    }
  },
  computed: {
    currentPlatform() {
      const id = this.activePlatform
      return this.platforms.find((p) => p.id === id) || this.platforms[0]
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
.platform-content {
  padding: 40px;
}
.platform-grid {
  display: flex;
  gap: 32px;
}
.platform-preview {
  width: 400px;
  flex-shrink: 0;
  background: rgba(26, 35, 50, 0.5);
  border-radius: var(--radius-lg);
  border: 1px solid var(--border-color);
  padding: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 220px;
}
.platform-badge {
  font-size: 12px;
  color: var(--text-muted);
  background: var(--bg-card);
  padding: 4px 10px;
  border-radius: 6px;
}
.feature-tag {
  font-size: 12px;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  padding: 6px 12px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
}
.agents-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 16px;
}
.agent-card {
  padding: 20px;
}

@media (max-width: 1024px) {
  .agents-grid {
    grid-template-columns: repeat(3, 1fr);
  }
  .platform-preview {
    display: none;
  }
  .platform-grid {
    flex-direction: column;
  }
}
@media (max-width: 768px) {
  .agents-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .platform-content {
    padding: 24px;
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

