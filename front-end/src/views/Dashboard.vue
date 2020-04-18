<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-4 p-2 mx-3 mx-sm-5">
        <h3>{{$t("string.dashboard.welcome")}} {{name}}{{$t("string.dashboard.youHave")}} <strong>{{appointments.length}}</strong> {{$t("string.dashboard.appointments")}}.</h3>
      </div>
      <div class="col-12 row d-flex flex-wrap-reverse">
        <div class="col-lg-8 col-md-12 col-sm-12 col-12 mx-2 p-0">
          <div v-for="(a,index) in appointments_others" :key="index">
            <div class="d-flex justify-content-around mx-2 my-3 p-2 rounded-lg" :class="{'bg-light-red': a.emergency}">
              <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-success':'']">{{a.status}}</span>
              <span>{{a.id}}</span><span class="hide-sm">{{a.type}}</span><span class="hide-sm">{{a.date}}</span>
              <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">{{$t("string.dashboard.details")}}</a>
              <div class="dropleft">
                  <button class="btn btn-outline-info badge badge-info p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{{$t("string.dashboard.operation")}}</button>
                  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                    <button class="dropdown-item text-success" @click="updateCancelId(a.id)" data-toggle="modal" data-target="#modal5">{{$t("string.dashboard.RYP")}}</button>
                    <button class="dropdown-item text-danger" @click="updateCancelId(a.id)" data-toggle="modal" data-target="#modal4">{{$t("string.dashboard.CTA")}}</button>
                  </div>
                </div>
            </div>
            <table class="table table-borderless card card-body collapse mx-3 mx-md-5 col-11" :id="'a'+index">
              <tbody>
                <tr>
                  <td>{{$t("string.dashboard.status")}}<span class="text-secondary">{{a.status}}</span></td>
                  <td>{{$t("string.dashboard.emergency")}}<span class="text-secondary">{{a.emergency}}</span></td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.appointmentDate")}}<span class="text-secondary">{{a.date}}</span></td>
                  <td>{{$t("string.dashboard.location")}}<span class="text-secondary">{{a.location}}</span></td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.symptom")}}<span class="text-secondary">{{a.symptom}}</span></td>
                  <td>{{$t("string.dashboard.type")}}<span class="text-secondary">{{a.type}}</span></td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.customerNote")}}<span class="text-secondary">{{a.message}}</span></td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.operationDate")}}<span class="text-secondary">{{a.operationTime}}</span></td>
                  <td>{{$t("string.dashboard.attendingDoctor")}}<span class="text-secondary">{{a.attendingDoctor}}</span></td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.dischargeDate")}}<span class="text-secondary">{{a.dischargeDate}}</span></td>
                </tr>
                
                <a class="text-left" data-toggle="collapse" :href="'#d'+a.id" role="button" aria-expanded="false" :aria-controls="'d'+a.id" @click="getDiscussion(a.id)">
                  <svg t="1587111515032" class="icon mb-1 mr-1" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2472" width="20" height="20"><path d="M808.533333 397.866667v-2.133334c0-157.866667-167.466667-286.933333-372.266666-286.933333S64 236.8 64 395.733333c0 88.533333 51.2 169.6 140.8 225.066667l24.533333 183.466667 152.533334-124.8c18.133333 2.133333 36.266667 3.2 54.4 3.2h2.133333c45.866667 72.533333 140.8 119.466667 246.4 119.466666h16l148.266667 112 11.733333-162.133333c62.933333-40.533333 98.133333-99.2 98.133333-163.2 1.066667-82.133333-57.6-154.666667-150.4-190.933333zM378.666667 635.733333l-9.6-1.066666-107.733334 88.533333-17.066666-129.066667-9.6-5.333333c-82.133333-46.933333-128-117.333333-128-193.066667 0-134.4 148.266667-244.266667 329.6-244.266666s329.6 109.866667 329.6 244.266666C765.866667 530.133333 617.6 640 436.266667 640c-19.2 0-38.4-2.133333-57.6-4.266667z m452.266666 85.333334l-9.6 5.333333-8.533333 105.6-98.133333-74.666667-7.466667 1.066667c-7.466667 0-14.933333 1.066667-21.333333 1.066667-81.066667 0-153.6-29.866667-196.266667-78.933334 160-18.133333 288-114.133333 314.666667-237.866666 69.333333 29.866667 113.066667 85.333333 113.066666 146.133333 0 51.2-32 99.2-86.4 132.266667z" p-id="2473" fill="#8a8a8a"></path><path d="M245.333333 317.866667h373.333334v42.666666H245.333333zM245.333333 434.133333h373.333334v42.666667H245.333333z" p-id="2474" fill="#8a8a8a"></path></svg>
                  {{$t("string.discussion.DWAD")}}
                </a>
                <div class="collapse pt-1" :id="'d'+a.id">
                  <div class="card card-body">
                    <div class="message-container" :id="'dm'+a.id">
                      <div v-for="(d,index) in discussions" :key="index">
                        <div class="small text-secondary">{{d.postTime}}</div>
                        <div class="bg-info rounded-lg py-1 px-2 my-4 text-left text-white bubble" :class="[d.employee?'mr-auto':'ml-auto']">{{d.content}}</div>
                      </div>
                    </div>
                    <hr/>
                    <div>
                      <textarea class="form-control border-0" rows="2" :placeholder="$t('string.discussion.IYMH')" v-model="messageText[a.id]"></textarea>
                      <div class="text-right pt-1"><button class="btn btn-outline-info rounded" @click="postDiscussion(a.id)">{{$t("string.button.send")}}</button></div>
                    </div>
                  </div>
                </div>
                
              </tbody>
            </table>
          </div>
        </div>
        <div class="col mx-4 px-0 px-sm-4">
          <div class="card card-body">
            <table class="table table-borderless">
              <tbody>
                <tr>
                  <td>
                    <h3>{{name}}</h3>
                  </td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.username")}}{{username}}</td>
                </tr>
                <tr>
                  <td>{{$t("string.dashboard.email")}}{{email}}</td>
                </tr>
                <tr>
                  <td><a class="text-info text-left" href="#exampleModal" data-toggle="modal">{{$t("string.dashboard.EYI")}}</a></td>
                  <Model @hintTitle="getHintTitle" @hintText="getHintText" @messageFailure="getMessageFailure"></Model>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="text-left p-2 mx-3 mx-sm-5">
        <a class="text-info" data-toggle="collapse" href="#completedAppointments" role="button" aria-expanded="false" aria-controls="completedAppointments">{{$t("string.dashboard.VCA")}}</a>
      </div>
      <div class="collapse" id="completedAppointments">
        <div class="col-12 row d-flex flex-wrap-reverse">
          <div class="col-lg-8 col-md-12 col-sm-12 col-12 mx-2 p-0">
            <div v-for="(a,index) in appointments_completed" :key="index">
              <div class="d-flex justify-content-around mx-2 my-3 p-2 rounded-lg" :class="{'bg-light-red': a.emergency}">
                <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-success':'']">{{a.status}}</span>
                <span>{{a.id}}</span><span class="hide-sm">{{a.type}}</span><span class="hide-sm">{{a.date}}</span>
                <a class="text-info" data-toggle="collapse" :href="'#a2'+index" role="button" aria-expanded="false" :aria-controls="index">{{$t("string.dashboard.details")}}</a>
                <div class="dropleft">
                    <button class="btn btn-outline-info badge badge-info p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" disabled>{{$t("string.dashboard.operation")}}</button>
                </div>
              </div>
              <table class="table table-borderless card card-body collapse mx-3 mx-md-5 col-11" :id="'a2'+index">
                <tbody>
                  <tr>
                    <td>{{$t("string.dashboard.status")}}<span class="text-secondary">{{a.status}}</span></td>
                    <td>{{$t("string.dashboard.emergency")}}<span class="text-secondary">{{a.emergency}}</span></td>
                  </tr>
                  <tr>
                    <td>{{$t("string.dashboard.appointmentDate")}}<span class="text-secondary">{{a.date}}</span></td>
                    <td>{{$t("string.dashboard.location")}}<span class="text-secondary">{{a.location}}</span></td>
                  </tr>
                  <tr>
                    <td>{{$t("string.dashboard.symptom")}}<span class="text-secondary">{{a.symptom}}</span></td>
                    <td>{{$t("string.dashboard.type")}}<span class="text-secondary">{{a.type}}</span></td>
                  </tr>
                  <tr>
                    <td>{{$t("string.dashboard.customerNote")}}<span class="text-secondary">{{a.message}}</span></td>
                  </tr>
                  <tr>
                    <td>{{$t("string.dashboard.operationDate")}}<span class="text-secondary">{{a.operationTime}}</span></td>
                    <td>{{$t("string.dashboard.attendingDoctor")}}<span class="text-secondary">{{a.attendingDoctor}}</span></td>
                  </tr>
                  <tr>
                    <td>{{$t("string.dashboard.dischargeDate")}}<span class="text-secondary">{{a.dischargeDate}}</span></td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="modal fade" id="modal4" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{$t("string.button.confirm")}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    {{$t("string.dashboard.CHint")}} 
                    <span class="badge badge-pill badge-secondary">Waiting</span> only
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">{{$t("string.button.close")}}</button>
                    <button type="button" class="btn btn-danger" @click="updateStatus(deleteId, 'Canceled')"
                        v-show="showButton">{{$t("string.button.confirm")}}</button>
                    <button class="btn btn-danger" type="button" v-show="!showButton" disabled>
                        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
                        {{$t("string.user.loading")}}
                    </button>
                </div>
            </div>
        </div>
    </div>
    <div class="modal fade" id="modal5" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{$t("string.button.confirm")}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    {{$t("string.dashboard.RHint")}} 
                    <span class="badge badge-pill badge-success">Discharged</span> only
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">{{$t("string.button.close")}}</button>
                    <button type="button" class="btn btn-success" @click="updateStatus(deleteId, 'Completed')"
                        v-show="showButton">{{$t("string.button.confirm")}}</button>
                    <button class="btn btn-success" type="button" v-show="!showButton" disabled>
                        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
                        {{$t("string.user.loading")}}
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
  import Model from "@/components/UpdateProfileModel.vue";
  import Message from '@/components/Message.vue'

  export default {
    data() {
      return {
        username: "",
        name: "",
        email: "",
        appointments: [],
        appointments_completed: [],
        appointments_others: [],
        hintTitle: "",
        hintText: "",
        messageFailure: false,
        showButton: true,
        deleteId: -1,
        messageText: {},
        discussions: [],
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
      document.title = this.$t("string.user.dashboard") + " | " + this.hospital;
    },

    mounted() {
      this.getProfile();
    },

    methods: {
      updateCancelId(id){
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

      getProfile() {
        let _this = this;

        this.$axios({
            method: 'get',
            url: this.$global.request("profile"),
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
              _this.username = response.data.data.basic.username;
              _this.email = response.data.data.basic.email;
              _this.name = response.data.data.basic.firstName + " " +response.data.data.basic.lastName;
              _this.appointments = response.data.data.appointments.reverse();
              _this.handleAppointments(_this.appointments);
            }
            if (response.data.code == 400) {
              $('.toast').toast('show');
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          })
          .catch(function (error) {
            if(!error.response==undefined){
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: 'LogIn',
                query: {
                  message: _this.$t("string.appointment.loginExpired"),
                  from: "/dashboard"
                }
              });
            } }else {
              $('.toast').toast('show');
              console.log(error);
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          });
      },

      updateStatus(id, status){
        let _this = this;

        this.$axios({
            method: 'put',
            url: this.$global.request("updateAppointment"),
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
            if(!error.response==undefined){
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: 'LogIn',
                query: {
                  message: _this.$t("string.appointment.loginExpired"),
                  from: "/dashboard"
                }
              });
            } }else {
              $('.toast').toast('show');
              console.log(error);
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          });
      },

      getDiscussion(discussionId) {
        let _this = this;
        this.discussion=[];

        this.$axios({
            method: 'get',
            url: this.$global.request("discussion/"+discussionId),
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              "Authorization": "bearer " + this.$token.getToken(1)
            }
          })
          .then(function (response) {
            console.log(response);
            if (response.data.code == 200) {
              _this.discussions=response.data.data.discussions;
            }
            if (response.data.code == 400) {
              $('.toast').toast('show');
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          })
          .catch(function (error) {
            if(!error.response==undefined){
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: 'LogIn',
                query: {
                  message: _this.$t("string.appointment.loginExpired"),
                  from: "/dashboard"
                }
              });
            } }else {
              $('.toast').toast('show');
              console.log(error);
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          });
      },

      postDiscussion(appointmentId) {
        let _this = this;

        this.$axios({
            method: 'post',
            url: this.$global.request("discussion"),
            headers: {
              'Content-Type': 'application/x-www-form-urlencoded',
              "Authorization": "bearer " + this.$token.getToken(1)
            },
            data: this.$qs.stringify({
              appointmentId: appointmentId,
              token: this.$token.getToken(0),
              content: this.messageText[appointmentId]
            })
          })
          .then(function (response) {
            _this.messageText[appointmentId]="";
            console.log(response);
            if (response.data.code == 200) {
              _this.getDiscussion(appointmentId);
            }
            if (response.data.code == 400) {
              $('.toast').toast('show');
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          })
          .catch(function (error) {
            if(!error.response==undefined){
            if (error.response.status == 401) {
              _this.$token.removeToken();
              _this.$router.push({
                name: 'LogIn',
                query: {
                  message: _this.$t("string.appointment.loginExpired"),
                  from: "/dashboard"
                }
              });
            } }else {
              $('.toast').toast('show');
              console.log(error);
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.user.unknowError");
              _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
            }
          });
      },
    }

  };
</script>

<style scoped>
.bubble{
  max-width: 70%; 
  width: fit-content;
}

.message-container{
  height: 300px; 
  overflow-y: scroll;
}
</style>