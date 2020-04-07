<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <div class="content">
      <div>
        <h5 class="text-left p-4">Accepted appointments ({{appointments_others.length}}):</h5>
        <div class="col-12 row d-flex flex-wrap-reverse">
          <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
            <div v-for="(a,index) in appointments_others" :key="index">
              <div class="d-flex justify-content-around m-4 p-1 rounded-lg" :class="{'bg-light-red': a.emergency}">
                <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'']">{{a.status}}</span>
                <span>{{a.id}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
                <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">Details</a>
                <div class="dropleft">
                  <button class="btn btn-outline-info badge badge-info p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">Operation</button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <button class="dropdown-item" @click="updateStatus(a.id, 'Operating')">Do an operation</button>
                    <button class="dropdown-item text-success" @click="updateStatus(a.id, 'Discharged')">End the operation</button>
                    <button type="button" class="dropdown-item text-danger" @click="updateDeleteId(a.id)" data-toggle="modal" data-target="#modal2">
                      Cancel the appointment
                    </button>
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
        <h5 class="text-left p-4">Completed appointments ({{appointments_completed.length}}):</h5>
        <div class="col-12 row d-flex flex-wrap-reverse">
          <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
            <div v-for="(a,index) in appointments_completed" :key="index">
              <div class="d-flex justify-content-around m-4 p-1 rounded-lg" :class="{'bg-light-red': a.emergency}">
                <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-danger':'']">{{a.status}}</span>
                <span>{{a.id}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
                <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">Details</a>
                <div class="dropleft">
                  <button class="btn btn-outline-info badge badge-info p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" disabled>Operation</button>
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
    </div>
    <div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Confirm</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    You are performing a dangerous operation. After canceling the order, the order will not be operated
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" @click="updateStatus(deleteId, 'Canceled')"
                        v-show="showButton">Confirm</button>
                    <button class="btn btn-danger" type="button" v-show="!showButton" disabled>
                        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
                        Loading...
                    </button>
                </div>
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
import Message from '@/components/Message.vue';

export default {
  data() {
    return {
      url: "http://127.0.0.1:5000/employeeAppointments",
      updateUrl: "http://127.0.0.1:5000/updateAppointment",
      appointments: [],
      appointments_completed: [],
      appointments_others: [],
      hintTitle: "",
      hintText: "",
      messageFailure: false,
      showButton: true,
      deleteId: -1,

      i: 0,
      n: 0,
      username: "",
      id: "",
      job: "",
      sex: "",
      salary: "",
      age: "",
      phoneNumber: "",
    };
  },
  components: {
    HeaderIf,
    Footer,
    Message,
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
    updateDeleteId(id){
      this.deleteId=id;
    }, 

    getHintTitle(data){
      this.hintTitle=data;
    },

    getHintText(data){
      this.hintText=data;
    },

    getMessageFailure(data){
      this.messageFailure=data;
    },

    handleAppointments(appointments){
      for(let i=0;i<appointments.length;i++){
        if(appointments[i].status=="Completed"||appointments[i].status=="Canceled"){
          this.appointments_completed.push(appointments[i]);
        }else{
          this.appointments_others.push(appointments[i]);
        }
      }
    },

    getAppointments() {
      let _this = this;
      this.showButton=false;

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
          _this.showButton=true;
          if (response.data.code == 200) {
            _this.appointments = response.data.data.appointments.reverse();
            _this.handleAppointments(_this.appointments);
          }
          if (response.data.code == 400) {
            $('.toast').toast('show');
            _this.messageFailure=true;
            _this.hintTitle="Unknow error";
            _this.hintText=response.data.msg+", please refresh the page";
          }
        })
        .catch(function (error) {
          _this.showButton=true;
          console.log(error);
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

    updateStatus(id, status){
      let _this = this;

      this.$axios({
          method: 'put',
          url: this.updateUrl,
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Authorization": "bearer " + this.$token.getToken(1)
          },
          data: this.$qs.stringify({
            id: id,
            token: this.$token.getToken(0),
            status: status
          })
        })
        .then(function (response) {
          if (response.data.code == 200) {
            $('.toast').toast('show');
            _this.messageFailure=false;
            _this.hintTitle="Success";
            _this.hintText="operation success";
            setTimeout("location.reload()",2000);
          }
          if (response.data.code == 400) {
            $('.toast').toast('show');
            _this.messageFailure=true;
            _this.hintTitle="Handle failed";
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