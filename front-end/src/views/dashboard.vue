<template>
  <div>
    <HeaderIf :hospital="hospital"></HeaderIf>
    <div class="content">
      <div class="title text-left text-info mt-4 p-2 ml-5">
        <h3>Welcome {{username}}, you have {{appointments.length}} appointments.</h3>
      </div>
      <div class="col-12 row p-2">
        <div class="col-8">
          <div v-for="(a,index) in appointments" :key="index">
            <div class="d-flex justify-content-around m-4">
              <span class="d-flex align-items-center badge badge-pill badge-secondary">Waiting</span>
              <span>{{index+1}}</span><span>{{a.type}}</span><span>{{a.date}}</span>
              <a class="text-info" data-toggle="collapse" :href="'#a'+index" role="button" aria-expanded="false" :aria-controls="index">Details</a>
              <a class="text-info">Operations</a>
            </div>
            <table class="table table-borderless card card-body collapse ml-5 col-11" :id="'a'+index">
              <tbody>
                <tr>
                  <td>Appointment date: <span class="text-secondary">{{a.date}}</span></td>
                  <td>Location: <span class="text-secondary">{{a.location}}</span></td>
                </tr>
                <tr>
                  <td>Syptom: <span class="text-secondary">{{a.symptom}}</span></td>
                  <td>Type: <span class="text-secondary">{{a.type}}</span></td>
                </tr>
                <tr>
                  <td>Customer's Notes: <span class="text-secondary">Undetermined</span></td>
                </tr>
                <tr>
                  <td>Operation date: <span class="text-secondary">Undetermined</span></td>
                  <td>Attending doctor: <span class="text-secondary">Undetermined</span></td>
                </tr>
                <tr>
                  <td>Discharge date: <span class="text-secondary">Undetermined</span></td>
                </tr>
                <tr>
                  <td>Doctor's Notes: <span class="text-secondary">Undetermined</span></td>
                </tr>
              </tbody>
            </table>
          </div>
          <a href class="mt-2 text-info">View more appointments</a>
        </div>
        <div class="col">
          <div class="card card-body">
            <table class="table table-borderless">
              <tbody>
                <tr>
                  <td>
                    <h3>{{name}}</h3>
                  </td>
                </tr>
                <tr>
                  <td>Username: {{username}}</td>
                </tr>
                <tr>
                  <td>Email: {{email}}</td>
                </tr>
                <tr>
                  <td><a class="text-info text-left" href="#exampleModal" data-toggle="modal">Edit your information</a></td>
                  <Model @hintTitle="getHintTitle" @hintText="getHintText" @messageFailure="getMessageFailure"></Model>
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
  import Message from '@/components/Message.vue'

  export default {
    data() {
      return {
        profileUrl: "http://127.0.0.1:5000/profile",
        username: "",
        name: "",
        email: "",
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
      this.getProfile();
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

      getProfile() {
        let _this = this;

        this.$axios({
            method: 'post',
            url: this.profileUrl,
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
    }

  };
</script>

<style scoped>
  td {
    text-align: left;
  }
</style>