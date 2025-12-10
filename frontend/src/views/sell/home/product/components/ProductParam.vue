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
    height: 70px;
    line-height: 70px;
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
</style>
