import router from '@/router';

/**
 *
 * 用于处理页面url的querystring向接口传递以及反向传递的处理
 * 
        key: type
        key: Number String Boolean
        key: [Array, String]
        key: [Array, Number]
 * 
 * @class QSValidator
 */
export class QSValidator {
  /**
   * @param {*} definition 定义字段
   * @memberof QSValidator
   */
  definition: object;

  constructor(definition) {
    this.definition = definition;
  }

  static arrayEqual(a, b) {
    // 比较两个数组是否一样
    return a.constructor == Array && b.constructor == Array && a.length == b.length && a.every((element, index) => element === b[index]);
  }
  /**
   * 读取当前页面url的querystring并且按照定义转换
   * @memberof QSValidator
   */
  from_qs(original_data: object) {
    let validated = {};
    for (const k in original_data) {
      let v = original_data[k];
      let typing = this.definition[k];
      if (typing == undefined || typing == String) {
        validated[k] = v;
      } else if (typing == Number) {
        validated[k] = Number.parseInt(v);
        if (isNaN(validated[k])) validated[k] = null;
      } else if (typing == Boolean) {
        if (['false', '0'].includes(v)) validated[k] = false;
        else if (['true', '1'].includes(v)) validated[k] = true;
        else console.log('invalid boolean value');
      } else if (QSValidator.arrayEqual(typing, [Array, String]) || typing == Array) {
        if (v.constructor == String && v) validated[k] = v.split(',');
        else validated[k] = v;
      } else if (QSValidator.arrayEqual(typing, [Array, Number])) {
        if (v.constructor == String) {
          validated[k] = [];
          for (const i of v.split(',')) {
            let parsed = Number.parseInt(i);
            if (!isNaN(parsed)) validated[k].push(parsed);
          }
        } else validated[k] = v;
      } else {
        console.error(`unsupported typing ${typing}`);
        validated[k] = v;
      }
    }
    return validated;
  }

  /**
   *js数据渲染成可放置于querystring的格式
   * @param {*} data
   * @memberof QSValidator
   */
  to_qs(target: object) {
    let validated = Object.assign({}, target);
    for (const k in this.definition) {
      let typing = this.definition[k];
      if (typing == Array || QSValidator.arrayEqual(typing, [Array, Number]) || QSValidator.arrayEqual(typing, [Array, String])) {
        if (validated[k]) validated[k] = validated[k].toString();
        else validated[k] = '';
      }
    }
    return validated;
  }
}

export const updateToQuery = (o: any) => {
  // 更新当前页的url的查询字串
  // update the querystring of current page and push it to vue-router

  const currentQS = Object.assign({}, router.currentRoute.value.query);
  let to_update = {};
  for (const k in o) {
    // 如果当前querystring没有指明参数的值（即使用缺省值）那么如果赋值为空文本或者null意即等同于不赋值
    // 为了减少router无意义跳转的次数，这种赋值需要被拦截
    if (currentQS[k] == null && (o[k] == null || o[k] === '' || o[k].length == 0)) continue;
    // 分页为1的是一个特例，这种赋值也没意义
    if (k == 'page' && currentQS['page'] == null && [null, '', 1, '1'].includes(o[k])) continue;
    to_update[k] = o[k];
  }
  const newQS = Object.assign(currentQS, to_update);
  for (const i in newQS) {
    if (newQS[i] != null && newQS[i].constructor == Array) {
      newQS[i] = newQS[i].toString(); // turn array to dot split string
    }
  }
  router.push({
    query: newQS,
  });
};

export const updateFilterDataFromQuery = (filterData) => {
  // 更新除了分页之外的其他字段到filterData
  let q = router.currentRoute.value.query;
  let to_update = {};
  for (const k in q) if (!['page', 'per_page'].includes(k)) to_update[k] = q[k];
  Object.assign(filterData, to_update);
};

export const updatePaginationFromQuery = (p) => {
  // 更新分页信息到p
  let q: object = router.currentRoute.value.query;
  let to_update = {};
  for (const k in q) if (['page', 'per_page'].includes(k)) to_update[k] = parseInt(q[k]);
  Object.assign(p, to_update);
};
