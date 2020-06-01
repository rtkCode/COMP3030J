<template>
    <div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{$t("string.dashboard.EYI")}}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <div class="form p-3">
                        <div class="row">
                            <label for="fn">{{$t("string.user.firstname")}}</label>
                            <input type="text" class="form-control" id="fn" v-model="firstName" required>
                            <small class="invalid text-danger">*2-10 letters</small>
                        </div>

                        <div class="row mt-1">
                            <label for="ln">{{$t("string.user.lastname")}}</label>
                            <input type="text" class="form-control" id="ln" v-model="lastName" required>
                            <small class="invalid text-danger">*2-10 letters</small>
                        </div>

                        <div class="row mt-1">
                            <label for="ea">{{$t("string.user.email")}}</label>
                            <input type="email" class="form-control" id="ea" v-model="email"
                                @blur="verifyUserId('email')" required>
                            <small class="invalid text-danger">*Please input the correct email address</small>
                            <small class="error-text text-danger">{{emailErrorText}}</small>
                        </div>
                    </div>
                    <p class="text-left m-0"><a class="text-primary cursor-pointer" type="button" data-target="#resetPasswordModal" data-toggle="modal" data-dismiss="modal">{{$t("string.password.rp")}}</a></p>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">{{$t("string.button.close")}}</button>
                    <button type="button" class="btn btn-primary" @click="verifyName()"
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
                firstName: "",
                lastName: "",
                email: "",
                emailErrorText: "",
                showButton: true,
            };
        },

        mounted() {
            $(".invalid").hide();
        },

        methods: {
            verifyName() {
                let nameReg = /^[A-Za-z]{2,10}$/;
                if (nameReg.test(this.firstName)) {
                    $(".invalid").eq(0).hide();
                    if (nameReg.test(this.lastName)) {
                        $(".invalid").eq(1).hide();
                        this.verifyEmail();
                    } else {
                        $(".invalid").eq(1).show();
                    }
                } else {
                    $(".invalid").eq(0).show();
                }
            },

            verifyEmail() {
                let emailReg = /^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$/;
                if (emailReg.test(this.email)) {
                    $(".invalid").eq(2).hide();
                    this.updateProfile()
                } else {
                    $(".invalid").eq(2).show();
                }
            },

            updateProfile() {
                let _this = this;
                this.showButton=false;
                this.$axios({
                        method: 'put',
                        url: this.$global.request("updateProfile"),
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded',
                            "Authorization": "bearer " + this.$token.getToken(1)
                        },
                        data: this.$qs.stringify({
                            firstName: this.firstName,
                            lastName: this.lastName,
                            email: this.email,
                            token: this.$token.getToken(0),
                        })
                    })
                    .then(function (response) {
                        _this.showButton=true;
                        $('.toast').toast('show');
                        if (response.data.code == 200) {
                            _this.$emit("messageFailure", false);
                            _this.$emit("hintTitle", "Update success");
                            _this.$emit("hintText", "Your information has been updated");
                            $("#exampleModal").modal('hide');
                            setTimeout("location.reload()",2000);
                        }
                        if (response.data.code == 400) {
                            _this.$emit("messageFailure", true);
                            _this.$emit("hintTitle", "Update failed");
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
            },

            verifyUserId(mode) {
                let data;
                let _this = this;

                if (mode == "username") {
                    data = this.$qs.stringify({
                        username: this.username
                    });
                } else if (mode == "email") {
                    data = this.$qs.stringify({
                        email: this.email
                    })
                }

                this.$axios({
                        method: 'post',
                        url: this.$global.request("verifyUserId"),
                        headers: {
                            'Content-Type': 'application/x-www-form-urlencoded'
                        },
                        data: data,
                    })
                    .then(function (response) {
                        if (response.data.code == 201) _this.usernameErrorText = "";
                        if (response.data.code == 202) _this.emailErrorText = "";
                        if (response.data.code == 401) _this.usernameErrorText = response.data.msg;
                        if (response.data.code == 402) _this.emailErrorText = response.data.msg;
                    })
                    .catch(function (error) {
                        console.log(error);
                    });
            },
        }
    }
</script>