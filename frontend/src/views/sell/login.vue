<template>
  <div class="login">
    <div class="container">
      <a href="/sell"><img src="/company-logo/LOGO2.png" alt="" /></a>
    </div>
    <div class="wrapper">
      <div class="container">
        <div class="login-form">
          <h3> <span class="checked">帐号登录</span><span class="sep-line">|</span><span>扫码登录</span> </h3>
          <div class="input">
            <input type="text" placeholder="请输入帐号" v-model="data.form.login_name" />
          </div>
          <div class="input">
            <input type="password" placeholder="请输入密码" v-model="data.form.password" />
          </div>
          <div class="btn-box">
            <a href="javascript:;" class="btn" @click="login">登录</a>
          </div>
          <div class="tips">
            <div class="reg">立即注册<span>|</span>忘记密码？</div>
          </div>
        </div>
      </div>
    </div>
    <div class="footer">
      <div class="footer-link">
        <a href="javascript:;">帮助中心</a><span>|</span> <a href="javascript:;">服务支持</a><span>|</span>
        <a href="javascript:;">线下门店</a><span>|</span>
        <a href="javascript:;">关于羿贝</a>
      </div>
      <div class="copyright">Copyright ©2025 Eabe All Rights Reserved.</div>
    </div>
  </div>
</template>
<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus';
  import { buildEncryptedPassword } from '@/utils/password.ts';
  import { waitRequest } from '@/utils/http/tools';
  import { userPasswordLogin } from '@/api/system';
  import { useAppStore } from '@/store/modules/app';

  const route = useRoute();

  const router = useRouter();

  const submitting = ref(false);

  const store = useAppStore();

  const formInit = () => {
    return {
      login_name: '',
      password: '',
    };
  };

  const data = reactive({
    form: formInit(),
  });

  const login = async () => {
    let resp;
    try {
      resp = await waitRequest(
        submitting,
        userPasswordLogin({
          data: {
            login_name: data.form.login_name,
            password: await buildEncryptedPassword(data.form.password),
          },
        }),
      );
    } catch (e) {
      data.form.password = '';
      return;
    }
    store.setToken(resp.data.data.token, resp.data.data.user, resp.data.data.privileges);
    ElMessage({ message: '登录成功', type: 'success' });
    gotoNextStep();
  };

  const gotoNextStep = () => {
    router.push('/sell/home');
  };
</script>
<style lang="scss">
  .login {
    & > .container {
      height: 113px;
      img {
        width: auto;
        height: 60px;
        margin-top: 30px;
      }
    }
    .wrapper {
      //background: url('./imgs/internet.png') no-repeat center;
      .container {
        height: 576px;
        .login-form {
          box-sizing: border-box;
          padding-left: 31px;
          padding-right: 31px;
          width: 410px;
          height: 510px;
          background-color: #ffffff;
          position: absolute;
          bottom: 29px;
          right: 0;
          h3 {
            line-height: 23px;
            font-size: 24px;
            text-align: center;
            margin: 40px auto 49px;
            .checked {
              color: #ff6600;
            }
            .sep-line {
              margin: 0 32px;
            }
          }
          .input {
            display: inline-block;
            width: 348px;
            height: 50px;
            border: 1px solid #e5e5e5;
            margin-bottom: 20px;
            input {
              width: 100%;
              height: 100%;
              border: none;
              padding: 18px;
            }
          }
          .btn {
            width: 100%;
            line-height: 50px;
            margin-top: 10px;
            font-size: 16px;
          }
          .tips {
            margin-top: 14px;
            display: flex;
            justify-content: space-between;
            font-size: 14px;
            cursor: pointer;
            .sms {
              color: #ff6600;
            }
            .reg {
              color: #999999;
              span {
                margin: 0 7px;
              }
            }
          }
        }
      }
    }
    .footer {
      height: 100px;
      padding-top: 60px;
      color: #999999;
      font-size: 16px;
      text-align: center;
      .footer-link {
        a {
          color: #999999;
          display: inline-block;
        }
        span {
          margin: 0 10px;
        }
      }
      .copyright {
        margin-top: 13px;
      }
    }
  }
</style>
