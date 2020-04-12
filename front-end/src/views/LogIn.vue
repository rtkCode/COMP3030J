<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">
      <div class="alert alert-info alert-dismissible fade show" role="alert">{{alertMessage}}
        <button type="button" class="close" data-dismiss="alert" aria-label="Close">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <form class="needs-validation" novalidate>
        <div class="form">

          <div class="row">
            <label for="validationCustomUsername">Username</label>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroupPrepend">@</span>
              </div>
              <input type="text" v-model="username" class="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required />
            </div>
            <small class="invalid">*Username format invalid</small>
          </div>

          <div class="row mt-1">
            <label for="pw">Password</label>
            <input type="password" v-model="password" class="form-control" id="pw" required />
            <small class="invalid">*Password format invalid</small>
          </div>
        </div>
      </form>
      <button class="btn btn-outline-info mt-3 px-4" type="submit" @click="verifyUsername()" v-show="showButton">Log in</button>
      <button class="btn btn-outline-info mt-2 px-4" type="button" v-show="!showButton" disabled>
        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
        Loading...
      </button>
    </section>
    <Message :hintTitle="loginHintTitle" :hintText="loginHintText" :failure="messageFailure"></Message>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>



<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";
import Message from '@/components/Message.vue'

export default {
  data(){
    return{
      username: this.$route.query.username,
      password: "",
      showButton: true,
      loginHintText: "",
      loginHintTitle: "",
      fromPath: this.$route.query.from,
      alertMessage: this.$route.query.message,
      messageFailure: false,
    }
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
    if(this.alertMessage==undefined) $(".alert").alert('close');
  },

  created() {
    document.title = `Log In | ${this.hospital}`;
  },

  methods: {
    verifyUsername(){
      let usernameReg=/^[a-zA-Z]{1}([a-zA-Z0-9]|[_]){3,15}$/;
      if(usernameReg.test(this.username)){
        $(".invalid").eq(0).hide();
        this.verifyPassword();
      }else{
        $(".invalid").eq(0).show();
      }
    },

    verifyPassword(){
      let passwordReg=/^(\S){6,18}$/;
      if(passwordReg.test(this.password)){
        $(".invalid").eq(1).hide();
        this.login();
      }else{
        $(".invalid").eq(1).show();
      }
    },

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
          employee:  "0"
        })
      })
      .then(function (response) {
        _this.showButton=true;
        if(response.data.code==400){
          $('.toast').toast('show');
          _this.messageFailure=true;
          _this.loginHintTitle="Login failed";
          _this.loginHintText=response.data.msg+", please correct and resubmit";
        }else if(response.data.code==200){
          let token=response.data.token;
          _this.$token.storeToken(token);
          if(_this.fromPath==undefined){
              _this.$router.push("/");
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
        _this.loginHintTitle="Unknown error";
        _this.loginHintText="unknown error, please check console log";
      });
    },

  }

};
</script>


<style scoped>
.invalid{
  color: #FF4136;
}
</style> 