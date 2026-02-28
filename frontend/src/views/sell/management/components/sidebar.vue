<template>
  <el-menu class="main-sidebar" :collapse="isCollapse" @open="handleOpen" @close="handleClose" router>
    <el-menu-item index="/sell/management">
      <el-icon><House /></el-icon>
      <template #title>概览</template>
    </el-menu-item>
    <el-menu-item index="/sell/management/month-bill">
      <el-icon><User /></el-icon>
      <template #title>月度账单</template>
    </el-menu-item>
    <el-menu-item index="/sell/management/order">
      <el-icon><User /></el-icon>
      <template #title>订单管理</template>
    </el-menu-item>
    <el-menu-item index="/sell/management/wallet">
      <el-icon><Wallet /></el-icon>
      <template #title>钱包中心</template>
    </el-menu-item>
  </el-menu>
</template>

<script lang="ts" setup>
  import { useAppStore } from '@/store/modules/app';
  // import { hasPrivilege, hasAnyPrivilege } from '@/utils/privilege';

  const isCollapse = ref(false); // 是否收起，默认不收起

  const appStore = useAppStore();

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
    () => appStore.sell_theme,
    (newVal) => refreshColorMode(newVal),
  );

  onMounted(async () => {
    refreshColorMode(appStore.sell_theme);
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
