<template>
  <div>
    <Header :hospital="hospital" ref="header"></Header>
    <section class="content d-flex flex-column justify-content-center align-items-center">
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
      <button class="btn btn-outline-info mt-3 px-4" type="submit" @click="verifyUsername()">Log in</button>
    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>



<script>
import Header from "@/components/Header.vue";
import SideBar from "@/components/SideBar.vue";
import Footer from "@/components/Footer.vue";

export default {
  data(){
    return{
      loginUrl: "https://jsonplaceholder.typicode.com/posts",
      username: "",
      password: ""
    }
  },

  props: {
    hospital: String
  },

  components: {
    Header,
    SideBar,
    Footer
  },

  mounted() {
    $(".invalid").hide();
    this.hilight();
  },

  created() {
    document.title = `Log In | ${this.hospital}`;
  },

  methods: {
    hilight() {
      let dom = this.$refs.header.$refs.login;
      $(dom).addClass("active");
    },

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
      console.log("ok");
      this.$axios({
        method: 'post',
        url: this.loginUrl,
        data: {
          username: this.username,
          password: this.password
        }
      })
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
    },

  }

};
</script>





<style scoped>
.content {
  height: 90vh;
}
.invalid{
  color: #FF4136;
}
</style> 