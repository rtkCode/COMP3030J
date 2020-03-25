<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-2 p-2 ml-2"><h3>Welcome {{username}}, you have {{appointments.length}} appointments.</h3></div>
      <div class="col-12 row p-2">
        <div class="col-8">
          <table class="table table-borderless" v-for="(a,index) in appointments" :key="index">
            <tbody>
              <tr>
                <td>Appointment Date: {{a.date}}</td>
                <td>Location: {{a.location}}</td>
              </tr>
              <tr>
                <td>Syptom: {{a.symptom}}</td>
                <td>Operation Date: 2020-02-??</td>
              </tr>
              <tr>
                <td>Attending Doctor: Mr.XXXX</td>
                <td>Contact Number: XXXXXXXXX</td>
              </tr>
              <tr>
                <td>Operation progress: XXXXXXXX</td>
                <td>Release Date: XXXXXXXX</td>
              </tr>
              <tr>
                <td>Doctors' Notes: XXXXXX XXXXX XXX XXX xXXXXXx XXXX</td>
              </tr>
              <hr/>
            </tbody>
          </table>
        </div>
        <div class="col">
          <div class="card card-body">
            <table class="table table-borderless">
            <tbody>
              <tr>
                <td><h3>{{name}}</h3></td>
              </tr>
              <tr>
                <td>Username: {{username}}</td>
              </tr>
              <tr>
                <td>Email: {{email}}</td>
              </tr>
              <a class="nav-link text-left" href="#">Edit your information</a>
            </tbody>
          </table>
          </div>
        </div>
      </div>
      

    </div>

    <a href>View history appointments</a>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
  import HeaderIf from "@/components/HeaderIf.vue";
  import Footer from "@/components/Footer.vue";

  export default {
    data() {
      return {
        profileUrl: "http://127.0.0.1:5000/profile",
        username: "",
        name:"",
        email: "",
        appointments: []
      };
    },

    components: {
      HeaderIf,
      Footer
    },

    props: {
      hospital: String
    },

    created() {
      document.title = `Dashboard | ${this.hospital}`;
    },

    mounted() {
      this.getProfile();
    },

    methods: {
      getToken(n){
        let token=localStorage.getItem('t');
        let t=window.decodeURIComponent(window.atob(token));
        if(n==0) return token;
        if(n==1) return t;
      },

      getProfile(){
        let _this=this;
        
        this.$axios({
          method: 'post',
          url: this.profileUrl,
          headers: {
            'Content-Type':'application/x-www-form-urlencoded',
            "Authorization": "bearer "+this.getToken(1)
          },
          data: this.$qs.stringify({
            token: this.getToken(0),
          })
        })
        .then(function (response) {
          console.log(response);
          // $('.toast').toast('show');
          if(response.data.code==200){
            _this.username=response.data.data.basic.username;
            _this.email=response.data.data.basic.email;
            _this.name=response.data.data.basic.firstName+response.data.data.basic.lastName;
            _this.appointments=response.data.data.appointments;
            // $(".toast").removeClass("bg-danger border-danger");
            // $(".toast").addClass("bg-success border-success");
            // _this.hintTitle=response.data.msg;
            // _this.hintText="The doctor has received your appointment";

          }
          if(response.data.code==400){
            // $(".toast").removeClass("bg-success border-success");
            // $(".toast").addClass("bg-danger border-danger");
            // _this.hintTitle="Failed to make appointment";
            // _this.hintText=response.data.msg+", please correct and resubmit";
          }
        })
        .catch(function (error) {
          if(error.response.status==401){
            localStorage.removeItem('t');
            _this.$router.push({
              name: 'LogIn',
              query:{ 
                message: "Login status expired, please log in again",
                from: "/dashboard"
              }
            });
          }else{
            console.log(error);
            // $('.toast').toast('show');
            // $(".toast").addClass("bg-danger border-danger");
            // _this.hintTitle="Failed to make appointment";
            // _this.hintText="unknown error, please check console log";
          }
        });
      },
    }

  };
</script>

<style scoped>
  td {
    font-size: 18px;
    text-align: left;
  }
</style>