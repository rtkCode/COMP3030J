<template>
    <div class="modal fade" id="resetPasswordModal" tabindex="-1" role="dialog" aria-labelledby="resetPasswordModalLabel" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{$t("string.password.rp")}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="form p-3">
                        <div class="row">
                            <label for="pp">{{$t("string.password.pp")}}</label>
                            <input type="password" class="form-control" id="pp" v-model="prePassword" required>
                        </div>

                        <div class="row mt-1">
                            <label for="np">{{$t("string.password.np")}}</label>
                            <input type="password" class="form-control" id="np" v-model="newPassword" required>
                        </div>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">{{$t("string.button.close")}}</button>
                    <button type="button" class="btn btn-primary" @click="updatePassword()"
                        v-show="showButton">{{$t("string.button.save")}}</button>
                    <button class="btn btn-primary" type="button" v-show="!showButton" disabled>
                        <span class="spinner-border spinner-border-sm mb-1" role="status" aria-hidden="true"></span>
                        {{$t("string.user.loading")}}
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
                prePassword: "",
                newPassword: "",
                showButton: true,
            };
        },

        methods: {
            updatePassword() {
                let _this = this;
                this.showButton=false;
                this.$axios({
                        method: 'put',
                        url: this.$global.request("changePassword"),
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                            "Authorization": "bearer " + this.$token.getToken(1)
                        },
                        data: this.$qs.stringify({
                            "prev_password": this.prePassword,
                            "new_password": this.newPassword,
                            token: this.$token.getToken(0),
                        })
                    })
                    .then(function (response) {
                        _this.showButton=true;
                        $('.toast').toast('show');
                        if (response.data.code == 200) {
                            _this.$emit("messageFailure", false);
                            _this.$emit("hintTitle", "Reset success");
                            _this.$emit("hintText", response.data.msg);
                            $("#resetPasswordModal").modal('hide');
                            setTimeout("console.log('Reset password successful')",2000);
                            _this.$token.removeToken();
                            _this.$router.push({
                                name: 'LogIn',
                                query: {
                                    message: _this.$t("string.appointment.loginExpired"),
                                    from: "/employee/personal"
                                }
                            });
                        }
                        if (response.data.code == 400) {
                            _this.$emit("messageFailure", true);
                            _this.$emit("hintTitle", "Reset failed");
                            _this.$emit("hintText", response.data.msg);
                        }
                    })
                    .catch(function (error) {
                        _this.showButton=true;
                        if(!error.response==undefined){
                        if (error.response.status == 401) {
                            localStorage.removeItem('t');
                            _this.$router.push({
                                name: 'LogIn',
                                query: {
                                    message: _this.$t("string.appointment.loginExpired"),
                                    from: "/dashboard"
                                }
                            });
                        } }else {
                            console.log(error);
                            _this.$emit("messageFailure", true);
                            _this.$emit("hintTitle", _this.$t("string.user.unknowError"));
                            _this.$emit("hintText", response.data.msg);
                        }
                    });
            }
        }
    }
</script>