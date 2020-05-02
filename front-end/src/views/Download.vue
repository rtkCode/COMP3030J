<template>
  <div :style="$global.bg1">
    <HeaderIf :hospital="hospital" :transparent="true" ref="header"></HeaderIf>
    <section class="content d-flex flex-column justify-content-center align-items-center">
        <div class="login-card text-white text-left mx-2 p-4">
            <h4>{{$t("string.hospital.download")}}</h4>
            <p>We also provide Android version of the system, and you can download it through following links</p>
            <a href="https://drive.google.com/open?id=1BxixXFmf-PSvl1msH5YC5cnijI9KzpFk" class="text-light" target="_blank">Download link 1 (Google Drive)</a><br/>
            <a href="https://drive.google.com/drive/folders/19uIE4CM-IHq3fnBMqWa5fkMTWuFNMwGs?usp=sharing" class="text-light" target="_blank">Download link 2 (Google Drive)</a><br/>
            <a href="https://share.weiyun.com/5CYWaWm" class="text-light" target="_blank">Download link 3 (Tencent Weiyun)</a><br/>
            <a href="https://lanzous.com/b034uzzgj" class="text-light" target="_blank">Download link 4 (Lanzou Cloud)</a><br/>
        </div>
    </section>
    <Message :hintTitle="loginHintTitle" :hintText="loginHintText" :failure="messageFailure"></Message>
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
        document.title = this.$t("string.hospital.download") + " | " + this.hospital;
    },
}
</script>

<style scoped>
.login-card{
    border-radius: 10px !important;
    border: none !important;
    background: rgba(0, 110, 117, 0.4);
}
</style>