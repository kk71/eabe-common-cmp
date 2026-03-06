<template>
  <!-- 父布局：必须包含 RouterView 才能渲染子路由（index.vue、products.vue 等） -->
  <RouterView />
</template>

<script>
/**
 * home.vue 作为 /sell/home 的父布局，必须提供 RouterView 供子路由渲染。
 * 当存在 home.vue 和 home/ 目录时，unplugin-vue-router 会创建嵌套路由：
 * - /sell/home -> home/index.vue
 * - /sell/home/products -> home/products.vue
 * 若缺少 RouterView，子路由内容无法显示，/sell/home/products 会错误地显示首页内容。
 */
export default {
  name: 'HomeLayout',
};
</script>

