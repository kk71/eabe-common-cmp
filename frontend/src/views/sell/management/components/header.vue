<template>
  <header class="sell-console-header">
    <user-password-dialog ref="userPasswordDialog" />
    <div class="console-header">
      <div class="header-left">
        <router-link to="/sell" class="console-logo">
          <svg width="28" height="28" viewBox="0 0 28 28" fill="none">
            <path d="M14 0L28 8v12L14 28 0 20V8L14 0z" fill="#3370FF" />
            <path d="M14 6l8 4.5v9L14 24l-8-4.5v-9L14 6z" fill="#14C9C9" />
          </svg>
          <span class="logo-text">羿贝综合云服务平台</span>
        </router-link>
        <span class="header-badge">
          费用中心 · {{ props.title }}
        </span>
      </div>
      <div class="header-right">
        <div class="header-search">
          <svg
            class="search-icon"
            width="16"
            height="16"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <circle cx="11" cy="11" r="8" />
            <line x1="21" y1="21" x2="16.65" y2="16.65" />
          </svg>
          <input type="text" placeholder="搜索产品或文档" class="search-input" />
        </div>
        <div class="header-actions">
          <el-tooltip :content="theme === 'light' ? '切换暗黑主题' : '切换明亮主题'">
            <button class="icon-btn" @click="toggleTheme()">
              <el-icon :size="16">
                <component :is="theme === 'dark' ? Sunny : Moon" />
              </el-icon>
            </button>
          </el-tooltip>
          <div class="header-user" @click="toggleUserMenu">
            <div class="user-avatar">
              {{ userInitial }}
            </div>
            <div v-if="showUserMenu" class="user-dropdown">
              <div class="dropdown-header">
                <div class="dropdown-avatar">
                  {{ userInitial }}
                </div>
                <div>
                  <div class="dropdown-name">{{ userName || '未登录用户' }}</div>
                </div>
              </div>
              <div class="dropdown-divider"></div>
              <button class="dropdown-item" @click.stop="gotoChangePassword">
                修改密码
              </button>
              <div class="dropdown-divider"></div>
              <button class="dropdown-item dropdown-logout" @click.stop="logout">
                退出登录
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>

<script setup>
  import { ElMessage } from 'element-plus';
  import { useDark, useToggle } from '@vueuse/core';
  import { useAppStore } from '@/store';
  import { Sunny, Moon } from '@element-plus/icons-vue';
  import UserPasswordDialog from '@/views/console/management/user/components/user-password-dialog.vue';

  const props = defineProps({
    title: {
      type: String,
      default: '...',
    },
  });

  const router = useRouter();
  const userPasswordDialog = useTemplateRef('userPasswordDialog');

  const appStore = useAppStore();

  const theme = computed(() => appStore.sell_theme);

  const isDark = useDark({
    selector: 'body',
    onChanged(dark) {
      appStore.toggleSellTheme(dark);
    },
  });

  const toggleTheme = useToggle(isDark);

  const userName = computed(() => appStore.user?.username || appStore.user?.name || '');
  const userInitial = computed(() => (userName.value ? userName.value.charAt(0) : 'U'));

  const showUserMenu = ref(false);

  const toggleUserMenu = () => {
    showUserMenu.value = !showUserMenu.value;
  };

  const logout = async () => {
    appStore.clearToken();
    showUserMenu.value = false;
    router.push('/sell/login');
    ElMessage({ message: '请重新登录。', type: 'success' });
  };

  const gotoChangePassword = async () => {
    await nextTick();
    await userPasswordDialog.value.show(appStore.user.id);
    appStore.clearToken();
    showUserMenu.value = false;
    router.push('/sell/login');
    ElMessage({ message: '密码已修改，请重新登录。', type: 'success' });
  };

  onMounted(() => {
    document.addEventListener('click', (e) => {
      if (showUserMenu.value && !(e.target.closest && e.target.closest('.header-user'))) {
        showUserMenu.value = false;
      }
    });
  });
</script>

<style lang="less" scoped>
  .sell-console-header {
    position: sticky;
    top: 0;
    z-index: 100;
  }

  .console-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 52px;
    padding: 0 20px;
    background: #ffffff;
    border-bottom: 1px solid #e5e6eb;
  }

  .header-left {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .console-logo {
    display: flex;
    align-items: center;
    gap: 8px;
    text-decoration: none;
    color: #1d2129;
  }

  .logo-text {
    font-size: 16px;
    font-weight: 600;
  }

  .header-badge {
    font-size: 13px;
    color: #3370ff;
    background: #e8f0ff;
    padding: 3px 12px;
    border-radius: 4px;
    font-weight: 500;
  }

  .header-right {
    display: flex;
    align-items: center;
    gap: 12px;
  }

  .header-search {
    position: relative;
    display: flex;
    align-items: center;
  }

  .search-icon {
    position: absolute;
    left: 10px;
    color: #86909c;
    pointer-events: none;
  }

  .search-input {
    width: 220px;
    height: 32px;
    padding: 0 12px 0 34px;
    border: 1px solid #e5e6eb;
    border-radius: 6px;
    font-size: 13px;
    outline: none;
    background: #f7f8fa;
    color: #1d2129;
    transition: border-color 0.2s;
  }

  .search-input:focus {
    border-color: #3370ff;
    background: #ffffff;
  }

  .search-input::placeholder {
    color: #c9cdd4;
  }

  .header-actions {
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .icon-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 32px;
    height: 32px;
    border-radius: 6px;
    border: none;
    background: transparent;
    color: #4e5969;
    cursor: pointer;
    transition: background 0.15s;
  }

  .icon-btn:hover {
    background: #f2f3f5;
  }

  .header-user {
    position: relative;
    cursor: pointer;
    padding: 4px 8px;
    border-radius: 6px;
    transition: background 0.15s;
  }

  .header-user:hover {
    background: #f2f3f5;
  }

  .user-avatar {
    width: 28px;
    height: 28px;
    border-radius: 50%;
    background: #3370ff;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 13px;
    font-weight: 600;
  }

  .user-dropdown {
    position: absolute;
    top: 42px;
    right: 0;
    width: 220px;
    background: #ffffff;
    border-radius: 8px;
    box-shadow: 0 4px 24px rgba(0, 0, 0, 0.12);
    border: 1px solid #e5e6eb;
    z-index: 200;
  }

  .dropdown-header {
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 14px;
  }

  .dropdown-avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: #3370ff;
    color: #ffffff;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 15px;
    font-weight: 600;
    flex-shrink: 0;
  }

  .dropdown-name {
    font-size: 14px;
    font-weight: 600;
    color: #1d2129;
  }

  .dropdown-divider {
    height: 1px;
    background: #e5e6eb;
  }

  .dropdown-item {
    width: 100%;
    text-align: left;
    padding: 10px 14px;
    font-size: 13px;
    color: #4e5969;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: background 0.15s;
  }

  .dropdown-item:hover {
    background: #f2f3f5;
  }

  .dropdown-logout {
    color: #f53f3f;
  }

  @media (max-width: 900px) {
    .header-search {
      display: none;
    }
  }
</style>
