<template>
    <div class="modal fade" id="modal2" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Confirm</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    You are performing a dangerous operation. After canceling the order, the order will not be operated
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-danger" @click="cancelAppointment()"
                        v-show="showButton">Confirm</button>
                    <button class="btn btn-primary" type="button" v-show="!showButton" disabled>
                        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
                        Loading...
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                updateUrl: "http://127.0.0.1:5000/updateProfile",
                showButton: true,
            };
        },

        methods: {
            updateStatus(id){
                let _this = this;

                this.$axios({
                    method: 'put',
                    url: this.updateUrl,
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
    }
</script>