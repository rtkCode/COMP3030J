<template>
  <div :style="$global.bg1">
    <HeaderIf :hospital="hospital" :transparent="true" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">

      <div class="login-card card px-4 py-5 shadow-lg">
        <div class="alert alert-info alert-dismissible fade show" role="alert">
          {{alertMessage}}
          <button type="button" class="close" data-dismiss="alert" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        
        <form class="needs-validation" novalidate>
          <div class="h3 mb-3 mr-4 text-left text-white">{{$t("string.user.employeeLogin")}}</div>
          <div class="form">
            <div class="input-div text-left">
              <label for="validationCustomUsername" class="text-white">{{$t("string.user.username")}}</label>
              <div class="input-group">
                <div class="input-group-prepend">
                  <span class="input-group-text text-white button-gradient" id="inputGroupPrepend">@</span>
                </div>
                <input type="text" v-model="username" class="form-control bg-white50" id="validationCustomUsername"
                  aria-describedby="inputGroupPrepend" required />
              </div>
              <small class="invalid">{{$t("string.user.usernameInvalid")}}</small>
            </div>

            <div class="input-div text-left mt-1">
              <label for="pw" class="text-white">{{$t("string.user.password")}}</label>
              <input type="password" v-model="password" class="form-control bg-white50" id="pw" required />
              <small class="invalid">{{$t("string.user.passwordInvalid")}}</small>
            </div>
          </div>
        </form>
        <div>
          <button class="btn button-gradient text-white rounded border-white mt-3 px-4" type="submit" @click="verifyUsername()" v-show="showButton">{{$t("string.user.login")}}</button>
          <button class="btn button-gradient text-white rounded border-white mt-3 px-4" type="button" v-show="!showButton" disabled>
            <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
            {{$t("string.user.loading")}}
          </button>
        </div>
      </div>
    </section>
    <Message :hintTitle="loginHintTitle" :hintText="loginHintText" :failure="messageFailure"></Message>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>



<script>
  import HeaderIf from "@/components/HeaderIf.vue";
  import Footer from "@/components/Footer.vue";
  import Message from '@/components/Message.vue';

  export default {
    data() {
      return {
        username: "",
        password: "",
        showButton: true,
        loginHintText: "",
        loginHintTitle: "",
        fromPath: this.$route.query.from,
        alertMessage: this.$route.query.message,
        messageFailure: false
      };
    },

    props: {
      hospital: String
    },

    components: {
      HeaderIf,
      Footer,
      Message
    },

    mounted() {
      $(".invalid").hide();
      this.$global.resizeContent();
      if (this.alertMessage == undefined) $(".alert").alert("close");
    },

    created() {
      document.title = this.$t("string.user.employeeLogin") + " | " + this.hospital;
    },

    methods: {
      login(){
        let _this=this;
        this.showButton=false;
        
        this.$axios({
          method: 'post',
          url: this.$global.request("login"),
          headers:{'Content-Type':'application/x-www-form-urlencoded'},
          data: this.$qs.stringify({
            username: this.username,
            password: this.password,
            employee:  "1"
          })
        })
        .then(function (response) {
          _this.showButton=true;
          if(response.data.code==400){
            $('.toast').toast('show');
            _this.messageFailure=true;
            _this.loginHintTitle=_this.$t("string.user.loginFailed");
            _this.loginHintText=response.data.msg+_this.$t("string.user.loginFailedHint");
          }else if(response.data.code==200){
            let token=response.data.token;
            _this.$token.storeEmployeeToken(token);
            if(_this.fromPath==undefined || _this.fromPath=="/"){
                _this.$router.push("/employee/dashboard");
            }else{
                _this.$router.push(_this.fromPath);
            }
          }
        })
        .catch(function (error) {
          console.log(error);
          _this.showButton=true;
          _this.messageFailure=true;
          $('.toast').toast('show');
          _this.loginHintTitle=_this.$t("string.user.unknowError");
          _this.loginHintText=_this.$t("string.user.unknowErrorHint");
        });
      },

      verifyUsername() {
        let usernameReg = /^[a-zA-Z]{1}([a-zA-Z0-9]|[_]){3,15}$/;
        if (usernameReg.test(this.username)) {
          $(".invalid")
            .eq(0)
            .hide();
          this.verifyPassword();
        } else {
          $(".invalid")
            .eq(0)
            .show();
        }
      },

      verifyPassword() {
        let passwordReg = /^(\S){6,18}$/;
        if (passwordReg.test(this.password)) {
          $(".invalid")
            .eq(1)
            .hide();
          this.login();
        } else {
          $(".invalid")
            .eq(1)
            .show();
        }
      }
    }
  };
</script>

<style scoped>
.login-card{
  border-radius: 10px !important;
  border: none !important;
  background: rgba(0, 110, 117, 0.4);
}
</style>