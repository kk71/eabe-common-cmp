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
      @clear="onClear"
      :props="{ label: 'label', value: 'id' }"
    />
  </div>
</template>

<script setup lang="ts">
  import { waitRequest } from '@/utils/http/tools';
  import { getUser } from '@/api/system';

  type UserOption = {
    id: string;
    label: string;
    name?: string;
    login_name?: string | null;
    disabled?: boolean;
    is_admin?: boolean;
  };

  const emits = defineEmits(['update:modelValue']);

  const props = defineProps<{
    modelValue: string | string[] | null;
    multiple?: boolean;
    placeholder?: string;
  }>();

  const multiple = computed(() => !!props.multiple);
  const placeholder = computed(() => props.placeholder || '选择或搜索（登录名）');

  const loading = ref(false);

  const data = reactive<{ options: UserOption[] }>({
    options: [],
  });

  const normalizeOption = (u: any): UserOption => {
    const loginName = u.login_name || '';
    const nickName = u.name || '';
    const label = loginName ? `${loginName}${nickName ? `（${nickName}）` : ''}` : nickName || u.id;
    return {
      id: u.id,
      label,
      name: u.name,
      login_name: u.login_name,
      disabled: u.disabled,
      is_admin: u.is_admin,
    };
  };

  const remoteMethod = async (q: string) => {
    const resp = await waitRequest(
      loading,
      getUser({
        params: {
          keyword: q,
          per_page: 50,
        },
      }),
    );
    const items = (resp.data.data || []).filter((u: any) => !u.is_admin);
    data.options = items.map(normalizeOption);
  };

  const onClear = async () => {
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

  const ensureSelectedLoaded = async () => {
    const ids = multiple.value
      ? ((innerModelValue.value as any) || []).filter((i: any) => !!i)
      : innerModelValue.value
        ? [innerModelValue.value]
        : [];
    const missing = ids.filter((id: string) => !data.options.some((o) => o.id === id));
    for (const id of missing) {
      const resp = await waitRequest(
        loading,
        getUser({
          params: {
            id,
            include_disabled: true,
            per_page: 1,
          },
        }),
      );
      const u = (resp.data.data || [])[0];
      if (u && !u.is_admin) {
        data.options = [...data.options, normalizeOption(u)];
      }
    }
  };

  onMounted(async () => {
    await remoteMethod('');
    await ensureSelectedLoaded();
  });

  watch(
    () => props.modelValue,
    async () => {
      await ensureSelectedLoaded();
    },
    { deep: true },
  );
</script>

<style scoped>
  .full-width {
    width: 100%;
  }
</style>

