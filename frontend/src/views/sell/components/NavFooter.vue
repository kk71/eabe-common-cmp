<template>
  <div class="footer">
    <div class="footer-logo">
      <img src="/company-logo/LOGO2.png" alt="" />
      <p>羿贝综合云服务平台</p>
    </div>
    <div class="footer-link">
      <a href="javascript:;">帮助中心</a><span>|</span> <a href="javascript:;">服务支持</a><span>|</span>
      <a href="javascript:;">关于羿贝</a>
    </div>
    <div class="copyright"> Copyright ©2025 <span class="domain">Eabe</span> All Rights Reserved. </div>
  </div>
</template>
<script>
  export default {
    name: 'nav-footer',
  };
</script>
<style lang="scss" scoped>
  .footer {
    height: 234px;
    border-top: 4px solid #3370ff;
    background-color: #ffffff;
    color: #4e5969;
    font-size: 16px;
    text-align: center;
    .footer-logo {
      margin-top: 46px;
      margin-bottom: 31px;
      img {
        width: 53px;
        height: 36px;
        margin-bottom: 13px;
      }
    }
    .footer-link {
      a {
        color: #4e5969;
        display: inline-block;
      }
      a:hover {
        color: #3370ff;
      }
      span {
        margin: 0 10px;
      }
      margin-bottom: 13px;
    }
    .copyright {
      .domain {
        color: #3370ff;
      }
    }
  }
</style>
