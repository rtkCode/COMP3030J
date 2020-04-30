<template>
  <div>
    <div class="notFound">
      <h2 class="text-white">
        <strong>404 not found !</strong>
      </h2>
      <hr />
      <h4
        class="m-4 text-white"
      >Sorry, the page not found. The link you followed probably broken or the page has been removed.</h4>
      <hr />
      <h4 class="m-4 text-white">
        You can try:
        <router-link class="m-4 text-white" to="/">return to home page</router-link>
      </h4>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    hospital: String
  },

  created() {
    document.title = "404NotFound" + " | " + this.hospital;
  }
};
</script>

<style scoped>
.notFound {
  padding: 40px;
  position: absolute;
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  border-radius: 10px;
  background: rgba(0, 110, 117, 0.4);
}
</style>


