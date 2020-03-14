<template>
  <div class="Appointment">
    <Header :hospital="hospital" ref="header"></Header>
    <div class="d-flex align-items-start flex-column content">

      <div class="p-4">
        <h4 class="text-left">Appointment Date</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(date,index) in dates" :key="index" :class="{checked:index==d}" @click="changeDate(index)">{{date.date}}, {{date.day}}</button>
        </div>
      </div>

      <div class="p-4">
        <h4 class="text-left">Pet Types</h4>
        <div>
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(pet,index) in pets" :key="index" :class="{checked:index==p}" @click="changePet(index)">{{pet}}</button>
        </div>
      </div>
      
      <div class="p-4">
        <h4 class="text-left">Location</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(city,index) in cities" :key="index" :class="{checked:index==c}" @click="changeCity(index)">{{city}}</button>
        </div>
      </div>

      <div class="p-4">
        <h4 class="text-left">Where do you think your pet is going wrong</h4>
        <div class="d-flex flex-wrap">
          <button class="btn btn-outline-info button-c p-2 m-2" v-for="(type,index) in types" :key="index" :class="{checked:index==t}" @click="changeType(index)">{{type}}</button>
        </div>
      </div>

      <div class="p-4" style="width: 80%">
        <h4 class="text-left">Leave a message</h4>
        <div class="d-flex">
          <textarea class="form-control flex-grow-1  p-2 m-2" rows="4" v-model="message" placeholder="Anything that you want to tell or remind the doctor, or any other symptoms of the pet"></textarea>
          <svg xmlns="http://www.w3.org/2000/svg" width="112" height="112" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="bg-info rounded-lg align-self-center ml-5 feather feather-arrow-right"><line x1="5" y1="12" x2="19" y2="12"></line><polyline points="12 5 19 12 12 19"></polyline></svg>
        </div>
      </div>

    </div>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>


<script>
import Header from "@/components/Header.vue";
import SideBar from "@/components/SideBar.vue";
import Footer from "@/components/Footer.vue";

export default {
  data() {
    return {
      dates: [],
      pets: ["Dog", "Cat"],
      cities: ["Beijing", "Shanghai", "Chengdu"],
      types: ["Surgery", "Internal medicine", "Ophthalmology", "Orthopedics", "Dermatology", "Obstetrics", "Others"],
      date: "",
      petType: "Dog",
      location: "Beijing",
      symptom: "Surgery",
      message: "",
      d: 0,
      p: 0,
      c: 0,
      t: 0
    };
  },

  components: {
    Header,
    SideBar,
    Footer
  },

  props: {
    hospital: String
  },

  created() {
    document.title = this.hospital;
  },

  mounted() {
    this.hilight();
    for(let i=0;i<7;i++){
      let dict={}
      dict["date"]=this.getDate(i);
      dict["day"]=this.getWeekDay(i);
      this.dates.push(dict);
    }
    this.date=this.getDate(0);
  },

  created() {
    document.title = `Appointment | ${this.hospital}`;
  },

  methods: {
    hilight() {
      let dom = this.$refs.header.$refs.appointment;
      $(dom).addClass("active");
    },

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
    }
  }
};
</script>

<style scoped>
.content{
  height: 87vh;
  max-height: 87vh;
  overflow-y: scroll;
}

.button-c{
  width: 150px;
}

.checked {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px #fff solid;
}

svg{
  transition: all 0.5s ease-in-out;
}

svg:hover{
  cursor: pointer;
  width: 140px;
}
</style>