<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div>
      <h2>Welcome {{username}}, you have x appointments at present.</h2>
      <hr />
    </div>
    <div id="information">
      <img src="../images/cat.png" />
      <table id="info">
        <tr>
          <td>Appointment Date:</td>
          <td>Location:</td>
        </tr>
        <tr>
          <td>Pathogeny:</td>
          <td>Operation Date:</td>
        </tr>
        <tr>
          <td>Attending Doctor:</td>
          <td>Contact Number:</td>
        </tr>
        <tr>
          <td>Operation progress:</td>
          <td>Release Date:</td>
        </tr>
      </table>
      <p>Doctors' Notes:</p>
      <div id="notes">
        <pre>......</pre>
      </div>
    </div>
    <hr />
    <div id="information">
      <img src="../images/dog.png" />
      <table id="info">
        <tr>
          <td>Appointment Date:</td>
          <td>Location:</td>
        </tr>
        <tr>
          <td>Pathogeny:</td>
          <td>Operation Date:</td>
        </tr>
        <tr>
          <td>Attending Doctor:</td>
          <td>Contact Number:</td>
        </tr>
        <tr>
          <td>Operation progress:</td>
          <td>Release Date:</td>
        </tr>
      </table>
      <p>Doctors' Notes:</p>
      <div id="notes">
        <pre>......</pre>
      </div>
      <hr />
      <a href>View history appointments</a>
    </div>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";

export default {
  data() {
    return {
      username: this.$route.query.username
    };
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
  }
};
</script>

<style scoped>
p {
  float: left;
  text-align: left;
  padding-left: 15px;
  width: 100%;
  font-size: 20px;
}
img {
  float: left;
  width: 12%;
  padding: 15px;
}
#info {
  float: left;
  width: 88%;
  margin-top: 10px;
}
td {
  font-size: 25px;
  text-align: left;
}
pre {
  float: center;
  text-align: left;
  width: 100%;
  font-size: 15px;
  height: 100px;
  white-space: pre-wrap;
  word-wrap: break-word;
  padding: 10px;
  border: solid 1px rgb(143, 143, 143);
}
#notes {
  padding: 15px 15px 0 15px;
}
a {
  float: left;
  text-align: left;
  width: 100%;
  padding-left: 15px;
}
h2 {
  margin-top: 10px;
  margin-left: 15px;
  text-align: left;
  color: #3ba2bd;
}
</style>
