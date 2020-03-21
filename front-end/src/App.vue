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

.content{
    min-height: 87vh;
}
</style>

<script>

export default {
  data(){
    return{
      hospital: "Dog&Cat Hospital",
    }
  }
}
</script>
