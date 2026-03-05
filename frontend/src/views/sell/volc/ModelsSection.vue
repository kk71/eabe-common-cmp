<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 500px;
        height: 500px;
        top: 50%;
        left: -100px;
        background: rgba(51, 112, 255, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Header -->
      <div class="flex items-center justify-between" style="margin-bottom: 48px">
        <div>
          <div class="flex items-center gap-3" style="margin-bottom: 16px">
            <div class="section-bar" style="background: var(--color-brand)"></div>
            <h2 class="section-title">豆包大模型</h2>
          </div>
          <p class="section-desc">更强模型、更低价格、更易落地</p>
        </div>
        <a href="#" class="link-arrow md-hide">
          查看全部模型
          <VolcIcon name="arrow-right" :size="16" />
        </a>
      </div>

      <!-- Model Cards -->
      <div class="models-grid">
        <a
          v-for="(model, idx) in models"
          :key="idx"
          href="#"
          class="card model-card"
        >
          <div class="flex items-start gap-4" style="margin-bottom: 16px">
            <div
              class="icon-box"
              :style="{
                width: '44px',
                height: '44px',
                borderRadius: '12px',
                background: model.bgColor
              }"
            >
          <img :src="model.icon" alt="" style="width: 22px; height: 22px" />
            </div>
            <div class="flex-1 min-w-0">
              <div class="flex items-center gap-2">
                <h3 class="model-name truncate">
                  {{ model.name }}
                </h3>
                <span
                  v-if="model.tag"
                  :class="['tag', model.tag === 'HOT' ? 'tag-hot' : 'tag-new']"
                >
                  {{ model.tag }}
                </span>
              </div>
            </div>
          </div>
          <p class="model-desc line-clamp-2">
            {{ model.description }}
          </p>
          <div
            class="hover-reveal link-arrow"
            style="margin-top: 16px; font-size: 12px"
          >
            了解更多
            <VolcIcon name="arrow-right" :size="14" />
          </div>
        </a>
      </div>

      <!-- Experience Banner -->
      <div class="card experience-banner">
        <div class="flex items-center gap-4">
          <div
            class="icon-box"
            style="
              width: 56px;
              height: 56px;
              border-radius: 16px;
              background: rgba(51, 112, 255, 0.1);
              flex-shrink: 0;
            "
          >
            <img :src="models[0].icon" alt="" style="width: 28px; height: 28px" />
          </div>
          <div>
            <h3
              style="
                font-size: 18px;
                font-weight: 600;
                color: var(--text-primary);
                margin-bottom: 4px;
              "
            >
              体验豆包大模型 1.6
            </h3>
            <p style="font-size: 14px; color: var(--text-muted)">
              即刻开启 AI 体验中心，体验最前沿能力
            </p>
          </div>
        </div>
        <div class="flex gap-3" style="flex-shrink: 0">
          <a href="#" class="btn-primary">
            立即体验
            <VolcIcon name="arrow-right" :size="16" />
          </a>
          <a href="#" class="btn-secondary">AI 体验中心</a>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import VolcIcon from './SvgIcons.vue'
import IconAiAssistant from '@/assets/icons/svg/icon-ai-assistant.svg'
import IconAiVideo from '@/assets/icons/svg/icon-ai-video.svg'
import IconAiAnalysis from '@/assets/icons/svg/icon-ai-analysis.svg'
import IconSms from '@/assets/icons/svg/icon-sms.svg'
import IconAiDesign from '@/assets/icons/svg/icon-ai-design.svg'
import IconAiExtract from '@/assets/icons/svg/icon-ai-extract.svg'

export default {
  name: 'ModelsSection',
  components: { VolcIcon },
  data() {
    return {
      models: [
        {
          icon: IconAiAssistant,
          name: '豆包大模型 1.6',
          tag: 'HOT',
          description:
            '更强的推理能力，多模态理解能力，GUI操作能力和前端页面编程能力',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: IconAiVideo,
          name: '豆包 · 视频生成模型',
          tag: 'NEW',
          description:
            '将文本、图像生成高质量视频，能够生成具备丰富细节层次的影视级视频',
          color: 'var(--color-accent)',
          bgColor: 'rgba(20,201,201,0.1)'
        },
        {
          icon: IconAiAnalysis,
          name: '豆包 · 视觉理解模型',
          tag: 'NEW',
          description:
            '对视觉内容有更强的识别能力，更强理解和推理能力，以及更细腻的视觉描述能力',
          color: 'var(--color-yellow)',
          bgColor: 'rgba(247,186,30,0.1)'
        },
        {
          icon: IconSms,
          name: '豆包 · 实时语音模型',
          tag: '',
          description:
            '真正的端到端语音模型，通过自然语言进行多种高级指令控制，具备超拟人交互能力',
          color: 'var(--color-green)',
          bgColor: 'rgba(159,219,29,0.1)'
        },
        {
          icon: IconAiDesign,
          name: '豆包 · 文生图模型',
          tag: '',
          description:
            '快速生成精美写真，支持50余种风格变换，并对图片实现扩图、重绘等创意延展',
          color: 'var(--color-brand)',
          bgColor: 'rgba(51,112,255,0.1)'
        },
        {
          icon: IconAiExtract,
          name: '豆包 · 声音复刻模型',
          tag: '',
          description:
            '5秒即可实现声音1:1克隆，对音色相似度和自然度进行高度还原，支持跨语种迁移',
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
.section-desc {
  font-size: 16px;
  color: var(--text-muted);
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
.models-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 48px;
}
.model-card {
  padding: 24px;
}
.model-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
}
.model-desc {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.6;
}
.experience-banner {
  padding: 40px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
  flex-wrap: wrap;
}

@media (max-width: 1024px) {
  .models-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 768px) {
  .models-grid {
    grid-template-columns: 1fr;
  }
  .experience-banner {
    padding: 24px;
    flex-direction: column;
    align-items: flex-start;
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

