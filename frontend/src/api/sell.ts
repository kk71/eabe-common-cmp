import { get, post, patch } from '@/utils/http/axios/sell';

export const getCart = (conf: any) => get({ ...conf, url: '/sell/cart' });
export const addToCart = (conf: any) => patch({ ...conf, url: '/sell/cart/add' });
export const deleteFromCart = (conf: any) => patch({ ...conf, url: '/sell/cart/delete' });
export const calcProductInfo = (conf: any) => post({ ...conf, url: '/sell/product/calc' });

// 统计
export const getOverallStats = (conf: any) => get({ ...conf, url: '/sell/stats/overall' });

// 账单
export const getMonthBills = (conf: any) => get({ ...conf, url: '/sell/bill/month' });

// 订单
export const getOrders = (conf: any) => get({ ...conf, url: '/sell/order' });
