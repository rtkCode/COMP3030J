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
</style>

<script>
import Header from '@/components/Header.vue'
import SideBar from '@/components/SideBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  data(){
    return{
      hospital: "Dog&Cat Hospital",
    }
  }
}
</script>
