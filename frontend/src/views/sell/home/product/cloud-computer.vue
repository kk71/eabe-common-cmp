<template>
  <div class="product">
    <div class="content">
      <!-- 产品介绍 -->
      <div class="product-intro">
        <div class="intro-header">
          <h1>云电脑</h1>
          <p class="intro-subtitle">安全、高效的云上电脑，易于创建、部署和统一管理</p>
          <p class="intro-desc">
            云电脑（Elastic Desktop
            Service）是一种安全、高效的云上电脑，易于创建、部署和统一管理，自带多重安全管控，访问灵活，资源调整弹性，广泛应用于办公、教育、协作等场景。
          </p>
        </div>
      </div>

      <!-- 产品优势 -->
      <div class="item-features">
        <div class="features-header">
          <h2>产品优势</h2>
        </div>
        <div class="features-grid">
          <div class="feature-card" v-for="feature in features" :key="feature.title">
            <div class="card-body">
              <div class="body-icon">
                <i :class="feature.icon"></i>
              </div>
              <div class="body-title">{{ feature.title }}</div>
              <div class="body-desc">{{ feature.desc }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 产品功能 -->
      <div class="product-functions">
        <div class="functions-header">
          <h2>产品功能</h2>
        </div>
        <div class="functions-tabs">
          <div
            class="tab-item"
            v-for="(tab, index) in functionTabs"
            :key="index"
            :class="{ active: activeFunctionTab === index }"
            @click="activeFunctionTab = index"
          >
            {{ tab.title }}
          </div>
        </div>
        <div class="functions-content">
          <div class="function-group" v-for="group in functionTabs[activeFunctionTab].groups" :key="group.title">
            <h3>{{ group.title }}</h3>
            <p class="group-desc">{{ group.desc }}</p>
            <div class="function-list">
              <div class="function-item" v-for="item in group.items" :key="item.title">
                <div class="item-title">{{ item.title }}</div>
                <div class="item-desc">{{ item.desc }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 应用场景 -->
      <div class="product-scenarios">
        <div class="scenarios-header">
          <h2>应用场景</h2>
        </div>
        <div class="scenarios-tabs">
          <div
            class="tab-item"
            v-for="(scenario, index) in scenarios"
            :key="index"
            :class="{ active: activeScenarioTab === index }"
            @click="activeScenarioTab = index"
          >
            {{ scenario.tabText }}
          </div>
        </div>
        <div class="scenarios-content">
          <div class="scenario-detail">
            <div class="scenario-image">
              <img :src="scenarios[activeScenarioTab].img" :alt="scenarios[activeScenarioTab].title" />
            </div>
            <div class="scenario-info">
              <h3>{{ scenarios[activeScenarioTab].title }}</h3>
              <p class="scenario-desc">{{ scenarios[activeScenarioTab].descText }}</p>
              <div class="scenario-solutions">
                <h4>能够解决</h4>
                <ul>
                  <li v-for="solution in scenarios[activeScenarioTab].solutions" :key="solution.title">
                    <strong>{{ solution.title }}</strong>
                    <p>{{ solution.detail }}</p>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'Product',

    data() {
      return {
        activeFunctionTab: 0,
        activeScenarioTab: 0,
        features: [
          {
            title: '安全可靠',
            desc: '数据统一保存在云端，降低泄露风险；接入协议安全加密；存储数据可靠性达9个9',
            icon: 'el-icon-lock',
          },
          {
            title: '易用高效',
            desc: '集中管控，高效云电脑管理；无需服务器、机房投资，免运维',
            icon: 'el-icon-setting',
          },
          {
            title: '灵活弹性',
            desc: '随用随买，按需创建；多端接入，随时随地访问统一电脑环境',
            icon: 'el-icon-refresh',
          },
          {
            title: '高性能',
            desc: '支持GPU（图像设计、建模等），高性能显示协议应对视频编辑需求',
            icon: 'el-icon-cpu',
          },
          {
            title: 'AI智能',
            desc: '基于大模型的AI助手，提升用户办公效率，激活创新潜能',
            icon: 'el-icon-magic-stick',
          },
          {
            title: '绿色节能',
            desc: '计算任务在云端完成，本地设备极致低功耗，有效减少电力成本',
            icon: 'el-icon-sunny',
          },
        ],
        functionTabs: [
          {
            title: '企业版',
            groups: [
              {
                title: '高效灵活',
                desc: '购买灵活、集中管控、高效便捷的云电脑维护管理',
                items: [
                  {
                    title: '接入便捷',
                    desc: '支持Windows客户端、MacOS客户端等多种终端接入，通过互联网可随时随地接入到统一的云电脑环境中，不受时间地域限制',
                  },
                  {
                    title: '高效管理',
                    desc: '可高效应对云电脑创建、分配、回收等维护操作，极大缩短IT设施准备时间，提高电脑交付效率',
                  },
                  {
                    title: '配置规格丰富',
                    desc: '提供多种配置规格可供选择，满足不同场景需求',
                  },
                  {
                    title: '按需购买，随用随创',
                    desc: '按需购买及创建，极大缩短IT资产准备时间，有效应对临时性、突发性的电脑需求',
                  },
                  {
                    title: 'USB外设支持种类丰富',
                    desc: '提供USB外设重定向功能，支持U盘、Ukey、打印机、扫描仪等多种设备',
                  },
                ],
              },
              {
                title: '安全可靠',
                desc: '有效防止数据泄漏，提供高可靠的数据保存',
                items: [
                  {
                    title: '数据防泄漏',
                    desc: '数据在云端，在本地客户端上不保存，仅通过加密的远程协议做像素显示',
                  },
                  {
                    title: 'USB外设行为可管控',
                    desc: '可控制USB外设的使能与禁用，对U盘类设备可控制数据的读写权限',
                  },
                  {
                    title: '录屏审计可溯源',
                    desc: '丰富的安全策略确保企业数据存在云端不落地，辅以录屏审计可溯源，从而减少数据泄漏的风险，实现精细化的安全管控',
                  },
                ],
              },
              {
                title: '更高性能',
                desc: '提供高性能的图形工作站，支持设计、建模等专业场景',
                items: [
                  {
                    title: '满足对GPU有需求的场景',
                    desc: '高性能的图形工作站，有效支持图形设计、建模、影视制作、视频编辑等专业场景，提供高效的综合解决方案',
                  },
                ],
              },
            ],
          },
          {
            title: '个人版',
            groups: [
              {
                title: '灵活易用',
                desc: '一体化购买，全端覆盖，使用便捷',
                items: [
                  {
                    title: '端内购买',
                    desc: '客户端内一站式便捷选购，下单成功后直接使用，无需跳转',
                  },
                  {
                    title: '灵活接入',
                    desc: '支持Windows客户端、MacOS客户端、微信及支付宝小程序等多种方式接入，不受时间地域限制',
                  },
                  {
                    title: 'USB外设支持种类丰富',
                    desc: '提供USB外设重定向功能，支持U盘、Ukey、打印机、扫描仪等多种设备',
                  },
                ],
              },
              {
                title: '高效便捷',
                desc: '产品功能丰富，支持多场景使用',
                items: [
                  {
                    title: '数据防泄漏',
                    desc: '数据在云端，在本地客户端上不保存，仅通过加密的远程协议做像素显示',
                  },
                  {
                    title: '镜像分享',
                    desc: '随时随地分发自定义镜像，快速复制并分享内容',
                  },
                  {
                    title: '按需升降配',
                    desc: '根据需求快速升降配电脑规格，扩大存储容量，提升网络带宽',
                  },
                ],
              },
            ],
          },
          {
            title: '商业版',
            groups: [
              {
                title: '用户体验',
                desc: '',
                items: [
                  {
                    title: '多端接入',
                    desc: '支持PC客户端（含Windows和macOS）、HTML5浏览器无插件、硬件终端、iOS和Android移动终端等设备接入和访问云电脑',
                  },
                  {
                    title: '悬浮球',
                    desc: '支持云电脑悬浮球显示网络状态，用户可以实时查看网络状态和时延，能够给出明确的网络时延、端到端时延、帧率、分辨率、上下行带宽等数据呈现',
                  },
                  {
                    title: '应用商店',
                    desc: '桌面内支持应用商店，包含业界主流应用软件，支持在线下载直接安装使用，提供给使用者更好的应用体验',
                  },
                ],
              },
              {
                title: '运维管控',
                desc: '',
                items: [
                  {
                    title: '云电脑监控',
                    desc: '支持云电脑实时监控，可监控云电脑当前使用情况（包含云电脑总数，运行状态，资源、会话连接数，登录时间、网络延迟，TOP资源等信息）',
                  },
                  {
                    title: '镜像分发',
                    desc: '提供在线镜像制作器，在开放环境下进行镜像在线制作、调试和发布',
                  },
                ],
              },
              {
                title: '安全管控',
                desc: '',
                items: [
                  {
                    title: '终端绑定',
                    desc: '支持云电脑用户与硬件终端/物理PC终端之间进行登陆绑定，实现安全性管控',
                  },
                  {
                    title: '安全水印',
                    desc: '支持屏幕盲水印功能，水印内容（显示云电脑ID、IP地址、客户端IP地址、云电脑当前时间等）',
                  },
                  {
                    title: '防截屏',
                    desc: '支持Windows和Mac客户端防截屏',
                  },
                  {
                    title: '磁盘映射',
                    desc: '支持本地磁盘映射管理，可控制用户读写、只读以及关闭本地磁盘在云电脑上的映射',
                  },
                  {
                    title: '剪切板',
                    desc: '支持剪贴板双向拷贝管理，可控制本地电脑与云电脑双向拷贝、单向拷贝、双向禁止',
                  },
                  {
                    title: '外设管理',
                    desc: '支持打印机重定向管理，用户允许或禁止在云电脑中使用本地终端连接的USB打印机和网络打印机',
                  },
                  {
                    title: '域名黑白名单',
                    desc: '支持域名黑白名单管理，用于控制云电脑可以访问的域名，支持*通配符',
                  },
                  {
                    title: '录屏审计',
                    desc: '支持平台自带的录屏审计管控，拥有全程录屏、间隔录屏以及用户操作录屏功能，以便管理员回看录屏，进行安全行为审计',
                  },
                  {
                    title: '磁盘加密',
                    desc: '支持系统盘和数据盘加密，更好地保密数据',
                  },
                ],
              },
            ],
          },
        ],
        scenarios: [
          {
            tabText: '短期使用场景',
            title: '短期使用场景',
            descText: '短期外包、实习生，考试认证的企业和机构',
            img: 'https://img.alicdn.com/imgextra/i3/O1CN013BIKI41XvdcGXUMrH_!!6000000002986-2-tps-1530-1140.png',
            solutions: [
              {
                title: '有效应对短期、临时电脑需求',
                detail: '按需弹性创建租用，灵活应对外包、实习生、考试机构等短期需求',
              },
            ],
          },
          {
            tabText: '数据安全管控场景',
            title: '数据安全管控场景',
            descText: '对企业数据和设计资料有保密要求，防止泄漏',
            img: 'https://img.alicdn.com/imgextra/i2/O1CN01OMSiw51GsZUnl7Gmr_!!6000000000678-2-tps-1530-1140.png',
            solutions: [
              {
                title: '数据不落地',
                detail: '数据保存在服务端，不在客户端有任何留存，避免被非授权拷贝',
              },
              {
                title: '显示协议加密传输',
                detail: '云电脑内容显示通过协议仅做像素级传输，且经过加密处理',
              },
            ],
          },
          {
            tabText: '分支机构在多地点的场景',
            title: '分支机构在多地点的场景',
            descText: '有多个办公地点分散在各地，单一地点规模较小，例如大型企业在各地的办事处、大型零售连锁商超等',
            img: 'https://img.alicdn.com/imgextra/i3/O1CN01IHl3MG1viOwrFuzPf_!!6000000006206-0-tps-1530-1140.jpg',
            solutions: [
              {
                title: '电脑维护和支持难保障',
                detail: '云电脑集中管控，可轻松管理散落在各地的终端设备',
              },
              {
                title: 'IT资产管理困难',
                detail: '以云电脑替代传统的PC，轻松处理各地IT资产管理问题',
              },
            ],
          },
          {
            tabText: '设计、制图、视频场景',
            title: '设计、制图、视频场景',
            descText: '专业设计领域，需要有GPU支持的桌面，同时对设计过程中的协作和设计成果的保护有较高要求',
            img: 'https://img.alicdn.com/imgextra/i2/O1CN01jhyKdB1d6hG726MfY_!!6000000003687-0-tps-1530-1140.jpg',
            solutions: [
              {
                title: '专业软件对GPU的需求',
                detail: '提供高性能的GPU型云电脑，满足专业制图等软件的使用需求',
              },
              {
                title: '设计过程中的协作',
                detail: '高性能NAS存储便于设计协作，HPC等服务可对建模结果及时渲染',
              },
              {
                title: '设计成果的保护',
                detail: '数据不落地的安全性，有效避免设计成果被恶意拷贝',
              },
            ],
          },
        ],
      };
    },
    mounted() {
      this.getProductInfo();
    },
    methods: {
      getProductInfo() {
        const id = this.$route.params.id;
        this.axios.get(`/api/product/${id}`).then((res) => {
          this.product = res;
        });
      },
      buy() {
        const id = this.$route.params.id;
        this.$router.push(`/detail/${id}`);
      },
      closeVideo() {
        this.showSlide = 'slideUp';
        setTimeout(() => {
          this.showSlide = '';
        }, 600);
      },
    },
  };
</script>
<style lang="scss" scoped>
  .product {
    background: #f5f5f5;
    min-height: 100vh;

    .content {
      max-width: 1280px;
      margin: 0 auto;
      padding: 50px 0;

      // 产品介绍
      .product-intro {
        background: #fff;
        padding: 60px 40px;
        margin-bottom: 40px;
        border-radius: 8px;

        .intro-header {
          text-align: center;

          h1 {
            font-size: 56px;
            color: #181818;
            margin-bottom: 20px;
            font-weight: 600;
          }

          .intro-subtitle {
            font-size: 24px;
            color: #333;
            margin-bottom: 20px;
            font-weight: 500;
          }

          .intro-desc {
            font-size: 16px;
            color: #666;
            line-height: 1.8;
            max-width: 900px;
            margin: 0 auto;
          }
        }
      }

      // 产品优势
      .item-features {
        margin-bottom: 60px;

        .features-header {
          text-align: center;
          margin-bottom: 40px;

          h2 {
            font-size: 36px;
            color: #181818;
            margin-bottom: 20px;
            font-weight: 600;
          }
        }

        .features-grid {
          display: grid;
          grid-template-columns: repeat(3, 1fr);
          gap: 20px;
          padding: 0 20px;

          .feature-card {
            background: #fff;
            border: 1px solid #ececec;
            border-radius: 8px;
            transition: all 0.3s ease;
            cursor: pointer;

            &:hover {
              box-shadow: 0px 4px 12px 0px rgba(0, 0, 0, 0.1);
              transform: translateY(-4px);
              border-color: #ff6a00;
            }

            .card-body {
              padding: 30px;

              .body-icon {
                margin-bottom: 16px;

                i {
                  font-size: 48px;
                  color: #ff6a00;
                }
              }

              .body-title {
                font-size: 20px;
                color: #181818;
                font-weight: 600;
                margin-bottom: 12px;
                line-height: 1.4;
              }

              .body-desc {
                font-size: 14px;
                color: #666;
                line-height: 1.8;
              }
            }
          }
        }
      }

      // 产品功能
      .product-functions {
        margin-bottom: 60px;

        .functions-header {
          text-align: center;
          margin-bottom: 40px;

          h2 {
            font-size: 36px;
            color: #181818;
            font-weight: 600;
          }
        }

        .functions-tabs {
          display: flex;
          justify-content: center;
          gap: 20px;
          margin-bottom: 40px;

          .tab-item {
            padding: 12px 32px;
            background: #fff;
            border: 1px solid #d8d8d8;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            color: #666;
            transition: all 0.3s ease;

            &:hover {
              border-color: #ff6a00;
              color: #ff6a00;
            }

            &.active {
              background: #ff6a00;
              border-color: #ff6a00;
              color: #fff;
            }
          }
        }

        .functions-content {
          background: #fff;
          padding: 40px;
          border-radius: 8px;

          .function-group {
            margin-bottom: 40px;

            &:last-child {
              margin-bottom: 0;
            }

            h3 {
              font-size: 24px;
              color: #181818;
              font-weight: 600;
              margin-bottom: 12px;
            }

            .group-desc {
              font-size: 14px;
              color: #666;
              margin-bottom: 24px;
              line-height: 1.6;
            }

            .function-list {
              display: grid;
              grid-template-columns: repeat(2, 1fr);
              gap: 20px;

              .function-item {
                padding: 20px;
                background: #f9f9f9;
                border-radius: 6px;
                transition: all 0.3s ease;

                &:hover {
                  background: #fff0e5;
                }

                .item-title {
                  font-size: 16px;
                  color: #181818;
                  font-weight: 600;
                  margin-bottom: 8px;
                }

                .item-desc {
                  font-size: 14px;
                  color: #666;
                  line-height: 1.6;
                }
              }
            }
          }
        }
      }

      // 应用场景
      .product-scenarios {
        margin-bottom: 60px;

        .scenarios-header {
          text-align: center;
          margin-bottom: 40px;

          h2 {
            font-size: 36px;
            color: #181818;
            font-weight: 600;
          }
        }

        .scenarios-tabs {
          display: flex;
          justify-content: center;
          gap: 20px;
          margin-bottom: 40px;
          flex-wrap: wrap;

          .tab-item {
            padding: 12px 24px;
            background: #fff;
            border: 1px solid #d8d8d8;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            color: #666;
            transition: all 0.3s ease;

            &:hover {
              border-color: #ff6a00;
              color: #ff6a00;
            }

            &.active {
              background: #ff6a00;
              border-color: #ff6a00;
              color: #fff;
            }
          }
        }

        .scenarios-content {
          background: #fff;
          padding: 40px;
          border-radius: 8px;

          .scenario-detail {
            display: flex;
            gap: 40px;
            align-items: flex-start;

            .scenario-image {
              flex: 1;
              max-width: 600px;

              img {
                width: 100%;
                height: auto;
                border-radius: 8px;
              }
            }

            .scenario-info {
              flex: 1;

              h3 {
                font-size: 28px;
                color: #181818;
                font-weight: 600;
                margin-bottom: 16px;
              }

              .scenario-desc {
                font-size: 16px;
                color: #666;
                line-height: 1.8;
                margin-bottom: 24px;
              }

              .scenario-solutions {
                h4 {
                  font-size: 20px;
                  color: #181818;
                  font-weight: 600;
                  margin-bottom: 16px;
                }

                ul {
                  list-style: none;
                  padding: 0;

                  li {
                    margin-bottom: 16px;
                    padding-left: 20px;
                    position: relative;

                    &:before {
                      content: '•';
                      position: absolute;
                      left: 0;
                      color: #ff6a00;
                      font-size: 20px;
                      line-height: 1.4;
                    }

                    strong {
                      display: block;
                      font-size: 16px;
                      color: #181818;
                      margin-bottom: 4px;
                    }

                    p {
                      font-size: 14px;
                      color: #666;
                      line-height: 1.6;
                      margin: 0;
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }

  @media screen and (max-width: 768px) {
    .product {
      .content {
        padding: 30px 0;

        .product-intro {
          padding: 40px 20px;
          margin-bottom: 30px;

          .intro-header {
            h1 {
              font-size: 32px;
            }

            .intro-subtitle {
              font-size: 18px;
            }

            .intro-desc {
              font-size: 14px;
            }
          }
        }

        .item-features {
          margin-bottom: 40px;

          .features-header {
            margin-bottom: 30px;

            h2 {
              font-size: 28px;
            }
          }

          .features-grid {
            grid-template-columns: 1fr;
            gap: 15px;

            .feature-card {
              .card-body {
                padding: 20px;

                .body-icon {
                  i {
                    font-size: 36px;
                  }
                }

                .body-title {
                  font-size: 18px;
                }

                .body-desc {
                  font-size: 13px;
                }
              }
            }
          }
        }

        .product-functions {
          margin-bottom: 40px;

          .functions-header {
            margin-bottom: 30px;

            h2 {
              font-size: 28px;
            }
          }

          .functions-tabs {
            flex-wrap: wrap;
            gap: 10px;
            padding: 0 20px;

            .tab-item {
              padding: 10px 20px;
              font-size: 14px;
            }
          }

          .functions-content {
            padding: 20px;

            .function-group {
              margin-bottom: 30px;

              h3 {
                font-size: 20px;
              }

              .group-desc {
                font-size: 13px;
              }

              .function-list {
                grid-template-columns: 1fr;
                gap: 15px;

                .function-item {
                  padding: 15px;

                  .item-title {
                    font-size: 15px;
                  }

                  .item-desc {
                    font-size: 13px;
                  }
                }
              }
            }
          }
        }

        .product-scenarios {
          margin-bottom: 40px;

          .scenarios-header {
            margin-bottom: 30px;

            h2 {
              font-size: 28px;
            }
          }

          .scenarios-tabs {
            gap: 10px;
            padding: 0 20px;

            .tab-item {
              padding: 10px 16px;
              font-size: 14px;
            }
          }

          .scenarios-content {
            padding: 20px;

            .scenario-detail {
              flex-direction: column;
              gap: 20px;

              .scenario-image {
                max-width: 100%;
              }

              .scenario-info {
                h3 {
                  font-size: 22px;
                }

                .scenario-desc {
                  font-size: 14px;
                }

                .scenario-solutions {
                  h4 {
                    font-size: 18px;
                  }

                  ul {
                    li {
                      margin-bottom: 12px;

                      strong {
                        font-size: 15px;
                      }

                      p {
                        font-size: 13px;
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
  }
</style>
