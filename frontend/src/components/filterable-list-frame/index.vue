<template>
  <slot />
  <slot name="paginator" v-if="!props.noPaginator">
    <paginator v-model="innerPagination" v-show="!loading" :querystring="!props.embedded" />
  </slot>
</template>
<script setup name="filterable-list-frame">
  import { QSValidator, updateToQuery, updateFilterDataFromQuery, updatePaginationFromQuery } from '@/utils/router';
  import { useRoute, useRouter } from 'vue-router';

  const props = defineProps({
    embedded: {
      // 嵌入式列表
      // 嵌入式列表不会监听querystring变化，
      // 转而要求提供filterData数据源，监听filterData的变化
      type: Boolean,
      default: false,
    },
    filterData: {
      // 查询参数
      // 嵌入式列表需要提供本参数
      type: Object,
      default: {},
    },
    pagination: {
      // 默认分页器的分页信息
      type: Object,
      default: {},
    },
    noPaginator: {
      // 关闭默认分页器
      type: Boolean,
      default: false,
    },
    filterDataTyping: {
      // 过滤字段的类型检查+转换
      // 不在类型转换内的字段默认即以文本对待
      type: QSValidator,
      default: null,
    },
  });

  // 是否加载中
  const loading = inject('loading');

  const emits = defineEmits([
    'update:filterData', // 更新查询参数
    'update:pagination', // 更新分页信息
    'filterChanged', // 查询参数变化
  ]);

  // 延迟刷新
  const delay = ref(0);

  const route = useRoute();

  const router = useRouter();

  // 监听filterData变化
  watch(
    props.filterData,
    async () => {
      clearTimeout(delay.value);
      delay.value = setTimeout(() => {
        if (props.embedded) {
          emits('filterChanged');
        } else {
          updateToQuery(props.filterData);
        }
      }, 500);
    },
    { deep: true },
  );

  watch(
    () => route.query,
    async () => {
      if (props.embedded) return;
      // 请注意，这一步必然是在非嵌入模式下执行的
      updatePaginationFromQuery(innerPagination.value);
      if (!props.filterDataTyping) updateFilterDataFromQuery(innerFilterData.value);
      else Object.assign(innerFilterData.value, props.filterDataTyping.from_qs(router.currentRoute.value.query));
      emits('filterChanged');
    },
    { deep: true },
  );

  const innerFilterData = computed({
    get() {
      return props.filterData;
    },
    set(v) {
      emits('update:filterData', v);
    },
  });

  // const paginate = async (page, per_page) => {
  //   // 发起分页
  //   innerPagination.value = {
  //     page: page,
  //     per_page: per_page,
  //   };
  //   emits('filterChanged');
  // };

  const innerPagination = computed({
    get() {
      return props.pagination;
    },
    set(v) {
      emits('update:pagination', v);
    },
  });

  onMounted(async () => {
    if (!props.embedded) {
      if (!props.filterDataTyping) updateFilterDataFromQuery(innerFilterData.value);
      else Object.assign(innerFilterData.value, props.filterDataTyping.from_qs(router.currentRoute.value.query));
      updatePaginationFromQuery(innerPagination.value);
    }
  });

  defineExpose({});
</script>
