// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import store from "./store/index";
import Antd from "ant-design-vue";
import "ant-design-vue/dist/antd.css";
import 'font-awesome/css/font-awesome.css'
import api from "./server/index";
Vue.use(Antd);
Vue.use(api);
// Vue.use()
// Vue.use(require("vue-wechat-title"));
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
