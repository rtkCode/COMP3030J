<template>
  <div class="Index" :style="bg">
    <HeaderIf :hospital="hospital" :transparent="true"></HeaderIf>
    <section class="content d-flex justify-content-center align-items-center text-white">
      <div class>
        <h1 class="seven24 text-shadow">7<small>x</small>24</h1>
        <h1 class="text-shadow">{{$t("string.hospital.AD")}}</h1>
        <button
          class="btn rounded-pill p-3 mt-2 button-gradient text-white border-light"
          @click="appointment">{{$t("string.hospital.SAN")}}</button>
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
        backgroundImage: "url(" + require("../../public/img/index.jpeg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "100% auto"
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


.button-gradient{
  background: linear-gradient(146deg, rgba(143,255,165,1) 1%, rgba(14,92,173,1) 100%);
  /* border: none; */
  opacity: 0.8;
  transition: all 0.3s;
}

.button-gradient:hover{
  opacity: 1;
}
</style>
