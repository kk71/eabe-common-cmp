<template>
  <div class="detail">
    <product-param title="存储"></product-param>
    <div class="wrapper">
      <div class="container clearfix">
        <div class="swiper">
          <img src="./imgs/global-network.png" alt="" />
        </div>
        <div class="content">
          <h2 class="item-title">块存储 EBS</h2>
          <p class="item-info">高性能、低延迟的块存储服务，为云服务器提供数据存储</p>
          <div class="line"></div>
          <div class="item-total">
            <div class="phone-info clearfix">
              <div class="fl">块存储 EBS</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <service-bar />
  </div>
</template>
<script setup>
  import ProductParam from './components/ProductParam.vue';
  import ServiceBar from '../../components/ServiceBar.vue';
</script>
<style lang="scss">
  @import '../../scss/config.scss';
  @import '../../scss/mixin.scss';
  .detail {
    .wrapper {
      .swiper {
        float: left;
        width: 642px;
        height: 617px;
        margin-top: 5px;
        img {
          width: 100%;
          height: 100%;
        }
      }
      .content {
        float: right;
        width: 584px;
        height: 870px;
        .item-title {
          font-size: 28px;
          padding-top: 30px;
          padding-bottom: 16px;
          height: 26px;
        }
        .item-info {
          font-size: 18px;
          color: #666;
          height: 36px;
        }
        .line {
          height: 0;
          margin-top: 25px;
          margin-bottom: 28px;
          border-top: 1px solid #e5e5e5;
        }
        .item-total {
          height: 108px;
          background: #fafafa;
          padding: 24px 33px 29px 30px;
          font-size: 14px;
          margin-top: 50px;
          margin-bottom: 30px;
          box-sizing: border-box;
        }
      }
    }
  }
</style>

