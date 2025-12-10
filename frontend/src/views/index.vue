<template>...</template>

<script setup lang="ts">
  import { useRouter } from 'vue-router';

  const router = useRouter();

  onMounted(() => {
    router.push('/sell');
  });
</script>

<style lang="less" scoped></style>
