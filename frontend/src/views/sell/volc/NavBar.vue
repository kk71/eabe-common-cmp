<template>
  <header class="navbar" :class="{ scrolled: isScrolled }">
    <div class="nav-container flex items-center justify-between">
      <!-- Logo -->
      <div class="flex items-center gap-6">
        <router-link to="/" class="flex items-center gap-2 logo-link">
          <img
            src="/company-logo/LOGO2.png"
            alt="羿贝综合云服务平台"
            width="28"
            height="28"
          />
          <span class="logo-text">羿贝综合云服务平台</span>
        </router-link>

        <nav class="nav-links md-hide">
          <a href="#" class="nav-link">最新活动</a>

          <!-- 大模型 with Mega Menu -->
          <div
            class="nav-dropdown"
            @mouseenter="openMenu('models')"
            @mouseleave="startClose('models')"
          >
            <router-link
              to="/models"
              class="nav-link flex items-center gap-1"
              :class="{ 'nav-link-active': activeMenu === 'models' }"
            >
              大模型
              <VolcIcon name="chevron-down" :size="14" />
            </router-link>
            <transition name="mega-fade">
              <div
                v-if="activeMenu === 'models'"
                class="mega-panel models-panel"
                @mouseenter="cancelClose('models')"
                @mouseleave="startClose('models')"
              >
                <div class="mega-inner">
                  <!-- Left categories -->
                  <div class="mega-sidebar">
                    <div
                      v-for="cat in modelCategories"
                      :key="cat.id"
                      class="mega-cat-item"
                      :class="{ active: activeModelCat === cat.id }"
                      @mouseenter="activeModelCat = cat.id"
                    >
                      <div
                        class="mega-cat-icon"
                        :style="{ background: cat.bgColor }"
                      >
                        <VolcIcon :name="cat.icon" :size="16" :color="cat.color" />
                      </div>
                      <div class="mega-cat-info">
                        <span class="mega-cat-name">{{ cat.name }}</span>
                        <span class="mega-cat-desc">{{ cat.desc }}</span>
                      </div>
                      <VolcIcon name="chevron-right" :size="14" class="mega-cat-arrow" />
                    </div>
                  </div>

                  <!-- Right detail -->
                  <div class="mega-detail">
                    <div class="mega-detail-header">
                      <h4 class="mega-detail-title">{{ currentModelCat.name }}</h4>
                      <router-link
                        to="/models"
                        class="mega-detail-link"
                        @click.native="closeAll"
                      >
                        查看全部
                        <VolcIcon name="arrow-right" :size="14" />
                      </router-link>
                    </div>
                    <div class="mega-detail-grid">
                      <router-link
                        v-for="(item, idx) in currentModelCat.items"
                        :key="idx"
                        to="/models"
                        class="mega-product-card"
                        @click.native="closeAll"
                      >
                        <div
                          class="mega-product-icon"
                          :style="{ background: item.bgColor }"
                        >
                          <VolcIcon :name="item.icon" :size="16" :color="item.color" />
                        </div>
                        <div class="mega-product-info">
                          <div class="flex items-center gap-2">
                            <span class="mega-product-name">{{ item.name }}</span>
                            <span
                              v-if="item.tag"
                              :class="[
                                'mega-tag',
                                item.tag === 'HOT' ? 'mega-tag-hot' : 'mega-tag-new'
                              ]"
                            >
                              {{ item.tag }}
                            </span>
                          </div>
                          <span class="mega-product-desc">{{ item.desc }}</span>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>

          <!-- 产品 with Mega Menu -->
          <div
            class="nav-dropdown"
            @mouseenter="openMenu('products')"
            @mouseleave="startClose('products')"
          >
            <router-link
              to="/products"
              class="nav-link flex items-center gap-1"
              :class="{ 'nav-link-active': activeMenu === 'products' }"
            >
              产品
              <VolcIcon name="chevron-down" :size="14" />
            </router-link>
            <transition name="mega-fade">
              <div
                v-if="activeMenu === 'products'"
                class="mega-panel products-panel"
                @mouseenter="cancelClose('products')"
                @mouseleave="startClose('products')"
              >
                <div class="mega-inner">
                  <!-- Left categories -->
                  <div class="mega-sidebar">
                    <div
                      v-for="cat in productCategories"
                      :key="cat.id"
                      class="mega-cat-item"
                      :class="{ active: activeProductCat === cat.id }"
                      @mouseenter="activeProductCat = cat.id"
                    >
                      <div
                        class="mega-cat-icon"
                        :style="{ background: cat.bgColor }"
                      >
                        <VolcIcon :name="cat.icon" :size="16" :color="cat.color" />
                      </div>
                      <div class="mega-cat-info">
                        <span class="mega-cat-name">{{ cat.name }}</span>
                        <span class="mega-cat-desc">{{ cat.desc }}</span>
                      </div>
                      <VolcIcon name="chevron-right" :size="14" class="mega-cat-arrow" />
                    </div>
                  </div>

                  <!-- Right detail -->
                  <div class="mega-detail">
                    <div class="mega-detail-header">
                      <h4 class="mega-detail-title">{{ currentProductCat.name }}</h4>
                      <router-link
                        to="/products"
                        class="mega-detail-link"
                        @click.native="closeAll"
                      >
                        查看全部
                        <VolcIcon name="arrow-right" :size="14" />
                      </router-link>
                    </div>
                    <div class="mega-detail-grid">
                      <router-link
                        v-for="(item, idx) in currentProductCat.items"
                        :key="idx"
                        to="/products"
                        class="mega-product-card"
                        @click.native="closeAll"
                      >
                        <div
                          class="mega-product-icon"
                          :style="{ background: item.bgColor }"
                        >
                          <VolcIcon :name="item.icon" :size="16" :color="item.color" />
                        </div>
                        <div class="mega-product-info">
                          <div class="flex items-center gap-2">
                            <span class="mega-product-name">{{ item.name }}</span>
                            <span
                              v-if="item.tag"
                              :class="[
                                'mega-tag',
                                item.tag === 'HOT' ? 'mega-tag-hot' : 'mega-tag-new'
                              ]"
                            >
                              {{ item.tag }}
                            </span>
                          </div>
                          <span class="mega-product-desc">{{ item.desc }}</span>
                        </div>
                      </router-link>
                    </div>
                  </div>
                </div>
              </div>
            </transition>
          </div>

          <a href="#" class="nav-link">解决方案</a>
          <a href="#" class="nav-link">定价</a>
          <a href="#" class="nav-link">生态与合作</a>
          <a href="#" class="nav-link">支持与服务</a>
          <a href="#" class="nav-link">开发者</a>
          <a href="#" class="nav-link">了解我们</a>
        </nav>
      </div>

      <!-- Right Actions -->
      <div class="flex items-center gap-3">
        <a href="#" class="nav-link md-hide">文档</a>
        <a href="#" class="nav-link md-hide">备案</a>
        <router-link to="/sell/management" class="nav-link md-hide">控制台</router-link>
        <router-link to="/sell/login" class="btn-ghost">登录</router-link>
        <a href="#" class="btn-primary-sm">立即注册</a>
        <button class="mobile-menu-btn lg-hide" @click="mobileOpen = !mobileOpen">
          <VolcIcon :name="mobileOpen ? 'x' : 'menu'" :size="22" />
        </button>
      </div>
    </div>

    <!-- Mobile Menu -->
    <transition name="slide">
      <div v-if="mobileOpen" class="mobile-menu lg-hide">
        <router-link to="/" class="mobile-link" @click.native="mobileOpen = false">
          首页
        </router-link>
        <div class="mobile-section">
          <div
            class="mobile-section-title"
            @click="mobileExpand === 'models' ? (mobileExpand = '') : (mobileExpand = 'models')"
          >
            <span>大模型</span>
            <VolcIcon
              :name="mobileExpand === 'models' ? 'chevron-down' : 'chevron-right'"
              :size="16"
            />
          </div>
          <transition name="slide">
            <div v-if="mobileExpand === 'models'" class="mobile-sub-list">
              <router-link
                v-for="cat in modelCategories"
                :key="cat.id"
                to="/models"
                class="mobile-sub-link"
                @click.native="mobileOpen = false"
              >
                <VolcIcon :name="cat.icon" :size="16" color="#000" />
                {{ cat.name }}
              </router-link>
            </div>
          </transition>
        </div>
        <div class="mobile-section">
          <div
            class="mobile-section-title"
            @click="
              mobileExpand === 'products' ? (mobileExpand = '') : (mobileExpand = 'products')
            "
          >
            <span>产品</span>
            <VolcIcon
              :name="mobileExpand === 'products' ? 'chevron-down' : 'chevron-right'"
              :size="16"
            />
          </div>
          <transition name="slide">
            <div v-if="mobileExpand === 'products'" class="mobile-sub-list">
              <router-link
                v-for="cat in productCategories"
                :key="cat.id"
                to="/products"
                class="mobile-sub-link"
                @click.native="mobileOpen = false"
              >
                <VolcIcon :name="cat.icon" :size="16" color="#000" />
                {{ cat.name }}
              </router-link>
            </div>
          </transition>
        </div>
        <a href="#" class="mobile-link">解决方案</a>
        <a href="#" class="mobile-link">定价</a>
        <a href="#" class="mobile-link">文档</a>
        <router-link
          to="/sell/login"
          class="mobile-link"
          @click.native="mobileOpen = false"
        >
          登录
        </router-link>
        <router-link
          to="/sell/management"
          class="mobile-link"
          @click.native="mobileOpen = false"
        >
          控制台
        </router-link>
      </div>
    </transition>

    <!-- Backdrop overlay -->
    <transition name="mega-fade">
      <div v-if="activeMenu" class="mega-backdrop" @mouseenter="closeAll"></div>
    </transition>
  </header>

