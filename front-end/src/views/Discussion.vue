<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <h3 class="title text-left text-info mt-4 p-2 ml-5">Online message board</h3>
    <table id="discuss">
      <tr>
        <h5>Please enter your appointment ID number:</h5>
        <input
          type="text"
          name="id_number"
          id="id_number"
          oninput="value=value.replace(/[^\d]/g,'')"
        />
      </tr>
      <tr>
        <h5>Discuss with the attending doctor:</h5>
      </tr>
      <tr>
        <small class="invalid">*Please enter something</small>
      </tr>
    </table>
    <textarea rows="3" cols="200" id="text"></textarea>
    <button
      class="btn btn-outline-info rounded-pill p-3 mt-5"
      @click="send()"
      v-show="showButton"
    >Send</button>
    <br />
    <br />
    <h5>Your appointments:</h5>
    <div v-for="(a,index) in appointments" :key="index">
      <table class="table table-borderless card card-body mx-3 mx-md-5 col-11" :id="'a'+index">
        <tbody>
          <tr>
            <td>
              Appointment ID:
              <span class="text-secondary">{{a.id}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Status:
              <span class="text-secondary">{{a.status}}</span>
            </td>
            <td>
              Emergency:
              <span class="text-secondary">{{a.emergency}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Appointment date:
              <span class="text-secondary">{{a.date}}</span>
            </td>
            <td>
              Location:
              <span class="text-secondary">{{a.location}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Syptom:
              <span class="text-secondary">{{a.symptom}}</span>
            </td>
            <td>
              Type:
              <span class="text-secondary">{{a.type}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Customer's Notes:
              <span class="text-secondary">{{a.message}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Operation date:
              <span class="text-secondary">{{a.operationTime}}</span>
            </td>
            <td>
              Attending doctor:
              <span class="text-secondary">{{a.attendingDoctor}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Discharge date:
              <span class="text-secondary">{{a.dischargeDate}}</span>
            </td>
          </tr>
          <tr>
            <td>
              Doctor's Notes:
              <span class="text-secondary">Undetermined</span>
            </td>
          </tr>
        </tbody>
      </table>
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
      profileUrl: "http://127.0.0.1:5000/profile",
      discussionUrl: "http://127.0.0.1:5000/discussion",
      content: "",
      post_time: "",
      employee: "",
      appointment_id: "",
      username: "",
      appointments: [],
      text: "",
      hintTitle: "",
      hintText: "",
      messageFailure: false,
      showButton: true
    };
  },
  components: {
    HeaderIf,
    Footer
  },
  created() {
    document.title = `Discussion | ${this.hospital}`;
  },

  mounted() {
    $(".invalid").hide();
    this.getProfile();
  },

  props: {
    hospital: String
  },
  methods: {
    nowDate() {
      var now = new Date();
      var year = now.getFullYear();
      var month = now.getMonth();
      var date = now.getDate();
      var day = now.getDay();
      var hour = now.getHours();
      var minu = now.getMinutes();
      var sec = now.getSeconds();
      month = month + 1;
      if (month < 10) month = "0" + month;
      if (date < 10) date = "0" + date;
      if (hour < 10) hour = "0" + hour;
      if (minu < 10) minu = "0" + minu;
      if (sec < 10) sec = "0" + sec;
      var time =
        year + "-" + month + "-" + date + " " + hour + ":" + minu + ":" + sec;
      return time;
    },
    getHintTitle(data) {
      this.hintTitle = data;
    },

    getHintText(data) {
      this.hintText = data;
    },

    getMessageFailure(data) {
      this.messageFailure = data;
    },

    handleAppointments(appointments) {
      for (let i = 0; i < appointments.length; i++) {
        this.status = appointments[i].status;
        this.emergency = appointments[i].emergency;
        this.date = appointments[i].date;
        this.location = appointments[i].location;
        this.symptom = appointments[i].symptom;
        this.type = appointments[i].type;
        this.message = appointments[i].message;
        this.operationTime = appointments[i].operationTime;
        this.attendingDoctor = appointments[i].attendingDoctor;
        this.dischargeDate = appointments[i].dischargeDate;
      }
    },
    send() {
      let text = document.getElementById("text").value;
      if (text == "") {
        $(".invalid").show();
      } else {
        $(".invalid").hide();
      }
      this.content = text;
      document.getElementById("text").value = "";
      let appointmentid = document.getElementById("id_number").value;
      this.appointment_id = appointmentid;
      let posttime = this.nowDate();
      this.post_time = posttime;
      console.log(this.appointment_id);
      let _this = this;
      this.showButton = false;
      this.$axios({
        method: "post",
        url: this.discussionUrl,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: "bearer " + this.$token.getToken(1)
        },
        data: this.$qs.stringify({
          appointment_id: this.appointment_id,
          content: this.content,
          post_time: this.post_time,
          employee: this.employee,
          token: this.$token.getToken(0)
        })
      })
        .then(function(response) {
          _this.showButton = true;
          $(".toast").toast("show");
          if (response.data.code == 200) {
            _this.messageFailure = false;
            _this.hintTitle = response.data.msg;
            _this.hintText = "The doctor has received your content";
            setTimeout(_this.route, 2000);
          }
          if (response.data.code == 400) {
            _this.messageFailure = true;
            _this.hintTitle = "Failed to make content";
            _this.hintText = response.data.msg + ", please correct and resend";
          }
        })
        .catch(function(error) {
          if (!error.response == undefined) {
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: "LogIn",
                query: {
                  message: "Login status expired, please log in again",
                  from: "/discussion"
                }
              });
            }
          } else {
            console.log(error);
            _this.showButton = true;
            _this.messageFailure = true;
            $(".toast").toast("show");
            _this.hintTitle = "Failed to make appointment";
            _this.hintText = "unknown error, please check console log";
          }
        });
    },
    getProfile() {
      let _this = this;
      this.$axios({
        method: "get",
        url: this.profileUrl,
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: "bearer " + this.$token.getToken(1)
        },
        data: this.$qs.stringify({
          token: this.$token.getToken(0)
        })
      })
        .then(function(response) {
          console.log(response);
          if (response.data.code == 200) {
            _this.username = response.data.data.basic.username;
            _this.appointments = response.data.data.appointments.reverse();
            _this.handleAppointments(_this.appointments);
          }
          if (response.data.code == 400) {
            $(".toast").toast("show");
            _this.messageFailure = true;
            _this.hintTitle = "Unknow error";
            _this.hintText = response.data.msg + ", please refresh the page";
          }
        })
        .catch(function(error) {
          if (!error.response == undefined) {
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: "LogIn",
                query: {
                  message: "Login status expired, please log in again",
                  from: "/discussion"
                }
              });
            }
          } else {
            $(".toast").toast("show");
            console.log(error);
            _this.messageFailure = true;
            _this.hintTitle = "Unknow error";
            _this.hintText = response.data.msg + ", please check console log";
          }
        });
    }
  }
};
</script>
<style scoped>
input {
  float: left;
  margin-left: 10px;
}
textarea {
  margin-left: 57px;
  margin-bottom: 10px;
  float: left;
}
h5 {
  margin-left: 57px;
  float: left;
}
#appointment_id {
  margin-left: 10px;
  float: left;
}
.invalid {
  color: #ff4136;
  float: left;
  margin-left: 57px;
  font-size: 20px;
}
</style>

