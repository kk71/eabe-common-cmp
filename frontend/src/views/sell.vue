<template>
  <div id="app">
    <router-view></router-view>
  </div>
</template>

<script setup>
  const router = useRouter();

  onMounted(async () => {
    // router.push('/sell/home');
  });
</script>

<style lang="scss">
  @import './sell/scss/base.scss';
  @import './sell/scss/reset.scss';
  @import './sell/scss/config.scss';
  @import './sell/scss/button.scss';
</style>
