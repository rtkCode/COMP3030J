<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">
      <h1 class="mb-3">Employee login</h1>

      <div class="alert alert-info alert-dismissible fade show" role="alert">
        {{alertMessage}}
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
              <input type="text" v-model="username" class="form-control" id="validationCustomUsername"
                aria-describedby="inputGroupPrepend" required />
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
      <button class="btn btn-outline-info mt-3 px-4" type="submit" @click="verifyUsername()" v-show="showButton">Log
        in</button>
      <button class="btn btn-outline-info mt-2 px-4" type="button" v-show="!showButton" disabled>
        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
        Loading...
      </button>
    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>



<script>
  import HeaderIf from "@/components/HeaderIf.vue";
  import Footer from "@/components/Footer.vue";

  export default {
    data() {
      return {
        loginUrl: "http://127.0.0.1:5000/employee_login",
        username: "",
        password: "",
        showButton: true,
        loginHintText: "",
        loginHintTitle: "",
        fromPath: this.$route.query.from,
        alertMessage: this.$route.query.message
      };
    },

    props: {
      hospital: String
    },

    components: {
      HeaderIf,
      Footer
    },

    mounted() {
      $(".invalid").hide();
      if (this.alertMessage == undefined) $(".alert").alert("close");
    },

    created() {
      document.title = `Employee Login | ${this.hospital}`;
    },

    methods: {
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
  .invalid {
    color: #ff4136;
  }
</style>