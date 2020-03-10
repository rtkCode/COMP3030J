<template>
  <div>
    <Header :hospital="hospital" ref="header"></Header>
    <section class="content d-flex flex-column justify-content-center align-items-center">
      <form class="needs-validation" novalidate>
        <div class="form">
          <div class="row">
            <label for="fn">First name</label>
            <input type="text" class="form-control" id="fn" v-model="firstName" required>
            <small class="invalid">*2-10 letters</small>
          </div>

          <div class="row mt-1">
            <label for="ln">Last name</label>
            <input type="text" class="form-control" id="ln" v-model="lastName" required>
            <small class="invalid">*2-10 letters</small>
          </div>

          <div class="row mt-1">
            <label for="validationCustomUsername">Username</label>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroupPrepend">@</span>
              </div>
              <input type="text" class="form-control" v-model="username" @blur="verifyUserId()" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
            </div>
            <small class="invalid">*4-16 digits, letters, numbers, underscore</small>
          </div>

          <div class="row mt-1">
            <label for="ea">Email address</label>
            <input type="email" class="form-control" id="ea" v-model="email" @blur="verifyUserId()" required>
            <small class="invalid">*Please input the correct email address</small>
          </div>

          <div class="row mt-1">
            <label for="pw">Password</label>
            <input type="password" class="form-control" id="pw" v-model="password" required>
            <small class="invalid">*6-18</small>
          </div>
        </div>
        <small>*By clicking sign up, you agree to the terms and conditions</small>
      </form>

      <button class="btn btn-outline-info mt-2 px-4" type="submit" @click="verifyName()">Sign up</button>

    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>


<script>
import Header from '@/components/Header.vue'
import SideBar from '@/components/SideBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  data(){
    return{
      verifyUserIdUrl: "http://127.0.0.1:5000/verifyUserId",
      registerUrl: "https://jsonplaceholder.typicode.com/posts",
      firstName: "",
      lastName: "",
      username: "",
      email: "",
      password: ""
    }
  },

  props:{
    "hospital": String
  },

  components: {
    Header,
    SideBar,
    Footer
  },

  mounted(){
    $(".invalid").hide();
    this.hilight();
  },

  created(){
    document.title = `Sign up | ${this.hospital}`;
  },

  methods:{
    hilight(){
      let dom=this.$refs.header.$refs.register;
      $(dom).addClass("active");
    },

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
      this.$axios({
        method: 'post',
        url: this.registerUrl,
        data: {
          firstName: this.firstName,
          lastName: this.lastName,
          username: this.username,
          email: this.email,
          password: this.password,
          others: "test",
        }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    },

    verifyUserId(){
      this.$axios({
        method: 'post',
        url: this.verifyUserIdUrl,
        headers:{'Content-Type':'application/x-www-form-urlencoded'},
        data: this.$qs.stringify({
          username: this.username,
          email: this.email,
        })
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    },

  }
}
</script>

<style scoped>
.content{
  height: 90vh;
}
.invalid{
  color: #FF4136;
}
</style>