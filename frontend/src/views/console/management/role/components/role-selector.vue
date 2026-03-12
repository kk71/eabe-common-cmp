<template>
  <div class="full-width">
    <el-select-v2
      v-if="editable"
      v-model="innerModelValue"
      filterable
      :multiple="multiple"
      :reserve-keyword="false"
      clearable
      remote
      :remote-method="remoteMethod"
      :options="data.options"
      v-loading="loading"
      placeholder="选择或搜索"
      loading-text="请稍等…"
      @clear="onClear"
      :props="{ label: 'name', value: 'id' }"
    />
    <span v-if="!editable" class="row-start gap">
      <el-tag v-for="i in selected">{{ i.name }}</el-tag>
    </span>
    <span v-if="!editable && !selected.length">-</span>
  </div>
</template>

<script setup>
  import { waitRequest } from '@/utils/http/tools';
  import { getRole } from '@/api/system';

  const emits = defineEmits(['update:modelValue']);

  const props = defineProps({
    modelValue: [String, Array, null],
    multiple: {
      // 是否列表（即可复选）
      type: Boolean,
      default: false,
    },
    editable: {
      type: Boolean,
      default: true,
    },
  });

  const loading = ref(false);

  const data = reactive({
    options: [],
  });

  const remoteMethod = async (q) => {
    const resp = await waitRequest(
      loading,
      getRole({
        params: {
          keyword: q,
          per_page: 999,
        },
      }),
    );
    data.options = resp.data.data;
  };

  const onClear = async () => {
    await remoteMethod('');
  };

  const innerModelValue = computed({
    get() {
      return props.modelValue;
    },
    set(v) {
      emits('update:modelValue', v);
    },
  });

  const selected = computed(() => {
    if (props.multiple) return data.options.filter((i) => innerModelValue.value.includes(i.id));
    else if (!props.multiple) return data.options.filter((i) => innerModelValue.value == i.id);
  });

  onMounted(async () => {
    await remoteMethod('');
  });
</script>
