<template>
  <div class="Appointment" :style="bg">
    <HeaderIf :hospital="hospital" ref="header"></HeaderIf>
    <div class="d-flex align-items-start flex-column content">

      <div class="p-sm-4 p-3">
        <h4 class="text-left">{{$t("string.appointment.date")}}</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(date,index) in dates" :key="index" :class="{checked:index==d}" @click="changeDate(index)">{{date.date}}, {{date.day}}</button>
        </div>
      </div>

      <div class="p-sm-4 p-3">
        <h4 class="text-left">{{$t("string.appointment.type")}}</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(pet,index) in pets" :key="index" :class="{checked:index==p}" @click="changePet(index)">{{pet}}</button>
        </div>
      </div>
      
      <div class="p-sm-4 p-3">
        <h4 class="text-left">{{$t("string.appointment.location")}}</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(city,index) in cities" :key="index" :class="{checked:index==c}" @click="changeCity(index)">{{city}}</button>
        </div>
      </div>

      <div class="p-sm-4 p-3">
        <h4 class="text-left">{{$t("string.appointment.symptom")}}</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(type,index) in types" :key="index" :class="{checked:index==t}" @click="changeType(index)">{{type}}</button>
        </div>
      </div>

      <div class="p-sm-4 p-3">
        <h4 class="text-left">{{$t("string.appointment.emergency")}}</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(i,index) in emergency" :key="index" :class="[{checked:index==e}, [index==1?'btn-outline-danger':'']]" @click="changeEmergency(index)">{{i}}</button>
        </div>
      </div>

      <div class="p-sm-4 p-3" style="width: 100%">
        <h4 class="text-left">{{$t("string.appointment.message")}}</h4>
        <div class="d-flex flex-wrap">
          <textarea class="form-control flex-grow-1  p-2 m-2 mr-4" rows="4" v-model="message" :placeholder="$t('string.appointment.messageHint')"></textarea>
          <button @click="makeAppointment()" v-show="showButton" class="btn btn-info align-self-center ml-1 submit-arrow-lg">
            <svg xmlns="http://www.w3.org/2000/svg" width="112" height="112" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
          </button>

          <button class="btn btn-success button-c p-2 m-2 submit-arrow" @click="makeAppointment()" v-show="showButton">{{$t("string.button.submit")}}</button>
          <button class="btn btn-success button-c p-2 m-2 submit-arrow" v-show="!showButton">
            <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
            {{$t("string.user.loading")}}
          </button>

          <button class="btn btn-info align-self-center ml-1 submit-arrow-lg" v-show="!showButton" style="width: 205px; height: 126px;" disabled>
            <span class="spinner-border" style="width: 3rem; height: 3rem;" role="status" aria-hidden="true"></span>
          </button>

          <button class="btn btn-outline-danger button-c p-2 m-2 submit-arrow">{{$t("string.button.cancel")}}</button>

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
import Message from '@/components/Message.vue'

export default {
  data() {
    return {
      bg: {
        backgroundImage: "url(" + require("../../public/img/appointment.png") + ")",
        backgroundRepeat: "no-repeat",
        backgroundSize: "cover",
        backgroundPosition: "center",
        backgroundAttachment: "fixed",
      },

      dates: [],
      emergency: [false, true],
      pets: ["Dog", "Cat"],
      cities: ["Beijing", "Shanghai", "Chengdu"],
      types: ["Surgery", "Internal medicine", "Ophthalmology", "Orthopedics", "Dermatology", "Obstetrics", "Others"],
      date: "",
      petType: "Dog",
      location: "Beijing",
      symptom: "Surgery",
      isEmergency: false,
      message: "",
      d: 0,
      p: 0,
      c: 0,
      t: 0,
      e: 0,
      hintTitle: "",
      hintText: "",
      showButton: true,
      messageFailure: false
    };
  },

  components: {
    HeaderIf,
    Footer,
    Message
  },

  props: {
    hospital: String
  },

  mounted() {
    this.$global.resizeContent();
    for(let i=0;i<7;i++){
      let dict={}
      dict["date"]=this.getDate(i);
      dict["day"]=this.getWeekDay(i);
      this.dates.push(dict);
    }
    this.date=this.getDate(0);
  },

  created() {
    document.title = this.$t("string.hospital.appointment") + " | " + this.hospital;
  },

  methods: {
    getDate(d){
      let today=new Date();
      let day=new Date();
      day.setTime(today.getTime()+3600*1000*24*d);
      return day.getFullYear()+"-"+(day.getMonth()+1)+"-"+day.getDate();
    },

    getWeekDay(d){
      let today=new Date();
      let day=new Date();
      day.setTime(today.getTime()+3600*1000*24*d);
      let weekDay="Sun,Mon,Tue,Wed,Thu,Fri,Sat";
      return weekDay.split(",")[day.getDay()];
    },

    changeEmergency(index){
      this.e=index;
      this.isEmergency=this.emergency[index];
    },

    changePet(index) {
      this.p = index;
      this.petType=this.pets[index];
    },

    changeCity(index) {
      this.c = index;
      this.location=this.cities[index];
    },

    changeDate(index) {
      this.d = index;
      this.date=this.dates[index]["date"];
    },

    changeType(index) {
      this.t = index;
      this.symptom=this.types[index];
    },

    makeAppointment(){
      let _this=this;
      this.showButton=false;
      
      this.$axios({
        method: 'post',
        url: this.$global.request("appointment"),
        headers: {
          'Content-Type':'application/x-www-form-urlencoded',
          "Authorization": "bearer "+this.$token.getToken(1)
        },
        data: this.$qs.stringify({
          date: this.date,
          petType: this.petType,
          location: this.location,
          symptom: this.symptom,
          message: this.message,
          emergency: this.isEmergency,
          token: this.$token.getToken(0),
        })
      })
      .then(function (response) {
        _this.showButton=true;
        $('.toast').toast('show');
        if(response.data.code==200){
          _this.messageFailure=false;
          _this.hintTitle=response.data.msg;
          _this.hintText=_this.$t("string.appointment.appointmentSuccess");
          setTimeout(_this.route,2000);
        }
        if(response.data.code==400){
          _this.messageFailure=true;
          _this.hintTitle=_this.$t("string.appointment.appointmentFailed");
          _this.hintText=response.data.msg+_this.$t("string.user.loginFailedHint");
        }
      })
      .catch(function (error) {
        if(!error.response==undefined){
          if(error.response.status==401){
            _this.$token.removeToken();
            _this.$router.push({
              name: 'LogIn',
              query:{ 
                message: _this.$t("string.appointment.loginExpired"),
                from: "/appointment"
              }
            });
          }
        }else{
          console.log(error);
          _this.showButton=true;
          _this.messageFailure=true;
          $('.toast').toast('show');
          _this.hintTitle=_this.$t("string.appointment.appointmentFailed");
          _this.hintText=_this.$t("string.user.unknowErrorHint");
        }
      });
    },

    route(){
      this.$router.push("/dashboard");
    }

  }
};
</script>

<style scoped>
.button-c{
  width: 150px;
}

.checked {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px solid #17a2b8;
}

svg{
  transition: all 0.3s ease-in-out;
}

svg:hover{
  cursor: pointer;
  width: 130px;
}

textarea{
  min-width: 220px;
  max-width: 410px;
}

.submit-arrow{
  display: none;
}

@media (max-width: 633px) {
  .submit-arrow-lg{
    display: none;
  }
  .submit-arrow{
    display: block;
  }
}
</style>