<template>
  <div class="Index" :style="$global.bg1">
    <HeaderIf :hospital="hospital" :transparent="true"></HeaderIf>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide data-hash="index">
        <section class="content d-flex justify-content-center align-items-center text-white">
          <div class>
            <h1 class="seven24 text-shadow">7<small>x</small>24</h1>
            <h1 class="text-shadow">{{$t("string.hospital.AD")}}</h1>
            <router-link
              class="btn rounded-pill p-3 mt-2 button-gradient text-white border-light"
              to="/appointment">{{$t("string.hospital.SAN")}}</router-link>
          </div>
        </section>
      </swiper-slide>
      <swiper-slide data-hash="about">
        <section class="d-flex justify-content-center align-items-center">
          <About class="d-flex justify-content-center align-items-center"></About>
        </section>
      </swiper-slide>
      <div class="swiper-pagination" slot="pagination"></div>
    </swiper>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";
import { Swiper, SwiperSlide } from 'vue-awesome-swiper';
import 'swiper/css/swiper.css';
import About from "@/views/About.vue";

export default {
  name: "Index",
  data(){
    return{
      swiperOption: {
        direction: 'vertical',
        slidesPerView: 1,
        height: window.innerHeight,
        mousewheel: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        hashnav: true
      },
    }
  },

  components: {
    HeaderIf,
    Footer,
    Swiper,
    SwiperSlide,
    About
  },

  props: {
    hospital: String
  },

  created() {
    document.title = this.hospital;
  },

  mounted(){
    this.$global.resizeContent();
    document.querySelector(".swiper").style.height=this.$global.minHeight()+"px";
  },
};
</script>

<style scoped>
.seven24 {
  font-size: 70px;
}
</style>
