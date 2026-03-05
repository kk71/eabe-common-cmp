<template>
  <div class="login-page">
    <!-- Left: Branding Panel with animated background -->
    <div class="login-left">
      <div class="login-left-bg">
        <div class="bg-orb bg-orb-1"></div>
        <div class="bg-orb bg-orb-2"></div>
        <div class="bg-orb bg-orb-3"></div>
        <div class="bg-grid"></div>
      </div>
      <div class="login-left-content">
        <router-link to="/sell/home" class="brand-logo">
          <img
            src="/company-logo/LOGO2.png"
            alt="羿贝引擎"
            width="40"
            height="40"
          />
          <span class="brand-name">羿贝引擎</span>
        </router-link>
        <h1 class="brand-heading">云上增长新动力</h1>
        <p class="brand-desc">
          一站式企业级技术服务平台，提供云计算、大数据、人工智能等全栈云服务，助力企业数字化转型与业务增长
        </p>
        <div class="brand-features">
          <div class="feature-item">
            <div class="feature-icon">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M12 2L2 7l10 5 10-5-10-5z" />
                <path d="M2 17l10 5 10-5" />
                <path d="M2 12l10 5 10-5" />
              </svg>
            </div>
            <div>
              <div class="feature-title">豆包大模型</div>
              <div class="feature-sub">智能高效的AI基座能力</div>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <rect x="2" y="3" width="20" height="14" rx="2" ry="2" />
                <line x1="8" y1="21" x2="16" y2="21" />
                <line x1="12" y1="17" x2="12" y2="21" />
              </svg>
            </div>
            <div>
              <div class="feature-title">全栈云服务</div>
              <div class="feature-sub">计算、网络、存储一站式</div>
            </div>
          </div>
          <div class="feature-item">
            <div class="feature-icon">
              <svg
                width="20"
                height="20"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              </svg>
            </div>
            <div>
              <div class="feature-title">安全可信</div>
              <div class="feature-sub">多重认证与安全保障</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Right: Login Form Panel -->
    <div class="login-right">
      <div class="login-form-wrapper">
        <div class="login-form-card">
          <h2 class="form-title">账号登录</h2>
          <p class="form-subtitle">登录羿贝引擎控制台</p>

          <!-- Tab Switcher -->
          <div class="login-tabs">
            <button
              class="login-tab"
              :class="{ active: loginMethod === 'password' }"
              @click="loginMethod = 'password'"
            >
              密码登录
            </button>
            <button
              class="login-tab"
              :class="{ active: loginMethod === 'sms' }"
              @click="loginMethod = 'sms'"
            >
              短信登录
            </button>
            <button
              class="login-tab"
              :class="{ active: loginMethod === 'qrcode' }"
              @click="loginMethod = 'qrcode'"
            >
              扫码登录
            </button>
          </div>

          <!-- Password Login -->
          <form
            v-if="loginMethod === 'password'"
            class="login-form"
            @submit.prevent="handleLogin"
          >
            <div class="form-field">
              <label class="field-label">账号</label>
              <div
                class="input-wrapper"
                :class="{ focused: focusField === 'account', error: errors.account }"
              >
                <svg
                  class="input-icon"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2" />
                  <circle cx="12" cy="7" r="4" />
                </svg>
                <input
                  type="text"
                  v-model="data.form.login_name"
                  placeholder="请输入邮箱/手机号/用户名"
                  class="form-input"
                  @focus="focusField = 'account'"
                  @blur="focusField = ''"
                />
              </div>
              <span v-if="errors.account" class="field-error">{{ errors.account }}</span>
            </div>
            <div class="form-field">
              <label class="field-label">密码</label>
              <div
                class="input-wrapper"
                :class="{ focused: focusField === 'password', error: errors.password }"
              >
                <svg
                  class="input-icon"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
                  <path d="M7 11V7a5 5 0 0 1 10 0v4" />
                </svg>
                <input
                  :type="showPassword ? 'text' : 'password'"
                  v-model="data.form.password"
                  placeholder="请输入密码"
                  class="form-input"
                  @focus="focusField = 'password'"
                  @blur="focusField = ''"
                />
                <button type="button" class="toggle-pwd" @click="showPassword = !showPassword">
                  <svg
                    v-if="!showPassword"
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z" />
                    <circle cx="12" cy="12" r="3" />
                  </svg>
                  <svg
                    v-else
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path
                      d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94"
                    />
                    <path
                      d="M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19"
                    />
                    <line x1="1" y1="1" x2="23" y2="23" />
                  </svg>
                </button>
              </div>
              <span v-if="errors.password" class="field-error">{{ errors.password }}</span>
            </div>
            <div class="form-options">
              <label class="remember-me">
                <input type="checkbox" v-model="extraForm.remember" />
                <span class="checkbox-custom"></span>
                <span>7天内自动登录</span>
              </label>
              <a href="javascript:;" class="forgot-link">忘记密码？</a>
            </div>
            <button type="submit" class="submit-btn" :class="{ loading: isLoading }">
              <span v-if="isLoading" class="btn-spinner"></span>
              <span>{{ isLoading ? '登录中...' : '登 录' }}</span>
            </button>
          </form>

          <!-- SMS Login -->
          <form
            v-if="loginMethod === 'sms'"
            class="login-form"
            @submit.prevent="handleLogin"
          >
            <div class="form-field">
              <label class="field-label">手机号</label>
              <div
                class="input-wrapper"
                :class="{ focused: focusField === 'phone', error: errors.phone }"
              >
                <svg
                  class="input-icon"
                  width="18"
                  height="18"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <rect x="5" y="2" width="14" height="20" rx="2" ry="2" />
                  <line x1="12" y1="18" x2="12.01" y2="18" />
                </svg>
                <div class="phone-prefix">+86</div>
                <input
                  type="tel"
                  v-model="extraForm.phone"
                  placeholder="请输入手机号"
                  class="form-input phone-input"
                  @focus="focusField = 'phone'"
                  @blur="focusField = ''"
                />
              </div>
              <span v-if="errors.phone" class="field-error">{{ errors.phone }}</span>
            </div>
            <div class="form-field">
              <label class="field-label">验证码</label>
              <div class="sms-row">
                <div
                  class="input-wrapper sms-input-wrap"
                  :class="{ focused: focusField === 'sms', error: errors.smsCode }"
                >
                  <svg
                    class="input-icon"
                    width="18"
                    height="18"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  >
                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
                  </svg>
                  <input
                    type="text"
                    v-model="extraForm.smsCode"
                    placeholder="请输入验证码"
                    class="form-input"
                    maxlength="6"
                    @focus="focusField = 'sms'"
                    @blur="focusField = ''"
                  />
                </div>
                <button
                  type="button"
                  class="sms-btn"
                  :disabled="smsCooldown > 0"
                  @click="sendSmsCode"
                >
                  {{ smsCooldown > 0 ? smsCooldown + 's 后重发' : '获取验证码' }}
                </button>
              </div>
              <span v-if="errors.smsCode" class="field-error">{{ errors.smsCode }}</span>
            </div>
            <button type="submit" class="submit-btn" :class="{ loading: isLoading }">
              <span v-if="isLoading" class="btn-spinner"></span>
              <span>{{ isLoading ? '登录中...' : '登 录' }}</span>
            </button>
          </form>

          <!-- QR Code Login -->
          <div v-if="loginMethod === 'qrcode'" class="qrcode-section">
            <div class="qrcode-box">
              <div class="qrcode-placeholder">
                <svg width="160" height="160" viewBox="0 0 160 160">
                  <rect
                    x="10"
                    y="10"
                    width="40"
                    height="40"
                    rx="4"
                    fill="#3370FF"
                    opacity="0.9"
                  />
                  <rect
                    x="60"
                    y="10"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.6"
                  />
                  <rect
                    x="85"
                    y="10"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.4"
                  />
                  <rect
                    x="110"
                    y="10"
                    width="40"
                    height="40"
                    rx="4"
                    fill="#3370FF"
                    opacity="0.9"
                  />
                  <rect
                    x="10"
                    y="60"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.5"
                  />
                  <rect
                    x="35"
                    y="60"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.3"
                  />
                  <rect
                    x="60"
                    y="60"
                    width="40"
                    height="40"
                    rx="4"
                    fill="#14C9C9"
                    opacity="0.7"
                  />
                  <rect
                    x="110"
                    y="60"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.5"
                  />
                  <rect
                    x="135"
                    y="60"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.3"
                  />
                  <rect
                    x="10"
                    y="85"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.4"
                  />
                  <rect
                    x="110"
                    y="85"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.6"
                  />
                  <rect
                    x="10"
                    y="110"
                    width="40"
                    height="40"
                    rx="4"
                    fill="#3370FF"
                    opacity="0.9"
                  />
                  <rect
                    x="60"
                    y="110"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.5"
                  />
                  <rect
                    x="85"
                    y="110"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.3"
                  />
                  <rect
                    x="110"
                    y="110"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.6"
                  />
                  <rect
                    x="135"
                    y="110"
                    width="40"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.4"
                  />
                  <rect
                    x="60"
                    y="135"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.4"
                  />
                  <rect
                    x="110"
                    y="135"
                    width="15"
                    height="15"
                    rx="2"
                    fill="#3370FF"
                    opacity="0.5"
                  />
                </svg>
              </div>
            </div>
            <p class="qrcode-tip">
              请使用 <strong>羿贝引擎APP</strong> 扫描二维码登录
            </p>
            <button class="refresh-qr" @click="refreshQR">
              <svg
                width="16"
                height="16"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
              >
                <polyline points="23 4 23 10 17 10" />
                <path
                  d="M20.49 15a9 9 0 1 1-2.12-9.36L23 10"
                />
              </svg>
              刷新二维码
            </button>
          </div>

          <!-- Divider -->
          <div class="login-divider" v-if="loginMethod !== 'qrcode'">
            <span class="divider-text">其他登录方式</span>
          </div>

          <!-- Social Login -->
          <div class="social-login" v-if="loginMethod !== 'qrcode'">
            <button class="social-btn" title="微信登录">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="#07C160">
                <path
                  d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 0 1 .213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 0 0 .167-.054l1.903-1.114a.864.864 0 0 1 .717-.098 10.16 10.16 0 0 0 2.837.403c.276 0 .543-.027.811-.05a6.2 6.2 0 0 1-.248-1.73c0-3.571 3.326-6.47 7.43-6.47.258 0 .507.025.764.04C16.755 4.985 13.074 2.188 8.691 2.188zm-2.6 4.408c.58 0 1.049.47 1.049 1.049 0 .58-.47 1.049-1.049 1.049-.58 0-1.049-.47-1.049-1.049 0-.58.47-1.049 1.049-1.049zm5.19 0c.58 0 1.049.47 1.049 1.049 0 .58-.47 1.049-1.049 1.049-.58 0-1.049-.47-1.049-1.049 0-.58.47-1.049 1.049-1.049zm5.088 3.084c-3.577 0-6.48 2.529-6.48 5.649 0 3.12 2.903 5.649 6.48 5.649a7.9 7.9 0 0 0 2.228-.322.7.7 0 0 1 .577.078l1.514.886a.263.263 0 0 0 .135.044.237.237 0 0 0 .234-.236c0-.058-.023-.116-.039-.172l-.312-1.178a.477.477 0 0 1 .172-.536C22.863 18.326 24 16.587 24 14.33c0-3.12-2.903-5.649-6.48-5.649zm-2.59 3.126c.468 0 .847.379.847.847a.847.847 0 0 1-.847.847.847.847 0 0 1-.847-.847c0-.468.379-.847.847-.847zm5.18 0c.468 0 .847.379.847.847a.847.847 0 0 1-.847.847.847.847 0 0 1-.847-.847c0-.468.379-.847.847-.847z"
                />
              </svg>
            </button>
            <button class="social-btn" title="飞书登录">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="#3370FF">
                <path
                  d="M4.5 3.5L11 7.5l-2 3.5L2 7l2.5-3.5zM13 8l7.5 4.5L18 16l-7.5-4.5L13 8zM9 12.5L15.5 16l-2 3.5L7 16l2-3.5zM3 8.5L9.5 12 7.5 15.5 1 12l2-3.5z"
                />
              </svg>
            </button>
            <button class="social-btn" title="抖音登录">
              <svg width="22" height="22" viewBox="0 0 24 24" fill="#FE2C55">
                <path
                  d="M19.321 5.562a5.124 5.124 0 0 1-.443-.258 6.228 6.228 0 0 1-1.137-.966c-.849-.971-1.166-1.956-1.282-2.645h.004c-.097-.573-.064-.943-.058-.943h-3.12v14.966c0 .201 0 .399-.008.595 0 .024-.003.046-.004.073 0 .012-.002.024-.003.036v.019a3.282 3.282 0 0 1-1.64 2.636 3.23 3.23 0 0 1-1.6.417 3.283 3.283 0 0 1-3.282-3.282 3.283 3.283 0 0 1 3.282-3.283c.347 0 .68.058.993.163v-3.17a6.349 6.349 0 0 0-.993-.08c-1.74 0-3.375.677-4.603 1.907A6.418 6.418 0 0 0 3.539 16.5c-.041.903.128 1.794.493 2.614a6.453 6.453 0 0 0 1.696 2.233 6.462 6.462 0 0 0 4.243 1.584c.348 0 .694-.03 1.033-.088a6.41 6.41 0 0 0 3.21-1.496 6.418 6.418 0 0 0 2.1-4.23l.038-7.17a9.074 9.074 0 0 0 5.343 1.727V8.557a5.966 5.966 0 0 1-2.374-.495V5.562z"
                />
              </svg>
            </button>
          </div>

          <!-- Register Link -->
          <div class="register-row">
            <span class="register-text">还没有账号？</span>
            <a href="javascript:;" class="register-link">立即注册</a>
          </div>
        </div>

        <!-- Footer -->
        <div class="login-footer">
          <span>登录即代表您同意</span>
          <a href="javascript:;">服务协议</a>
          <span>和</span>
          <a href="javascript:;">隐私政策</a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
  import { computed, onBeforeUnmount, reactive, ref } from 'vue';
  import { useRouter } from 'vue-router';
  import { ElMessage } from 'element-plus';
  import { buildEncryptedPassword } from '@/utils/password.ts';
  import { waitRequest } from '@/utils/http/tools';
  import { userPasswordLogin } from '@/api/system';
  import { useAppStore } from '@/store/modules/app';

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

  const extraForm = reactive({
    remember: false,
    phone: '',
    smsCode: '',
  });

  const loginMethod = ref('password');
  const focusField = ref('');
  const showPassword = ref(false);
  const smsCooldown = ref(0);
  let smsTimer = null;

  const errors = reactive({
    account: '',
    password: '',
    phone: '',
    smsCode: '',
  });

  const isLoading = computed(() => submitting.value);

  const gotoNextStep = () => {
    router.push('/sell/home');
  };

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

  const handleLogin = async () => {
    errors.account = '';
    errors.password = '';
    errors.phone = '';
    errors.smsCode = '';

    let valid = true;

    if (loginMethod.value === 'password') {
      if (!data.form.login_name.trim()) {
        errors.account = '请输入账号';
        valid = false;
      }
      if (!data.form.password) {
        errors.password = '请输入密码';
        valid = false;
      }
      if (!valid) return;
      await login();
    } else if (loginMethod.value === 'sms') {
      if (!extraForm.phone.trim()) {
        errors.phone = '请输入手机号';
        valid = false;
      } else if (!/^1[3-9]\d{9}$/.test(extraForm.phone)) {
        errors.phone = '请输入正确的手机号';
        valid = false;
      }
      if (!extraForm.smsCode.trim()) {
        errors.smsCode = '请输入验证码';
        valid = false;
      }
      if (!valid) return;
      ElMessage.warning('暂未开通短信登录，请使用账号密码登录');
    }
  };

  const sendSmsCode = () => {
    errors.phone = '';

    if (!extraForm.phone.trim()) {
      errors.phone = '请先输入手机号';
      return;
    }
    if (!/^1[3-9]\d{9}$/.test(extraForm.phone)) {
      errors.phone = '请输入正确的手机号';
      return;
    }
    if (smsCooldown.value > 0) return;

    smsCooldown.value = 60;
    smsTimer = setInterval(() => {
      smsCooldown.value -= 1;
      if (smsCooldown.value <= 0 && smsTimer) {
        clearInterval(smsTimer);
        smsTimer = null;
      }
    }, 1000);
  };

  const refreshQR = () => {
    // 预留：刷新二维码登录
  };

  onBeforeUnmount(() => {
    if (smsTimer) {
      clearInterval(smsTimer);
      smsTimer = null;
    }
  });
