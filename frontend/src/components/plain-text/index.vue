<template>
  <el-input
    v-show="props.editable"
    v-model="innerModelValue"
    :type="props.type"
    :style="props.style"
    :size="props.size"
    :placeholder="props.placeholder"
    :autosize="props.autosize"
    :clearable="props.clearable"
    :rows="props.rows"
  />

  <span v-show="!props.editable && props.size == 'default'">
    <pre v-if="needUsePre" :style="props.style" class="display-pre">{{ innerModelValue }}</pre>
    <span v-if="!needUsePre" :style="props.style">{{ innerModelValue }}</span>
  </span>
  <h3 v-show="!props.editable && props.size == 'large'">
    <pre v-if="needUsePre" :style="props.style" class="display-pre">{{ innerModelValue }}</pre>
    <span v-if="!needUsePre" :style="props.style">{{ innerModelValue }}</span>
  </h3>
</template>

<script setup name="plain-text">
  const props = defineProps({
    editable: {
      // 是否允许修改值（也就是控件是否可编辑）
      // 注意，如果不可修改值，那么产品线也不允许增加
      type: Boolean,
      default: true,
    },
    // 下面都是传递给el-input的属性
    modelValue: {
      type: [Number, Array, null, String],
      default: '',
    },
    style: {
      type: [String, Object],
      default: '',
    },
    placeholder: {
      type: String,
      default: '',
    },
    size: {
      type: String,
      default: 'default',
    },
    type: {
      type: String,
      default: 'text',
    },
    autosize: {
      type: [null, Object],
      default: { minRows: 5, maxRows: 20 },
    },
    rows: {
      type: Number,
      default: 3,
    },
    clearable: {
      type: Boolean,
      default: false,
    },
  });

  const emits = defineEmits(['update:modelValue']);

  const innerModelValue = computed({
    get() {
      if (props.modelValue == null) return '';
      return props.modelValue;
    },
    set(v) {
      emits('update:modelValue', v);
    },
  });

  const needUsePre = computed(() => {
    try {
      return innerModelValue.value.indexOf('\n') != -1;
    } catch (e) {}
    return false;
  });
</script>

<style lang="less" scoped>
  .display-pre {
    text-wrap: balance;
  }
</style>
