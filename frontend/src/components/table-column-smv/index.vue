<template>
  <el-table-column>
    <template #default="scope">
      <csm :editable="false" :flag="props.flag" v-model="scope.row[props.prop]" />
    </template>
  </el-table-column>
</template>
<script setup lang="ts">
  const props = defineProps({
    flag: {
      required: true,
      type: String,
    },
    prop: {
      type: String,
      required: true,
    },
  });
</script>
