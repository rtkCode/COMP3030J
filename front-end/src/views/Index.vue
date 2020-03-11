<template>
  <div class="Index">
    <Header :hospital="hospital"></Header>
    <section class="content d-flex justify-content-center align-items-center">
      <div class="">
        <h1 class="seven24">7<small>x</small>24</h1>
        <h1>Take care of your pet in all aspects</h1>
        <button class="btn btn-outline-info rounded-pill p-3 mt-2">start appointment now</button>
      </div>
    </section>
    <Footer :hospital="hospital"></Footer>
  </div>
</template>

<script>
import Header from '@/components/Header.vue'
import SideBar from '@/components/SideBar.vue'
import Footer from '@/components/Footer.vue'

export default {
  name: 'Index',
  components: {
    Header,
    SideBar,
    Footer
  },
  props:{
    "hospital": String
  },
  created(){
    document.title = this.hospital;
  }
}
</script>

<style scoped>
.content{
  height: 90vh;
}
.seven24{
  font-size: 70px;
}
</style>
