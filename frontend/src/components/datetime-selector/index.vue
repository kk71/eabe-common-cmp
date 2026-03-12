<template>
  <el-date-picker
    v-model="innerModelValue"
    v-if="editable"
    :shortcuts="innerShortcuts"
    :placeholder="innerPlaceholder"
    :value-format="getValueFormat"
    :type="type"
    :default-time="defaultTime"
    @change="(v) => $emit('change', v)"
  />
  <datetime-label
    v-else
    :value="modelValue"
    :type="type"
    :display-relative="displayRelative"
    :display-highlighted-today="displayHighlightedToday"
  />
</template>
<script setup>
  import { dToStr, dtToStr } from '@/utils/datetime';

  const emits = defineEmits(['update:modelValue', 'change']);

  const props = defineProps({
    editable: {
      type: Boolean,
      default: true,
    },
    modelValue: {
      type: [String, null, Date],
      default: null,
    },
    shortcuts: {
      // 快捷选项。默认已经配置了一批
      type: [Object, String, null, Array],
      default: [],
    },
    placeholder: {
      type: String,
      default: null,
    },
    type: {
      // 选择日期时间还是仅日期
      type: String,
      default: 'datetime',
    },
    defaultTime: {
      // 用于取选择后的默认hh:mm:ss,前面的日期是不用管的
      // 只选择日期的状态下不需要考虑这个参数
      type: Date,
      default: new Date(),
    },
    displayRelative: {
      // 以相对时间展示
      type: Boolean,
      default: true,
    },
    displayHighlightedToday: {
      // 展示时，如果日期是当日，则高亮展示
      type: Boolean,
      default: true,
    },
  });

  const data = reactive({
    shortcutsToLoad: [
      {
        text: '一周前',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '前天',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() - 3600 * 1000 * 48);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '昨天',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() - 3600 * 1000 * 24);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '今天',
        value: () => {
          const date = new Date();
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '明天',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() + 3600 * 1000 * 24);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '后天',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() + 3600 * 1000 * 48);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
      {
        text: '一周后',
        value: () => {
          const date = new Date();
          date.setTime(date.getTime() + 3600 * 1000 * 24 * 7);
          date.setHours(props.defaultTime.getHours());
          date.setMinutes(props.defaultTime.getMinutes());
          date.setSeconds(props.defaultTime.getSeconds());
          return date;
        },
      },
    ],
  });

  const selectToday = () => {
    // 选择当日
    if (isDate.value) {
      innerModelValue.value = dToStr(new Date());
    } else if (isDatetime.value) {
      const d = new Date();
      d.setHours(props.defaultTime.getHours());
      d.setMinutes(props.defaultTime.getMinutes());
      d.setSeconds(props.defaultTime.getSeconds());
      d.setMilliseconds(0);
      innerModelValue.value = dtToStr(d);
    }
  };

  const innerModelValue = computed({
    get() {
      return props.modelValue;
    },
    set(v) {
      $emit('update:modelValue', v);
    },
  });

  const innerShortcuts = computed(() => {
    return data.shortcutsToLoad.concat(props.shortcuts);
  });

  const isDate = computed(() => {
    return props.type == 'date';
  });

  const isDatetime = computed(() => {
    return props.type == 'datetime';
  });

  const innerPlaceholder = computed(() => {
    // 提示信息
    if (props.placeholder) return props.placeholder;
    if (props.isDatetime) return '选择日期时间';
    if (props.isDate) return '选择日期';
  });

  const getValueFormat = computed(() => {
    // 指定输入输出的文本日期时间的格式，这个必须与后端保持一致，否则无法识别
    if (isDate.value) return 'YYYY-MM-DD';
    if (isDatetime.value) return 'YYYY-MM-DD HH:mm:ss';
  });
</script>
