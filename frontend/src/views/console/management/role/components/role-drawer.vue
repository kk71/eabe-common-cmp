<template>
  <el-drawer v-model="data.shown" size="40%" append-to-body title="角色编辑">
    <el-form ref="theForm" :model="data.form" :rules="data.rules" label-width="60" label-position="left">
      <el-form-item label="名称" prop="name">
        <plain-text v-model="data.form.name" />
      </el-form-item>
      <el-form-item label="权限" props="privileges">
        <el-tree
          class="full-width"
          ref="privilegeTree"
          :data="data.privilegesGroup"
          show-checkbox
          node-key="id"
          :props="{ label: 'title' }"
          default-expand-all
          @check-change="onCheckChange"
        />
      </el-form-item>
    </el-form>
    <template #footer>
      <edit-buttons v-model="data.form_editable" @submit="save" @cancel="onCancel" />
    </template>
  </el-drawer>
</template>
<script setup>
  import { ElMessage } from 'element-plus';
  import { waitRequest } from '@/utils/http/tools';
  import { getRole, getAllPrivilegeGroup, addRole, editRole } from '@/api/system';

  const emits = defineEmits([]);

  const loading = ref(false);

  const theForm = useTemplateRef('theForm');

  const submitting = ref(false);

  const privilegeTree = useTemplateRef('privilegeTree');

  const formInit = () => {
    return {
      id: null,
      name: '',
      privileges: [],
    };
  };

  const data = reactive({
    shown: false,
    form: formInit(),
    privilegesGroup: [],
    privilegesMapping: {},
    rules: {
      name: [{ required: true, message: '必填项。', trigger: 'change' }],
    },
    cb: null,
    form_editable: true,
  });

  const isNewAdding = computed(() => {
    return data.form.id == null;
  });

  const onCancel = () => {
    data.form_editable = false;
    data.shown = false;
  };

  const save = async () => {
    if (!(await theForm.value.validate((isValid, invalidFields) => {}))) {
      return ElMessage({ message: '请完善后重新提交。', type: 'warning' });
    }
    data.form.privileges = getCheckedPrivilegeNames();
    if (isNewAdding.value) await waitRequest(submitting, addRole({ data: data.form }));
    else await waitRequest(submitting, editRole({ params: { id: data.form.id }, data: data.form }));
    ElMessage({ message: '已保存', type: 'success' });
    data.cb();
    data.shown = false;
  };

  const showAdd = async (defaultObj) => {
    data.form = { ...formInit(), ...defaultObj };
    data.shown = true;
    await setCheckedPrivilegeNames();
    return new Promise((resolve, reject) => {
      data.cb = resolve;
    });
  };

  const setCheckedPrivilegeNames = async () => {
    const resp = await waitRequest(loading, getAllPrivilegeGroup({}));
    data.privilegesGroup = [resp.data.data.root_group];
    data.privilegesMapping = resp.data.data.privilege_id_mapping;
    let idsToCheck = [];
    for (const name of data.form.privileges) {
      idsToCheck = [...idsToCheck, ...data.privilegesMapping[name]];
    }
    privilegeTree.value.setCheckedKeys(idsToCheck);
  };

  const getCheckedPrivilegeNames = () => {
    const keys = privilegeTree.value.getCheckedKeys();
    const names = [];
    for (const k of keys) {
      for (const i in data.privilegesMapping) {
        if (data.privilegesMapping[i].includes(k)) names.push(i);
      }
    }
    return names;
  };

  const onCheckChange = async (target, checked) => {
    if (target.children != undefined) return;
    for (const i of data.privilegesMapping[target.name]) privilegeTree.value.setChecked(i, checked);
  };

  const show = async (role_id) => {
    if (!role_id) throw Error('role_id is null');
    const resp = await waitRequest(loading, getRole({ params: { id: role_id } }));
    if (!resp.data.data) {
      ElMessage({ message: '找不到角色', type: 'error' });
      throw new Error('找不到角色');
    }
    data.form = resp.data.data[0];
    data.shown = true;
    data.form_editable = true;
    await setCheckedPrivilegeNames();
    return new Promise((resolve, reject) => {
      data.cb = resolve;
    });
  };

  defineExpose({
    showAdd,
    show,
  });
</script>