</template>

<script>
import VolcIcon from './SvgIcons.vue'

export default {
  name: 'NavBar',
  components: { VolcIcon },
  data() {
    return {
      isScrolled: false,
      mobileOpen: false,
      mobileExpand: '',
      activeMenu: null,
      closeTimer: null,
      activeModelCat: 'doubao',
      activeProductCat: 'compute',
      modelCategories: [
        {
          id: 'doubao',
          name: '豆包大模型',
          desc: '更强模型、更低价格',
          icon: 'brain',
          color: '#3370ff',
          bgColor: 'rgba(51,112,255,0.1)',
          items: [
            {
              name: '豆包大模型 1.6',
              desc: '更强推理与多模态理解能力',
              icon: 'brain',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '豆包 · 视频生成',
              desc: '高质量影视级视频生成',
              icon: 'video',
              tag: 'NEW',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '豆包 · 视觉理解',
              desc: '强视觉识别与推理能力',
              icon: 'eye',
              tag: 'NEW',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '豆包 · 实时语音',
              desc: '端到端超拟人交互语音模型',
              icon: 'mic',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            },
            {
              name: '豆包 · 文生图',
              desc: '50余种风格快速生成精美图片',
              icon: 'image',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '豆包 · 声音复刻',
              desc: '5秒克隆1:1高仿真音色',
              icon: 'audio-lines',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            }
          ]
        },
        {
          id: 'agent',
          name: 'Agent 开发平台',
          desc: '全链路 Agent 开发工具',
          icon: 'bot',
          color: '#14c9c9',
          bgColor: 'rgba(20,201,201,0.1)',
          items: [
            {
              name: '羿贝方舟',
              desc: '一站式大模型开发平台',
              icon: 'layers',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '扣子 (Coze)',
              desc: 'AI Agent 开发工具',
              icon: 'bot',
              tag: 'HOT',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: 'HiAgent',
              desc: '企业 AI 中台',
              icon: 'workflow',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: 'AgentKit',
              desc: '通用Agent解决方案',
              icon: 'settings',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            }
          ]
        },
        {
          id: 'ai-app',
          name: 'AI 应用',
          desc: '企业级精选AI产品',
          icon: 'sparkles',
          color: '#f7ba1e',
          bgColor: 'rgba(247,186,30,0.1)',
          items: [
            {
              name: 'AI 知识管理',
              desc: '多模态内容理解知识管理专家',
              icon: 'book-open',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: 'AI 视频翻译',
              desc: '一键字幕+配音+口型翻译',
              icon: 'languages',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: 'Data Agent',
              desc: '企业级AI数字专家',
              icon: 'bar-chart',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '安全智能体',
              desc: '7x24小时全自动威胁研判',
              icon: 'shield',
              color: '#f53f3f',
              bgColor: 'rgba(245,63,63,0.1)'
            }
          ]
        },
        {
          id: 'experience',
          name: 'AI 体验中心',
          desc: '体验前沿模型能力',
          icon: 'wand',
          color: '#9fdb1d',
          bgColor: 'rgba(159,219,29,0.1)',
          items: [
            {
              name: '模型体验广场',
              desc: '一站体验超全大模型',
              icon: 'sparkles',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '文生图体验',
              desc: '快速生成各类风格精美图片',
              icon: 'image',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '语音对话体验',
              desc: '体验实时语音AI交互',
              icon: 'mic',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '视频生成体验',
              desc: '文字/图片一键生成视频',
              icon: 'video',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            }
          ]
        }
      ],
      productCategories: [
        {
          id: 'compute',
          name: '计算',
          desc: '弹性计算与GPU算力',
          icon: 'server',
          color: '#3370ff',
          bgColor: 'rgba(51,112,255,0.1)',
          items: [
            {
              name: 'GPU云服务器',
              desc: '高性能GPU计算实例',
              icon: 'cpu',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '云服务器ECS',
              desc: '安全稳定弹性云服务器',
              icon: 'server',
              tag: 'HOT',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '弹性裸金属服务器',
              desc: '兼顾物理机性能与云便捷',
              icon: 'hard-drive',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '函数服务',
              desc: '无服务器函数计算托管平台',
              icon: 'zap',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            },
            {
              name: '弹性伸缩',
              desc: '自动伸缩计算资源',
              icon: 'bar-chart',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            }
          ]
        },
        {
          id: 'network',
          name: '网络与CDN',
          desc: '全球加速与网络互联',
          icon: 'globe',
          color: '#14c9c9',
          bgColor: 'rgba(20,201,201,0.1)',
          items: [
            {
              name: '公网IP',
              desc: '弹性灵活安全的公网服务',
              icon: 'globe',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '负载均衡',
              desc: '高可用流量分发服务',
              icon: 'network',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: 'CDN加速',
              desc: '全球节点内容分发网络',
              icon: 'zap',
              tag: 'HOT',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '私有网络VPC',
              desc: '逻辑隔离安全虚拟私有云',
              icon: 'lock',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            }
          ]
        },
        {
          id: 'storage',
          name: '存储',
          desc: '海量安全云端存储',
          icon: 'hard-drive',
          color: '#f7ba1e',
          bgColor: 'rgba(247,186,30,0.1)',
          items: [
            {
              name: '对象存储',
              desc: '10EB级高可用对象存储',
              icon: 'hard-drive',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '文件存储NAS',
              desc: '高性能共享文件存储',
              icon: 'file-text',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '云盘',
              desc: '高可靠云硬盘块存储服务',
              icon: 'database',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            }
          ]
        },
        {
          id: 'database-cat',
          name: '数据库',
          desc: '高可靠云端数据库',
          icon: 'database',
          color: '#9fdb1d',
          bgColor: 'rgba(159,219,29,0.1)',
          items: [
            {
              name: '云数据库 MySQL',
              desc: '即开即用弹性MySQL服务',
              icon: 'database',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '云数据库 PostgreSQL',
              desc: '高兼容性关系型数据库',
              icon: 'database',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '缓存数据库 Redis',
              desc: '兼具缓存高性能与持久化',
              icon: 'memory-stick',
              tag: 'HOT',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            },
            {
              name: '云数据库 MongoDB',
              desc: '全托管文档型NoSQL数据库',
              icon: 'database',
              color: '#9fdb1d',
              bgColor: 'rgba(159,219,29,0.1)'
            },
            {
              name: '云搜索服务',
              desc: '全托管AI信息检索分析平台',
              icon: 'search',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            }
          ]
        },
        {
          id: 'container-cat',
          name: '容器与中间件',
          desc: '云原生容器服务',
          icon: 'container',
          color: '#3370ff',
          bgColor: 'rgba(51,112,255,0.1)',
          items: [
            {
              name: '容器服务 VKE',
              desc: '高性能K8s容器集群管理',
              icon: 'container',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '镜像仓库',
              desc: '安全稳定的容器镜像托管',
              icon: 'layers',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '消息队列 Kafka',
              desc: '全托管高吞吐消息队列',
              icon: 'workflow',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            }
          ]
        },
        {
          id: 'bigdata',
          name: '大数据',
          desc: '一站式大数据平台',
          icon: 'bar-chart',
          color: '#14c9c9',
          bgColor: 'rgba(20,201,201,0.1)',
          items: [
            {
              name: 'AI数据湖服务',
              desc: '大模型时代AI数据基建',
              icon: 'brain',
              tag: 'NEW',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: 'EMR',
              desc: '全托管弹性MapReduce',
              icon: 'server',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '数据湖仓',
              desc: '湖仓一体化分析平台',
              icon: 'database',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            }
          ]
        },
        {
          id: 'video-cat',
          name: '视频与通信',
          desc: '视频云与实时音视频',
          icon: 'video',
          color: '#f7ba1e',
          bgColor: 'rgba(247,186,30,0.1)',
          items: [
            {
              name: '视频点播',
              desc: '一站式音视频点播服务',
              icon: 'video',
              tag: 'HOT',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: '视频直播',
              desc: '低延时高并发直播服务',
              icon: 'monitor',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: '实时音视频RTC',
              desc: '全球低延时实时通信',
              icon: 'headphones',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            }
          ]
        },
        {
          id: 'security-cat',
          name: '安全',
          desc: '全方位安全防护',
          icon: 'shield',
          color: '#f53f3f',
          bgColor: 'rgba(245,63,63,0.1)',
          items: [
            {
              name: '大模型应用防火墙',
              desc: '大语言模型推理安全防护',
              icon: 'shield',
              tag: 'NEW',
              color: '#3370ff',
              bgColor: 'rgba(51,112,255,0.1)'
            },
            {
              name: 'DDoS防护',
              desc: 'T级DDoS流量清洗服务',
              icon: 'shield-check',
              color: '#14c9c9',
              bgColor: 'rgba(20,201,201,0.1)'
            },
            {
              name: 'Web应用防火墙',
              desc: 'Web应用安全防护',
              icon: 'lock',
              color: '#f7ba1e',
              bgColor: 'rgba(247,186,30,0.1)'
            }
          ]
        }
      ]
    }
  },
  computed: {
    currentModelCat() {
      const id = this.activeModelCat
      const found = this.modelCategories.find((c) => c.id === id)
      return found || this.modelCategories[0]
    },
    currentProductCat() {
      const id = this.activeProductCat
      const found = this.productCategories.find((c) => c.id === id)
      return found || this.productCategories[0]
    }
  },
  mounted() {
    window.addEventListener('scroll', this.handleScroll)
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll)
  },
  methods: {
    handleScroll() {
      this.isScrolled = window.scrollY > 10
    },
    openMenu(menu) {
      if (this.closeTimer) {
        clearTimeout(this.closeTimer)
        this.closeTimer = null
      }
      this.activeMenu = menu
    },
    startClose() {
      this.closeTimer = setTimeout(() => {
        this.activeMenu = null
      }, 150)
    },
    cancelClose() {
      if (this.closeTimer) {
        clearTimeout(this.closeTimer)
        this.closeTimer = null
      }
    },
    closeAll() {
      this.activeMenu = null
      this.mobileOpen = false
    }
  }
}
</script>

