<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <div class="content">
      <div>
        <h5 class="text-left p-4">Accepted appointments ({{appointments.length}}):</h5>
        <div class="col-12 row d-flex flex-wrap-reverse">
          <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
            <div v-for="(a,index) in appointments" :key="index">
              <div class="d-flex justify-content-around m-4 p-1 rounded-lg" :class="{'bg-light-red': a.emergency}">
                <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'']">{{a.status}}</span>
                <span>{{a.id}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
                <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">Details</a>
                <div class="dropleft">
                  <button class="btn btn-outline-info badge badge-info p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Operation</button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <a class="dropdown-item" href="#">Do an operation</a>
                    <a class="dropdown-item text-success" href="#">End the operation</a>
                    <a class="dropdown-item text-danger" href="#">Cancel the appointment</a>
                  </div>
                </div>
              </div>
              <table class="table table-borderless card card-body collapse mx-3 mx-md-5 col-11" :id="'a'+index">
                <tbody>
                  <tr>
                    <td>Status: <span class="text-secondary">{{a.status}}</span></td>
                    <td>Emergency: <span class="text-secondary">{{a.emergency}}</span></td>
                  </tr>
                  <tr>
                    <td>Appointment date: <span class="text-secondary">{{a.date}}</span></td>
                    <td>Location: <span class="text-secondary">{{a.location}}</span></td>
                  </tr>
                  <tr>
                    <td>Syptom: <span class="text-secondary">{{a.symptom}}</span></td>
                    <td>Type: <span class="text-secondary">{{a.type}}</span></td>
                  </tr>
                  <tr>
                    <td>Customer's Notes: <span class="text-secondary">{{a.message}}</span></td>
                  </tr>
                  <tr>
                    <td>Operation date: <span class="text-secondary">{{a.operationTime}}</span></td>
                    <td>Attending doctor: <span class="text-secondary">{{a.attendingDoctor}}</span></td>
                  </tr>
                  <tr>
                    <td>Discharge date: <span class="text-secondary">{{a.dischargeDate}}</span></td>
                  </tr>
                  <tr>
                    <td>Doctor's Notes: <span class="text-secondary">Undetermined</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div>
          <button class="btn btn-outline-info button-c px-3 m-2" @click="previous">&lt;</button>
          <button class="btn btn-outline-info button-c px-3 m-2" @click="next">&gt;</button>
        </div>
      </div>
      <div>
        <h5 class="text-left p-4">Completed appointments ({{completed_appointments.length}}):</h5>
        <div class="col-12 row d-flex flex-wrap-reverse">
          <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
            <div v-for="(a,index) in appointments" :key="index">
              <div class="d-flex justify-content-around m-4 p-1 rounded-lg" :class="{'bg-light-red': a.emergency}">
                <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'']">{{a.status}}</span>
                <span>{{index+1}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
                <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">Details</a>
                <button class="btn btn-outline-info badge badge-info" @click="updateStatus(a.id)" :disabled="a.employeeId">Handle</button>
              </div>
              <table class="table table-borderless card card-body collapse mx-3 mx-md-5 col-11" :id="'a'+index">
                <tbody>
                  <tr>
                    <td>Status: <span class="text-secondary">{{a.status}}</span></td>
                    <td>Emergency: <span class="text-secondary">{{a.emergency}}</span></td>
                  </tr>
                  <tr>
                    <td>Appointment date: <span class="text-secondary">{{a.date}}</span></td>
                    <td>Location: <span class="text-secondary">{{a.location}}</span></td>
                  </tr>
                  <tr>
                    <td>Syptom: <span class="text-secondary">{{a.symptom}}</span></td>
                    <td>Type: <span class="text-secondary">{{a.type}}</span></td>
                  </tr>
                  <tr>
                    <td>Customer's Notes: <span class="text-secondary">{{a.message}}</span></td>
                  </tr>
                  <tr>
                    <td>Operation date: <span class="text-secondary">{{a.operationTime}}</span></td>
                    <td>Attending doctor: <span class="text-secondary">{{a.attendingDoctor}}</span></td>
                  </tr>
                  <tr>
                    <td>Discharge date: <span class="text-secondary">{{a.dischargeDate}}</span></td>
                  </tr>
                  <tr>
                    <td>Doctor's Notes: <span class="text-secondary">Undetermined</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
        <div>
          <button class="btn btn-outline-info button-c px-3 m-2" @click="previous">&lt;</button>
          <button class="btn btn-outline-info button-c px-3 m-2" @click="next">&gt;</button>
        </div>
      </div>
      <!-- <table>
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
      </!-->
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
      url: "http://127.0.0.1:5000/allAppointments",
      updateUrl: "http://127.0.0.1:5000/updateAppointment",
      appointments: [],
      hintTitle: "",
      hintText: "",
      messageFailure: false,

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

  created() {
    document.title = `Personal Panel | ${this.hospital}`;
  },

  mounted() {
    this.getAppointments();
  },

  methods: {
    getAppointments() {
      let _this = this;

      this.$axios({
          method: 'get',
          url: this.url,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Authorization": "bearer " + this.$token.getToken(1)
          },
          data: this.$qs.stringify({
            token: this.$token.getToken(0),
          })
        })
        .then(function (response) {
          console.log(response);
          if (response.data.code == 200) {
            _this.appointments = response.data.data.appointments.reverse();
          }
          if (response.data.code == 400) {
            $('.toast').toast('show');
            _this.messageFailure=true;
            _this.hintTitle="Unknow error";
            _this.hintText=response.data.msg+", please refresh the page";
          }
        })
        .catch(function (error) {
          if (error.response.status == 401) {
            _this.$token.removeToken();
            _this.$router.push({
              name: 'LogIn',
              query: {
                message: "Login status expired, please log in again",
                from: "/dashboard"
              }
            });
          } else {
            $('.toast').toast('show');
            console.log(error);
            _this.messageFailure=true;
            _this.hintTitle="Unknow error";
            _this.hintText=response.data.msg+", please check console log";
          }
        });
    },

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