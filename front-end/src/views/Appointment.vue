<template>
  <div class="Appointment">
    <Header :hospital="hospital" ref="header"></Header>
    <div class="d-flex align-items-start flex-column" style="height: 90vh">

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
      types: ["Surgery", "Internal medicine", "Ophthalmology", "Orthopedics", "Dermatology", "Obstetrics"],
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

.button-c{
  width: 150px;
}

.checked {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px #fff solid;
}
</style>