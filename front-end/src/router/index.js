import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import Appointment from '../views/Appointment.vue'
import LogOut from '../views/LogOut.vue'
import Dashboard from '../views/Dashboard.vue'
import employeeLogIn from '../views/employeeLogIn.vue'
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
      toLogout: true
    },
  },
  {
    path: '/register',
    name: 'SignUp',
    component: SignUp,
    // lazy-loaded
    // component: () => import(/* webpackChunkName: "register" */ '../views/SignUp.vue')
    meta: {
      toLogout: true
    },
  },
  {
    path: '/appointment',
    name: 'Appointment',
    component: Appointment,
    meta: {
      requireAuth: true
    },
  },
  {
    path: '/logout',
    name: 'LogOut',
    component: LogOut,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    meta: {
      requireAuth: true
    },
  },
  {
    path: '/employee_login',
    name: 'employeeLogIn',
    component: employeeLogIn
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    let token = localStorage.getItem('t');
    let t = window.decodeURIComponent(window.atob(token));

    if (token == null) {
      next({
        name: 'LogIn',
        query: {
          message: "In order to complete this operation, you must log in",
          from: to.path
        }
      });
    } else {
      axios({
        method: 'post',
        url: "http://127.0.0.1:5000/verifyToken",
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          "Authorization": "bearer " + t
        },
        data: qs.stringify({
          token: token
        })
      })

        .then(function (response) {
          if (response.data.code == 200) {
            next();
          } else {
            next("/");
          }
        })

        .catch(function (error) {
          if (error.response) {
            if (error.response.status == 401) {
              localStorage.removeItem('t');
              next({
                name: 'LogIn',
                query: {
                  message: "Login status expired, please log in again",
                  from: to.path
                }
              });
            } else {
              console.log(error);
            }
          } else {
            console.log(error);
          }
        });
    }
  } else if (to.meta.toLogout) {
    let token = localStorage.getItem('t');
    if (token == null) {
      next();
    } else {
      next({
        name: 'LogOut',
        query: {
          from: to.path,
          to: from.path
        }
      });
    }
  } else {
    next();
  }
})

export default router
