<template>
  <div id="app">
    <router-view :hospital="hospital"></router-view>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.router-link-exact-active{
  color: rgba(0,0,0,.9) !important;
}

td {
  text-align: left;
}

.bg-light-red{
  background: #ffc4c4;
}

.bg-light-light{
  background: #e1e5ea;
}

.invalid{
  color: #FF4136;
}

.input-div{
  min-width: 304px;
}

@media (max-width: 420px) {
  .hide-sm{
    display: none;
  }
}

.text-shadow{
  text-shadow:3px 2px 1px #212121;
}
</style>

<script>

export default {
  data(){
    return{
      hospital: this.$t("string.hospital.name"),
    }
  }
}
</script>
