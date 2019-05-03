<template>
  <div>
    <a-col :span="4" :offset="20">
      <a-col :span="8">
        <a-avatar :size="48" icon="user"/>
      </a-col>
      <a-col :span="8">
        <span class="user">{{userName}}</span>
      </a-col>
      <a-col :span="8">
        <a-tag v-if="isLogin" color="#E6A23C" @click="logout">注销</a-tag>
        <a-tag v-if="!isLogin" color="#108ee9"  @click="goToLogin">登陆</a-tag>
        <!-- <a-tag v-if="!isLogin" color="#108ee9" @click="isRegister">注册</a-tag> -->
      </a-col>
    </a-col>
  </div>
</template>
<script>
export default {
  name: "Login",
  data() {
    return {
      userName: "请登录",
      isLogin: false
    };
  },
  mounted() {
    this.userName = this.$store.state.user.userName;
    this.isLogin = this.$store.state.user.isLogin;
  },
  watch: {
    "$store.state.user.isLogin": function() {
      this.userName = this.$store.state.user.userName;
      this.isLogin = this.$store.state.user.isLogin;
    }
  },
  methods: {
    goToLogin: function() {
        this.$router.push("/login");
    },
    logout: function() {
        this.isLoginUser = false;
        this.userName = "请登录";
        this.$store.commit("LOGOUT");
    }
  }
};
</script>
<style scoped>
.user{
  color: #fff
}
</style>


