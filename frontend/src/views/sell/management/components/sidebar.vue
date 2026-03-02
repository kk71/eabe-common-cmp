<template>
  <aside class="sell-left-sidebar">
    <h4 class="sidebar-heading">费用中心</h4>
    <ul class="sidebar-menu">
      <li v-for="item in menus" :key="item.id">
        <a
          href="javascript:;"
          class="menu-item"
          :class="{ active: isActive(item) }"
          @click.prevent="handleClick(item)"
        >
          <span class="menu-text">
            <el-icon v-if="item.icon" class="menu-icon">
              <component :is="item.icon" />
            </el-icon>
            {{ item.label }}
          </span>
        </a>
      </li>
    </ul>
  </aside>
</template>

<script lang="ts" setup>
  import { useRoute, useRouter } from 'vue-router';
  import { House, Wallet, Document, DocumentChecked, User } from '@element-plus/icons-vue';

  const router = useRouter();
  const route = useRoute();

  const menus = [
    { id: 'overview', label: '账户总览', path: '/sell/management', icon: House },
    { id: 'wallet', label: '收支明细', path: '/sell/management/wallet', icon: Wallet },
    { id: 'month-bill', label: '账单概览', path: '/sell/management/month-bill', icon: Document },
    { id: 'bill-detail', label: '账单详情', path: '/sell/management/bill-detail', icon: DocumentChecked },
    { id: 'order', label: '订单管理', path: '/sell/management/order', icon: User },
  ];

  const isActive = (item: (typeof menus)[number]) => {
    return route.path === item.path;
  };

  const handleClick = (item: (typeof menus)[number]) => {
    if (item.path && item.path !== route.path) {
      router.push(item.path);
    }
  };
</script>

<style lang="less" scoped>
  .sell-left-sidebar {
    width: 180px;
    flex-shrink: 0;
    background: #ffffff;
    border-right: 1px solid #e5e6eb;
    padding: 16px 0;
    overflow-y: auto;
  }

  .sidebar-heading {
    font-size: 14px;
    font-weight: 600;
    color: #1d2129;
    padding: 0 16px 12px;
  }

  .sidebar-menu {
    list-style: none;
    margin: 0;
    padding: 0;
  }

  .menu-item {
    display: flex;
    align-items: center;
    padding: 8px 16px;
    font-size: 13px;
    color: #4e5969;
    text-decoration: none;
    transition: all 0.15s;
    cursor: pointer;
    white-space: nowrap;
  }

  .menu-item:hover {
    color: #3370ff;
    background: #f7f8fa;
  }

  .menu-item.active {
    color: #3370ff;
    font-weight: 500;
    background: #e8f3ff;
  }

  .menu-text {
    display: flex;
    align-items: center;
    gap: 6px;
  }

  .menu-icon {
    font-size: 16px;
  }

  @media (max-width: 640px) {
    .sell-left-sidebar {
      width: 100%;
      border-right: none;
      border-bottom: 1px solid #e5e6eb;
      display: flex;
      flex-direction: column;
    }

    .sidebar-menu {
      display: flex;
      overflow-x: auto;
    }

    .menu-item {
      padding: 8px 12px;
    }
  }
</style>
