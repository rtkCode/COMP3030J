<template>
  <div :style="$global.bg1">
    <HeaderIf :hospital="hospital" :transparent="true" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">
      <div class="login-card text-white mx-2 p-4">
        <h2 class="text-white"><strong>404 not found!</strong></h2>
        <hr />
        <h4 class="m-4 text-white">Sorry, the page not found. The link you followed probably broken or the page has been removed.</h4>
        <hr />
        <h4 class="m-4 text-white">You can try:
          <router-link class="m-4 text-white" to="/">return to home page</router-link>
        </h4>
      </div>
    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";

export default {
  props: {
    hospital: String
  },

  components: {
    HeaderIf,
    Footer
  },

  mounted() {
    this.$global.resizeContent();
  },

  created() {
    document.title = "404 NotFound" + " | " + this.hospital;
  }
};
</script>

<style scoped>
.notFound {
  padding: 40px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
  background: rgba(0, 110, 117, 0.4);
}

.login-card{
    border-radius: 10px !important;
    border: none !important;
    background: rgba(0, 110, 117, 0.4);
}
</style>


