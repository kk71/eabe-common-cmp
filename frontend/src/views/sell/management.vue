<template>
  <div class="common-layout">
    <el-container v-if="upperReady">
      <el-aside width="180px"> <sidebar /> </el-aside>
      <el-container>
        <el-header> <Header :title="title" /></el-header>
        <el-main ref="consoleFrame">
          <router-view @update-title="onUpdateTitle" />
        </el-main>
      </el-container>
    </el-container>
  </div>
</template>

<script setup lang="ts">
  import sidebar from './management/components/sidebar.vue';
  import Header from './management/components/header.vue';
  import { useAppStore } from '@/store';

  const title = ref('羿贝综合云服务平台');

  const store = useAppStore();

  // 标记业务以上的层面是否以准备完毕。
  const upperReady = ref(false);

  // 业务层的最外层引用
  const consoleFrame = ref(null);
  provide('consoleFrame', consoleFrame);

  // 业务层整体是否在拉取数据的标识位
  const loading = ref(false);
  provide('loading', loading);

  // 业务层整体是否在提交数据的标识位
  const submitting = ref(false);
  provide('submitting', submitting);

  const onUpdateTitle = (newTitle: string) => {
    // 下层希望修改elheaderde的标题
    title.value = newTitle;
  };

  onMounted(async () => {
    await store.fetchConf();
    await store.fetchAllPrivileges();
    await store.renewToken();
    await nextTick();
    upperReady.value = true;
  });
</script>

<style lang="less" src="./management/style/main.less" />

<style lang="less" scoped>
  .common-layout {
    height: 100%;

    .el-container {
      height: 100%;
      background-color: var(--el-bg-color);
    }

    .el-header {
      padding: 0;
      background-color: var(--el-bg-color);
    }
  }
</style>
