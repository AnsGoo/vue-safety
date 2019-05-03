.<template>
  <!-- <div class="login-views"> -->
  <a-layout>
    <a-layout-header class="login-views"></a-layout-header>
    <a-layout-content  class="login-center">
      <a-col :span="14" class="welcome">
        <a-row>
          <img class="logo" src="../../assets/hava.svg" @click="goToIndex">
        </a-row>
        <a-row>
          <a-col :offset="8">————HAVA 测试平台最佳伴侣</a-col>
        </a-row>
      </a-col>
      <a-col :span="8" class="login">
        <a-col></a-col>
        <a-form :form="form">
          <a-form-item :label-col="{span:8}" :wrapper-col="{span:16}">
            <span slot="label" class="lable">用户名</span>
            <a-input
              v-decorator="[
          'username',
          {rules: [{ required: true, message: '请输入用户名' }]}
        ]"
              placeholder="请输入用户名"
            />
          </a-form-item>
          <a-form-item :label-col="{span:8}" :wrapper-col="{span:16}">
            <span slot="label" class="lable">密码</span>
            <a-input
              type="password"
              v-decorator="[
          'password',
          {rules: [{ required: true, message: '请输入密码' }]}
        ]"
              placeholder="请输入密码"
            />
          </a-form-item>
          <a-form-item>
            <a-button type="primary" @click="login">登陆</a-button>
          </a-form-item>
        </a-form>
      </a-col>
    </a-layout-content>
    <a-layout-footer class="login-foot">
      <p class="copyright">
      2019 ©
      <a target="_blank" href="http://119.29.153.78/">华为科技有限公司</a> &nbsp;|&nbsp;
      <a href="http://119.29.153.78/" title="华为科技" target="_blank">华为科技</a>
    </p>
    </a-layout-footer>
  </a-layout>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      form: this.$form.createForm(this)
    };
  },
  methods: {
    goToIndex:function() {
        this.$router.push("/index");
    },
    login:function(){
      this.$api.login(this.form.getFieldsValue()).then(resp=>{
        if(resp.status){
          this.$store.commit('UPDATELOGINSTATUS',resp)
          this.$message.success('登录成功')
          this.$router.push('/')
        }else{
          this.$message.warning('登录失败')
        }
      })
    }
  }
};
</script>
<style scoped>
.login-views {
  padding-top: 100px;
  background-color: #0c548e;
}
.login-center {
  margin: 50px 0px;
  height: 300px;
  /* background-color:#0c548e */
}
.login-foot{
  height: 50xp;
}
.login {
  padding-top: 30px;
}
.lable {
  /* color: #edf4f8; */
  font-size: 16px;
  font-weight: 400 !important;
  margin-bottom: 30px;
}

</style>
