import { useAppStore } from '@/store/modules/app';

export const hasPrivilege = (privilege) => {
  // 判断当前登录人是否有此权限
  // privilege可以是权限的name，也可以是权限对象，也可是上述的数组
  // 如果是数组，则执行且逻辑
  const appStore = useAppStore();
  if (privilege.constructor == Array) {
    for (const i of privilege) {
      let r = hasPrivilege(i);
      if (!r) return false;
    }
    return true;
  } else if (privilege.constructor == String) {
    if (!appStore.privilegesNames.includes(privilege)) {
      console.error(`unknown privilege: ${privilege}, return true`);
      return true;
    }
    return appStore.userPrivilegesNames.includes(privilege);
  } else if (privilege.constructor == Object) {
    return hasPrivilege(privilege.name);
  } else console.error('bad privilege: ', privilege);
};

export const hasAnyPrivilege = (privilege) => {
  // 判断当前登录人是否有此权限中的任意一个
  // 数组，执行或逻辑
  if (privilege.constructor == Array) {
    for (const i of privilege) {
      let r = hasPrivilege(i);
      if (r) return true;
    }
    return false;
  } else console.error('bad any privilege: ', privilege);
};
