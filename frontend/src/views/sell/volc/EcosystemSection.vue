<template>
  <section class="section">
    <div
      class="glow"
      style="
        width: 500px;
        height: 500px;
        top: 0;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(51, 112, 255, 0.04);
      "
    ></div>

    <div class="container" style="position: relative">
      <!-- Ecosystem Header -->
      <div style="margin-bottom: 48px">
        <div class="flex items-center gap-3" style="margin-bottom: 16px">
          <div class="section-bar" style="background: var(--color-brand)"></div>
          <h2 class="section-title">
            聚焦伙伴生态、开发者与前沿研究成果
          </h2>
        </div>
      </div>

      <!-- Ecosystem Cards -->
      <div class="eco-grid" style="margin-bottom: 64px">
        <a href="#" class="card eco-card">
          <div class="flex items-start gap-4" style="margin-bottom: 16px">
            <div
              class="icon-box"
              style="
                width: 48px;
                height: 48px;
                border-radius: 12px;
                background: rgba(51, 112, 255, 0.1);
              "
            >
              <SvgIcon name="code" :size="24" color="var(--color-brand)" />
            </div>
            <div>
              <h3
                style="
                  font-size: 18px;
                  font-weight: 700;
                  color: var(--text-primary);
                  margin-bottom: 8px;
                "
              >
                开发者社区与 Seed 最新研究成果
              </h3>
              <p
                style="
                  font-size: 14px;
                  color: var(--text-muted);
                  line-height: 1.7;
                "
              >
                提供丰富官方开发工具与资源，助力开发者技术交流与能力提升，聚焦模型性能优化、应用场景拓展等前沿领域
              </p>
            </div>
          </div>
          <div class="eco-link" style="color: var(--color-brand)">
            了解更多
            <SvgIcon name="arrow-right" :size="16" />
          </div>
        </a>
        <a href="#" class="card eco-card">
          <div class="flex items-start gap-4" style="margin-bottom: 16px">
            <div
              class="icon-box"
              style="
                width: 48px;
                height: 48px;
                border-radius: 12px;
                background: rgba(20, 201, 201, 0.1);
              "
            >
              <SvgIcon name="users" :size="24" color="var(--color-accent)" />
            </div>
            <div>
              <h3
                style="
                  font-size: 18px;
                  font-weight: 700;
                  color: var(--text-primary);
                  margin-bottom: 8px;
                "
              >
                生态资源与伙伴服务
              </h3>
              <p
                style="
                  font-size: 14px;
                  color: var(--text-muted);
                  line-height: 1.7;
                "
              >
                羿贝综合云服务平台致力通过多样化的生态合作模式，携手伙伴一起为客户构建云上增长新动力
              </p>
            </div>
          </div>
          <div class="eco-link" style="color: var(--color-accent)">
            了解更多
            <SvgIcon name="arrow-right" :size="16" />
          </div>
        </a>
      </div>

      <!-- Security Section -->
      <div>
        <div class="flex items-center gap-3" style="margin-bottom: 32px">
          <div class="section-bar" style="background: var(--color-accent)"></div>
          <h2 class="section-title">安全合规 透明可信</h2>
        </div>

        <!-- Security Cards -->
        <div class="eco-grid" style="margin-bottom: 32px">
          <a href="#" class="card security-card">
            <div
              class="icon-box"
              style="
                width: 48px;
                height: 48px;
                border-radius: 12px;
                background: rgba(51, 112, 255, 0.1);
              "
            >
              <SvgIcon
                name="shield-check"
                :size="24"
                color="var(--color-brand)"
              />
            </div>
            <div class="flex-1">
              <h4
                style="
                  font-size: 15px;
                  font-weight: 600;
                  color: var(--text-primary);
                  margin-bottom: 4px;
                "
              >
                全方位安全保障
              </h4>
              <p style="font-size: 14px; color: var(--text-muted)">
                从基础设施到应用层的多级安全防护体系
              </p>
            </div>
            <SvgIcon name="arrow-right" :size="20" color="var(--text-muted)" />
          </a>
          <a href="#" class="card security-card">
            <div
              class="icon-box"
              style="
                width: 48px;
                height: 48px;
                border-radius: 12px;
                background: rgba(20, 201, 201, 0.1);
              "
            >
              <SvgIcon
                name="file-check"
                :size="24"
                color="var(--color-accent)"
              />
            </div>
            <div class="flex-1">
              <h4
                style="
                  font-size: 15px;
                  font-weight: 600;
                  color: var(--text-primary);
                  margin-bottom: 4px;
                "
              >
                行业分析师报告
              </h4>
              <p style="font-size: 14px; color: var(--text-muted)">
                Gartner、IDC等权威机构认可的云服务领导者
              </p>
            </div>
            <SvgIcon name="arrow-right" :size="20" color="var(--text-muted)" />
          </a>
        </div>

        <!-- Certifications -->
        <p
          style="
            font-size: 14px;
            color: var(--text-muted);
            font-weight: 500;
            margin-bottom: 24px;
          "
        >
          权威认证
        </p>
        <div class="certs-grid">
          <div
            v-for="(cert, idx) in certifications"
            :key="idx"
            class="card cert-card"
          >
            <div
              class="icon-box"
              style="
                width: 40px;
                height: 40px;
                border-radius: 10px;
                background: rgba(51, 112, 255, 0.05);
                margin: 0 auto 12px;
              "
            >
              <SvgIcon
                name="award"
                :size="20"
                color="rgba(51,112,255,0.6)"
              />
            </div>
            <p
              style="
                font-size: 12px;
                font-weight: 600;
                color: var(--text-primary);
                margin-bottom: 4px;
              "
            >
              {{ cert.name }}
            </p>
            <p
              style="
                font-size: 11px;
                color: var(--text-muted);
                line-height: 1.5;
              "
            >
              {{ cert.description }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import SvgIcon from './SvgIcons.vue'

export default {
  name: 'EcosystemSection',
  components: { SvgIcon },
  data() {
    return {
      certifications: [
        { name: 'ISO 27001', description: '信息安全管理体系认证' },
        { name: 'ISO 27017', description: '云服务信息安全管理体系认证' },
        { name: 'ISO 27701', description: '隐私信息管理体系认证' },
        { name: 'ISO 42001', description: '人工智能管理体系认证' },
        { name: 'PCI DSS', description: '支付卡行业数据安全标准' },
        { name: 'CMMI 5', description: 'CMMI 五级认证' },
        { name: '等级保护', description: '网络安全等级保护' },
        { name: 'SOC 1/2/3', description: '服务组织控制报告' }
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
.eco-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}
.eco-card {
  padding: 32px;
}
.eco-link {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-size: 14px;
  font-weight: 500;
  transition: gap 0.2s;
}
.eco-card:hover .eco-link {
  gap: 10px;
}
.security-card {
  padding: 24px;
  display: flex;
  align-items: center;
  gap: 16px;
}
.certs-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 12px;
}
.cert-card {
  padding: 16px;
  text-align: center;
}

@media (max-width: 1024px) {
  .certs-grid {
    grid-template-columns: repeat(4, 1fr);
  }
}
@media (max-width: 768px) {
  .eco-grid {
    grid-template-columns: 1fr;
  }
  .certs-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .section-title {
    font-size: 22px;
  }
}
</style>

