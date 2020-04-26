<template>
  <div>
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <div class="content">

      <div class="dashboard-bg d-flex align-items-start flex-column p-4 shadow-lg">
        <h1 class="text-left text-white mt-auto mx-xl-4">{{$t("string.personal.ED")}}</h1>
        <div class="d-flex flex-wrap status-cards mx-xl-4">
          <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0 shadow">
            <span class="h2 m-0">{{allNum}}</span>
            <small>{{$t("string.dashboard.AA")}}</small>
          </div>
          <div class="d-flex justify-content-around flex-column card border-radius10 status-card p-3 mr-4 mb-4 border-0 shadow">
            <span class="h2 m-0 text-secondary">{{accNun}}</span>
            <small>{{$t("string.personal.accepted")}}</small>
          </div>
          <div class="d-flex justify-content-around flex-column card-hide card border-radius10 status-card p-3 mr-4 mb-4 border-0 shadow">
            <span class="h2 m-0 text-info">{{opeNum}}</span>
            <small>{{$t("string.personal.operating")}}</small>
          </div>
          <div class="d-flex justify-content-around flex-column card-hide card border-radius10 status-card p-3 border-0 shadow">
            <span class="h2 m-0 text-success">{{docNum}}</span>
            <small>{{$t("string.dashboard.DOC")}}</small>
          </div>
        </div>
      </div>

      <!-- placeholder -->
      <div class="mt-5 pt-5"></div>

      <div class="col-12 d-flex flex-wrap">
        <div class="col-lg-5 col-sm-12 shadow my-4 mx-lg-4 mx-sm-0 border-radius10">
          <h5 class="text-left mx-4 my-4 p-1">{{$t("string.personal.AP")}} ({{appointments_others.length}})</h5>
          <div v-for="(a,index) in appointments_others" :key="index">
            <div class="d-flex justify-content-around mx-2 my-3 p-2 rounded-lg" :class="{'bg-light-red': a.emergency}">
              <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-success':'']">{{a.status}}</span>
              <span>{{a.id}}</span><span class="hide-sm">{{a.type}}</span><span class="hide-sm">{{a.date}}</span>
              <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">{{$t("string.dashboard.details")}}</a>
              <div class="dropleft">
                <button class="btn btn-outline-info badge badge-info button-gradient p-1 dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">{{$t("string.dashboard.operation")}}</button>
                <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
                  <button class="dropdown-item" @click="updateOperationId(a.id)" data-toggle="modal" data-target="#modal3">{{$t("string.personal.COD")}}</button>
                  <button class="dropdown-item" @click="updateStatus(a.id, 'Operating')">{{$t("string.personal.DAO")}}</button>
                  <div class="dropdown-divider"></div>
                  <button class="dropdown-item text-success" @click="updateDischargeId(a.id)" data-toggle="modal" data-target="#modal3">{{$t("string.personal.CDD")}}</button>
                  <button class="dropdown-item text-success" @click="updateStatus(a.id, 'Discharged')">{{$t("string.personal.ETO")}}</button>
                  <div class="dropdown-divider"></div>
                  <button type="button" class="dropdown-item text-danger" @click="updateDeleteId(a.id)" data-toggle="modal" data-target="#modal2">
                    {{$t("string.personal.CTA")}}
                  </button>
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
                        <div class="bg-info rounded-lg py-1 px-2 my-4 text-left text-white bubble" :class="[!d.employee?'mr-auto':'ml-auto']">{{d.content}}</div>
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

        <div class="col-lg-5 col-sm-12 shadow my-4 mx-lg-4 mx-sm-0 border-radius10">
          <h5 class="text-left mx-4 my-4 p-1">{{$t("string.personal.CP")}} ({{appointments_completed.length}})</h5>
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

    <div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
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
    <div class="modal fade" id="modal3" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel">
      <div class="modal-dialog modal-dialog-centered" role="document">
        <div class="modal-content">
          <div class="modal-header">
              <h5 class="modal-title">Choose {{operationText}} date</h5>
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
              </button>
          </div>
          <div class="modal-body">
              <calendar
                ref="calendar1"
                :value="calendar1.value" 
                :begin="calendar1.begin" 
                :end="calendar1.end" 
                :weeks="calendar1.weeks" 
                :months="calendar1.months" 
                @select="calendar1.select"
                @selectMonth="calendar1.selectMonth"
                @selectYear="calendar1.selectYear">
            </calendar>
          </div>
          <div class="modal-footer">
              <button type="button" class="btn btn-secondary" data-dismiss="modal">{{$t("string.button.close")}}</button>
              <button type="button" class="btn btn-info" @click="updateDate()"
                  v-show="showButton">{{$t("string.button.confirm")}}</button>
              <button class="btn btn-info" type="button" v-show="!showButton" disabled>
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
import Message from '@/components/Message.vue';
import calendar from '@/components/Calender.vue';

