<template>
  <router-view></router-view>
</template>

<script setup>
  import { useAppStore } from '@/store/modules/app';

  const router = useRouter();
  const route = useRoute();
  const appStore = useAppStore();

  onMounted(async () => {
    if (route.path !== '/console') return;

    if (!appStore.token) {
      router.replace('/console/login');
      return;
    }

    await appStore.renewToken();
    router.replace(appStore.token ? '/console/management' : '/console/login');
  });
</script>
