<template>
  <svg aria-hidden="true" class="svg-icon-spin" :class="calsses" :style="inlineStyle">
    <use :xlink:href="symbolId" />
  </svg>
</template>

<script lang="ts" setup>
  const props = defineProps({
    prefix: {
      type: String,
      default: 'icon',
    },
    name: {
      type: String,
      required: true,
    },
    color: {
      type: String,
      default: '#333',
    },
    size: {
      type: [String, Number],
      default: 'default',
    },
  });
  const symbolId = computed(() => `#${props.prefix}-${props.name}`);
  const calsses = computed(() => {
    const isNumberSize = typeof props.size === 'number' || /^\d+(\.\d+)?$/.test(String(props.size));
    return {
      [`sdms-size-${props.size}`]: props.size && !isNumberSize,
    };
  });
  const fontSize = reactive({ default: '32px', small: '20px', large: '48px' });

  const inlineStyle = computed(() => {
    if (typeof props.size === 'number') {
      return { width: `${props.size}px`, height: `${props.size}px` };
    }
    const s = String(props.size);
    if (/^\d+(\.\d+)?$/.test(s)) {
      return { width: `${s}px`, height: `${s}px` };
    }
    return null;
  });
</script>
<style lang="less" scoped>
  .svg-icon-spin {
    width: v-bind('fontSize.default');
    height: v-bind('fontSize.default');
    vertical-align: middle;
    color: v-bind(color);

    &.sdms-size-small {
      font-size: v-bind('fontSize.small');
      height: v-bind('fontSize.small');
    }

    &.sdms-size-large {
      font-size: v-bind('fontSize.large');
      height: v-bind('fontSize.large');
    }
  }
</style>
