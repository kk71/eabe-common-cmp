<template>
  <div
    style="text-align: right; z-index: 999; position: relative"
    :class="{ animate__animated: true, 'expand-style': !compact }"
    class="row-end"
  >
    <slot name="pre" />
    <el-button :loading="submitting" :size="buttonSize" v-show="deleteButton" type="danger" @click="$emit('delete')">删除</el-button>
    <el-button
      :size="buttonSize"
      :loading="submitting"
      v-show="!innerModelValue && editButton"
      type="primary"
      @click="
        $emit('edit');
        innerModelValue = true;
      "
      >编辑</el-button
    >
    <el-button :size="buttonSize" :loading="submitting" v-show="innerModelValue && cancelButton" @click="$emit('cancel')">取消</el-button>
    <el-button :loading="submitting" :size="buttonSize" v-show="innerModelValue && submitButton" type="primary" @click="$emit('submit')">{{
      submitButtonName
    }}</el-button>
    <slot name="post" />
  </div>
</template>
<script setup name="edit-buttons">
  import { ref, defineProps, defineEmits, computed, inject } from 'vue';

  // 当前是否在提交
  const submitting = inject('submitting', undefined);

  const props = defineProps({
    cancelButton: {
      // 是否包含取消按钮
      type: Boolean,
      default: true,
    },
    editButton: {
      // 是否展示编辑按钮
      type: Boolean,
      default: false,
    },
    deleteButton: {
      // 是否包含一个删除按钮
      // 这个按钮是不受v-model的控制的
      type: Boolean,
      default: false,
    },
    submitButton: {
      // 是否展示提交按钮，在v-model的基础上
      type: Boolean,
      default: true,
    },
    buttonSize: {
      // 按钮尺寸
      type: String,
      default: 'default',
    },
    modelValue: {
      // v-model存放的是当前是否处于可编辑状态
      type: Boolean,
      default: false,
    },
    submitButtonName: {
      // 用于提交数据的按钮的展示文本
      type: String,
      default: '提交',
    },
    compact: {
      // 样式紧缩模式
      type: Boolean,
      default: false,
    },
  });

  const emits = defineEmits([
    'update:modelValue',
    'edit', // 点击编辑
    'cancel', // 点击放弃编辑
    'submit', // 点击保存
    'delete', // 点击删除
  ]);

  const innerModelValue = computed({
    get() {
      return props.modelValue;
    },
    set(v) {
      emits('update:modelValue', v);
    },
  });
</script>

<style scoped>
  .expand-style {
    padding: 20px 20px 0 20px;
  }
</style>
