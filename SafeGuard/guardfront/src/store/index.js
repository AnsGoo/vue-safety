import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

var store = new Vuex.Store({
  state: {
    user: {
      isLogin: sessionStorage.getItem("isLogin") || false,
      userName: sessionStorage.getItem("username") || "请登录",
      isAdmin: eval(sessionStorage.getItem("isAdmin")) || false,
      token: sessionStorage.getItem("token") || null,
      group:sessionStorage.getItem("group") || null
    }
  },
  mutations: {
    UPDATELOGINSTATUS(state, user) {
      sessionStorage.setItem("isLogin", user.status);
      sessionStorage.setItem("username", user.username);
      sessionStorage.setItem("token", user.token);
      sessionStorage.setItem("group",user.group);
      localStorage.setItem("gurad", user.token);
      sessionStorage.setItem("isAdmin", user.isadmin);
      state.user.isLogin=user.status;
      state.user.userName=user.username;
      state.user.isAdmin=user.isadmin;
      state.user.token=user.token;
      state.user.group=user.group;
    },
    LOGOUT(state) {
      state.user = { username: "", token: "", isLogin: "" };
      sessionStorage.removeItem("isLogin");
      sessionStorage.removeItem("username");
      sessionStorage.removeItem("token");
      sessionStorage.removeItem("isAdmin");
      localStorage.removeItem("gurad", user.token)
      state.user.isLogin=false;
      state.user.userName='请登录';
      state.user.isAdmin=false;
      state.user.token=null;
      state.user.group=null;
    }
  },
  actions: {}
});
export default store;