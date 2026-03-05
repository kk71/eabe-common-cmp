<template>
  <footer class="footer">
    <div class="container">
      <!-- Links Grid -->
      <div class="footer-grid">
        <div v-for="group in footerLinks" :key="group.title" class="footer-col">
          <h4 class="footer-col-title">
            {{ group.title }}
          </h4>
          <ul>
            <li v-for="link in group.links" :key="link.label">
              <a href="#" class="footer-link">
                {{ link.label }}
              </a>
            </li>
          </ul>
        </div>
      </div>

      <!-- Bottom Bar -->
      <div class="footer-bottom">
        <div class="flex items-center gap-3">
          <img
            src="/company-logo/LOGO2.png"
            alt="羿贝综合云服务平台"
            width="28"
            height="28"
          />
          <span
            style="
              font-size: 15px;
              font-weight: 600;
              color: #111827;
            "
          >
            羿贝综合云服务平台
          </span>
        </div>
        <div class="footer-legal">
          <a href="#">服务条款</a>
          <span class="divider">|</span>
          <a href="#">隐私政策</a>
          <span class="divider">|</span>
          <a href="#">法律声明</a>
          <span class="divider">|</span>
          <span>京ICP备xxxxxxxx号-x</span>
        </div>
        <p style="font-size: 12px; color: #9ca3af">
          Copyright © 2024 羿贝综合云服务平台. All rights reserved.
        </p>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'FooterSection',
  data() {
    return {
      footerLinks: [
        {
          title: '产品',
          links: [
            { label: '豆包大模型' },
            { label: '羿贝方舟' },
            { label: '扣子' },
            { label: 'GPU云服务器' },
            { label: '容器服务' },
            { label: '对象存储' }
          ]
        },
        {
          title: '解决方案',
          links: [
            { label: '汽车行业' },
            { label: '金融行业' },
            { label: '泛互联网' },
            { label: '消费行业' },
            { label: '教育行业' },
            { label: '智能终端' }
          ]
        },
        {
          title: '开发者',
          links: [
            { label: '开发者社区' },
            { label: '技术文档' },
            { label: 'API参考' },
            { label: 'SDK下载' },
            { label: '开源项目' },
            { label: '技术博客' }
          ]
        },
        {
          title: '关于我们',
          links: [
            { label: '公司介绍' },
            { label: '新闻动态' },
            { label: '加入我们' },
            { label: '联系我们' },
            { label: '合作伙伴' },
            { label: '信任中心' }
          ]
        },
        {
          title: '支持',
          links: [
            { label: '帮助中心' },
            { label: '在线客服' },
            { label: '工单系统' },
            { label: '备案中心' },
            { label: '定价' },
            { label: 'SLA承诺' }
          ]
        }
      ]
    }
  }
}
</script>

<style scoped>
.footer {
  border-top: 1px solid #e5e7eb;
  background: linear-gradient(180deg, #f1f5f9 0%, #f9fafb 40%, #ffffff 100%);
  color: #111827;
}
.footer-grid {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 32px;
  padding: 64px 0;
}
.footer-col-title {
  font-size: 14px;
  font-weight: 600;
  color: #111827;
  margin-bottom: 20px;
  border-left: 3px solid #2563eb;
  padding-left: 8px;
}
.footer-col ul {
  display: flex;
  flex-direction: column;
  gap: 12px;
}
.footer-link {
  font-size: 14px;
  color: #4b5563;
  transition: color 0.16s ease;
}
.footer-link:hover {
  color: #2563eb;
}
.footer-bottom {
  border-top: 1px solid var(--border-color);
  padding: 32px 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-wrap: wrap;
}
.footer-legal {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 16px;
  font-size: 12px;
  color: #6b7280;
}
.footer-legal a {
  transition: color 0.16s ease;
}
.footer-legal a:hover {
  color: #2563eb;
}
.divider {
  color: #d1d5db;
}

@media (max-width: 1024px) {
  .footer-grid {
    grid-template-columns: repeat(3, 1fr);
  }
}
@media (max-width: 768px) {
  .footer-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 24px;
    padding: 40px 0;
  }
  .footer-bottom {
    flex-direction: column;
    align-items: flex-start;
  }
}
</style>

