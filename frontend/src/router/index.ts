import { createRouter, createWebHistory } from 'vue-router';
import { routes } from 'vue-router/auto-routes';
import NProgress from 'nprogress';
import 'nprogress/nprogress.css';

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

  next();
});

router.afterEach((_to) => {
  NProgress.done();
});

export default router;
