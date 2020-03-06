<template>
  <div>
    <Header :hospital="hospital" ref="header"></Header>
    <section class="content d-flex justify-content-center align-items-center">
      <form class="needs-validation" novalidate>
        <div class="form">

          <div class="row">
            <label for="fn">First name</label>
            <input type="text" class="form-control" id="fn" required>
            <div class="valid-feedback">Looks good!</div>
          </div>

          <div class="row mt-1">
            <label for="ln">Last name</label>
            <input type="text" class="form-control" id="ln" required>
            <div class="valid-feedback">Looks good!</div>
          </div>

          <div class="row mt-1">
            <label for="validationCustomUsername">Username</label>
            <div class="input-group">
              <div class="input-group-prepend">
                <span class="input-group-text" id="inputGroupPrepend">@</span>
              </div>
              <input type="text" class="form-control" id="validationCustomUsername" aria-describedby="inputGroupPrepend" required>
              <div class="invalid-feedback">Please choose a username.</div>
            </div>
          </div>

          <div class="row mt-1">
            <label for="ea">Email address</label>
            <input type="email" class="form-control" id="ea" required>
            <div class="valid-feedback">Looks good!</div>
          </div>

          <div class="row mt-1">
            <label for="pw">Password</label>
            <input type="password" class="form-control" id="pw" required>
            <div class="valid-feedback">Looks good!</div>
          </div>

        </div>
        
        <div class="form-group mt-2">
          <div class="form-check">
            <input class="form-check-input" type="checkbox" value="" id="invalidCheck" required>
            <label class="form-check-label" for="invalidCheck">Agree to terms and conditions</label>
            <div class="invalid-feedback">You must agree before submitting.</div>
          </div>
        </div>

        <button class="btn btn-outline-info col-6" type="submit">Sign up</button>
      </form>

    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>


<script>
import Header from '@/components/Header.vue'
import SideBar from '@/components/SideBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  props:{
    "hospital": String
  },
  components: {
    Header,
    SideBar,
    Footer
  },
  mounted(){
    this.hilight();
    this.verifyText();
  },
  created(){
    document.title = `Sign up | ${this.hospital}`;
  },
  methods:{
    hilight(){
      let dom=this.$refs.header.$refs.register;
      $(dom).addClass("active");
    },
    verifyText(){
      'use strict';
        window.addEventListener('load', function() {
          let forms = document.getElementsByClassName('needs-validation');
          let validation = Array.prototype.filter.call(forms, function(form) {
            form.addEventListener('submit', function(event) {
              if (form.checkValidity() === false) {
                event.preventDefault();
                event.stopPropagation();
              }
              form.classList.add('was-validated');
            }, false);
          });
        }, false);
    }
  }
}
</script>

<style scoped>
.content{
  height: 90vh;
}
</style>