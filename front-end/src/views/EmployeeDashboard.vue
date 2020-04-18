<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-4 p-2 mx-5 d-flex justify-content-between">
        <h3>{{$t("string.discussion.TAC")}} <strong>{{appointments.length}}</strong> {{$t("string.discussion.AITS")}}</h3>
        <router-link to="/employee/personal" type="button" class="btn btn-outline-info d-flex justify-content-center align-items-center">{{$t("string.personal.pPanel")}}</router-link>
      </div>

      <div class="text-left mx-4 px-4">
        <svg t="1586605345946" class="icon ml-3 mb-1 mr-1" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="2269" xmlns:xlink="http://www.w3.org/1999/xlink" width="16" height="16"><defs></defs><path d="M923.363328 24.0128C915.376128 9.6256 902.627328 0 886.704128 0H38.832128C22.857728 0 10.160128 9.6256 3.760128 24.0128a39.424 39.424 0 0 0 6.3488 43.2128L309.782528 409.6v358.4a39.424 39.424 0 0 0 14.336 30.4128l74.9568 62.4128a36.096 36.096 0 0 0 28.672 7.9872 41.3696 41.3696 0 0 0 25.4976-14.4384 38.2464 38.2464 0 0 0 7.9872-28.7744 45.568 45.568 0 0 0-14.336-27.1872l-62.1568-51.2V393.6256a36.4032 36.4032 0 0 0-9.5744-25.6L123.260928 78.336h675.7888l-250.2144 288a43.52 43.52 0 0 0-9.5744 27.2384v590.336c0 22.4256 17.5104 40.0384 38.2464 40.0384 20.736 0 38.2464-17.6128 38.2464-39.9872V408.0128l299.6224-342.4256c11.1616-11.1616 12.8-28.7744 7.9872-41.5744z m-186.4704 431.9744c0 20.7872 15.9232 38.4 36.6592 39.9872h211.968c20.736 0 38.2464-17.5616 38.2464-39.936a38.656 38.656 0 0 0-11.1616-28.8256 45.7216 45.7216 0 0 0-28.672-11.2128h-210.432a40.0384 40.0384 0 0 0-36.608 39.9872z m247.04 377.6h-210.432c-22.272 0-38.1952 17.6128-38.1952 40.0384 0 22.3744 17.5104 39.936 38.2464 39.936h211.968c22.3232 0 38.2464-17.5616 38.2464-39.936a38.656 38.656 0 0 0-11.1616-28.8256 38.3488 38.3488 0 0 0-28.672-11.2128z m0-207.9744h-211.968c-22.3232 0-38.2464 17.6128-38.2464 39.9872 0 22.4256 17.5104 39.9872 38.2464 39.9872h211.968c22.3232 0 38.2464-17.6128 38.2464-39.9872a38.656 38.656 0 0 0-11.1616-28.8256 28.7744 28.7744 0 0 0-27.136-11.1616z" fill="#9cabb9" p-id="2270"></path></svg>
        <a class="text-secondary" data-toggle="collapse" href="#filterCollapse" aria-expanded="false" aria-controls="filterCollapse">{{$t("string.discussion.showFilter")}}</a>
      </div>

      <div class="mx-4 p-2 collapse" id="filterCollapse">
        <div class="px-4 py-2 mx-2">
          <h5 class="text-left ml-1">{{$t("string.discussion.status")}}</h5>
          <div class="d-flex flex-wrap">
            <button class="btn btn-outline-info button-c p-2 m-2" v-for="(sta,index) in status" :key="index" :class="{checked:index==s}" @click="changeStatus(index)">{{sta}}</button>
          </div>
        </div>

        <div class="px-4 py-2 mx-2">
          <h5 class="text-left ml-1">{{$t("string.discussion.pet")}}</h5>
          <div class="d-flex flex-wrap">
            <button class="btn btn-outline-info button-c p-2 m-2" v-for="(sta,index) in pets" :key="index" :class="{checked:index==p}" @click="changePet(index)">{{sta}}</button>
          </div>
        </div>

        <div class="px-4 py-2 mx-2">
          <h5 class="text-left ml-1">{{$t("string.discussion.location")}}</h5>
          <div class="d-flex flex-wrap">
            <button class="btn btn-outline-info button-c p-2 m-2" v-for="(sta,index) in locations" :key="index" :class="{checked:index==l}" @click="changeLocation(index)">{{sta}}</button>
          </div>
        </div>

        <div class="px-4 py-2 mx-2">
          <h5 class="text-left ml-1">{{$t("string.discussion.emergency")}}</h5>
          <div class="d-flex flex-wrap">
            <button class="btn btn-outline-info button-c p-2 m-2" v-for="(sta,index) in emergencys" :key="index" :class="{checked:index==e}" @click="changeEmergency(index)">{{sta}}</button>
          </div>
        </div>

        <div class="px-4 py-2 mx-2">
          <h5 class="text-left ml-1">{{$t("string.discussion.order")}}</h5>
          <div class="d-flex flex-wrap">
            <button class="btn btn-outline-info button-c p-2 m-2" v-for="(sta,index) in orders" :key="index" :class="{checked:index==o}" @click="changeOrder(index)">{{sta}}</button>
          </div>
        </div>

        <hr class="mx-4 px-1"/>

        <div class="px-4 py-2 mx-2">
          <div class="d-flex flex-wrap">
            <a class="btn btn-success button-c p-2 m-2" data-toggle="collapse" href="#filterCollapse" aria-expanded="false" aria-controls="filterCollapse" @click="getAppointments()">{{$t("string.button.confirm")}}</a>
            <a class="btn btn-outline-danger button-c p-2 m-2" data-toggle="collapse" href="#filterCollapse" aria-expanded="false" aria-controls="filterCollapse">{{$t("string.button.cancel")}}</a>
          </div>
        </div>
      </div>

      <div class="col-12 d-flex flex-wrap-reverse">
        <div class="col-lg-12 col-md-12 col-sm-12 col ml-2">
          <div v-for="(a,index) in appointments" :key="index">
            <div class="d-flex justify-content-around m-4 px-1 py-3 rounded-lg" :class="{'bg-light-red': a.emergency, 'bg-light-light': !a.emergency}">
              <span class="d-flex align-items-center badge badge-pill" :class="[a.status=='Waiting'?'badge-secondary':'', a.status=='Processing'?'badge-info':'', a.status=='Operating'?'badge-primary':'', a.status=='Discharged'?'badge-success':'', a.status=='Canceled'?'badge-danger':'', a.status=='Completed'?'badge-success':'']">{{a.status}}</span>
              <span>{{index+1}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
              <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">{{$t("string.dashboard.details")}}</a>
              <button class="btn btn-outline-info badge badge-info" @click="updateStatus(a.id)" :disabled="a.employeeId">{{$t("string.discussion.handle")}}</button>
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
        baseUrl: "",
        url: "",
        appointments: [],
        hintTitle: "",
        hintText: "",
        messageFailure: false,
        s: 0,
        selectedStatus: "all",
        status: ["all", "Waiting", "Processing", "Operating", "Discharged", "Completed", "Canceled"],
        p: 0,
        selectedPet: "all",
        pets: ["all", "Dog", "Cat"],
        o: 0,
        selectedOrder: "normal",
        orders: ["normal", "by date"],
        selectedEmergency: "all",
        emergencys: ["all", "true", "false"],
        e: 0,
        selectedLocation: "all",
        locations: ["all", "Shanghai", "Chengdu", "Beijing"],
        l: 0,
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
      this.baseUrl=this.$global.request("allAppointments");
      this.getAppointments();
    },

    methods: {
      updateTheUrl(){
        this.url=this.baseUrl+"/"+this.selectedStatus+"/"+this.selectedPet+"/"+this.selectedEmergency+"/"+this.selectedLocation+"/"+this.selectedOrder;
      },

      changeStatus(index) {
        this.s = index;
        this.selectedStatus=this.status[index];
      },

      changePet(index) {
        this.p = index;
        this.selectedPet=this.pets[index];
      },

      changeOrder(index) {
        this.o = index;
        this.selectedOrder=this.orders[index];
      },

      changeLocation(index) {
        this.l = index;
        this.selectedLocation=this.locations[index];
      },

      changeEmergency(index) {
        this.e = index;
        this.selectedEmergency=this.emergencys[index];
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

      getAppointments(){
        let _this = this;
        this.updateTheUrl();
        this.appointments=[];
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

      updateStatus(id){
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
              status: "Processing"
            })
          })
          .then(function (response) {
            console.log(response);
            if (response.data.code == 200) {
              $('.toast').toast('show');
              _this.messageFailure=false;
              _this.hintTitle=_this.$t("string.dashboard.handleSuccess");
              _this.hintText=_this.$t("string.dashboard.handleSuccessHint");
              _this.getAppointments();
            }
            if (response.data.code == 400) {
              $('.toast').toast('show');
              _this.messageFailure=true;
              _this.hintTitle=_this.$t("string.dashboard.handleFailed");
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
      }
    }

  };
</script>

<style scoped>
.button-c{
  width: 100px;
}

.checked {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px #fff solid;
}
</style>