</script>

<style scoped>
.login-page {
  display: flex;
  min-height: 100vh;
  background: #f7f8fa;
}

/* ======================== Left Branding Panel ======================== */
.login-left {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  overflow: hidden;
  padding: 60px;
}

.login-left-bg {
  position: absolute;
  inset: 0;
  z-index: 0;
}

.bg-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(100px);
  animation: orbFloat 12s ease-in-out infinite;
}
.bg-orb-1 {
  width: 500px;
  height: 500px;
  background: rgba(51, 112, 255, 0.15);
  top: -10%;
  left: -10%;
}
.bg-orb-2 {
  width: 400px;
  height: 400px;
  background: rgba(20, 201, 201, 0.1);
  bottom: -5%;
  right: -5%;
  animation-delay: -4s;
}
.bg-orb-3 {
  width: 300px;
  height: 300px;
  background: rgba(51, 112, 255, 0.08);
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  animation-delay: -8s;
}

@keyframes orbFloat {
  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }
  33% {
    transform: translate(30px, -20px) scale(1.05);
  }
  66% {
    transform: translate(-20px, 15px) scale(0.95);
  }
}

.bg-grid {
  position: absolute;
  inset: 0;
  background-image: linear-gradient(rgba(51, 112, 255, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(51, 112, 255, 0.04) 1px, transparent 1px);
  background-size: 60px 60px;
}

.login-left-content {
  position: relative;
  z-index: 1;
  max-width: 480px;
}

.brand-logo {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  margin-bottom: 48px;
}

.brand-logo img {
  width: 32px;
  height: 32px;
}

.brand-name {
  font-size: 22px;
  font-weight: 700;
  color: #1d2129;
  letter-spacing: 1px;
}

.brand-heading {
  font-size: 40px;
  font-weight: 700;
  color: #1d2129;
  line-height: 1.3;
  margin-bottom: 16px;
  letter-spacing: -0.5px;
}

.brand-desc {
  font-size: 15px;
  color: #4e5969;
  line-height: 1.7;
  margin-bottom: 48px;
}

.brand-features {
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 16px 20px;
  background: rgba(255, 255, 255, 0.92);
  border: 1px solid #e5e6eb;
  border-radius: 12px;
  transition: all 0.3s;
}

.feature-item:hover {
  background: rgba(51, 112, 255, 0.08);
  border-color: rgba(51, 112, 255, 0.2);
}

.feature-icon {
  width: 44px;
  height: 44px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 10px;
  background: rgba(51, 112, 255, 0.12);
  color: #3370ff;
  flex-shrink: 0;
}

.feature-title {
  font-size: 15px;
  font-weight: 600;
  color: #1d2129;
  margin-bottom: 2px;
}

.feature-sub {
  font-size: 13px;
  color: #4e5969;
}

/* ======================== Right Form Panel ======================== */
.login-right {
  width: 520px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #ffffff;
  border-left: 1px solid #e5e6eb;
  padding: 40px;
}

.login-form-wrapper {
  width: 100%;
  max-width: 400px;
  display: flex;
  flex-direction: column;
  min-height: 580px;
  justify-content: space-between;
}

.login-form-card {
  flex: 1;
}

.form-title {
  font-size: 28px;
  font-weight: 700;
  color: #1d2129;
  margin-bottom: 6px;
}

.form-subtitle {
  font-size: 14px;
  color: #4e5969;
  margin-bottom: 32px;
}

/* Tabs */
.login-tabs {
  display: flex;
  gap: 0;
  margin-bottom: 28px;
  background: #f2f3f5;
  border-radius: 10px;
  padding: 4px;
}

.login-tab {
  flex: 1;
  padding: 10px 0;
  font-size: 14px;
  font-weight: 500;
  color: #4e5969;
  background: transparent;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.25s;
}

.login-tab:hover {
  color: #1d2129;
}

.login-tab.active {
  color: #3370ff;
  background: #ffffff;
  box-shadow: 0 1px 4px rgba(0, 0, 0, 0.08);
}

/* Form fields */
.login-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-field {
  display: flex;
  flex-direction: column;
  gap: 6px;
}

.field-label {
  font-size: 13px;
  font-weight: 500;
  color: #4e5969;
}

.input-wrapper {
  display: flex;
  align-items: center;
  gap: 10px;
  height: 46px;
  padding: 0 14px;
  background: #ffffff;
  border: 1px solid #e5e6eb;
  border-radius: 10px;
  transition: all 0.25s;
}

.input-wrapper.focused {
  border-color: #3370ff;
  background: rgba(51, 112, 255, 0.06);
  box-shadow: 0 0 0 3px rgba(51, 112, 255, 0.1);
}

.input-wrapper.error {
  border-color: #f53f3f;
  background: rgba(245, 63, 63, 0.04);
}

.input-icon {
  color: #4e5969;
  flex-shrink: 0;
}

.input-wrapper.focused .input-icon {
  color: #3370ff;
}

.form-input {
  flex: 1;
  background: none;
  border: none;
  outline: none;
  font-size: 14px;
  color: #1d2129;
  font-family: inherit;
  height: 100%;
}

.form-input::placeholder {
  color: #c9cdd4;
}

.phone-prefix {
  font-size: 14px;
  color: #4e5969;
  padding-right: 10px;
  border-right: 1px solid #e5e6eb;
  margin-right: 2px;
  white-space: nowrap;
}

.toggle-pwd {
  background: none;
  border: none;
  cursor: pointer;
  color: #86909c;
  display: flex;
  padding: 2px;
  transition: color 0.2s;
}

.toggle-pwd:hover {
  color: #4e5969;
}

.field-error {
  font-size: 12px;
  color: #f53f3f;
  padding-left: 2px;
}

/* SMS row */
.sms-row {
  display: flex;
  gap: 10px;
}

.sms-input-wrap {
  flex: 1;
}

.sms-btn {
  flex-shrink: 0;
  height: 46px;
  padding: 0 18px;
  background: rgba(51, 112, 255, 0.1);
  border: 1px solid rgba(51, 112, 255, 0.25);
  border-radius: 10px;
  color: #3370ff;
  font-size: 13px;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.25s;
  white-space: nowrap;
  font-family: inherit;
}

.sms-btn:hover:not(:disabled) {
  background: rgba(51, 112, 255, 0.18);
}

.sms-btn:disabled {
  opacity: 0.5;
  cursor: not-allowed;
}

/* Options row */
.form-options {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.remember-me {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 13px;
  color: #4e5969;
  cursor: pointer;
  user-select: none;
}

.remember-me input {
  display: none;
}

.checkbox-custom {
  width: 16px;
  height: 16px;
  border: 1.5px solid #c9cdd4;
  border-radius: 4px;
  position: relative;
  transition: all 0.2s;
  flex-shrink: 0;
}

.remember-me input:checked + .checkbox-custom {
  background: #3370ff;
  border-color: #3370ff;
}

.remember-me input:checked + .checkbox-custom::after {
  content: '';
  position: absolute;
  left: 4.5px;
  top: 1.5px;
  width: 5px;
  height: 9px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}

.forgot-link {
  font-size: 13px;
  color: #3370ff;
  text-decoration: none;
  transition: color 0.2s;
}

.forgot-link:hover {
  color: #4080ff;
}

/* Submit */
.submit-btn {
  width: 100%;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: #3370ff;
  border: none;
  border-radius: 10px;
  color: #ffffff;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  font-family: inherit;
  margin-top: 4px;
}

.submit-btn:hover {
  background: #4080ff;
  box-shadow: 0 4px 16px rgba(51, 112, 255, 0.35);
}

.submit-btn.loading {
  opacity: 0.7;
  pointer-events: none;
}

.btn-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top-color: #fff;
  border-radius: 50%;
  animation: spin 0.7s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* QR Code */
.qrcode-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px 0 8px;
}

.qrcode-box {
  width: 200px;
  height: 200px;
  background: #ffffff;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 20px;
}

.qrcode-tip {
  font-size: 14px;
  color: #86909c;
  text-align: center;
  margin-bottom: 12px;
}

.qrcode-tip strong {
  color: #1d2129;
}

.refresh-qr {
  display: flex;
  align-items: center;
  gap: 6px;
  background: none;
  border: none;
  color: #3370ff;
  font-size: 13px;
  cursor: pointer;
  font-family: inherit;
  transition: color 0.2s;
}

.refresh-qr:hover {
  color: #4080ff;
}

/* Divider */
.login-divider {
  display: flex;
  align-items: center;
  gap: 16px;
  margin: 24px 0 20px;
}

.login-divider::before,
.login-divider::after {
  content: '';
  flex: 1;
  height: 1px;
  background: #e5e6eb;
}

.divider-text {
  font-size: 12px;
  color: #4e5969;
  white-space: nowrap;
}

/* Social */
.social-login {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-bottom: 24px;
}

.social-btn {
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 12px;
  background: #ffffff;
  border: 1px solid #e5e6eb;
  cursor: pointer;
  transition: all 0.25s;
}

.social-btn:hover {
  background: #f7f8fa;
  border-color: #c9cdd4;
  transform: translateY(-2px);
}

/* Register */
.register-row {
  text-align: center;
  font-size: 14px;
}

.register-text {
  color: #4e5969;
}

.register-link {
  color: #3370ff;
  text-decoration: none;
  font-weight: 500;
  margin-left: 4px;
  transition: color 0.2s;
}

.register-link:hover {
  color: #4080ff;
}

/* Footer */
.login-footer {
  text-align: center;
  font-size: 12px;
  color: #4e5969;
  padding-top: 20px;
}

.login-footer a {
  color: #3370ff;
  text-decoration: none;
  margin: 0 2px;
}

.login-footer a:hover {
  color: #4080ff;
}

/* ======================== Responsive ======================== */
@media (max-width: 1024px) {
  .login-left {
    display: none;
  }
  .login-right {
    width: 100%;
    border-left: none;
  }
}

@media (max-width: 480px) {
  .login-right {
    padding: 24px 20px;
  }
  .form-title {
    font-size: 24px;
  }
  .login-tabs {
    flex-wrap: nowrap;
  }
  .login-tab {
    font-size: 13px;
    padding: 8px 0;
  }
  .sms-btn {
    padding: 0 12px;
    font-size: 12px;
  }
}
</style>

