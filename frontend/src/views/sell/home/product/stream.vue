<template>
  <div class="detail">
    <product-param title="基础产品"></product-param>
    <div class="wrapper" v-loading="loading">
      <div class="container clearfix">
        <div class="swiper">
          <img src="./imgs/global-network.png" alt="" />
        </div>
        <div class="content">
          <h2 class="item-title">手机流量充值服务</h2>
          <p v-if="false" class="item-info"> </p>
          <div class="line"></div>
          <div class="item-version">
            <h2>选择时间段</h2>
            <csm flag="product-stream-period" v-model="data.product.period" type="radio" size="large" />
          </div>
          <div class="item-version">
            <h2>选择流量</h2>
            <csm flag="product-stream-quantity" v-model="data.product.quantity" type="radio" size="large" />
          </div>
          <div class="item-version">
            <h2>充值号码</h2>
            <plain-text v-model="data.product.target_phone_number" />
          </div>
          <div class="item-total" v-if="data.calc_info.price">
            <div class="phone-info clearfix">
              <div class="fl">{{ data.calc_info.desc }} </div>
              <div class="fr">{{ data.calc_info.price }} 元</div>
            </div>
            <div class="phone-total">总计：{{ data.calc_info.price }}元</div>
          </div>
          <div class="item-total" v-else>
            <div class="phone-info clearfix">
              <div class="fl">请选择其他配置</div>
            </div>
          </div>
          <div class="btn-group">
            <a v-if="ableToAddCart" href="javascript:;" class="btn btn-huge fl" @click="addCart">加入购物车</a>
          </div>
        </div>
      </div>
    </div>
    <service-bar />
  </div>
</template>
<script setup>
  import { ElMessage } from 'element-plus';

  import { calcProductInfo, addToCart } from '@/api/sell';

  import ProductParam from './components/ProductParam.vue';
  import ServiceBar from '../../components/ServiceBar.vue';

  const data = reactive({
    product: {
      type: 'stream',
      target_phone_number: '',
      period: null,
      quantity: null,
    },
    calc_info: {
      price: null,
      desc: null,
    },
  });

  const loading = ref(false);

  const calcProduct = async () => {
    const resp = await calcProductInfo({ data: data.product });
    data.calc_info = resp.data.data;
  };

  const ableToAddCart = computed(() => {
    return data.calc_info.price > 0;
  });

  const addCart = async () => {
    if (!data.product.target_phone_number) {
      return ElMessage({ message: '请输入充值号码。', type: 'error' });
    }
    await addToCart({ data: data.product });
  };

  watch(
    () => data.product,
    async () => {
      await calcProduct();
    },
    { deep: true },
  );
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
          font-size: 22px;
          font-weight: 800;
          height: 36px;
        }
        .delivery {
          font-size: 16px;
          color: #ff6700;
          margin-top: 26px;
          margin-bottom: 14px;
          height: 15px;
        }
        .item-price {
          font-size: 20px;
          color: #ff6700;
          height: 19px;
          .del {
            font-size: 16px;
            color: #999999;
            margin-left: 10px;
            text-decoration: line-through;
          }
        }
        .line {
          height: 0;
          margin-top: 25px;
          margin-bottom: 28px;
          border-top: 1px solid #e5e5e5;
        }
        .item-addr {
          height: 108px;
          background-color: #fafafa;
          border: 1px solid #e5e5e5;
          box-sizing: border-box;
          padding-top: 31px;
          padding-left: 64px;
          font-size: 14px;
          line-height: 14px;
          position: relative;
          .icon-loc {
            position: absolute;
            top: 27px;
            left: 34px;
            @include bgImg(20px, 20px, './imgs/icon-loc.png');
          }
          .addr {
            color: #666666;
          }
          .stock {
            margin-top: 15px;
            color: #ff6700;
          }
        }
        .item-version,
        .item-color {
          margin-top: 30px;
          h2 {
            font-size: 18px;
            margin-bottom: 20px;
          }
        }
        .item-version,
        .item-color {
          .phone {
            width: 287px;
            height: 50px;
            line-height: 50px;
            font-size: 16px;
            color: #333333;
            border: 1px solid #e5e5e5;
            box-sizing: border-box;
            text-align: center;
            cursor: pointer;
            span {
              color: #666666;
              margin-left: 15px;
            }
            .color {
              display: inline-block;
              width: 14px;
              height: 14px;
              background-color: #666666;
            }
            &.checked {
              border: 1px solid #ff6600;
              color: #ff6600;
            }
          }
        }
        .item-total {
          height: 108px;
          background: #fafafa;
          padding: 24px 33px 29px 30px;
          font-size: 14px;
          margin-top: 50px;
          margin-bottom: 30px;
          box-sizing: border-box;
          .phone-total {
            font-size: 24px;
            color: #ff6600;
            margin-top: 18px;
          }
        }
      }
    }
    .price-info {
      background-color: #f3f3f3;
      height: 340px;
      h2 {
        font-size: 24px;
        color: #333333;
        padding-top: 38px;
        margin-bottom: 30px;
      }
    }
  }
</style>
