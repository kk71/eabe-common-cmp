<template>
  <el-dialog title="用户信息" width="40%" draggable v-model="data.shown" :lock-scroll="false">
    <el-form ref="theForm" label-width="100px" :model="data.form" :rules="data.rules" v-loading="loading">
      <el-form-item label="昵称" prop="name">
        <plain-text v-model="data.form.name" />
      </el-form-item>
      <el-form-item label="头像" prop="avatar">
        <plain-text v-model="data.form.avatar" />
      </el-form-item>
      <el-form-item label="密码登录名" prop="login_name">
        <plain-text v-model="data.form.login_name" />
      </el-form-item>
      <el-form-item label="角色" prop="roles" v-if="hasPrivilege('system_control')">
        <role-selector v-model="data.form.role_ids" :editable="data.form_editable" multiple />
      </el-form-item>
      <el-form-item v-if="hasPrivilege('system_control')">
        <el-checkbox v-model="data.form.is_admin" label="管理员" />
      </el-form-item>
      <el-form-item v-if="hasPrivilege('system_control')">
        <el-checkbox v-model="data.form.disabled" label="禁用" />
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <edit-buttons compact v-model="data.form_editable" @submit="save" @cancel="data.shown = false" />
      </span>
    </template>
  </el-dialog>
</template>
<script setup>
  import { ElMessage } from 'element-plus';
  import { confirmBox } from '@/utils/msgbox';
  import { waitRequest } from '@/utils/http/tools';
  import { hasPrivilege } from '@/utils/privilege';
  import { getUser, addUser, editUser } from '@/api/system';
  import RoleSelector from '../../role/components/role-selector.vue';

  const theForm = useTemplateRef('theForm');

  const loading = ref(false);

  const formInit = () => {
    return {
      id: null,
      name: '',
      avatar: null,
      is_admin: false,
      disabled: false,
      login_name: '',
      role_ids: [],
    };
  };

  const data = reactive({
    shown: false,
    form: formInit(),
    form_editable: true,
    cb: null,
    rules: {
      name: [{ required: true, message: '必填项。', trigger: 'change' }],
      login_name: [{ required: true, message: '必填项。', trigger: 'change' }],
    },
  });

  const showAdd = async (defaultObj) => {
    data.shown = true;
    data.form = { ...formInit(), ...defaultObj };
    return new Promise((resolve, reject) => {
      data.cb = resolve;
    });
  };

  const show = async (user_id) => {
    if (!user_id) throw Error('user_id is null');
    data.shown = true;
    let resp = await waitRequest(
      loading,
      getUser({
        params: {
          id: user_id,
          include_disabled: true,
        },
      }),
    );
    data.form = resp.data.data[0];
    return new Promise((resolve, reject) => {
      data.cb = resolve;
    });
  };

  const isNewAdding = computed(() => {
    return data.form.id == null;
  });

  const save = async () => {
    if (!(await theForm.value.validate((isValid, invalidFields) => {}))) {
      return ElMessage({ message: '请完善后重新提交。', type: 'warning' });
    }
    if (isNewAdding.value) {
      let resp = await addUser({ data: data.form });
      ElMessage({ message: '已保存', type: 'success' });
      data.cb(resp.data.data.id);
    } else {
      await editUser({ params: { id: data.form.id }, data: data.form });
      ElMessage({ message: '已保存', type: 'success' });
      data.cb();
    }
    data.shown = false;
  };

  defineExpose({
    showAdd,
    show,
  });
</script>

<style lang="less">
  .el-form-item {
    margin-bottom: 18px !important;
  }
</style>
