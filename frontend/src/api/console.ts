import { get, post } from '@/utils/http/axios/console';

// 统计
export const getOverallStats = (conf: any) => get({ ...conf, url: '/console/stats/overall' });
export const getPaymentStats = (conf: any) => get({ ...conf, url: '/console/stats/payment' });

// 账单
export const getMonthBills = (conf: any) => get({ ...conf, url: '/console/bill/month' });
export const getMonthBillSummary = (conf: any) => get({ ...conf, url: '/console/bill/month/summary' });

// 钱包 / 余额
export const getWalletAccounts = (conf: any) => get({ ...conf, url: '/console/wallet' });
export const getWalletTransactions = (conf: any) => get({ ...conf, url: '/console/wallet/tx' });
export const rechargeWallet = (conf: any) => post({ ...conf, url: '/console/wallet/recharge' });

// 订单
export const getOrders = (conf: any) => get({ ...conf, url: '/console/order' });
export const payOrderByWallet = (conf: any) => post({ ...conf, url: '/console/order/pay' });
