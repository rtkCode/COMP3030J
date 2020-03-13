<template>
  <div class="Appointment">
    <Header :hospital="hospital" ref="header"></Header>
    <div>
      <br />
      <h3>Appointment Date</h3>
      <ul>
        <li
          v-for="date,index of date"
          :key="item"
          :class="{checked:index==d}"
          @click="changeDate(index)"
        >{{date}}</li>
      </ul>
      <hr />
      <h3>Pet Types</h3>
      <ul>
        <li
          v-for="pet,index of pet"
          :key="item"
          :class="{checked:index==p}"
          @click="changePet(index)"
        >{{pet}}</li>
      </ul>
      <hr />
      <h3>Location</h3>
      <ul>
        <li
          v-for="city,index of city"
          :key="item"
          :class="{checked:index==c}"
          @click="changeCity(index)"
        >{{city}}</li>
      </ul>
      <hr />
      <h3>Where do you think your pet is going wrong</h3>
      <ul>
        <li
          v-for="type,index of type"
          :key="item"
          :class="{checked:index==t}"
          @click="changeType(index)"
        >{{type}}</li>
      </ul>
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
      nowDate: "",
      nowWeek: "",
      date: [],
      pet: ["Dog", "Cat"],
      city: ["Beijing", "Shanghai", "Chengdu"],
      type: ["Surgery", "Internal medicine", "Ophthalmology"],
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
    this.currentTime();
    this.date.push(this.getBeforeDate(0, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-1, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-2, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-3, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-4, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-5, this.currentTime()) + this.nowWeek);
    this.date.push(this.getBeforeDate(-6, this.currentTime()) + this.nowWeek);
  },
  created() {
    document.title = `Appointment | ${this.hospital}`;
  },
  methods: {
    hilight() {
      let dom = this.$refs.header.$refs.appointment;
      $(dom).addClass("active");
    },
    currentTime() {
      setInterval(this.getDate, 500);
    },
    getBeforeDate(num, time) {
      let n = num;
      let d = "";
      if (time) {
        d = new Date(time);
      } else {
        d = new Date();
      }
      let year = d.getFullYear();
      let mon = d.getMonth() + 1;
      let day = d.getDate();
      let week = d.getDay();
      if (day <= n) {
        if (mon > 1) {
          mon = mon - 1;
        } else {
          year = year - 1;
          mon = 12;
        }
      }
      d.setDate(d.getDate() - n);
      year = d.getFullYear();
      mon = d.getMonth() + 1;
      day = d.getDate();
      week = d.getDay();
      if (week == 1) {
        this.nowWeek = "Mon";
      } else if (week == 2) {
        this.nowWeek = "Tue";
      } else if (week == 3) {
        this.nowWeek = "Wed";
      } else if (week == 4) {
        this.nowWeek = "Thu";
      } else if (week == 5) {
        this.nowWeek = "Fri";
      } else if (week == 6) {
        this.nowWeek = "Sat";
      } else {
        this.nowWeek = "Sun";
      }
      let date =
        year +
        "-" +
        (mon < 10 ? "0" + mon : mon) +
        "-" +
        (day < 10 ? "0" + day : day) +
        " ";
      return date;
    },
    changePet(index) {
      this.p = index;
    },
    changeCity(index) {
      this.c = index;
    },
    changeDate(index) {
      this.d = index;
    },
    changeType(index) {
      this.t = index;
    }
  }
};
</script>

<style scoped>
.content  {
  height: 90vh;
}
.seven24  {
  font-size: 70px;
}
li {
  width: 150px;
  height: 50px;
  display: inline-block;
  border-radius: 30px;
  border: 1px #3ba2bd solid;
  text-align: center;
  line-height: 50px;
  cursor: pointer;
  margin-left: 8px;
  margin-bottom: 10px;
  color: #3ba2bd;
}
li:hover {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px#fff solid;
}

li.checked {
  background-color: #3ba2bd;
  color: #fff;
  border: 1px #fff solid;
}
</style>