<style src="./volc-main.css"></style>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 100;
  background: rgba(255, 255, 255, 0.75);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(229, 230, 235, 0.6);
  transition: all 0.3s;
}
.navbar.scrolled {
  background: rgba(255, 255, 255, 0.95);
  border-bottom-color: var(--border-color);
}
.nav-container {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
  height: 64px;
}
.logo-link {
  flex-shrink: 0;
}
.logo-link img {
  width: 24px;
  height: 24px;
}
.logo-text {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
  white-space: nowrap;
}
.nav-links {
  display: flex;
  align-items: center;
  gap: 2px;
}
.nav-link {
  padding: 6px 12px;
  font-size: 13px;
  color: var(--text-secondary);
  border-radius: 6px;
  transition: all 0.2s;
  white-space: nowrap;
  cursor: pointer;
}
.nav-link:hover,
.nav-link-active {
  color: var(--text-primary);
  background: rgba(51, 112, 255, 0.08);
}
.btn-ghost {
  padding: 6px 14px;
  font-size: 13px;
  color: var(--text-secondary);
  border-radius: 6px;
  transition: all 0.2s;
  white-space: nowrap;
}
.btn-ghost:hover {
  color: var(--text-primary);
}
.btn-primary-sm {
  display: inline-flex;
  align-items: center;
  padding: 6px 16px;
  font-size: 13px;
  background: var(--color-brand);
  color: #fff;
  border-radius: 6px;
  font-weight: 500;
  transition: background 0.2s;
  white-space: nowrap;
}
.btn-primary-sm:hover {
  background: var(--color-brand-hover);
}

