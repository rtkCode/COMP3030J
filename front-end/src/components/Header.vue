<template>
  <header>
    <!-- navbar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm rounded">
      <!-- nav title -->
      <a class="navbar-brand" href="/">
        <svg t="1583465325680" class="icon mb-2" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="5179" xmlns:xlink="http://www.w3.org/1999/xlink" width="24" height="24"><defs></defs><path d="M992 192h-128l-14.32-28.62A64 64 0 0 0 792.44 128H685.2l-54.56-54.56C610.46 53.28 576 67.56 576 96.06v299.68l256 91.42V416h64c70.7 0 128-57.3 128-128v-64c0-17.68-14.32-32-32-32z m-224 96c-17.68 0-32-14.32-32-32s14.32-32 32-32 32 14.32 32 32-14.32 32-32 32zM192 448c-35.28 0-64-28.72-64-64 0-35.34-28.66-64-64-64S0 348.66 0 384c0 83.32 53.66 153.7 128 180.2V992c0 17.68 14.32 32 32 32h128c17.68 0 32-14.32 32-32V768h320v224c0 17.68 14.32 32 32 32h128c17.68 0 32-14.32 32-32V555.1L532.1 448H192z" p-id="5180"></path></svg>
        {{hospitalName}}
      </a>
      <!-- nav collapse button -->
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <!-- links -->
        <nav class="navbar-nav m-auto">
          <a class="nav-link" href="/">Appointment</a>
          <a class="nav-link" href="/">Announcement</a>
          <a class="nav-link" href="/">Discussion</a>
          <a class="nav-link" href="/">About</a>
        </nav>
        <!-- login & register links -->
        <nav class="navbar-nav ml-auto">
            <a class="nav-link" href="/login">Log in</a>
            <a class="nav-link" href="/register">Sign up</a>
        </nav>
      </div>
    </nav>
  </header>
</template>

<script>
export default {
    data(){
        return{
            hospitalName: "Dog&Cat Hospital"
        }
    }
};
</script>

<style scoped>
.navbar-brand{
  margin-left: 16px;
}
</style>