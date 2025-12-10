import App from './App.vue';
import router from './router';
import piniaStore from './store';

import '@/styles/index.less';
import '@/styles/reset.less';

// 支持SVG
import 'virtual:svg-icons-register';
import '@arco-design/web-vue/dist/arco.css';

import 'virtual:uno.css';

// DevUI
import 'vue-devui/style.css';
import '@devui-design/icons/icomoon/devui-icon.css';

// element-plus CSS
import 'element-plus/dist/index.css';
import 'element-plus/theme-chalk/dark/css-vars.css';

import { ThemeServiceInit, devuiDarkTheme } from 'devui-theme';

const themeService = ThemeServiceInit({ devuiDarkTheme }, 'infinityTheme');

themeService?.applyTheme(devuiDarkTheme);

//vue3的挂载方式
const app = createApp(App);

// 装载element-plus并且配置中文
import ElementPlus from 'element-plus';
import zhCn from 'element-plus/es/locale/lang/zh-cn';
app.use(ElementPlus, {
  locale: zhCn,
});

// 注册elementplus icons的全部图标
import * as ElementPlusIconsVue from '@element-plus/icons-vue';
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

// register vue-axios
import axios from 'axios';
import VueAxios from 'vue-axios';
app.use(VueAxios, axios);

app.use(router);
app.use(piniaStore);

app.mount('#app');
