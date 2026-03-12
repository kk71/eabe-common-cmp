import { Ref } from 'vue';

export const waitRequest = async <T = any>(injection: Ref<boolean>, pms: Promise<T>) => {
  // 等待请求周期，控制injection作为请求的开始结束标识位
  // injection: 应当为页面上的一个inject
  // pms: 请求的promise
  // if (injection.value) throw new Error('another load request is running, cancelled.');
  injection.value = true;
  try {
    const respData = await pms;
    injection.value = false;
    return respData;
  } catch (e) {
    injection.value = false;
    throw e;
  }
};

export class SortedBatchGet {
  // 请求方法
  request: Function;
  // 额外需要传入字段
  extraParam: object = {};
  // 全部需要的id
  ids: any[];
  // 查询的id逗号分隔字段名
  queryIdKey: string;
  // 返回结果中id的key
  respIdKey: string;
  // 单次请求最大数量
  batchSize: number = 10;

  pendingIds: any[] = [];
  data: any[] = [];

  constructor(d) {
    this.request = d.request;
    this.extraParam = d.extraParam;
    this.queryIdKey = d.queryIdKey;
    this.ids = d.ids;
    this.respIdKey = d.respIdKey;
    this.batchSize = d.batchSize || 10;
    this.pendingIds = [...this.ids];
    this.data = [];
  }

  async fetchMore() {
    // 拉取更多数据并排序
    if (!this.pendingIds.length) return;
    const toLoad = this.pendingIds.splice(0, this.batchSize);
    const req = this.request({
      params: {
        page: 1,
        per_page: 99,
        ...this.extraParam,
        [this.queryIdKey]: toLoad.toString(),
      },
    });
    const resp = await req;
    for (const itemToLoad of toLoad) {
      for (const respData of resp.data.data) {
        if (respData[this.respIdKey] == itemToLoad) {
          this.data.push(respData);
          break;
        }
      }
    }
  }

  async fetchAll() {
    // 把尚未拉取的数据全部拉完
    while (this.pendingIds.length) {
      await this.fetchMore();
    }
  }
}
