<template>
  <router-view></router-view>
</template>

<script setup>
  const router = useRouter();

  onMounted(async () => {
    // router.push('/console/management');
  });
</script>
