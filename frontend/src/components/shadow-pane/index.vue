<template>
  <div :class="{ 'shadow-pane-inner': innerShadow, unembedded: !innerShadow }" :style="props.innerStyle">
    <slot></slot>
  </div>
</template>

<script setup name="shadow-pane">
  const props = defineProps({
    shadow: {
      type: [Boolean, null],
      default: null,
    },
    float: {
      // 是否漂浮
      type: Boolean,
      default: false,
    },
    target: {
      // 漂浮的上层容器的class
      type: String,
      default: '',
    },
    offset: {
      // 漂浮距离边界的偏移量
      type: Number,
      default: 0,
    },
    position: {
      // 漂浮的类型：top  bottom
      type: String,
      default: 'top',
    },
    innerStyle: {
      // 内部div的style
      type: [String, Object],
      default: '',
    },
  });

  const embedded = inject('embedded', undefined);

  const innerShadow = computed(() => {
    if (props.shadow != null) return props.shadow;
    return !embedded;
  });
</script>

<style scope lang="less">
  .shadow-pane-inner {
    background-color: var(--el-bg-color);
    box-shadow: 0 0px 10px #0000005e;
    border-radius: 8px;
    padding: 16px;
    margin: 10px;
  }

  .unembedded {
    margin: 10px 10px 10px 10px;
  }
</style>
