import { getAllStatusMachineValues } from '@/api/sm';

let commonStatusMachines: statusMachine[] = [];

export const initializeStatusMachines = async () => {
  // 初始化全部导出的状态机值
  // 请注意，通用状态机的值不在这里获取
  // 该方法会在frame初始化之前被调用，但是某些界面展示需要更高的优先级，初始化这类界面的时候，frame方法调用的数据可能还没有返回
  // 这种情况下，可以手动在用到该数据之前的地方await本方法，确保一定可以拿到数据
  let resp = await getAllStatusMachineValues();
  commonStatusMachines = resp.data.data;
};

export interface statusMachineValue {
  value: string | number;
  name: string;
  next_status: string[] | null;
  extra: any;
}

export interface statusMachine {
  export_flag: string;
  docstring: string;
  smvs: statusMachineValue[];
  tags: [];
}

export const getStatusMachine = (export_flag: string): statusMachine | undefined => {
  // 根据状态机的输出标识查询状态机
  for (const i of commonStatusMachines) {
    if (i.export_flag == export_flag) return i;
  }
  console.error(`no status machine exported as ${export_flag}`);
};

export const getSmv = (export_flag: string, value: string | number) => {
  // 根据状态机的值查询该值的smv
  for (const i of commonStatusMachines[export_flag]) {
    if (i.value == value) return Object.assign({}, i);
  }
  console.error(`no status machine exported as ${export_flag}`);
};
