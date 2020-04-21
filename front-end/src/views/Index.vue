<template>
  <div class="Index" :style="bg">
    <HeaderIf :hospital="hospital" :transparent="true"></HeaderIf>
    <swiper class="swiper" :options="swiperOption">
      <swiper-slide>
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
      <swiper-slide>
        <section class="content"></section>
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

export default {
  name: "Index",
  data(){
    return{
      bg: {
        backgroundImage: "url(" + require("../../public/img/index.jpeg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "100% auto"
      },

      swiperOption: {
        direction: 'vertical',
        slidesPerView: 1,
        height: window.innerHeight,
        mousewheel: true,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      },
    }
  },

  components: {
    HeaderIf,
    Footer,
    Swiper,
    SwiperSlide
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

.button-gradient{
  background: linear-gradient(146deg, rgba(143,255,165,1) 1%, rgba(14,92,173,1) 100%);
  opacity: 0.8;
  transition: all 0.3s;
}

.button-gradient:hover{
  opacity: 1;
}
</style>
