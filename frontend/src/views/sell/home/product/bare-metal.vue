<template>
  <div class="product">
    <div class="content">
      <!-- 产品介绍 -->
      <div class="product-intro">
        <div class="intro-header">
          <h1>弹性裸金属服务器</h1>
          <p class="intro-subtitle">可弹性伸缩的高性能计算服务，物理级隔离，分钟级交付</p>
          <p class="intro-desc">
            弹性裸金属服务器（ECS Bare Metal
            Server）是一种可弹性伸缩的高性能计算服务，计算性能与传统物理机无差别，具有安全物理隔离的特点。分钟级的交付周期将提供给您实时的业务响应能力，助力您的核心业务飞速成长。
          </p>
        </div>
      </div>

      <!-- 产品优势 -->
      <div class="item-features">
        <div class="features-header">
          <h2>产品优势</h2>
        </div>
        <div class="features-grid">
          <div class="feature-card">
            <div class="card-body">
              <div class="body-icon">
                <img src="./imgs/product/icon-performance.png" alt="云原生应用最佳载体" />
              </div>
              <div class="body-title">云原生应用最佳载体</div>
              <div class="body-desc">性能比物理机普遍提升20%+，响应时间大幅下降，业务丝般顺滑</div>
            </div>
          </div>
          <div class="feature-card">
            <div class="card-body">
              <div class="body-icon">
                <img src="./imgs/product/icon-security.png" alt="安全可靠，卓越性能" />
              </div>
              <div class="body-title">安全可靠，卓越性能</div>
              <div class="body-desc">物理资源独占，性能无损，符合客户对于安全合规的要求</div>
            </div>
          </div>
          <div class="feature-card">
            <div class="card-body">
              <div class="body-icon">
                <img src="./imgs/product/icon-elastic.png" alt="特性无损，支持二次虚拟化" />
              </div>
              <div class="body-title">特性无损，支持二次虚拟化</div>
              <div class="body-desc">特性无损，支持二次虚拟化且性能不受影响，满足混合云和多云部署诉求</div>
            </div>
          </div>
          <div class="feature-card">
            <div class="card-body">
              <div class="body-icon">
                <img src="./imgs/product/icon-network.png" alt="分钟级交付，弹性扩容" />
              </div>
              <div class="body-title">分钟级交付，弹性扩容</div>
              <div class="body-desc">分钟级交付，弹性扩容，部署和运维全自动化</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 产品功能 -->
      <div class="product-functions">
        <div class="functions-header">
          <h2>产品功能</h2>
        </div>
        <div class="functions-content">
          <div class="functions-grid">
            <div class="function-item" v-for="func in productFunctions" :key="func.title">
              <div class="item-title">{{ func.title }}</div>
              <div class="item-desc">{{ func.desc }}</div>
            </div>
          </div>
        </div>
      </div>

      <!-- 性能对比 -->
      <div class="product-comparison">
        <div class="comparison-header">
          <h2>性能对比</h2>
        </div>
        <div class="comparison-content">
          <div class="comparison-table">
            <div class="comparison-row header">
              <div class="comparison-cell">特性</div>
              <div class="comparison-cell">弹性裸金属服务器</div>
              <div class="comparison-cell">传统物理机</div>
              <div class="comparison-cell">虚拟化云服务器</div>
            </div>
            <div class="comparison-row">
              <div class="comparison-cell">计算性能</div>
              <div class="comparison-cell highlight">100% 物理机性能</div>
              <div class="comparison-cell">100% 物理机性能</div>
              <div class="comparison-cell">有虚拟化损耗</div>
            </div>
            <div class="comparison-row">
              <div class="comparison-cell">交付时间</div>
              <div class="comparison-cell highlight">分钟级</div>
              <div class="comparison-cell">天级/周级</div>
              <div class="comparison-cell">秒级</div>
            </div>
            <div class="comparison-row">
              <div class="comparison-cell">弹性伸缩</div>
              <div class="comparison-cell highlight">支持</div>
              <div class="comparison-cell">不支持</div>
              <div class="comparison-cell">支持</div>
            </div>
            <div class="comparison-row">
              <div class="comparison-cell">资源隔离</div>
              <div class="comparison-cell highlight">物理级隔离</div>
              <div class="comparison-cell">物理级隔离</div>
              <div class="comparison-cell">虚拟化隔离</div>
            </div>
            <div class="comparison-row">
              <div class="comparison-cell">云产品互通</div>
              <div class="comparison-cell highlight">完全兼容</div>
              <div class="comparison-cell">需要配置</div>
              <div class="comparison-cell">完全兼容</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'product',
    data() {
      return {
        product: {}, //商品信息
        productFunctions: [
          {
            title: '计算',
            desc: '无性能损失，无特性损失，无资源争抢。',
          },
          {
            title: '存储',
            desc: '完全兼容虚拟机云盘系统，完全兼容虚拟机镜像系统，使用云盘启动，免操作系统安装，系统盘快速重置。',
          },
          {
            title: '网络',
            desc: '完全兼容虚拟机VPC网络，弹性裸金属和虚拟机之间VPC通信无性能瓶颈。',
          },
          {
            title: '运维',
            desc: '分钟级交付，非本地盘实例支持宕机自动迁移，支持实例在弹性裸金属和虚拟机之间相互迁移。',
          },
          {
            title: '管控',
            desc: '完全兼容虚拟机管控系统，VNC等用户体验和虚拟机保持一致。',
          },
          {
            title: '付费方式',
            desc: '支持包年包月、按量付费购买，适用节省计划和预留实例券，支持抢占式实例。',
          },
        ],
      };
    },
    mounted() {
      this.getProductInfo();
    },
    methods: {
      getProductInfo() {
        let id = this.$route.params.id;
        this.axios.get(`/api/product/${id}`).then((res) => {
          this.product = res;
        });
      },
      buy() {
        let id = this.$route.params.id;
        this.$router.push(`/detail/${id}`);
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
          grid-template-columns: repeat(2, 1fr);
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
                width: 60px;
                height: 60px;

                img {
                  width: 100%;
                  height: 100%;
                  object-fit: contain;
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

        .functions-content {
          background: #fff;
          padding: 40px;
          border-radius: 8px;

          .functions-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
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

      // 性能对比
      .product-comparison {
        margin-bottom: 60px;

        .comparison-header {
          text-align: center;
          margin-bottom: 40px;

          h2 {
            font-size: 36px;
            color: #181818;
            font-weight: 600;
          }
        }

        .comparison-content {
          background: #fff;
          padding: 40px;
          border-radius: 8px;

          .comparison-table {
            background: #ffffff;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 2px 12px rgba(0, 0, 0, 0.08);

            .comparison-row {
              display: grid;
              grid-template-columns: 1.2fr 1fr 1fr 1fr;
              border-bottom: 1px solid #e0e0e0;

              &:last-child {
                border-bottom: none;
              }

              &.header {
                background: #f5f5f5;

                .comparison-cell {
                  font-weight: 600;
                  color: #333333;
                  font-size: 16px;
                }
              }

              .comparison-cell {
                padding: 20px 24px;
                font-size: 14px;
                color: #666666;
                border-right: 1px solid #e0e0e0;
                display: flex;
                align-items: center;
                justify-content: center;
                text-align: center;

                &:first-child {
                  justify-content: flex-start;
                  font-weight: 500;
                  color: #333333;
                }

                &:last-child {
                  border-right: none;
                }

                &.highlight {
                  color: #ff6a00;
                  font-weight: 600;
                  background: #fff8f0;
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
                  width: 48px;
                  height: 48px;
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

          .functions-content {
            padding: 20px;

            .functions-grid {
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

        .product-comparison {
          margin-bottom: 40px;

          .comparison-header {
            margin-bottom: 30px;

            h2 {
              font-size: 28px;
            }
          }

          .comparison-content {
            padding: 20px;

            .comparison-table {
              .comparison-row {
                grid-template-columns: 1fr;

                .comparison-cell {
                  padding: 15px;
                  border-right: none;
                  border-bottom: 1px solid #e0e0e0;

                  &:first-child {
                    justify-content: center;
                  }

                  &:last-child {
                    border-bottom: none;
                  }
                }

                &.header {
                  .comparison-cell {
                    font-size: 14px;
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
