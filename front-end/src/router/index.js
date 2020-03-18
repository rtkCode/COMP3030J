import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import Appointment from '../views/Appointment.vue'
import axios from 'axios'
import qs from 'qs';

axios.defaults.headers.post['Content-Type'] = 'Content-Type:application/x-www-form-urlencoded; charset=UTF-8'
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Index',
    component: Index
  },
  {
    path: '/login',
    name: 'LogIn',
    component: LogIn,
    // lazy-loaded
    // component: () => import(/* webpackChunkName: "login" */ '../views/LogIn.vue')
    meta: {
      requireAuth: true,
      elsePath: "logout"
    },
  },
  {
    path: '/register',
    name: 'SignUp',
    component: SignUp,
    // lazy-loaded
    // component: () => import(/* webpackChunkName: "register" */ '../views/SignUp.vue')
    meta: {
      requireAuth: true,
      elsePath: "logout"
    },
  },
  {
    path: '/appointment',
    name: 'Appointment',
    component: Appointment,
    meta: {
      requireAuth: true,
      elsePath: "login"
    },
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if(to.meta.requireAuth){
    let token=localStorage.getItem('t');
    let t=window.decodeURIComponent(window.atob(token));

    axios({
      method: 'post',
      url: "http://127.0.0.1:5000/verifyToken",
      headers:{
        'Content-Type': 'application/x-www-form-urlencoded',
        "Authorization": t
      },
      data: qs.stringify({
        token: token
      })
    })
    .then(function (response) {
      console.log(response);
      if(response.data.code==200){
        if(to.meta.elsePath=="logout"){
          next("/logout");
        }else{
          next();
        }
      }else if(response.data.code==400){
        localStorage.removeItem('t');
        if(to.meta.elsePath=="login"){
          next("/login");
        }else{
          next("/");
        }
      }
    })
    .catch(function (error) {
      console.log(error);
    });
  }else{
    next();
  }
})

export default router
