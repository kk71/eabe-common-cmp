<template>
  <div class="sell-console-layout" v-if="upperReady">
    <!-- 顶部控制台头部，样式对齐羿贝控制台 -->
    <Header :title="title" />

    <!-- 控制台主体区域：左侧主导航 + 右侧内容 -->
    <div class="sell-console-body">
      <sidebar />
      <main class="sell-console-main" ref="consoleFrame">
        <router-view @update-title="onUpdateTitle" />
      </main>
    </div>
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
  .sell-console-layout {
    min-height: 100vh;
    background: #f0f1f5;
    color: #1d2129;
    display: flex;
    flex-direction: column;
  }

  .sell-console-body {
    display: flex;
    min-height: calc(100vh - 52px);
  }

  .sell-console-main {
    flex: 1;
    min-width: 0;
    display: flex;
    flex-direction: column;
  }

  @media (max-width: 640px) {
    .sell-console-body {
      flex-direction: column;
    }
  }
</style>
