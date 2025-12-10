<template>
  <div ref="simpleBarChart" v-if="!loading" style="height: 300px; width: 2000px"></div>
  <el-skeleton :rows="5" animated v-if="loading" />
</template>

<script setup>
  import echarts from '@/common/echarts';

  const simpleBarChart = ref(null);

  const props = defineProps({
    loading: {
      type: Boolean,
      default: false,
    },
    data: {
      type: [Array, null],
      required: true,
    },
    xKey: {
      // x轴字段
      type: String,
      default: 'key',
    },
    xName: {
      type: String,
      default: '',
    },
    yKey: {
      // y轴字段
      type: String,
      default: 'value',
    },
    yName: {
      type: String,
      default: '',
    },
    theme: {
      type: String,
      default: 'vintage',
    },
  });

  const buildChart = async (bar) => {
    let xItems = [];
    let yItems = [];
    for (const i of props.data) {
      xItems.push(i[props.xKey]);
      yItems.push(i[props.yKey]);
    }
    await nextTick();
    const myEChart = echarts.init(bar, props.theme);
    const option = {
      xAxis: {
        name: props.xName,
        data: xItems,
      },
      yAxis: {
        name: props.yName,
      },
      series: [
        {
          type: 'line',
          data: yItems,
          barWidth: '20%',
          label: {
            show: true,
            position: 'top',
          },
        },
      ],
    };
    myEChart.setOption(option);
    window.addEventListener('resize', function () {
      myEChart.resize();
    });
  };

  watch(
    () => props.data,
    async () => {
      if (props.loading) return;
      if (!props.data || props.data.constructor != Array) return;
      await buildChart(simpleBarChart.value);
    },
    { deep: true },
  );
</script>

<style lang="less"></style>
