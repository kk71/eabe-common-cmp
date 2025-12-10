<template>
  <span class="outer">
    <el-select-v2
      v-model="innerModelValue"
      v-if="editAsSelector"
      filterable
      clearable
      :reserve-keyword="false"
      :options="data.optionsForEditing"
      :placeholder="props.placeholder"
      :multiple="props.multiple"
      :size="props.size"
      :props="{ label: 'name' }"
      scrollbar-always-on
      class="selector"
      @change="emit('change')"
    >
      <template #default="{ item }">
        <slot name="select-item" :item="item">
          <el-tag effect="dark" disable-transitions v-if="getExtraTagType(item)" :type="getExtraTagType(item)">{{ item.name }}</el-tag>
          <div v-if="!getExtraTagType(item)">{{ item.name }}</div>
        </slot>
      </template>
    </el-select-v2>

    <el-segmented
      v-model="innerModelValue"
      :options="data.optionsForEditing"
      :size="props.size"
      v-if="editAsRadio"
      :props="{ label: 'name' }"
    />

    <span v-if="!editable" v-for="c in currentForDisplay">
      <el-tag effect="dark" disable-transitions v-if="getExtraTagType(c)" :type="getExtraTagType(c)">{{ c.name }}</el-tag>
      <el-tag effect="dark" disable-transitions v-if="!getExtraTagType(c)">{{ c.name }}</el-tag>
    </span>
    <span v-if="!editable && !currentForDisplay.length">-</span>
  </span>
</template>

<script setup>
  import { getStatusMachine } from '@/utils/statusMachine';

  const emit = defineEmits(['update:modelValue', 'change']);

  const props = defineProps({
    flag: {
      // 状态机唯一标识
      type: String,
      required: true,
    },
    editable: {
      // 是否可编辑
      type: Boolean,
      default: true,
    },
    forAll: {
      // 是否展示一个额外选项：全部
      type: Boolean,
      default: false,
    },
    forAllValue: {
      // "全部"这个选项的值。默认是null
      default: null,
    },
    multiple: {
      // 是否多选
      type: Boolean,
      default: false,
    },
    modelValue: {
      type: [String, Array, null],
    },
    placeholder: {
      // 展示的提示信息
      type: String,
      default: null,
    },
    editExclude: {
      // 针对当前状态机，输入需要排除的值。
      // 需要排除的值仅在编辑的时候排除，展示的时候依然可以展示
      type: Array,
      default: [],
    },
    type: {
      // 使用何种方式进行选择
      type: String,
      default: 'auto',
      validator(value) {
        return ['auto', 'selector', 'radio'].includes(value);
      },
    },
    autoRadioMax: {
      // 在type==auto情况下，radio允许的最大选项数
      type: Number,
      default: 4,
    },
    size: {
      // 可编辑的状态下，编辑控件的大小
      default: 'default',
      validator(value) {
        return ['large', 'default', 'small'].includes(value);
      },
    },
  });

  const data = reactive({
    // 全部选项
    allOptions: [],

    // 用于编辑的选项
    optionsForEditing: [],
  });

  const innerModelValue = computed({
    get() {
      return props.modelValue;
    },
    set(v) {
      if (v == undefined) v = null;
      emit('update:modelValue', v);
    },
  });

  const currentForDisplay = computed(() => {
    // 查询当前值（用于editable==false）
    let r = [];
    for (const opt of data.allOptions) {
      if (props.modelValue == null || props.modelValue == undefined) {
      } else if (props.modelValue.constructor === String || props.modelValue.constructor === Number) {
        // 单选
        if (opt.value == props.modelValue) {
          r.push(opt);
        }
      } else if (props.modelValue.constructor === Array) {
        // 多选
        for (const v of props.modelValue) {
          if (opt.value == v) {
            r.push(opt);
          }
        }
      } else console.log(props.modelValue.constructor);
    }
    return r;
  });

  const editAsSelector = computed(() => {
    // 当前可编辑且以下拉框编辑
    if (!props.editable) return false;
    return !editAsRadio.value;
  });

  const editAsRadio = computed(() => {
    // 当前可编辑且以radio编辑
    if (!props.editable) return false;
    if (props.multiple) return false;
    if (props.type == 'radio') return true;
    if (props.type == 'auto' && data.optionsForEditing.length <= props.autoRadioMax) return true;
  });

  const refreshOptions = () => {
    try {
      getStatusMachine(props.flag).smvs;
    } catch (e) {
      throw new Error(`status machine with flag '${props.flag}' not found.`);
    }

    data.allOptions = getStatusMachine(props.flag).smvs;
    data.optionsForEditing = [];
    for (const i of getStatusMachine(props.flag).smvs) {
      if (props.editExclude && !props.editExclude.includes(i.value)) data.optionsForEditing.push(i);
    }
    if (props.forAll)
      data.optionsForEditing.splice(0, 0, {
        value: props.forAllValue,
        name: '-全部-',
      });
  };

  const getExtraTagType = (i) => {
    // 返回标签类型，结构定义在smv.extra.tag_type里
    if (i.extra == null) return;
    if (!i.extra.tag_type) return;
    return i.extra.tag_type;
  };

  onMounted(async () => {
    refreshOptions();
  });
</script>

<style lang="less">
  .outer {
    display: inline-flex;
    width: 100%;

    .selector {
      width: 100%;
    }

    .el-segmented {
      --el-border-radius-base: 16px;
    }
  }
</style>