/* ===== Dropdown Container ===== */
.nav-dropdown {
  position: relative;
}

/* ===== Mega Panel ===== */
.mega-panel {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  background: #ffffff;
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
  z-index: 200;
}
.mega-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
  display: flex;
  min-height: 420px;
}

/* ===== Sidebar ===== */
.mega-sidebar {
  width: 280px;
  flex-shrink: 0;
  padding: 20px 0;
  border-right: 1px solid var(--border-color);
}
.mega-cat-item {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 16px;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.2s;
  margin-bottom: 2px;
}
.mega-cat-item:hover,
.mega-cat-item.active {
  background: rgba(51, 112, 255, 0.06);
}
.mega-cat-item.active .mega-cat-name {
  color: var(--text-primary);
}
.mega-cat-item.active .mega-cat-arrow {
  color: var(--color-brand);
  opacity: 1;
}
.mega-cat-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.mega-cat-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.mega-cat-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-secondary);
  transition: color 0.2s;
}
.mega-cat-desc {
  font-size: 12px;
  color: var(--text-muted);
}
.mega-cat-arrow {
  color: var(--text-muted);
  opacity: 0;
  transition: all 0.2s;
  flex-shrink: 0;
}

/* ===== Detail Panel ===== */
.mega-detail {
  flex: 1;
  padding: 20px 0 20px 32px;
  min-width: 0;
}
.mega-detail-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 20px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border-color);
}
.mega-detail-title {
  font-size: 16px;
  font-weight: 700;
  color: var(--text-primary);
}
.mega-detail-link {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  font-size: 13px;
  font-weight: 500;
  color: var(--color-brand);
  transition: gap 0.2s;
}
.mega-detail-link:hover {
  gap: 8px;
}

