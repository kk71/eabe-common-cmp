<template>
  <el-table-column>
    <template #default="scope">
      <datetime-label :value="displayedProp(scope.row)" :type="type" />
    </template>
  </el-table-column>
</template>
<script setup>
  const props = defineProps({
    prop: {
      type: String,
      required: true,
    },
    type: {
      // datetime or date
      type: String,
      default: 'datetime',
    },
  });

  const displayedProp = (row) => {
    let r = row;
    for (const i of props.prop.split('.')) {
      r = r[i];
    }
    return r;
  };
</script>
