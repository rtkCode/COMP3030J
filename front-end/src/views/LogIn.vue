<template>

  <div>

    <Header :hospital="hospital" ref="header"></Header>

    <section class="content d-flex justify-content-center align-items-center">

      <form class="needs-validation" novalidate>

        <div class="form">

          <div class="row mt-1">

            <label for="validationCustomUsername">Username</label>

            <div class="input-group">

              <div class="input-group-prepend">

                <span class="input-group-text" id="inputGroupPrepend">@</span>

              </div>

              <input

                type="text"

                class="form-control"

                id="validationCustomUsername"

                aria-describedby="inputGroupPrepend"

                required

              />

              <div class="invalid-feedback">Please enter your username.</div>

            </div>

          </div>

          <div class="row mt-1">

            <label for="pw">Password</label>



            <input type="password" class="form-control" id="pw" required />



            <div class="invalid-feedback">Please enter your password.</div>

          </div>

        </div>



        <br />



        <button class="btn btn-outline-info col-6" type="submit">Log In</button>

      </form>

    </section>



    <Footer :hospital="hospital"></Footer>

  </div>

</template>



<script>

import Header from "@/components/Header.vue";



import SideBar from "@/components/SideBar.vue";



import Footer from "@/components/Footer.vue";



export default {

  props: {

    hospital: String

  },



  components: {

    Header,



    SideBar,



    Footer

  },



  mounted() {

    this.hilight();



    this.verifyText();

  },



  created() {

    document.title = `Log In | ${this.hospital}`;

  },



  methods: {

    hilight() {

      let dom = this.$refs.header.$refs.login;



      $(dom).addClass("active");

    },



    verifyText() {

      "use strict";



      window.addEventListener(

        "load",



        function() {

          let forms = document.getElementsByClassName("needs-validation");



          let validation = Array.prototype.filter.call(forms, function(form) {

            form.addEventListener(

              "submit",



              function(event) {

                if (form.checkValidity() === false) {

                  event.preventDefault();



                  event.stopPropagation();

                }



                form.classList.add("was-validated");

              },



              false

            );

          });

        },



        false

      );

    }

  }

};

</script>





<style scoped>

.content {

  height: 90vh;

}

</style> 