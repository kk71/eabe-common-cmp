import { get } from '@/utils/http/axios/console';

export const getAllStatusMachineValues = () => get({ url: '/sm' });