export default {
  data() {
    return {
      appointments: [],
      appointments_completed: [],
      appointments_others: [],
      hintTitle: "",
      hintText: "",
      messageFailure: false,
      showButton: true,
      deleteId: -1,
      operationId: -1,
      operationDate: "",
      operationText: "operation",
      messageText: {},
      discussions: [],
      allNum: 0,
      accNun: 0,
      opeNum: 0,
      docNum: 0,

      calendar1:{
        value:[2017,7,20],
        weeks:['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        months:['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
        select(value){
            let month=value[1];
            if(value[1]<10) month="0"+value[1]
            let day=value[2];
            if(value[2]<10) day="0"+value[2]
            let d=new Date();
            d.$soodd(value[0]+"-"+month+"-"+day)
        },
        selectMonth(month,year){},
        selectYear(year){},
        timestamp:Date.now()
      },

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
    calendar
  },

  props: {
    hospital: String
  },

  created() {
    document.title = this.$t("string.personal.pPanel") + " | " + this.hospital;
  },

  mounted() {
    this.$global.resizeContent();
    this.getAppointments();
    this.calendar1.value=this.getToday();
    this.operationDate=this.getToday();
    let _this=this;
    Date.prototype.$soodd=function(date){
      _this.operationDate=date;
    }
  },

  methods: {
    getToday(){
      let day = new Date();
      day.setTime(day.getTime());
      let dayList=[];
      dayList.push(day.getFullYear());
      dayList.push(day.getMonth()+1);
      dayList.push(day.getDate());
      return dayList
    },

    updateDeleteId(id){
      this.deleteId=id;
    }, 

    updateOperationId(id){
      this.operationId=id;
      this.operationText="operation";
    }, 

    updateDischargeId(id){
      this.operationId=id;
      this.operationText="discharge";
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
        if(appointments[i].status=="Operating"){
          this.opeNum++;
        }else if(appointments[i].status=="Discharged"||appointments[i].status=="Completed"){
          this.docNum++;
        }

        if(appointments[i].status=="Completed"||appointments[i].status=="Canceled"){
          this.appointments_completed.push(appointments[i]);
        }else{
          this.accNun++;
          this.appointments_others.push(appointments[i]);
        }
      }
      this.allNum=appointments.length;
    },

    getAppointments() {
      let _this = this;
      this.showButton=false;

      this.$axios({
          method: 'get',
          url: this.$global.request("employeeAppointments"),
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
            _this.hintTitle=_this.$t("string.user.unknowError");
            _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
          }
        })
        .catch(function (error) {
          _this.showButton=true;
          console.log(error);
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
      this.showButton=false;
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
          _this.showButton=true;
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
            _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
          }
        })
        .catch(function (error) {
          _this.showButton=true;
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

    updateDate(){
      let _this = this;
      let data={}
      this.showButton=false;
      if(this.operationText=="operation"){
        data=this.$qs.stringify({
            id: this.operationId,
            token: this.$token.getToken(0),
            operationTime: this.operationDate
          })
      }else if(this.operationText=="discharge"){
        data=this.$qs.stringify({
            id: this.operationId,
            token: this.$token.getToken(0),
            dischargeDate: this.operationDate
          })
      }

      this.$axios({
          method: 'put',
          url: this.$global.request("updateAppointment"),
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            "Authorization": "bearer " + this.$token.getToken(1)
          },
          data: data
        })
        .then(function (response) {
          _this.showButton=true;
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
            _this.hintText=response.data.msg+_this.$t("string.user.unknowErrorHint");
          }
        })
        .catch(function (error) {
          _this.showButton=true;
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
.bubble{
  max-width: 70%; 
  width: fit-content;
}

.message-container{
  height: 300px; 
  overflow-y: scroll;
}

.info-card{
  max-height: 260px;
}

.status-card{
  min-width: 200px;
  max-width: 220px;
  height: 100px;
}

.status-cards{
  position: relative;
  top: 80px;
}

.dashboard-bg h1{
  position: relative;
  top: 60px;
}

.dashboard-bg{
  height: 300px;
  background: rgb(143,255,163);
  background: linear-gradient(146deg, rgba(143,255,163,1) 0%, rgba(14,92,173,1) 100%);
}

@media (max-width: 496px) {
  .card-hide{
    display: none !important;
  }
}
</style>