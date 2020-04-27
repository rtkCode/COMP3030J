<template>
    <div id="discussionModal" v-show="showModal" class="mx-2">
        <div class="modal-dialog shadow-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <div class="modal-title text-left">
                        <h5 class="p-0 m-0">Discussion <small>with <strong v-if="employee">Customer</strong><strong v-else>{{attendingDoctor}}</strong></small></h5>
                        <small class="text-secondary"><small>appointment id: {{discussionId}}</small></small>
                    </div>
                    <button type="button" class="close" @click="showModal=false">
                    <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="message-container">
                        <div v-for="(d,index) in discussions" :key="index">
                            <div class="small text-secondary">{{d.postTime}}</div>
                            <div v-if="employee" class="bg-info rounded-lg py-1 px-2 my-4 text-left text-white bubble" :class="[d.employee?'ml-auto':'mr-auto']">{{d.content}}</div>
                            <div v-else class="bg-info rounded-lg py-1 px-2 my-4 text-left text-white bubble" :class="[d.employee?'mr-auto':'ml-auto']">{{d.content}}</div>
                        </div>
                    </div>
                    <hr/>
                    <div>
                        <textarea class="form-control border-0" rows="2" :placeholder="$t('string.discussion.IYMH')" v-model="messageText[discussionId]"></textarea>
                        <div class="text-right pt-1"><button class="btn button-gradient border-white text-white rounded" @click="postDiscussion(discussionId)">{{$t("string.button.send")}}</button></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
#discussionModal{
    position: fixed;
    right: 0px;
    bottom: 0px;
    width: 350px;
}

.bubble{
    max-width: 70%; 
    width: fit-content;
}

.message-container{
    height: 300px; 
    overflow-y: scroll;
}
</style>


<script>
export default {
    data(){
        return{
            hintTitle: "",
            hintText: "",
            messageFailure: false,
            showButton: true,
            messageText: {},
            discussions: [],
        }
    },

    props: {
        discussionId: Number,
        showModal: Boolean,
        employee: Boolean,
        attendingDoctor: String,
    },

    mounted(){
        this.getDiscussion(this.discussionId);
    },

    methods: {
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
}
</script>