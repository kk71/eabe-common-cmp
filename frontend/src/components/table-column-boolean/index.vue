<template>
  <el-table-column>
    <template #default="scope">
      <el-icon size="20" v-if="getPropValue(scope.row) === true" color="var(--el-color-success)"><SuccessFilled /></el-icon>
      <el-icon size="20" v-else><CircleCloseFilled /></el-icon>
    </template>
  </el-table-column>
</template>
<script setup lang="ts">
  const props = defineProps({
    prop: {
      type: String,
      required: true,
    },
  });

  const getPropValue = (row) => {
    let r = row;
    for (const i of props.prop.split('.')) {
      r = r[i];
    }
    return r;
  };
</script>
