<template>
  <header class="antialiased bg-white Male text-slate-600">
    <user-dialog ref="userDialog" />
    <user-password-dialog ref="userPasswordDialog" />
    <div
      class="sticky top-0 z-40 w-full backdrop-blur flex-none transition-colors duration-500 lg:z-50 lg:border-b lg:border-slate-900/10 bg-white/95 supports-backdrop-blur:bg-white/60"
    >
      <div class="mx-auto max-w-8xl">
        <div class="px-4 py-4 border-b border-slate-900/10 lg:px-8 lg:border-0">
          <div class="relative flex items-center text-2xl sm:text-2xl font-blimone">
            <span class="mr-3 flex-none w-[2.0625rem] md:w-auto leading-6">{{ props.title }}</span>
            <div class="relative items-center hidden ml-auto lg:flex">
              <div class="flex items-center pl-6">
                <el-dropdown>
                  <el-button :shape="'circle'" type="info" plain :icon="User" circle size="small" />
                  <template #dropdown>
                    <el-dropdown-menu>
                      <el-dropdown-item :icon="Setting" @click="gotoUserDetail">个人信息</el-dropdown-item>
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
  import { useAppStore } from '@/store';
  import { User, Setting, Key } from '@element-plus/icons-vue';
  import UserDialog from '../user/components/user-dialog.vue';
  import UserPasswordDialog from '../user/components/user-password-dialog.vue';

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

  const gotoUserDetail = async () => {
    await nextTick();
    await userDialog.value.show(appStore.user.id);
  };

  const logout = async () => {
    appStore.clearToken();
    router.push('/console/login');
    ElMessage({ message: '请重新登录。', type: 'success' });
  };

  const gotoChangePassword = async () => {
    await nextTick();
    await userPasswordDialog.value.show(appStore.user.id);
    appStore.clearToken();
    router.push('/console/login');
    ElMessage({ message: '密码已修改，请重新登录。', type: 'success' });
  };
</script>

<style lang="less" scoped>
  .tag {
    margin-bottom: 0;
  }

  a {
    color: inherit;
  }
</style>
