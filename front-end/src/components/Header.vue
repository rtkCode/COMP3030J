<template>
  <header>
    <!-- navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm" :class="{'opacity07': transparent}">
      <!-- nav title -->
      <router-link class="navbar-brand" to="/">
        <svg
          t="1583465325680"
          class="icon mb-2"
          viewBox="0 0 1024 1024"
          version="1.1"
          xmlns="http://www.w3.org/2000/svg"
          p-id="5179"
          xmlns:xlink="http://www.w3.org/1999/xlink"
          width="24"
          height="24"
        >
          <defs />
          <path
            d="M992 192h-128l-14.32-28.62A64 64 0 0 0 792.44 128H685.2l-54.56-54.56C610.46 53.28 576 67.56 576 96.06v299.68l256 91.42V416h64c70.7 0 128-57.3 128-128v-64c0-17.68-14.32-32-32-32z m-224 96c-17.68 0-32-14.32-32-32s14.32-32 32-32 32 14.32 32 32-14.32 32-32 32zM192 448c-35.28 0-64-28.72-64-64 0-35.34-28.66-64-64-64S0 348.66 0 384c0 83.32 53.66 153.7 128 180.2V992c0 17.68 14.32 32 32 32h128c17.68 0 32-14.32 32-32V768h320v224c0 17.68 14.32 32 32 32h128c17.68 0 32-14.32 32-32V555.1L532.1 448H192z"
            p-id="5180"
            :fill="blackOrWhite"
          />
        </svg>
        <span class="hospital-name ml-1" :class="{'text-white': transparent}">{{hospital}}</span>
        <span class="hospital-name-sm ml-1" :class="{'text-white': transparent}"><small>{{hospital}}</small></span>
      </router-link>
      <!-- nav collapse button -->
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarSupportedContent"
        aria-controls="navbarSupportedContent"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- links -->
        <nav class="navbar-nav m-auto">
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/appointment" ref="appointment">{{$t("string.hospital.appointment")}}</router-link>
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/discussion">{{$t("string.hospital.discussion")}}</router-link>
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/#about">{{$t("string.hospital.about")}}</router-link>
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/download">{{$t("string.hospital.download")}}</router-link>
        </nav>
        <!-- login & register links -->
        <nav class="navbar-nav ml-auto">
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/login">{{$t("string.user.login")}}</router-link>
          <router-link class="nav-link" :class="{'link-text': transparent}" to="/register">{{$t("string.user.register")}}</router-link>
        </nav>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
  data(){
    return{
      blackOrWhite: this.transparent?"#ffffff":"#000000",
    }
  },

  props: {
    hospital: String,
    transparent: Boolean
  }
};
</script>

<style scoped>
.opacity07{
  background: rgba(0, 110, 117, 0.4) !important;
}

.link-text{
  color: rgba(255, 255, 255, 0.6) !important;
}

.link-text:hover{
  color: rgba(255, 255, 255, 0.8) !important;
}

.navbar-brand {
  margin-left: 16px;
}

.hospital-name-sm{
  display: none;
}

@media (max-width: 443px) {
  .hospital-name{
    display: none;
  }

  .hospital-name-sm{
    display: inline;
  }
}

@media (max-width: 384px) {
  .navbar-brand{
    margin-left: 3px;
    margin-right: 3px;
  }
}
</style>