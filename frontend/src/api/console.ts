import { get, post, patch, del } from '@/utils/http/axios/console';

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
export const setWalletBalance = (conf: any) => post({ ...conf, url: '/console/wallet/set-balance' });

// 订单
export const getOrders = (conf: any) => get({ ...conf, url: '/console/order' });
export const payOrderByWallet = (conf: any) => post({ ...conf, url: '/console/order/pay' });

// 导入
export const importOrders = (conf: any) => post({ ...conf, url: '/console/imports/orders' });
export const importMonthBills = (conf: any) => post({ ...conf, url: '/console/imports/month-bills' });
export const importOrdersFile = (conf: any) => post({ ...conf, url: '/console/imports/orders/file' });
export const importMonthBillsFile = (conf: any) => post({ ...conf, url: '/console/imports/month-bills/file' });
export const importWalletTransactionsFile = (conf: any) => post({ ...conf, url: '/console/imports/wallet-transactions/file' });

// 月账单扣费记录
export const getMonthBillChargeRecords = (conf: any) => get({ ...conf, url: '/console/bill/charge' });

// 随机消费规则
export const getRandomConsumptionRules = (conf: any) => get({ ...conf, url: '/console/random_consumption' });
export const createRandomConsumptionRule = (conf: any) => post({ ...conf, url: '/console/random_consumption' });
export const updateRandomConsumptionRule = (conf: any) => patch({ ...conf, url: '/console/random_consumption' });

// 客户
export const getCustomers = (conf: any) => get({ ...conf, url: '/console/customer' });
export const getCustomerDetail = (conf: any) => get({ ...conf, url: '/console/customer/detail' });
export const createCustomer = (conf: any) => post({ ...conf, url: '/console/customer' });
export const updateCustomer = (conf: any) => patch({ ...conf, url: '/console/customer' });
export const deleteCustomer = (conf: any) => del({ ...conf, url: '/console/customer' });