/* ===== Product Cards in Detail ===== */
.mega-detail-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 8px;
}
.mega-product-card {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  padding: 14px 16px;
  border-radius: 10px;
  transition: all 0.2s;
  cursor: pointer;
}
.mega-product-card:hover {
  background: rgba(51, 112, 255, 0.06);
}
.mega-product-card:hover .mega-product-name {
  color: var(--color-brand);
}
.mega-product-icon {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
.mega-product-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}
.mega-product-name {
  font-size: 14px;
  font-weight: 600;
  color: var(--text-primary);
  transition: color 0.2s;
  white-space: nowrap;
}
.mega-product-desc {
  font-size: 12px;
  color: var(--text-muted);
  line-height: 1.5;
}
.mega-tag {
  font-size: 10px;
  font-weight: 600;
  padding: 1px 5px;
  border-radius: 3px;
  white-space: nowrap;
  flex-shrink: 0;
  line-height: 1.4;
}
.mega-tag-hot {
  background: rgba(245, 63, 63, 0.15);
  color: var(--color-red);
}
.mega-tag-new {
  background: rgba(20, 201, 201, 0.15);
  color: var(--color-accent);
}

/* ===== Backdrop ===== */
.mega-backdrop {
  position: fixed;
  top: 64px;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 99;
  background: rgba(0, 0, 0, 0.18);
}

