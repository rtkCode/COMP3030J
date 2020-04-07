<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-4 p-2 mx-5 d-flex justify-content-between">
        <h3>There are currently {{appointments.length}} appointments in the system.</h3>
        <router-link to="/employee/personal" type="button" class="btn btn-outline-info">Personal Panel</router-link>
      </div>
      <div class="col-12 row d-flex flex-wrap-reverse">
        <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
          <div v-for="(a,index) in appointments" :key="index">
            <div class="d-flex justify-content-around m-4 p-1 rounded-lg" :class="{'bg-light-red': a.emergency}">
              <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-danger':'']">{{a.status}}</span>
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
    </div>
    <Message :hintTitle="hintTitle" :hintText="hintText" :failure="messageFailure"></Message>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
  import HeaderIf from "@/components/HeaderIf.vue";
  import Footer from "@/components/Footer.vue";
  import Model from "@/components/UpdateProfileModel.vue";
  import Message from '@/components/Message.vue';

  export default {
    data() {
      return {
        url: "http://127.0.0.1:5000/allAppointments",
        updateUrl: "http://127.0.0.1:5000/updateAppointment",
        appointments: [],
        hintTitle: "",
        hintText: "",
        messageFailure: false
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
      document.title = `Dashboard | ${this.hospital}`;
    },

    mounted() {
      this.getAppointments();
    },

    methods: {
      getHintTitle(data){
        this.hintTitle=data;
      },

      getHintText(data){
        this.hintText=data;
      },

      getMessageFailure(data){
        this.messageFailure=data;
      },

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

      updateStatus(id){
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
              status: "Processing"
            })
          })
          .then(function (response) {
            console.log(response);
            if (response.data.code == 200) {
              $('.toast').toast('show');
              _this.messageFailure=false;
              _this.hintTitle="Handle success";
              _this.hintText="you can view this appointment in your personal panel";
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
      }
    }

  };
</script>