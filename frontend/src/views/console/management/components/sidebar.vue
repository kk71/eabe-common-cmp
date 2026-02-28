<template>
  <el-menu class="main-sidebar" :collapse="isCollapse" @open="handleOpen" @close="handleClose" router>
    <el-menu-item index="/console/management">
      <el-icon><House /></el-icon>
      <template #title>概览</template>
    </el-menu-item>
    <el-menu-item index="/console/management/month-bill">
      <el-icon><User /></el-icon>
      <template #title>月度账单</template>
    </el-menu-item>
    <el-menu-item index="/console/management/reconcile">
      <el-icon><Histogram /></el-icon>
      <template #title>对账中心</template>
    </el-menu-item>
    <el-menu-item index="/console/management/order">
      <el-icon><User /></el-icon>
      <template #title>订单管理</template>
    </el-menu-item>

    <el-menu-item index="/console/management/wallet">
      <el-icon><Money /></el-icon>
      <template #title>财务资金管理</template>
    </el-menu-item>
    <el-menu-item @click="showTips">
      <el-icon><Present /></el-icon>
      <template #title>客户支持</template>
    </el-menu-item>
    <el-menu-item @click="showTips">
      <el-icon><Suitcase /></el-icon>
      <template #title>运维中心</template>
    </el-menu-item>
    <el-menu-item @click="showTips">
      <el-icon><Tools /></el-icon>
      <template #title>数据统计分析</template>
    </el-menu-item>

    <el-sub-menu index="system" v-if="hasPrivilege('system_control')">
      <template #title>
        <el-icon><Grid /></el-icon>
        <span>系统</span>
      </template>
      <el-menu-item index="/console/management/user">
        <el-icon><User /></el-icon>
        <template #title>用户</template>
      </el-menu-item>
      <el-menu-item index="/console/management/role">
        <el-icon><Open /></el-icon>
        <template #title>角色权限</template>
      </el-menu-item>
      <el-menu-item v-if="false" index="/console/management/celery-task">
        <el-icon><Promotion /></el-icon>
        <template #title>异步任务</template>
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<script lang="ts" setup>
  import { useAppStore } from '@/store/modules/app';
  import { hasPrivilege } from '@/utils/privilege';

  const isCollapse = ref(false); // 是否收起，默认不收起

  const appStore = useAppStore();

  const showTips = async () => {
    ElMessage({ message: '权限不足', type: 'warning' });
  };

  const refreshColorMode = (theme: string) => {
    if (theme == 'dark') {
      document.body.style.setProperty('--el-menu-bg-color', 'black');
      document.body.style.setProperty('--el-menu-text-color', 'white');
      document.body.style.setProperty('--el-menu-active-color', 'white');
      document.body.style.setProperty('--el-menu-hover-bg-color', '#4c4c4c');
    } else if (theme == 'light') {
      document.body.style.setProperty('--el-menu-bg-color', '#fef9ef');
      document.body.style.setProperty('--el-menu-text-color', 'gray');
      document.body.style.setProperty('--el-menu-active-color', 'black');
      document.body.style.setProperty('--el-menu-hover-bg-color', 'orange');
    }
  };

  watch(
    () => appStore.console_theme,
    (newVal) => refreshColorMode(newVal),
  );

  onMounted(async () => {
    refreshColorMode(appStore.console_theme);
  });

  const handleOpen = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
  };
  const handleClose = (key: string, keyPath: string[]) => {
    console.log(key, keyPath);
  };
</script>

<style lang="less">
  .main-sidebar {
    height: 100%;
  }
</style>
