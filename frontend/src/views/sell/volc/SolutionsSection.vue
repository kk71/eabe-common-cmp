<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 500px;
        height: 500px;
        bottom: -100px;
        left: -80px;
        background: rgba(247, 186, 30, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Header -->
      <div >
        <div class="flex items-center gap-3" style="margin-bottom: 16px">
          <div class="section-bar" style="background: var(--color-red)"></div>
          <h2 class="section-title">行业领先的场景化解决方案</h2>
        </div>
      </div>

      <!-- Industry Tabs -->
      <div class="tab-bar" style="margin-bottom: 10px">
        <button
          v-for="tab in industryTabs"
          :key="tab.id"
          :class="['tab-item', { active: activeIndustry === tab.id }]"
          @click="activeIndustry = tab.id"
          style="display: flex; align-items: center; gap: 8px"
        >
          <VolcIcon :name="tab.icon" :size="16" />
          {{ tab.label }}
        </button>
      </div>

      <!-- Industry Content -->
      <div class="solution-grid">
        <!-- Main Content -->
        <div class="card" style="padding: 32px">
          <h3
            style="
              font-size: 20px;
              font-weight: 700;
              color: var(--text-primary);
              margin-bottom: 12px;
            "
          >
            {{ currentContent.title }}
          </h3>
          <p
            style="
              font-size: 14px;
              color: var(--text-muted);
              line-height: 1.7;
              margin-bottom: 24px;
            "
          >
            {{ currentContent.description }}
          </p>
          <a href="#" class="link-arrow">
            了解详情
            <VolcIcon name="arrow-right" :size="16" />
          </a>
        </div>

        <!-- Cases -->
        <div class="cases-col">
          <a
            v-for="(c, idx) in currentContent.cases"
            :key="idx"
            href="#"
            class="card case-card"
          >
            <div class="flex items-center gap-2" style="margin-bottom: 8px">
              <div
                :style="{
                  width: '8px',
                  height: '8px',
                  borderRadius: '50%',
                  background:
                    idx === 0 ? 'var(--color-brand)' : 'var(--color-accent)'
                }"
              ></div>
              <p
                style="
                  font-size: 14px;
                  font-weight: 600;
                  color: var(--text-primary);
                "
              >
                {{ c.company }}
              </p>
            </div>
            <p
              style="
                font-size: 12px;
                color: var(--text-muted);
                line-height: 1.6;
              "
            >
              {{ c.detail }}
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
              查看详情
              <VolcIcon name="arrow-right" :size="12" />
            </div>
          </a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VolcIcon from './SvgIcons.vue'

export default {
  name: 'SolutionsSection',
  components: { VolcIcon },
  data() {
    return {
      activeIndustry: 'auto',
      industryTabs: [
        { id: 'auto', label: '汽车', icon: 'car' },
        { id: 'finance', label: '金融', icon: 'landmark' },
        { id: 'internet', label: '泛互', icon: 'smartphone' },
        { id: 'consumer', label: '消费', icon: 'flask' },
        { id: 'research', label: '科研医药', icon: 'pill' },
        { id: 'education', label: '教育', icon: 'graduation-cap' },
        { id: 'device', label: '智能终端', icon: 'cpu' }
      ],
      industryContent: {
        auto: {
          title: '全域 AI 营销解决方案',
          description:
            '依托豆包大模型，提升全域数字营销能力。在AI赋能下，让用户洞察更精准，让销售效率更高，线索实现更高转化。',
          cases: [
            {
              company: '梅赛德斯奔驰',
              detail:
                '全新纯电长轴距CLA接入豆包大模型，为车主打造个性化的智能交互体验'
            },
            {
              company: '赛力斯',
              detail:
                '携手豆包大模型提升用户满意度，提升用户反馈闭环效率'
            }
          ]
        },
        finance: {
          title: '智能金融解决方案',
          description:
            '结合大模型与金融行业知识，为银行、保险、证券等金融机构提供智能客服、风控分析、文档审核等AI能力。',
          cases: [
            {
              company: '某大型银行',
              detail: '应用AI智能客服解决方案，客户问题解决率提升40%'
            },
            {
              company: '某保险集团',
              detail: '利用大模型自动审核保单，处理效率提升数倍'
            }
          ]
        },
        internet: {
          title: '泛互联网智能化解决方案',
          description:
            '面向社交、电商、游戏等泛互联网行业，提供内容生成、推荐优化、智能审核等全链路AI能力。',
          cases: [
            {
              company: '某头部社交平台',
              detail:
                '借助AI内容理解和生成能力，大幅提升内容分发效率和用户粘性'
            },
            {
              company: '某电商平台',
              detail:
                'AI驱动的商品描述生成和智能客服，转化率显著提升'
            }
          ]
        },
        consumer: {
          title: '消费行业智能解决方案',
          description:
            '为零售、快消、餐饮等消费行业提供智能营销、用户运营、供应链优化等AI能力，助力品牌数字化增长。',
          cases: [
            {
              company: '某知名品牌',
              detail: '基于AI的全域营销方案，品牌曝光量提升3倍'
            },
            {
              company: '某连锁餐饮',
              detail:
                'AI驱动的智能排班和库存管理，运营效率大幅提升'
            }
          ]
        },
        research: {
          title: '科研医药AI解决方案',
          description:
            '借助大模型的强大理解和推理能力，为科研机构和医药企业提供文献分析、药物发现、临床辅助等AI能力。',
          cases: [
            {
              company: '某研究院',
              detail:
                'AI辅助文献综述和数据分析，科研产出效率提升显著'
            },
            {
              company: '某医药企业',
              detail: '大模型赋能药物筛选流程，显著缩短研发周期'
            }
          ]
        },
        education: {
          title: '教育行业智能解决方案',
          description:
            '面向K12、高等教育、职业培训等教育场景，提供智能辅导、自适应学习、自动批改等AI教育能力。',
          cases: [
            {
              company: '某在线教育平台',
              detail:
                'AI自适应学习系统上线后，学生学习效果提升明显'
            },
            {
              company: '某高校',
              detail:
                '引入AI辅助教学和科研工具，教学质量和科研效率显著提升'
            }
          ]
        },
        device: {
          title: '智能终端AI解决方案',
          description:
            '为手机、可穿戴设备、智能家居等终端设备提供端侧AI能力，实现更自然的人机交互和更智能的设备体验。',
          cases: [
            {
              company: '某手机厂商',
              detail: '集成豆包大模型的AI助手，用户日活大幅增长'
            },
            {
              company: '某智能音箱品牌',
              detail:
                '接入实时语音模型，对话自然度和用户满意度显著提升'
            }
          ]
        }
      }
    }
  },
  computed: {
    currentContent() {
      return this.industryContent[this.activeIndustry]
    }
  }
}
</script>

<style scoped>
.section {
  padding: 20px 0;
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
.solution-grid {
  display: grid;
  grid-template-columns: 3fr 2fr;
  gap: 24px;
}
.cases-col {
  display: flex;
  flex-direction: column;
  gap: 16px;
}
.case-card {
  padding: 20px;
  flex: 1;
}

@media (max-width: 768px) {
  .solution-grid {
    grid-template-columns: 1fr;
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

