<template>
  <el-dialog title="修改密码" width="40%" draggable v-model="data.shown" :lock-scroll="false">
    <el-form ref="theForm" label-width="100px" :model="data.form" :rules="data.rules" v-loading="loading">
      <el-form-item label="旧密码" prop="old_password" v-if="!hasPrivilege('system_control')">
        <el-input v-model="data.form.old_password" type="password" show-password />
      </el-form-item>
      <el-form-item label="新密码" prop="new_password">
        <el-input v-model="data.form.new_password" type="password" show-password />
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
  import { changeUserPassword } from '@/api/system';
  import { hasPrivilege } from '@/utils/privilege';
  import { buildEncryptedPassword } from '@/utils/password';

  const theForm = useTemplateRef('theForm');

  const loading = ref(false);

  const formInit = () => {
    return {
      id: null,
      old_password: '',
      new_password: '',
    };
  };

  const data = reactive({
    shown: false,
    form: formInit(),
    form_editable: true,
    cb: null,
    rules: {
      old_password: [
        {
          validate: (rule, value, callback) => {
            if (!hasPrivilege('system_control') && !value) {
              callback(new Error('必填项。'));
            } else {
              callback();
            }
          },
          trigger: 'change',
        },
      ],
      new_password: [{ required: true, message: '必填项。', trigger: 'change' }],
    },
  });

  const show = async (user_id) => {
    if (!user_id) throw Error('user_id is null');
    data.form = { ...formInit(), id: user_id };
    data.shown = true;
    return new Promise((resolve, reject) => {
      data.cb = resolve;
    });
  };

  const save = async () => {
    if (!(await theForm.value.validate((isValid, invalidFields) => {}))) {
      return ElMessage({ message: '请完善后重新提交。', type: 'warning' });
    }
    await waitRequest(
      loading,
      changeUserPassword({
        data: {
          ...data.form,
          old_password: data.form.old_password ? await buildEncryptedPassword(data.form.old_password) : '',
          new_password: await buildEncryptedPassword(data.form.new_password),
        },
      }),
    );
    ElMessage({ message: '修改成功', type: 'success' });
    data.cb();
    data.shown = false;
  };

  defineExpose({
    show,
  });
</script>

<style lang="less">
  .el-form-item {
    margin-bottom: 18px !important;
  }
</style>
