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
</style>
