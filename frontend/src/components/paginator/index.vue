<template>
  <el-pagination
    class="paginator"
    v-model:current-page="page"
    v-model:page-size="perPage"
    :page-count="props.modelValue.pages"
    :total="props.modelValue.total"
    :page-sizes="[10, 20, 30, 40, 50, 100, 200, 300]"
    background
    hide-on-single-page
    layout="prev, pager, next, total, sizes"
  />
</template>

<script setup>
  import { useRoute } from 'vue-router';
  import { updateToQuery } from '@/utils/router';

  const emit = defineEmits([
    'update:modelValue', // 只有当不使用querystring分页的时候才会触发更新
    'scroll-top', // 要求console滚动到顶部
  ]);

  const props = defineProps({
    scrollTop: {
      // 是否展示在点击分页之后滑到顶部
      type: Boolean,
      default: true,
    },
    querystring: {
      // 是否使用querystring分页
      type: Boolean,
      default: true,
    },
    modelValue: {
      // 分页对象，字段page per_page total
      type: Object,
    },
  });

  const consoleFrame = inject('consoleFrame');

  const page = computed({
    get() {
      return props.modelValue.page;
    },
    set(v) {
      const d = { page: v };
      if (props.querystring) updateToQuery(d);
      else {
        emit('update:modelValue', { ...props.modelValue, ...d });
      }
      if (props.scrollTop) consoleFrame.value.$el.scrollTo(0, 0);
    },
  });

  const perPage = computed({
    get() {
      return props.modelValue.per_page;
    },
    set(v) {
      const d = { per_page: v };
      if (props.querystring) updateToQuery(d);
      else {
        emit('update:modelValue', { ...props.modelValue, ...d });
      }
      if (props.scrollTop) consoleFrame.value.$el.scrollTo(0, 0);
    },
  });

  onMounted(async () => {});
</script>

<style>
  .paginator {
    padding-top: 20px;
    padding-bottom: 20px;
    justify-content: flex-end;
  }
</style>
