<template>
  <div id="app">
    <a-locale-provider :locale="zh_CN">
      <router-view/>
    </a-locale-provider>
  </div>
</template>

<script>
import zh_CN from "ant-design-vue/lib/locale-provider/zh_CN";
import moment from "moment";
import "moment/locale/zh-cn";

moment.locale("zh-cn");
export default {
  name: "App",
  data() {
    return {
      zh_CN
    };
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  /* margin-top: 60px; */
}
th {
  background-color: #0c548e !important;
  color: azure !important;
}
.btn-success {
  background-color: #67c23a !important;
  color: azure !important;
}
.btn-warning {
  background-color: #e6a23c;
  color: azure !important;
}
.btn-ensure {
  background-color: #2db7f5;
  color: azure !important;
}
.btn-danger {
  background-color: #f50 !important;
  color: azure !important;
}
</style>
