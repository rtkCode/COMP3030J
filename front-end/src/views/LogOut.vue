<template>
  <div>
    <Header :hospital="hospital" ref="header"></Header>

    <div class="confirm">
      <h2>Confirm</h2>
      <hr />
      <h4>You have already logged in, you need to log out before logging in as different user.</h4>
      <hr />
      <button
        class="btn btn-outline-info rounded-pill mt-2 px-4"
        @click="logout"
        id="logout"
      >log out</button>
      <button class="btn btn-outline-info rounded-pill mt-2 px-4" @click="cancel" id="cancel">cancel</button>
    </div>

    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import Header from "@/components/Header.vue";
import SideBar from "@/components/SideBar.vue";
import Footer from "@/components/Footer.vue";

export default {
  components: {
    Header,
    SideBar,
    Footer
  },
  props: {
    hospital: String
  },
  created() {
    document.title = this.hospital;
  },
  methods: {
    logout() {
      this.$router.push({ path: "/login" });
    },
    cancel() {
      this.$router.push({ path: "/" });
    }
  }
};
</script>

<style scoped>
.content {
  height: 90vh;
}
.seven24 {
  font-size: 70px;
}
h2 {
  color: #3ba2bd;
}
.confirm {
  border: 1px solid #d1d0d0;
  padding: 30px;
  margin: 120px 300px 120px 300px;
}
#logout {
  margin-right: 30px;
}
#cancel {
  margin-left: 30px;
}
</style>
