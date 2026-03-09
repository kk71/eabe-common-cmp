<template>
  <div class="service">
    <div class="container">
      <ul>
        <li><span class="icon-setting"></span>全天候高效服务</li>
        <li><span class="icon-7day"></span>多渠道无忧服务</li>
        <li><span class="icon-15day"></span>专属贴身服务</li>
        <li><span class="icon-post"></span>专业上云服务</li>
      </ul>
    </div>
  </div>
</template>
<script>
  export default {
    name: 'service-bar',
  };
</script>
<style lang="scss">
  @import '../scss/mixin.scss';
  .service {
    padding: 33px 0;
    color: #666666;
    font-size: 16px;
    ul {
      display: flex;
      flex-wrap: wrap;
    }
    li {
      display: inline-block;
      width: 24.9%;
      text-align: center;
      border-right: 1px solid #e5e5e5;
      span {
        display: inline-block;
        width: 20px;
        height: 20px;
        vertical-align: middle;
        margin-right: 8px;
      }
      .icon-setting {
        @include bgImg(20px, 20px, '/imgs/icon-setting.png');
      }
      .icon-7day {
        @include bgImg(20px, 20px, '/imgs/icon-7day.png');
      }
      .icon-15day {
        @include bgImg(20px, 20px, '/imgs/icon-15day.png');
      }
      .icon-post {
        @include bgImg(20px, 20px, '/imgs/icon-post.png');
      }
    }
  }

  @media (max-width: 768px) {
    .service {
      padding: 20px 0;
      font-size: 14px;

      li {
        width: 50%;
        padding: 10px 0;
        border-right: none;
      }
    }
  }

  @media (max-width: 360px) {
    .service {
      li {
        width: 100%;
      }
    }
  }
</style>
