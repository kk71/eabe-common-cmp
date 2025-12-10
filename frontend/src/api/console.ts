import { get } from '@/utils/http/axios/console';

// 统计
export const getOverallStats = (conf: any) => get({ ...conf, url: '/console/stats/overall' });

// 账单
export const getMonthBills = (conf: any) => get({ ...conf, url: '/console/bill/month' });

// 订单
export const getOrders = (conf: any) => get({ ...conf, url: '/console/order' });
