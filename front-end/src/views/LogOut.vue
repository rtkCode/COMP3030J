<template>
  <div :style="bg">
    <HeaderIf :hospital="hospital" :transparent="true" ref="header"></HeaderIf>

    <div class="content d-flex justify-content-center align-items-center">
      <div class="confirm">
        <h2 class="text-white">{{$t("string.user.confirm")}}</h2>
        <hr />
        <h4 class="m-4 text-white">{{$t("string.user.logoutHint")}}</h4>
        <hr />
        <button class="btn btn-outline-danger rounded-pill mt-2 px-3" @click="logout" id="logout">{{$t("string.user.logout")}}</button>
        <button class="btn button-gradient text-white border-white rounded-pill mt-2 px-3" @click="cancel" id="cancel">{{$t("string.user.cancel")}}</button>
      </div>
    </div>

    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    HeaderIf,
    Footer
  },

  data(){
    return{
      bg: {
        backgroundImage: "url(" + require("../../public/img/index.jpeg") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center"
      },

      fromPath: this.$route.query.from,
      toPath: this.$route.query.to,
    }
  },

  props: {
    hospital: String
  },

  mounted() {
    this.$global.resizeContent();
  },

  created() {
    document.title = this.$t("string.user.logout") + " | " + this.hospital;
  },

  methods: {
    logout() {
      this.$token.removeToken();
      if(this.fromPath==undefined) this.fromPath="/";
      this.$router.push(this.fromPath);
    },

    cancel() {
      if(this.toPath==undefined) this.toPath="/";
      this.$router.push(this.toPath);
    }
  }
};
</script>

<style scoped>
h2 {
  color: #3ba2bd;
}

.confirm {
  /* border: 1px solid #d1d0d0; */
  padding: 40px;
  margin-left: 30px;
  margin-right: 30px;
  border-radius: 10px;
  border: none !important;
  background: rgba(0, 110, 117, 0.4);
}

#logout {
  margin-right: 30px;
}

#cancel {
  margin-left: 30px;
}
</style>
