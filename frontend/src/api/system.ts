import { get, post, patch, del } from '@/utils/http/axios/console';

// 查询当前系统状态
export const getConf = (conf) => get({ ...conf, url: '/conf' });

// 异步任务查询
export const getCeleryTaskRecord = (conf) => get({ ...conf, url: '/celery' });

// 登录用户
// 以密码登录，或者根据已有的token换取新的token，并返回用户登录信息
export const userPasswordLogin = (conf) => post({ ...conf, url: '/auth/login' });

// 用户
export const getUser = (conf) => get({ ...conf, url: '/auth/user' });
export const addUser = (conf) => post({ ...conf, url: '/auth/user' });
export const editUser = (conf) => patch({ ...conf, url: '/auth/user' });
export const deleteUser = (conf) => del({ ...conf, url: '/auth/user' });
export const setUserRole = (conf) => patch({ ...conf, url: '/auth/user/role' });
export const changeUserPassword = (conf) => patch({ ...conf, url: '/auth/user/password' });

// 角色+权限
export const getRole = (conf) => get({ ...conf, url: '/auth/role' });
export const addRole = (conf) => post({ ...conf, url: '/auth/role' });
export const editRole = (conf) => patch({ ...conf, url: '/auth/role' });
export const deleteRole = (conf) => del({ ...conf, url: '/auth/role' });

// 权限
export const getAllPrivilege = (conf) => get({ ...conf, url: '/auth/privilege' });
export const getAllPrivilegeGroup = (conf) => get({ ...conf, url: '/auth/privilege/group' });
