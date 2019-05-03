<template>
  <a-layout id="content">
    <a-layout-sider class="sider">
      <img src="../../assets/hava_whit.svg" class="logo">
      <a-menu class="menu" mode="inline" theme="dark">
        <a-sub-menu key="sub1">
          <span slot="title">
            <a-icon type="team" />用户群组
          </span>
          <a-menu-item key="1"><router-link to="/user/list"><a-icon type="user" /> 用户管理</router-link></a-menu-item>
          <a-menu-item key="2"><router-link to="/group/list"><a-icon type="team" />群组管理</router-link></a-menu-item>
          <a-menu-item key="3">权限管理</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub2">
          <span slot="title">
            <a-icon type="cluster" />资产管理
          </span>
          <a-menu-item key="5"><router-link to="/cmdb/list"><a-icon type="laptop" />资产明细</router-link></a-menu-item>
          <a-menu-item key="6" ><a-icon type="mobile" />Device明细</a-menu-item>
          <a-menu-item key="7"><a-icon type="code" />WebSSH</a-menu-item>
          <a-menu-item key="8"><i class="fa fa-mobile" style="font-sise:30px"/>option8</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub3">
          <span slot="title">
            <a-icon type="notification"/>任务管理
          </span>
          <a-menu-item key="9">option9</a-menu-item>
          <a-menu-item key="10">option10</a-menu-item>
          <a-menu-item key="11">option11</a-menu-item>
          <a-menu-item key="12">option12</a-menu-item>
        </a-sub-menu>
        <a-sub-menu key="sub4">
          <span slot="title">
            <a-icon type="notification"/>日志审计
          </span>
          <a-menu-item key="13">option9</a-menu-item>
          <a-menu-item key="14">option10</a-menu-item>
          <a-menu-item key="15">option11</a-menu-item>
          <a-menu-item key="16">option12</a-menu-item>
        </a-sub-menu>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header><User/></a-layout-header>
      <a-layout-content class="body"><router-view/></a-layout-content>
      <a-layout-footer class="foot">
        <p class="copyright">
          2019 ©
          <a target="_blank" href="http://119.29.153.78/">华为科技有限公司</a> &nbsp;|&nbsp;
          <a href="http://119.29.153.78/" title="华为科技" target="_blank">华为科技</a>
        </p>
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script>
import User from "./User";
export default {
  data() {
    return {};
  },
  components: {
    User
  }
};
</script>

<style scoped>
#content{
    min-width: 1200px;
}
#content .logo {
  height: 100px;
  float: left;
}
#content .header {
  height: 100px;
  background-color: #676a6c;
}
#content .sider {
  width: 200px;
  color: #fff;
  background-color: #0c548e;
}
#content .menu {
  width: 200px;
  color: #fff;
  height: 100%;
  background-color: #0c548e;
}

#content .ant-menu-sub {
  width: 200px;
  color: #fff;
  background-color: #0c548e !important;
}

#content .menu {
  width: 200px;
  color: #fff;
  margin: 0px;
  padding: 0px;
  background-color: #293846;
}
#content .ant-layout-header {
  padding: 0px 0px;
  background-color: #676a6c;
  /* background-color:#293846; */
  /* background-color:#fff; */
}
#content .body {
  background: #fff;
  padding: 5px;
  margin: 0px 0px;
  min-height: 960px;
}
#content .foot {
  /* background: #fff; */
  /* padding: 5px; */
  height: 50px;
  margin: 0px 0px;
  /* min-height: 960px */
}
</style>