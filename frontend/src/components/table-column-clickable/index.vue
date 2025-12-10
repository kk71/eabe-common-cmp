<template>
  <el-table-column>
    <template #default="scope">
      <div class="clickable" @click="emits('linkClick', scope.row)">
        {{ displayedProp(scope.row) }}
      </div>
    </template>
  </el-table-column>
</template>
<script setup lang="ts">
  const emits = defineEmits(['linkClick']);

  const props = defineProps({
    prop: {
      type: String,
      required: true,
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
