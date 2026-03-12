<template>
  <div style="width: 100%">
    <el-button @click="onAdd" type="warning" text bg size="small" v-if="editable">
      <el-icon><Plus /></el-icon>
    </el-button>
    <div v-for="(v, $index) in innerModelValue" class="list-item gap">
      <slot :item="innerModelValue[$index]" :index="$index" />
      <el-button @click="onDelete($index)" type="danger" text bg size="small" v-if="editable">
        <el-icon><CloseBold /></el-icon>
      </el-button>
    </div>
  </div>
</template>
<script setup>
  import { CloseBold, Plus } from '@element-plus/icons-vue';
  import { confirmBox } from '@/utils/msgbox';

  const emit = defineEmits(['update:modelValue', 'add']);

  const props = defineProps({
    modelValue: {
      type: Array,
    },
    defaultObject: {
      // 新增数据的默认值
      type: [Object, String, Number],
      required: true,
    },
    editable: {
      // 编辑状态
      type: Boolean,
    },
    askBeforeDelete: {
      // 删除前先询问
      type: Boolean,
      default: true,
    },
  });

  const onAdd = async () => {
    // 添加
    const toAdd = JSON.parse(JSON.stringify(props.defaultObject));
    innerModelValue.value.splice(0, 0, toAdd);
    await emit('add', toAdd);
  };

  const onDelete = async ($index) => {
    if (props.askBeforeDelete && !(await confirmBox('确认删除吗？'))) return;
    innerModelValue.value.splice($index, 1);
  };

  const innerModelValue = computed({
    get() {
      if (!props.modelValue) innerModelValue.value = [];
      return props.modelValue;
    },
    set(v) {
      emit('update:modelValue', v);
    },
  });
</script>

<style lang="less" scoped>
  .list-item {
    display: flex;
    flex-direction: row;
    align-items: center;
    margin-bottom: 5px;
    padding: 5px;
    background-color: rgba(230, 230, 230, 0.3);
  }
</style>
