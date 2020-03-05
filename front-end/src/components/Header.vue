<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-light bg-light shadow-sm rounded">
      <a class="navbar-brand ml-6" href="/">{{hospitalName}}</a>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ml-auto">
          <li class="nav-item">
            <a class="nav-link" href="/login">Log in</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/register">Sign up</a>
          </li>
        </ul>
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