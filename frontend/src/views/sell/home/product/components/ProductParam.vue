<template>
  <div class="nav-bar is_fixed">
    <div class="container">
      <div class="pro-title">
        {{ props.title }}
      </div>
      <div class="pro-param">
        <a href="javascript:;">概述</a><span>|</span> {{ props.description }}<span>|</span>
        <slot name="buy"></slot>
      </div>
    </div>
  </div>
</template>

<script setup>
  const props = defineProps({
    title: String,
    description: String,
  });
</script>

<style lang="scss">
  @import '@/views/sell/scss/config.scss';
  @import '@/views/sell/scss/mixin.scss';
  .nav-bar {
    height: 56px;
    line-height: 56px;
    border-top: 1px solid $colorH;
    background-color: $colorG;
    z-index: 10;
    &.is_fixed {
      position: fixed;
      top: 0;
      width: 100%;
      box-shadow: 0 5px 5px $colorE;
    }
    .container {
      @include flex();
      .pro-title {
        font-size: $fontH;
        color: $colorB;
        font-weight: bold;
      }
      .pro-param {
        font-size: $fontJ;
        span {
          margin: 0 10px;
        }
        a {
          color: $colorC;
        }
      }
    }
  }

  /* 产品详情页（旧版 product/*.vue）整体缩小区块高度与上下间距 */
  .detail {
    .wrapper {
      padding-top: 10px;

      .container {
        padding-top: 6px;
        padding-bottom: 6px;
      }

      .container .swiper {
        height: 520px;
        margin-top: 0;
      }

      .container .content {
        height: auto;
        min-height: 680px;

        .item-title {
          padding-top: 18px;
          padding-bottom: 10px;
        }

        .item-info {
          height: auto;
          line-height: 1.4;
        }

        .line {
          margin-top: 16px;
          margin-bottom: 18px;
        }

        .item-total {
          height: auto;
          padding: 18px 24px;
          margin-top: 24px;
          margin-bottom: 18px;
        }
      }
    }
  }

  @media (max-width: 768px) {
    .nav-bar {
      height: auto;
      line-height: 1.4;
      padding: 10px 0;

      .container {
        flex-direction: column;
        align-items: flex-start;
        gap: 6px;
      }

      .pro-param {
        width: 100%;
        font-size: 12px;
        word-break: break-word;

        span {
          margin: 0 6px;
        }
      }
    }

    /* 旧版产品详情页：移动端改为上下布局，避免固定宽溢出 */
    .detail {
      .wrapper {
        .swiper,
        .content {
          float: none !important;
          width: 100% !important;
          height: auto !important;
        }

        .swiper {
          margin-top: 0 !important;

          img {
            height: auto;
          }
        }

        .content {
          .item-title,
          .item-info {
            height: auto !important;
          }

          .item-title {
            padding-top: 18px !important;
          }

          .line {
            margin-top: 16px !important;
            margin-bottom: 16px !important;
          }

          .item-total {
            height: auto !important;
            margin-top: 18px !important;
            margin-bottom: 16px !important;
            padding: 16px !important;
          }
        }
      }
    }
  }
</style>
