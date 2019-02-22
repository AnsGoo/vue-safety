import Vue from "vue";
import Vuex from "vuex";
Vue.use(Vuex);

var store = new Vuex.Store({
  state: {
    user: {
      isLogin: sessionStorage.getItem("isLogin") || false,
      userName: sessionStorage.getItem("username") || null,
      token: sessionStorage.getItem("token") || null
    }
  },
  mutations: {
    updateLoginStatus(state, user) {
      sessionStorage.setItem("isLogin", user.status);
      sessionStorage.setItem("username", user.username);
      sessionStorage.setItem("token", user.token);
      state.user = user;
    },
    logout(state) {
      state.user = { username: "", token: "", isLogin: "" };
      sessionStorage.removeItem("isLogin");
      sessionStorage.removeItem("username");
      sessionStorage.removeItem("token");
    }
  },
  actions: {}
});
export default store;
