<template>
  <div :style="$global.bg1">
    <HeaderIf :hospital="hospital" :transparent="true" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">

      <div class="login-card card px-3 py-4 shadow-lg">
        <form class="needs-validation" novalidate>
          <div class="form">
            <div class="col-12 text-left">
              <label for="fn" class="text-white">{{$t("string.user.firstname")}}</label>
              <input type="text" class="form-control bg-white50" id="fn" v-model="firstName" required>
              <small class="invalid">*2-10 letters</small>
            </div>

            <div class="col-12 text-left mt-1">
              <label for="ln" class="text-white">{{$t("string.user.lastname")}}</label>
              <input type="text" class="form-control bg-white50" id="ln" v-model="lastName" required>
              <small class="invalid">*2-10 letters</small>
            </div>

            <div class="col-12 text-left mt-1">
              <label for="validationCustomUsername" class="text-white">{{$t("string.user.username")}}</label>
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text text-white button-gradient" id="inputGroupPrepend">@</span>
                </div>
                <input type="text" class="form-control bg-white50" v-model="username" @blur="verifyUserId('username')" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
              </div>
              <small class="invalid">*4-16 digits, letters, numbers, underscore</small>
              <small class="error-text">{{usernameErrorText}}</small>
            </div>

            <div class="col-12 text-left mt-1">
              <label for="ea" class="text-white">{{$t("string.user.email")}}</label>
              <input type="email" class="form-control bg-white50" id="ea" v-model="email" @blur="verifyUserId('email')" required>
              <small class="invalid">*Please input the correct email address</small>
              <small class="error-text">{{emailErrorText}}</small>
            </div>

            <div class="col-12 text-left mt-1">
              <label for="pw" class="text-white">{{$t("string.user.password")}}</label>
              <input type="password" class="form-control bg-white50" id="pw" v-model="password" required>
              <small class="invalid">*6-18</small>
            </div>

            <div class="col-12 text-left mt-1 mb-2">
              <label for="irc" class="text-white">{{$t("string.user.IRC")}}</label>
              <input type="password" class="form-control bg-white50" id="irc" v-model="irc" :placeholder="$t('string.user.LIBIYRAC')">
            </div>
          </div>
          <small class="text-black-50">{{$t("string.user.registerHint")}}</small>
        </form>
        <div>
          <button class="btn button-gradient rounded border-white text-white mt-2 px-4" type="submit" @click="verifyName()" v-show="showButton">{{$t("string.user.register")}}</button>
          <button class="btn button-gradient rounded border-white text-white mt-2 px-4" type="button" v-show="!showButton" disabled>
            <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
            {{$t("string.user.loading")}}
          </button>
        </div>
      </div>
    </section>
    <Message :hintTitle="registerHintTitle" :hintText="registerHintText" :failure="messageFailure"></Message>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>


<script>
import HeaderIf from '@/components/HeaderIf.vue'
import Footer from '@/components/Footer.vue'
import Message from '@/components/Message.vue'

export default {
  data(){
    return{
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: "",
      usernameErrorText: "",
      emailErrorText: "",
      registerHintTitle: "",
      registerHintText: "",
      showButton: true,
      messageFailure: false,
      irc: "",
      employee: "0"
    }
  },

  props:{
    "hospital": String
  },

  components: {
    HeaderIf,
    Footer,
    Message
  },

  mounted(){
    $(".invalid").hide();
    this.$global.resizeContent();
  },

  created(){
    document.title = this.$t("string.user.register") + " | " + this.hospital;
  },

  methods:{

    verifyName(){
      let nameReg=/^[A-Za-z]{2,10}$/;
      if(nameReg.test(this.firstName)){
        $(".invalid").eq(0).hide();
        if(nameReg.test(this.lastName)){
          $(".invalid").eq(1).hide();
          this.verifyUsername();
        }else{
          $(".invalid").eq(1).show();
        }
      }else{
        $(".invalid").eq(0).show();
      }
    },

    verifyUsername(){
      let usernameReg=/^[a-zA-Z]{1}([a-zA-Z0-9]|[_]){3,15}$/;
      if(usernameReg.test(this.username)){
        $(".invalid").eq(2).hide();
        this.verifyEmail();
      }else{
        $(".invalid").eq(2).show();
      }
    },

    verifyEmail(){
      let emailReg=/^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
      if(emailReg.test(this.email)){
        $(".invalid").eq(3).hide();
        this.verifyPassword();
      }else{
        $(".invalid").eq(3).show();
      }
    },

    verifyPassword(){
      let passwordReg=/^(\S){6,18}$/;
      if(passwordReg.test(this.password)){
        $(".invalid").eq(4).hide();
        this.register();
      }else{
        $(".invalid").eq(4).show();
      }
    },

    register(){
      let _this=this;
      this.showButton=false;
      if(this.irc!="") this.employee="1";

      this.$axios({
        method: 'post',
        url: this.$global.request("register"),
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        data: this.$qs.stringify({
          firstName: this.firstName,
          lastName: this.lastName,
          username: this.username,
          email: this.email,
          password: this.password,
          others: "test",
          employee: this.employee,
          IRC: this.irc
        })
      })
      .then(function (response) {
        _this.showButton=true;
        $('.toast').toast('show');
        if(response.data.code==200){
          _this.messageFailure=false;
          _this.registerHintTitle=_this.$t("string.user.registerSuccess");
          _this.registerHintText=response.data.msg+_this.$t("string.user.registerSuccessHint");
          setTimeout(_this.routeToLogin,2000);
        }
        if(response.data.code==400){
          _this.messageFailure=true;
          _this.registerHintTitle=_this.$t("string.user.registerFailed");
          _this.registerHintText=response.data.msg+_this.$t("string.user.loginFailedHint");
        }
      })
      .catch(function (error) {
        console.log(error);
        _this.showButton=true;
        $('.toast').toast('show');
        _this.messageFailure=true;
        _this.registerHintTitle=_this.$t("string.user.unknowError");
        _this.registerHintText=_this.$t("string.user.unknowErrorHint");
      });
    },

    verifyUserId(mode){
      let data;
      let _this=this;

      if(mode=="username"){
        data=this.$qs.stringify({
          username: this.username
        });
      }else if(mode=="email"){
        data=this.$qs.stringify({
          email: this.email
        })
      }

      this.$axios({
        method: 'post',
        url: this.$global.request("verifyUserId"),
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        data: data,
      })
      .then(function (response) {
        if(response.data.code==201) _this.usernameErrorText="";
        if(response.data.code==202) _this.emailErrorText="";
        if(response.data.code==401) _this.usernameErrorText=response.data.msg;
        if(response.data.code==402) _this.emailErrorText=response.data.msg;
      })
      .catch(function (error) {
        console.log(error);
      });
    },

    routeToLogin(){
      if(this.employee=="1"){
        this.$router.push({name: 'EmployeeLogIn',query:{ username: this.username}});
      }else if(this.employee=="0"){
        this.$router.push({name: 'LogIn',query:{ username: this.username}});
      }
    }
  }
}
</script>

<style scoped>
.login-card{
  border-radius: 10px !important;
  border: none !important;
  background: rgba(0, 110, 117, 0.4);
}
</style>