export const dToStr = (d) => {
  // date对象转日期文本
  if (d.constructor == String) return d;
  if (!d) return;
  let items = [];
  items.push(String(d.getFullYear()));
  items.push(String(d.getMonth() + 1));
  items.push(String(d.getDate()));
  for (const i in items) {
    if (items[i].length == 1) items[i] = '0' + items[i];
  }
  return items.join('-');
};

export const dtToStr = (dt) => {
  // date对象转日期文本
  if (dt.constructor == String) return dt;
  if (!dt) return;
  let items = [];
  items.push(String(dt.getHours()));
  items.push(String(dt.getMinutes()));
  items.push(String(dt.getSeconds()));
  for (const i in items) {
    if (items[i].length == 1) items[i] = '0' + items[i];
  }
  return dToStr(dt) + ' ' + items.join(':');
};

export const dtTodayStart = () => {
  // 返回当日的开始时间（以工作时间9点为准
  let d = new Date();
  d.setHours(9);
  d.setMinutes(0);
  d.setSeconds(0);
  d.setMilliseconds(0);
  return d;
};

export const dtTodayEnd = () => {
  // 返回当日的开始时间（以23点为准
  let d = new Date();
  d.setHours(23);
  d.setMinutes(59);
  d.setSeconds(0);
  d.setMilliseconds(0);
  return d;
};
