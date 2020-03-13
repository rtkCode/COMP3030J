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
    // lazy-loaded
    component: LogIn
    // component: () => import(/* webpackChunkName: "login" */ '../views/LogIn.vue')
  },
  {
    path: '/register',
    name: 'SignUp',
    component: SignUp
    // lazy-loaded
    // component: () => import(/* webpackChunkName: "register" */ '../views/SignUp.vue')
  },
  {
    path: '/appointment',
    name: 'Appointment',
    component: Appointment
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
