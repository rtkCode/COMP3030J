<template>
  <div class="Index">
    <HeaderIf :hospital="hospital"></HeaderIf>
    <section class="content d-flex justify-content-center align-items-center" :style="bg">
      <div class>
        <h1 class="seven24">7<small>x</small>24</h1>
        <h1>Take care of your pet in all aspects</h1>
        <button
          class="btn btn-outline-info rounded-pill p-3 mt-2"
          @click="appointment">start appointment now</button>
      </div>
    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";

export default {
  name: "Index",
  data(){
    return{
      bg: {
        // backgroundImage: "url(" + require("../../public/img/index.jpeg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "100% 100%" 
      },
    }
  },
  components: {
    HeaderIf,
    Footer
  },
  props: {
    hospital: String
  },
  created() {
    document.title = this.hospital;
  },
  methods: {
    appointment() {
      this.$router.push({ path: "/appointment" });
    }
  }
};
</script>

<style scoped>
.seven24 {
  font-size: 70px;
}
</style>
