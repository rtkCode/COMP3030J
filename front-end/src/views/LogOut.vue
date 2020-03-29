<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>

    <div class="content d-flex justify-content-center align-items-center">
      <div class="confirm">
        <h2>Confirm</h2>
        <hr />
        <h4>You have already logged in, you need to log out before logging in as different user.</h4>
        <hr />
        <button class="btn btn-outline-info rounded-pill mt-2 px-4" @click="logout" id="logout">log out</button>
        <button class="btn btn-outline-info rounded-pill mt-2 px-4" @click="cancel" id="cancel">cancel</button>
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
      fromPath: this.$route.query.from,
      toPath: this.$route.query.to,
    }
  },

  props: {
    hospital: String
  },

  created() {
    document.title = `Log Out | ${this.hospital}`;
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
  border: 1px solid #d1d0d0;
  padding: 40px;
  margin-left: 30px;
  margin-right: 30px;
}

#logout {
  margin-right: 30px;
}

#cancel {
  margin-left: 30px;
}
</style>
