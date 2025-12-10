前端
====

主要使用Vue3+ElementPlus编写的用户界面

## 环境依赖

请安装最新的nodejs，以及下载最新的pnpm: https://github.com/pnpm/pnpm/releases


## 安装依赖包

```shell
pnpm install
```

## 运行测试服

```shell
pnpm dev
```

## 编译并部署到正式服

请注意这个脚本依赖sftp上传代码，需要确认本机能登录服务器并且已配置了sshkey

```shell
./fe-update.sh
```
