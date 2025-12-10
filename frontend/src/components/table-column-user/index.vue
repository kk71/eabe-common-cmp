<template>
  <el-table-column>
    <template #default="scope"> no-user </template>
  </el-table-column>
</template>
<script setup>
  import { defineProps } from 'vue';

  const props = defineProps({
    prop: {
      type: String,
      required: true,
    },
    multiple: {
      type: Boolean,
      default: false,
    },
  });
</script>