/* ===== Transitions ===== */
.mega-fade-enter-active,
.mega-fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}
.mega-fade-enter,
.mega-fade-leave-to {
  opacity: 0;
}
.mega-fade-enter .mega-panel,
.mega-fade-leave-to .mega-panel {
  transform: translateY(-8px);
}

/* ===== Mobile ===== */
.mobile-menu-btn {
  display: none;
  color: var(--text-secondary);
  background: none;
}
.mobile-menu {
  padding: 16px 24px 24px;
  display: flex;
  flex-direction: column;
  gap: 2px;
  background: rgba(255, 255, 255, 0.98);
  border-top: 1px solid var(--border-color);
  max-height: calc(100vh - 64px);
  overflow-y: auto;
}
.mobile-link {
  padding: 12px 16px;
  font-size: 14px;
  color: var(--text-secondary);
  border-radius: 8px;
  transition: all 0.2s;
  display: block;
}
.mobile-link:hover {
  background: var(--bg-card);
  color: var(--text-primary);
}
.mobile-section {
  border-bottom: 1px solid var(--border-color);
  padding-bottom: 4px;
  margin-bottom: 4px;
}
.mobile-section-title {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px 16px;
  font-size: 14px;
  color: var(--text-secondary);
  cursor: pointer;
  border-radius: 8px;
  transition: all 0.2s;
}
.mobile-section-title:hover {
  background: var(--bg-card);
  color: var(--text-primary);
}
.mobile-sub-list {
  padding: 0 0 8px 12px;
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.mobile-sub-link {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  font-size: 13px;
  color: var(--text-muted);
  border-radius: 8px;
  transition: all 0.2s;
}
.mobile-sub-link:hover {
  background: var(--bg-card);
  color: var(--text-primary);
}

.slide-enter-active,
.slide-leave-active {
  transition: all 0.3s ease;
}
.slide-enter,
.slide-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}

@media (max-width: 1024px) {
  .mobile-menu-btn {
    display: flex;
  }
  .nav-links {
    display: none;
  }
}
@media (min-width: 1025px) {
  .mobile-menu {
    display: none !important;
  }
}
</style>

