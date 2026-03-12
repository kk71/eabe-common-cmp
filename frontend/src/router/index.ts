import { createRouter, createWebHistory } from 'vue-router';
import { routes } from 'vue-router/auto-routes';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';
import { useAppStore } from '@/store/modules/app';

const baseURL = import.meta.env.VITE_BASE_URL;
//导入生成的路由数据
const router = createRouter({
  history: createWebHistory(baseURL),
  routes,
});

router.beforeEach(async (to, _from, next) => {
  NProgress.start();

  // 兼容尾部斜杠：让 /console/ 与 /console 行为一致（保留 query/hash）
  if (to.path === '/console/') {
    next({ path: '/console', query: to.query, hash: to.hash, replace: true });
    return;
  }

  // 管理员禁止进入客户侧的管理后台（sell/management）
  if (to.path === '/sell/management' || to.path.startsWith('/sell/management/')) {
    const store = useAppStore();
    // 若已有token则尽量拉取用户信息，以便判定是否管理员
    if ((store as any).token) {
      await (store as any).renewToken();
    }
    if ((store as any).user?.is_admin) {
      next({ path: '/console', replace: true });
      return;
    }
  }

  next();
});

router.afterEach((_to) => {
  NProgress.done();
});

export default router;
