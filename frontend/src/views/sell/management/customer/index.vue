<template>
  <div class="card page" v-loading="loading">
    <div class="page-header">
      <div>
        <h2 class="page-title">客户信息</h2>
        <p class="page-subtitle">查看并修改当前登录用户所属客户信息（不展示备注）</p>
      </div>
      <div class="page-actions">
        <el-button type="primary" @click="doSave" :disabled="!data.loaded">保存</el-button>
      </div>
    </div>

    <el-form :model="data.form" label-width="100px" style="max-width: 520px">
      <el-form-item label="客户名">
        <plain-text v-model="data.form.name" clearable />
      </el-form-item>
      <el-form-item label="联系电话">
        <plain-text v-model="data.form.contact_phone" clearable />
      </el-form-item>
      <el-form-item label="主要负责人">
        <plain-text v-model="data.form.principal" clearable />
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup lang="ts">
  import { inject, onMounted, reactive } from 'vue';
  import { waitRequest } from '@/utils/http/tools';
  import { getMyCustomer, updateMyCustomer } from '@/api/sell';

  const emits = defineEmits(['update-title']);
  const loading: any = inject('loading');

  const data = reactive<any>({
    loaded: false,
    id: null,
    form: {
      name: '',
      contact_phone: '',
      principal: '',
    },
  });

  async function load() {
    const resp = await waitRequest(loading, getMyCustomer({}));
    const c = resp.data.data;
    data.id = c.id;
    data.form.name = c.name || '';
    data.form.contact_phone = c.contact_phone || '';
    data.form.principal = c.principal || '';
    data.loaded = true;
  }

  async function doSave() {
    await waitRequest(
      loading,
      updateMyCustomer({
        data: {
          name: data.form.name,
          contact_phone: data.form.contact_phone || null,
          principal: data.form.principal || null,
        },
      }),
    );
    await load();
  }

  onMounted(async () => {
    emits('update-title', '客户信息');
    await load();
  });
</script>

<style scoped lang="less">
  .page {
    margin: 20px 24px;
  }
  .card {
    background: #fff;
    border-radius: 8px;
    padding: 20px;
    border: 1px solid #e5e6eb;
  }
  .page-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 12px;
    margin-bottom: 16px;
  }
  .page-title {
    margin: 0;
    font-size: 18px;
    font-weight: 600;
    color: #1d2129;
  }
  .page-subtitle {
    margin: 6px 0 0;
    font-size: 13px;
    color: #86909c;
  }
</style>

