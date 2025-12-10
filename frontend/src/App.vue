<template>
  <router-view v-if="data.initialized" />
</template>

<script setup lang="ts">
  import { initializeStatusMachines } from '@/utils/statusMachine';

  const data = reactive({
    initialized: false,
  });

  onBeforeMount(async () => {
    await initializeStatusMachines();
    data.initialized = true;
  });
</script>

<style>
  html,
  body {
    height: 100%;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    color: #2c3e50;
    background-color: var(--color-bg-1);
    height: 100%;
  }
</style>
