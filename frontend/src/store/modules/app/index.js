import { defineStore } from 'pinia';
import router from '@/router/index';
import { userPasswordLogin, getConf, getAllPrivilege } from '@/api/system';

export const useAppStore = defineStore('app', {
  state: () => ({
    // 是否打印额外日志
    debug: false,
    // 是否处于正式环境
    prod_env: false,
    // 总后台主题
    console_theme: '',
    // 客户后台主题
    sell_theme: '',
    // 系统的全部权限信息
    privileges: [],
    // 当前登录所得token
    token: null,
    // 当前登录人的信息
    user: null,
    // 当前登录人所拥有的权限
    user_privileges: [],
  }),

  getters: {
    getAuthorization() {
      // 输出一个直接可以用在http请求头的authorization字段的值
      return `bearer ${this.token}`;
    },

    privilegesNames() {
      // 返回所有的权限名称列表
      return this.privileges.map((i) => i.name);
    },

    userPrivilegesNames() {
      // 返回当前登录人所有的权限名称列表
      return this.user_privileges.map((i) => i.name);
    },
  },

  actions: {
    toggleConsoleTheme(dark) {
      if (dark) {
        this.console_theme = 'dark';
        document.documentElement.classList.add('dark');
      } else {
        this.console_theme = 'light';
        document.documentElement.classList.remove('dark');
      }
    },

    toggleSellTheme(dark) {
      if (dark) {
        this.sell_theme = 'dark';
        document.documentElement.classList.add('dark');
      } else {
        this.sell_theme = 'light';
        document.documentElement.classList.remove('dark');
      }
    },

    async fetchConf() {
      // 从后端查询当前状态
      let resp = await getConf();
      this.debug = resp.data.data.debug;
      this.prod_env = resp.data.data.prod_env;
    },

    async fetchAllPrivileges() {
      // 从后端查询所有的权限信息
      let resp = await getAllPrivilege();
      this.privileges = resp.data.data;
    },

    async renewToken() {
      // 如果已有token，尝试刷新并重新获取用户登录信息
      if (this.token && this.user) return;
      if (!this.token) return this.clearToken();
      let resp;
      try {
        resp = await userPasswordLogin({ data: {} });
      } catch (e) {
        return this.clearToken();
      }
      this.setToken(resp.data.data.token, resp.data.data.user, resp.data.data.privileges);
    },

    setToken(token, user, user_privileges) {
      // 设置token
      this.token = token;
      this.user = user;
      this.user_privileges = user_privileges;
    },

    clearToken() {
      // 清空token
      this.token = null;
      this.user = null;
      this.user_privileges = [];
    },
  },

  persist: {
    storage: localStorage,
    pick: ['theme', 'token'],
  },
});
