<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-4 p-2 ml-5">
        <h3>Select an appointment to contact with the attending doctor:</h3>
      </div>
      <div class="col-12 row d-flex flex-wrap-reverse">
        <div class="col-lg-8 col-md-12 col-sm-12 col ml-2">
          <div v-for="(a,index) in appointments" :key="index">
            <div
              class="d-flex justify-content-around m-4 p-1 rounded-lg"
              :class="{'bg-light-red': a.emergency}"
            >
              <span
                class="d-flex align-items-center badge badge-pill"
                :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-success':'']"
              >{{a.status}}</span>
              <span>{{a.id}}</span>
              <span>{{a.type}}</span>
              <span>{{a.date}}</span>
              <span>{{a.attendingDoctor}}</span>
              <a
                class="text-info"
                data-toggle="collapse"
                :href="'#a'+index"
                role="button"
                aria-expanded="false"
                :aria-controls="index"
              >Details</a>

              <div class="dropleft">
                <button
                  class="btn btn-outline-info badge p-1"
                  type="button"
                  id="dropdownMenuButton"
                  @click="getAppointmentId(a.id)"
                >Select</button>
              </div>
            </div>

            <table
              class="table table-borderless card card-body collapse mx-3 mx-md-5 col-11"
              :id="'a'+index"
            >
              <tbody>
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
        </div>
        <div class="col ml-4">
          <div class="card card-body">
            <table class="table table-borderless">
              <tbody>
                <tr>
                  <td>
                    <h3>{{name}}</h3>
                  </td>
                </tr>
                <tr>
                  <td>Username: {{username}}</td>
                </tr>
                <tr>
                  <td>Email: {{email}}</td>
                </tr>
                <tr>
                  <td>
                    <a
                      class="text-info text-left"
                      href="#exampleModal"
                      data-toggle="modal"
                    >Edit your information</a>
                  </td>
                  <Model
                    @hintTitle="getHintTitle"
                    @hintText="getHintText"
                    @messageFailure="getMessageFailure"
                  ></Model>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div id="selected" style="display:none">
        <div class="title text-left text-info mt-4 ml-5">
          <h3>
            You have selected No.
            <strong>{{appointmentId}}</strong> appointment.
          </h3>
        </div>
        <div class="col-12 row mt-4 p-2 ml-5">
          <div
            class="col-lg-8 col-md-12 col-sm-12 col"
            style="height:200px;overflow-y:auto;border:1px solid #d1d0d0;border-style:solid solid none solid;"
          >
            <div v-for="(i,index) in discussions" :key="index">
              <table class="table table-borderless p-1 col-12" style="table-layout:fixed;">
                <tr>
                  <td style="word-wrap:break-word;">
                    <h5 style="text-align:left">
                      <strong>{{username}}:</strong>
                    </h5>
                    <h4>{{i.content}}</h4>
                  </td>
                  <td>
                    <p style="text-align:right">--{{i.postTime}}</p>
                  </td>
                </tr>
              </table>
            </div>
          </div>

          <table class="table table-bordered col-8">
            <tr>
              <td>
                Please enter your message:
                <small class="invalid">*Please enter something</small>
                <div style="float:right">
                  <button class="btn btn-outline-info badge p-2" type="button" @click="send">Send</button>
                </div>
              </td>
            </tr>
            <tr>
              <td colspan="2">
                <textarea
                  rows="2"
                  cols="100"
                  id="message"
                  style="width: 100%; height: 100%; border-style:none;"
                ></textarea>
              </td>
            </tr>
          </table>
        </div>
      </div>
    </div>

    <Message :hintTitle="hintTitle" :hintText="hintText" :failure="messageFailure"></Message>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import HeaderIf from "@/components/HeaderIf.vue";
import Footer from "@/components/Footer.vue";
import Model from "@/components/UpdateProfileModel.vue";
import Message from "@/components/Message.vue";

export default {
  data() {
    return {
      url: "",
      appointmentId: 1,
      content: "",
      username: "",
      name: "",
      email: "",
      appointments: [],
      discussions: [],
      hintTitle: "",
      hintText: "",
      messageFailure: false,
      showButton: true
    };
  },

  components: {
    HeaderIf,
    Footer,
    Model,
    Message
  },

  props: {
    hospital: String
  },

  created() {
    document.title = `Discussion | ${this.hospital}`;
  },

  mounted() {
    this.getProfile();
    $(".invalid").hide();
  },

  methods: {
    getAppointmentId(id) {
      let selected = document.getElementById("selected");
      selected.style.display = "block";
      this.appointmentId = id;
      this.getDiscussion();
    },
    send() {
      let content = document.getElementById("message").value;
      if (content == "") {
        $(".invalid").show();
      } else {
        $(".invalid").hide();
        this.content = content;
        document.getElementById("message").value = "";
        this.sendMessage();
      }
    },
    sendMessage() {
      let _this = this;
      this.showButton = false;

      this.$axios({
        method: "post",
        url: this.$global.request("discussion"),
        headers: {
          "Content-Type": "application/x-www-form-urlencoded",
          Authorization: "bearer " + this.$token.getToken(1)
        },
        data: this.$qs.stringify({
          appointmentId: this.appointmentId,
          content: this.content,
          token: this.$token.getToken(0)
        })
      })
        .then(function(response) {
          _this.showButton = true;
          $(".toast").toast("show");
          if (response.data.code == 200) {
            _this.messageFailure = false;
            _this.hintTitle = response.data.msg;
            _this.hintText = "The doctor has received your message";
            setTimeout(_this.route, 2000);
          }
          if (response.data.code == 400) {
            _this.messageFailure = true;
            _this.hintTitle = "Failed to send message";
            _this.hintText =
              response.data.msg + ", please correct and resubmit";
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
            _this.hintTitle = "Failed to send message";
            _this.hintText = "unknown error, please check console log";
          }
        });
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

    handleDiscussions(discussions) {
      for (let i = 0; i < discussions.length; i++) {
        if (discussions[i].appointmentId == this.appointmentId) {
          this.discussions.push(discussions[i]);
        }
      }
      this.getDiscussion();
    },
    updateTheUrl() {
      this.url = this.$global.request("discussion") + "/" + this.appointmentId;
    },

    getProfile() {
      let _this = this;

      this.$axios({
        method: "get",
        url: this.$global.request("profile"),
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
            _this.email = response.data.data.basic.email;
            _this.name =
              response.data.data.basic.firstName +
              " " +
              response.data.data.basic.lastName;
            _this.appointments = response.data.data.appointments.reverse();
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
    },
    getDiscussion() {
      let _this = this;
      this.updateTheUrl();
      this.$axios({
        method: "get",
        url: this.url,
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
            _this.discussions = response.data.data.discussions;
            _this.handleDiscussions(_this.discussions);
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
