import axios from 'axios';
import { ElMessage } from 'element-plus';
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse, AxiosError, InternalAxiosRequestConfig } from 'axios';
import router from '@/router/index';
import { useAppStore } from '@/store/modules/app';

export const showMessage = (status: number | string): string => {
  let message = '';
  switch (status) {
    case 400:
      message = '请求错误(400)';
      break;
    case 401:
      message = '未授权，请重新登录(401)';
      break;
    case 403:
      message = '拒绝访问(403)';
      break;
    case 404:
      message = '请求出错(404)';
      break;
    case 408:
      message = '请求超时(408)';
      break;
    case 500:
      message = '服务器错误(500)';
      break;
    case 501:
      message = '服务未实现(501)';
      break;
    case 502:
      message = '网络错误(502)';
      break;
    case 503:
      message = '服务不可用(503)';
      break;
    case 504:
      message = '网络超时(504)';
      break;
    case 505:
      message = 'HTTP版本不受支持(505)';
      break;
    default:
      message = `连接出错(${status})!`;
  }
  return `${message}，请检查网络或联系管理员！`;
};

const service: AxiosInstance = axios.create({
  baseURL: import.meta.env.VITE_APP_API_BASEURL,
  timeout: 30000,
});

// axios实例拦截请求
service.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    const store = useAppStore();
    config.headers.authorization = store.getAuthorization;
    return config;
  },
  (error: AxiosError) => {
    return Promise.reject(error);
  },
);

// axios实例拦截响应
service.interceptors.response.use(
  (response: AxiosResponse) => {
    if (response.status === 200) {
      return response;
    }
    showMessage(response.status);
    return response;
  },
  // 请求失败
  (error: any) => {
    const data = error.response.data;
    const status_code = error.response.status;
    if (status_code == 401) {
      // token失效
      ElMessage({
        message: '认证已过期，请重新登录。',
        type: 'error',
      });
      const store = useAppStore();
      store.clearToken();
      router.push({
        path: '/console/login',
        query: {
          nextStep: location.pathname + location.search,
        },
      });
    } else if (status_code == 502) {
      // 后端连接失败
      ElMessage({
        message: '后端服务不可用，请稍后再试。',
        type: 'error',
        duration: 6000,
      });
      return Promise.reject(error);
    } else {
      // 其他错误直接展示错误信息
      let msg = data['msg'];
      if (!msg) msg = data;
      ElMessage({ message: msg, type: 'error', duration: 6000 });
      return Promise.reject(error);
    }
  },
);

// 返回res.data的interface
export interface IResponse<T = any> {
  data: T;
  msg: string;
}

const request = async <T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> => {
  const resp: AxiosResponse<IResponse> = await service.request<any, AxiosResponse<IResponse>>(config);
  const r = {
    ...resp,
    data: { ...resp.data, data: resp.data?.data as T },
  };
  return r;
};

export function get<T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> {
  return request({ ...config, method: 'GET' });
}

export function post<T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> {
  return request({ ...config, method: 'POST' });
}

export function patch<T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> {
  return request({ ...config, method: 'patch' });
}

export function put<T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> {
  return request({ ...config, method: 'put' });
}

export function del<T = any>(config: AxiosRequestConfig): Promise<AxiosResponse<IResponse<T>>> {
  return request({ ...config, method: 'delete' });
}

export default request;
