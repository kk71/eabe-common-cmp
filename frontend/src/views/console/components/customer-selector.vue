<template>
  <div class="full-width">
    <el-select-v2
      v-model="innerModelValue"
      filterable
      :multiple="multiple"
      :reserve-keyword="false"
      clearable
      remote
      :remote-method="remoteMethod"
      :options="data.options"
      v-loading="loading"
      :placeholder="placeholder"
      loading-text="请稍等…"
      no-data-text="未找到可用客户（请确认客户已创建且已配置客户编号）"
      @clear="onClear"
      :props="{ label: 'label', value: 'code' }"
      @change="onChange"
    />
  </div>
</template>

<script setup lang="ts">
  import { waitRequest } from '@/utils/http/tools';
  import { getCustomers } from '@/api/console';

  type CustomerOption = {
    id?: number;
    code: string;
    name?: string;
    label: string;
    disabled?: boolean;
  };

  const emits = defineEmits(['update:modelValue', 'update:customerName', 'selected']);

  const props = defineProps<{
    modelValue: string | string[] | null;
    customerName?: string | null;
    multiple?: boolean;
    placeholder?: string;
  }>();

  const multiple = computed(() => !!props.multiple);
  const placeholder = computed(() => props.placeholder || '选择或搜索（客户名）');

  const loading = ref(false);

  const data = reactive<{ options: CustomerOption[] }>({
    options: [],
  });

  const normalizeOption = (c: any): CustomerOption => {
    const code = String(c.code ?? c.customer_code ?? '').trim();
    const name = String(c.name ?? c.customer_name ?? '').trim();
    const hasCode = !!code;
    // el-select-v2 需要稳定且唯一的 value，这里对“未配置 code”的客户使用不可选的占位 value
    const optionValue = hasCode ? code : `__missing_code__${String(c.id ?? '') || name || 'unknown'}`;
    const label = hasCode
      ? (name ? `${name}（${code}）` : code)
      : (name ? `${name}（未配置客户编号）` : `未配置客户编号（ID=${String(c.id ?? '') || '-'}）`);
    return {
      id: c.id,
      code: optionValue,
      name,
      label,
      disabled: !!c.disabled || !hasCode,
    };
  };

  const remoteMethod = async (q: string) => {
    const resp = await waitRequest(
      loading,
      getCustomers({
        params: {
          keyword: q,
          per_page: 50,
        },
      }),
    );
    const items = resp.data.data || [];
    data.options = items.map(normalizeOption);
    ensureCurrentOptionVisible();
  };

  const ensureCurrentOptionVisible = () => {
    const codes = multiple.value
      ? ((innerModelValue.value as any) || []).filter((i: any) => !!i)
      : innerModelValue.value
        ? [innerModelValue.value]
        : [];
    for (const code of codes) {
      if (!data.options.some((o) => o.code === code) && typeof code === 'string' && code.trim()) {
        const fallbackName = !multiple.value ? (props.customerName || '').trim() : '';
        data.options = [
          ...data.options,
          {
            code: code.trim(),
            name: fallbackName || undefined,
            label: fallbackName ? `${fallbackName}（${code.trim()}）` : code.trim(),
          },
        ];
      }
    }
  };

  const onClear = async () => {
    emits('update:customerName', null);
    await remoteMethod('');
  };

  const innerModelValue = computed({
    get() {
      return props.modelValue;
    },
    set(v: any) {
      emits('update:modelValue', v);
    },
  });

  const onChange = () => {
    if (multiple.value) return;
    const code = innerModelValue.value as any;
    const opt = data.options.find((o) => o.code === code);
    // 如果选择了“未配置编号”的占位项（理论上 disabled 不可选），则不回填 name
    if (typeof code === 'string' && code.startsWith('__missing_code__')) {
      emits('update:customerName', null);
      emits('selected', null);
      return;
    }
    const name = opt?.name || null;
    emits('update:customerName', name);
    emits('selected', opt || null);
  };

  onMounted(async () => {
    await remoteMethod('');
    ensureCurrentOptionVisible();
    onChange();
  });

  watch(
    () => props.modelValue,
    async () => {
      ensureCurrentOptionVisible();
      onChange();
    },
    { deep: true },
  );

  watch(
    () => props.customerName,
    () => {
      ensureCurrentOptionVisible();
      onChange();
    },
  );
</script>

<style scoped>
  .full-width {
    width: 100%;
  }
</style>

