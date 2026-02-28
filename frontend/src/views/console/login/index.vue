<template>
  <!-- form section start -->
  <section class="w3l-hotair-form">
    <h1>羿贝综合云服务平台 - 管控后台</h1>
    <div class="container">
      <!-- /form -->
      <div class="workinghny-form-grid">
        <div class="main-hotair">
          <div class="content-wthree">
            <h2>登录</h2>
            <form v-loading="submitting">
              <input type="text" class="text" name="text" placeholder="用户名" required="" autofocus v-model="data.form.login_name" />
              <input
                type="password"
                class="password"
                name="password"
                placeholder="密码"
                required=""
                autofocus
                v-model="data.form.password"
              />
              <button class="btn" @click="login" onclick="return false">登录</button>
            </form>
            <p class="account">还没注册吗? <a href="javascript: " @click="signin">注册</a></p>
          </div>
          <div class="w3l_form align-self">
            <div class="left_grid_info">
              <img src="./images/1.png" alt="" class="img-fluid" />
            </div>
          </div>
        </div>
      </div>
      <!-- //form -->
    </div>
    <!-- copyright-->
    <div class="copyright text-center">
      <p class="copy-footer-29"></p>
    </div>
    <!-- //copyright-->
  </section>
  <!-- //form section start -->
</template>

<script setup>
  import { useRoute, useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus';
  import { buildEncryptedPassword } from '@/utils/password.ts';
  import { waitRequest } from '@/utils/http/tools';
  import { userPasswordLogin } from '@/api/system';
  import { useAppStore } from '@/store/modules/app';
  import './css/style.css';

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
    if (route.query.nextStep) router.push(route.query.nextStep);
    else router.push('/console/management');
  };

  onMounted(async () => {
    await store.fetchConf();
  });
</script>
