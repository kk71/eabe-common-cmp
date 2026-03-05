<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 400px;
        height: 400px;
        top: 30%;
        right: -80px;
        background: rgba(20, 201, 201, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Header -->
      <div style="margin-bottom: 48px">
        <div class="flex items-center gap-3" style="margin-bottom: 16px">
          <div class="section-bar" style="background: var(--color-green)"></div>
          <h2 class="section-title">多样的大模型应用场景</h2>
        </div>
      </div>

      <!-- Scenario Tabs -->
      <div class="tab-bar" style="margin-bottom: 40px">
        <button
          v-for="tab in scenarioTabs"
          :key="tab.id"
          :class="['tab-item', { active: activeScenario === tab.id }]"
          @click="activeScenario = tab.id"
          style="display: flex; align-items: center; gap: 8px"
        >
          <VolcIcon :name="tab.icon" :size="16" />
          {{ tab.label }}
        </button>
      </div>

      <!-- Scenario Content -->
      <div class="features-grid" style="margin-bottom: 32px">
        <div
          v-for="(feature, idx) in currentContent.features"
          :key="idx"
          class="card feature-card"
        >
          <div class="flex items-center gap-3" style="margin-bottom: 16px">
            <div
              class="icon-box"
              :style="{
                width: '32px',
                height: '32px',
                borderRadius: '8px',
                fontSize: '14px',
                fontWeight: '700',
                background:
                  idx === 0
                    ? 'rgba(51,112,255,0.1)'
                    : idx === 1
                    ? 'rgba(20,201,201,0.1)'
                    : 'rgba(247,186,30,0.1)',
                color:
                  idx === 0
                    ? 'var(--color-brand)'
                    : idx === 1
                    ? 'var(--color-accent)'
                    : 'var(--color-yellow)'
              }"
            >
              {{ String(idx + 1).padStart(2, '0') }}
            </div>
            <h4
              style="
                font-size: 15px;
                font-weight: 600;
                color: var(--text-primary);
              "
            >
              {{ feature.title }}
            </h4>
          </div>
          <p
            style="font-size: 14px; color: var(--text-muted); line-height: 1.7"
          >
            {{ feature.description }}
          </p>
        </div>
      </div>

      <!-- Related Products -->
      <div class="flex flex-wrap items-center gap-3">
        <span style="font-size: 14px; color: var(--text-muted)">
          相关产品与解决方案
        </span>
        <a
          v-for="(product, idx) in currentContent.products"
          :key="idx"
          href="#"
          class="product-link"
        >
          {{ product }}
          <VolcIcon name="arrow-right" :size="14" />
        </a>
      </div>
    </div>
  </section>
</template>

<script>
import VolcIcon from './SvgIcons.vue'

export default {
  name: 'ScenariosSection',
  components: { VolcIcon },
  data() {
    return {
      activeScenario: 'social',
      scenarioTabs: [
        { id: 'social', label: '社交娱乐', icon: 'message-circle' },
        { id: 'hardware', label: '硬件助手', icon: 'gamepad' },
        { id: 'education', label: '学习教育', icon: 'graduation-cap' },
        { id: 'service', label: '客服与销售', icon: 'headphones' },
        { id: 'marketing', label: '营销提效', icon: 'trending-up' }
      ],
      scenarioContent: {
        social: {
          features: [
            {
              title: '情感陪伴',
              description:
                '支持文本、语音、图像多种输入，多模态协同，丰富交流情境，提供更真实陪伴'
            },
            {
              title: '角色扮演',
              description:
                '灵活扮演各类角色，遵循人设逻辑，长期记忆记住用户喜好与过往交流，构建沉浸式互动体验'
            },
            {
              title: '剧情创作',
              description:
                '基于设定好的故事背景和人设，自动推演剧情，在互动或游戏中，让用户获得创作乐趣'
            }
          ],
          products: ['豆包大模型', '扣子', '羿贝方舟']
        },
        hardware: {
          features: [
            {
              title: '智能语音交互',
              description:
                '端到端语音交互能力，支持自然对话、情感识别和多轮会话，让硬件设备更懂用户'
            },
            {
              title: '视觉感知',
              description:
                '先进的视觉理解能力，支持物体识别、场景理解和手势操控，构建直觉式人机交互'
            },
            {
              title: '个性化助手',
              description:
                '基于用户习惯和偏好的自适应学习能力，提供个性化建议和服务，越用越懂你'
            }
          ],
          products: ['豆包大模型', '实时语音模型', '视觉理解模型']
        },
        education: {
          features: [
            {
              title: '智能辅导',
              description:
                '根据学生知识水平自适应调整教学内容和难度，实现千人千面的个性化学习体验'
            },
            {
              title: '作业批改',
              description:
                'AI自动批改作业，精准识别错误并给出详细解析，减轻教师负担提升教学效率'
            },
            {
              title: '知识问答',
              description:
                '7x24小时在线知识问答服务，覆盖全学科全学段，随时随地解答学习疑问'
            }
          ],
          products: ['豆包大模型', '羿贝方舟', 'AI知识管理']
        },
        service: {
          features: [
            {
              title: '智能客服',
              description:
                '全渠道覆盖的AI客服解决方案，支持文本、语音、视频多模态交互，大幅提升服务效率'
            },
            {
              title: '销售助手',
              description:
                '基于客户画像的智能销售辅助，实时提供话术建议和产品推荐，助力成交转化'
            },
            {
              title: '工单处理',
              description:
                'AI自动分类、派发和跟踪工单，智能预判问题升级，确保高效闭环管理'
            }
          ],
          products: ['羿贝方舟', 'HiAgent', '扣子']
        },
        marketing: {
          features: [
            {
              title: '内容生成',
              description:
                '一键生成多样化营销内容，覆盖文案、图片、视频等多种形式，大幅提升创作效率'
            },
            {
              title: '精准投放',
              description:
                'AI驱动的广告投放优化，智能识别高价值受众，提升ROI和转化率'
            },
            {
              title: '数据洞察',
              description:
                '全链路营销数据分析，AI自动生成洞察报告，帮助快速发现增长机会'
            }
          ],
          products: ['豆包大模型', '文生图模型', 'Data Agent']
        }
      }
    }
  },
  computed: {
    currentContent() {
      return this.scenarioContent[this.activeScenario]
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
.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
.feature-card {
  padding: 24px;
}
.product-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  color: var(--text-secondary);
  background: var(--bg-secondary);
  padding: 8px 16px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  transition: all 0.2s;
}
.product-link:hover {
  border-color: var(--border-hover);
  color: var(--text-primary);
}

@media (max-width: 768px) {
  .features-grid {
    grid-template-columns: 1fr;
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

