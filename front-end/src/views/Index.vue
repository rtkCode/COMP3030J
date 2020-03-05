<template>
  <div class="Index">
    <Header></Header>
    <SideBar></SideBar>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import SideBar from '@/components/SideBar.vue'

export default {
  name: 'Index',
  components: {
    Header,
    SideBar
  },
  beforeCreate(){
    document.title = "Dog&Cat Hospital";
  }
}
</script>
