<template>
  <div class="dt-display">
    <el-icon v-if="isDate" size="16" color="#a8abb2">
      <Calendar />
    </el-icon>
    <el-icon v-if="isDatetime" size="16" color="#a8abb2">
      <Clock />
    </el-icon>
    <div class="dt-display-inner">
      <span class="human-readable-dt">
        <span v-if="!isToday || !displayHighlightedToday">
          {{ display }}
        </span>
        <el-tag type="warning" v-else>{{ display }}</el-tag>
      </span>
      <span class="original-dt">{{ props.value ? props.value : '-' }}</span>
    </div>
  </div>
</template>
<script setup>
  const props = defineProps({
    value: {
      type: [String, Date, null],
    },
    type: {
      // 选择日期时间还是仅日期
      type: String,
      default: 'datetime',
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

  const isDate = computed(() => {
    return props.type == 'date';
  });

  const isDatetime = computed(() => {
    return props.type == 'datetime';
  });

  const isToday = computed(() => {
    // 日期是今日
    const now = new Date();
    let v = props.value;
    if (!v || v === null || v === undefined || v == '') return false;
    if ([String, Number].includes(v.constructor)) v = new Date(v);
    return v.getFullYear() == now.getFullYear() && v.getMonth() == now.getMonth() && v.getDate() == now.getDate();
  });

  const display = computed(() => {
    // 用于人性化展示时间
    const now = new Date();
    let v = props.value;
    if (!v) return '-';
    if ([String, Number].includes(v.constructor)) v = new Date(v);
    if (v.constructor != Date) throw Error('bad date object');
    let absolute_day;
    if (v.getFullYear() == now.getFullYear()) absolute_day = `${v.getMonth() + 1}月${v.getDate()}日`;
    else absolute_day = `${v.getFullYear()}年${v.getMonth() + 1}月${v.getDate()}日`;
    let full_absolute;
    let hourMinute;
    if (isDatetime.value) {
      if (v.getSeconds()) hourMinute = `${v.getHours()}:${v.getMinutes()}:${v.getSeconds()}`;
      else hourMinute = `${v.getHours()}:${v.getMinutes()}`;
      full_absolute = `${absolute_day}${hourMinute}`;
    } else if (isDate.value) {
      full_absolute = absolute_day;
    } else throw Error('???');
    if (!props.displayRelative) return full_absolute;
    const db_yesterday = new Date(now);
    db_yesterday.setDate(now.getDate() - 2);
    const yesterday = new Date(now);
    yesterday.setDate(now.getDate() - 1);
    const tomorrow = new Date(now);
    tomorrow.setDate(now.getDate() + 1);
    const da_tomorrow = new Date(now);
    da_tomorrow.setDate(now.getDate() + 2);
    const mappings = {
      前天:
        v.getFullYear() == db_yesterday.getFullYear() && v.getMonth() == db_yesterday.getMonth() && v.getDate() == db_yesterday.getDate(),
      昨天: v.getFullYear() == yesterday.getFullYear() && v.getMonth() == yesterday.getMonth() && v.getDate() == yesterday.getDate(),
      今天: v.getFullYear() == now.getFullYear() && v.getMonth() == now.getMonth() && v.getDate() == now.getDate(),
      明天: v.getFullYear() == tomorrow.getFullYear() && v.getMonth() == tomorrow.getMonth() && v.getDate() == tomorrow.getDate(),
      后天: v.getFullYear() == da_tomorrow.getFullYear() && v.getMonth() == da_tomorrow.getMonth() && v.getDate() == da_tomorrow.getDate(),
    };
    for (const k in mappings) {
      if (mappings[k] === true && isDatetime.value) return `${k}${hourMinute}`;
      if (mappings[k] === true && isDate.value) return k;
    }
    return full_absolute;
  });
</script>
<style lang="less">
  .dt-display {
    display: flex;
    align-items: center;
    gap: 5px;
    position: relative; // 因为滚动会固定，增了这个解决了

    .dt-display-inner {
      display: flex;
      align-items: center;
      margin: 1px 0 0 0;

      .human-readable-dt {
        position: absolute;
        opacity: 1;
      }

      .original-dt {
        opacity: 0;
      }
    }
  }

  .dt-display:hover .human-readable-dt {
    opacity: 0;
    transition: all 0.1s ease;
  }

  .dt-display:hover .original-dt {
    opacity: 1;
  }
</style>
