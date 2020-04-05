<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <center>
      <table>
        <tbody>
          <tr>
            <td>Employee Name: {{username}}</td>
            <td>Id Number: {{id}}</td>
          </tr>
          <tr>
            <td>Gender: {{sex}}</td>
            <td>Job: {{job}}</td>
          </tr>
          <tr>
            <td>Age: {{age}}</td>
            <td>Salary: {{salary}}</td>
          </tr>
          <tr>
            <td colspan="2">Phone Number: {{phoneNumber}}</td>
          </tr>
          <tr>
            <td colspan="2">Accepted appointments ({{appointments.length}}):</td>
          </tr>
          <tr id="accepted">
            <td colspan="2">
              <p>{{appointments[i]}}</p>
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <center>
                <button class="btn btn-outline-info button-c p-2 m-2" @click="previous">&lt;</button>
                <button class="btn btn-outline-info button-c p-2 m-2" @click="next">&gt;</button>
              </center>
            </td>
          </tr>
          <tr>
            <td colspan="2">Completed appointments ({{completed_appointments.length}}):</td>
          </tr>
          <tr id="completed">
            <td colspan="2">
              <p>{{completed_appointments[n]}}</p>
            </td>
          </tr>
          <tr>
            <td colspan="2">
              <center>
                <button
                  class="btn btn-outline-info button-c p-2 m-2"
                  @click="completed_previous"
                >&lt;</button>
                <button class="btn btn-outline-info button-c p-2 m-2" @click="completed_next">&gt;</button>
              </center>
            </td>
          </tr>
        </tbody>
      </table>
    </center>

    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";

export default {
  data() {
    return {
      i: 0,
      n: 0,
      username: "",
      id: "",
      job: "",
      sex: "",
      salary: "",
      age: "",
      phoneNumber: "",
      appointments: ["1", "2", "3"],
      completed_appointments: ["4", "5", "6", "7"]
    };
  },
  components: {
    HeaderIf,
    Footer
  },

  props: {
    hospital: String
  },
  methods: {
    previous() {
      let a = this.i;
      if (a != 0) {
        a = a - 1;
        this.i = a;
      } else {
        this.i = this.appointments.length - 1;
      }
    },
    next() {
      let a = this.i;
      if (a != this.appointments.length - 1) {
        a = a + 1;
        this.i = a;
      } else {
        this.i = 0;
      }
    },
    completed_previous() {
      let b = this.n;
      if (b != 0) {
        b = b - 1;
        this.n = b;
      } else {
        this.n = this.completed_appointments.length - 1;
      }
    },
    completed_next() {
      let b = this.n;
      if (b != this.completed_appointments.length - 1) {
        b = b + 1;
        this.n = b;
      } else {
        this.n = 0;
      }
    }
  }
};
</script>
<style scoped>
h3 {
  margin: 15px;
}
table {
  width: 100%;
  margin-top: 15px;
  table-layout: fixed;
}
td {
  text-align: left;
  font-size: 20px;
  padding-left: 20px;
  padding-bottom: 10px;
}
button {
  width: 50px;
  margin-right: 50px;
}
#accepted {
  color: dimgrey;
}
#completed {
  color: dimgrey;
}
</style>
