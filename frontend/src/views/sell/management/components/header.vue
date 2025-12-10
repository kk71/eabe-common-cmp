<template>
  <header class="antialiased bg-white Male text-slate-500 dark:text-slate-400 dark:bg-slate-900">
    <user-password-dialog ref="userPasswordDialog" />
    <div
      class="sticky top-0 z-40 w-full backdrop-blur flex-none transition-colors duration-500 lg:z-50 lg:border-b lg:border-slate-900/10 dark:border-slate-50/[0.06] bg-white/95 supports-backdrop-blur:bg-white/60 dark:bg-transparent"
    >
      <div class="mx-auto max-w-8xl">
        <div class="px-4 py-4 border-b border-slate-900/10 lg:px-8 lg:border-0 dark:border-slate-300/10">
          <div class="relative flex items-center text-2xl sm:text-2xl font-blimone">
            <span class="mr-3 flex-none w-[2.0625rem] md:w-auto leading-6 dark:text-slate-200">{{ props.title }}</span>
            <div class="relative items-center hidden ml-auto lg:flex">
              <div class="flex items-center pl-6 ml-6 border-l border-slate-200 dark:border-slate-800">
                <el-tooltip :content="theme === 'light' ? '设置暗黑主题' : '设置明亮主题'">
                  <el-button
                    class="nav-btn"
                    :shape="'circle'"
                    type="info"
                    plain
                    :icon="theme === 'dark' ? Sunny : Moon"
                    circle
                    size="small"
                    @click="toggleTheme()"
                  />
                </el-tooltip>
              </div>
              <div class="flex items-center pl-6">
                <el-dropdown>
                  <el-button :shape="'circle'" type="info" plain :icon="User" circle size="small" />
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item :icon="Key" @click="gotoChangePassword">修改密码</el-dropdown-item>
                      <el-dropdown-item @click="logout">退出</el-dropdown-item>
                    </el-dropdown-menu>
                  </template>
                </el-dropdown>
              </div>
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
  import { Sunny, Moon, User, Setting, Key } from '@element-plus/icons-vue';
  import UserPasswordDialog from '@/views/console/management/user/components/user-password-dialog.vue';

  const props = defineProps({
    title: {
      type: String,
      default: '...',
    },
  });

  const router = useRouter();

  const userDialog = useTemplateRef('userDialog');

  const userPasswordDialog = useTemplateRef('userPasswordDialog');

  const appStore = useAppStore();

  const theme = computed(() => {
    return appStore.sell_theme;
  });

  const isDark = useDark({
    selector: 'body',
    onChanged(dark) {
      appStore.toggleSellTheme(dark);
    },
  });

  const toggleTheme = useToggle(isDark);

  const logout = async () => {
    appStore.clearToken();
    router.push('/sell/login');
    ElMessage({ message: '请重新登录。', type: 'success' });
  };

  const gotoChangePassword = async () => {
    await nextTick();
    await userPasswordDialog.value.show(appStore.user.id);
    appStore.clearToken();
    router.push('/sell/login');
    ElMessage({ message: '密码已修改，请重新登录。', type: 'success' });
  };
</script>

<style lang="less" scoped>
  .tag {
    margin-bottom: 0;
  }

  html.dark {
    a {
      color: white !important;
    }
  }

  html {
    a {
      color: black !important;
    }
  }
</style>
