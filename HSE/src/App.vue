<template>
  <div id="app">
    <el-container class="s-container">
      <el-header class="s-head">
        <el-row :gutter="24">
          <el-col :span="24">
            <el-menu
              :default-active="activeIndex"
              class="el-menu-demo"
              mode="horizontal"
              background-color="#545c64"
              text-color="#fff"
              active-text-color="#ffd04b"
            >
              <el-menu-item index="1">
                <router-link to="/foo">处理中心</router-link>
              </el-menu-item>
              <el-submenu index="2">
                <template slot="title">
                  <router-link to="/foo">我的工作台</router-link>
                </template>
                <el-menu-item index="2-1">选项1</el-menu-item>
                <el-menu-item index="2-2">选项2</el-menu-item>
                <el-menu-item index="2-3">选项3</el-menu-item>
              </el-submenu>
              <el-menu-item index="3">
                <router-link to="/foo">消息中心</router-link>
              </el-menu-item>
              <el-menu-item index="4">
                <router-link to="/foo">订单管理</router-link>
              </el-menu-item>

              <el-menu-item index="-1" disabled style="float:right" v-if="!isLogin">
                <el-col :span="10">
                  <el-input size="medium" v-model="userName" placeholder="请输入用户名"></el-input>
                </el-col>
                <el-col :span="10">
                  <el-input size="medium" type="password" v-model="passWord" placeholder="请输入密码"></el-input>
                </el-col>
                <el-col :span="4">
                  <el-button type="info" plain v-on:click="login">登陆</el-button>
                </el-col>
              </el-menu-item>
              <el-menu-item index="-1" disabled style="float:right" v-if="isLogin">
                <el-button type="text" disabled>{{user}}</el-button>
                <el-button type="info" plain v-on:click="logout">注销</el-button>
              </el-menu-item>
            </el-menu>
          </el-col>
          <!-- <el-col :span="8" class="s-user">
            <el-col :span="12">
              <el-input size="medium" v-model="input" placeholder="请输入用户名"></el-input>
            </el-col>
            <el-col :span="12">
              <el-input size="medium" v-model="input" placeholder="请输入密码"></el-input>
            </el-col>
          </el-col>-->
        </el-row>
      </el-header>
      <el-main class="s-body">
        <router-view/>
      </el-main>
      <el-footer class="s-foot">
        <p class="copyright">
          2018 © 江湖科技
          <a target="_blank" href="http://119.29.153.78/">ChengHaiwen</a> &nbsp;|&nbsp;
          <a href="http://119.29.153.78/" title="为未来而生" target="_blank">为未来而生!</a>
        </p>
      </el-footer>
    </el-container>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      activeIndex: "1",
      user: null,
      isLogin: false,
      userName: null,
      passWord: null
    };
  },
  mounted() {
    this.getUser();
  },
  methods: {
    getUser: function() {
      this.$axios.get("http://127.0.0.1:8000/user/get_user/").then(resp => {
        console.log(resp.data);
        let loginStatus = resp.data;
        this.isLogin = loginStatus.status;
        this.user = loginStatus.user;
      });
    },
    login: function() {
      var params = new URLSearchParams();
      params.append("username", this.userName);
      params.append("password", this.passWord);
      this.$axios.post("http://127.0.0.1:8000/login/", params).then(resp => {
        console.log(resp.data);
        let loginStatus = resp.data;
        this.user = loginStatus.user;
        this.isLogin = true;
      });
    },
    logout: function() {
      this.$axios.get("http://127.0.0.1:8000/logout/").then(resp => {
        console.log(resp.data);
        this.isLogin = false;
        this.user = null;
      });
    }
  }
};
</script>

<style>
.s-container {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  width: 1200px;
  margin: 0 auto;
}
.s-head {
  padding: 0 0px;
  background-color: "#545c64";
}
.s-body {
  min-height: 960px;
  background-color: seashell;
}
.s-foot {
  background-color: #545c64;
  color: beige;
}
.s-user {
  background-color: "#545c64";
}
.login-input {
  background-color: azure;
}
</style>
