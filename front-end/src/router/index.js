import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import LogIn from '../views/LogIn.vue'
import SignUp from '../views/SignUp.vue'
import Appointment from '../views/Appointment.vue'
import LogOut from '../views/LogOut.vue'
import Dashboard from '../views/Dashboard.vue'
import EmployeeLogIn from '../views/EmployeeLogIn.vue'
import EmployeeDashboard from '../views/EmployeeDashboard.vue'
import EmployeePersonal from '../views/EmployeePersonal.vue'
import Discussion from '../views/Discussion.vue'
import axios from 'axios'
import qs from 'qs';
import token from '../token.js'
import global from "../global.js"

Vue.use(VueRouter)
axios.defaults.headers.post['Content-Type'] = 'Content-Type:application/x-www-form-urlencoded; charset=UTF-8'
Vue.prototype.$axios = axios
Vue.prototype.$qs = qs
Vue.prototype.$token = token
Vue.prototype.$global = global

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
      requireAuth: true,
      employee: true
    },
  },
  {
    path: '/employee/login',
    name: 'EmployeeLogIn',
    component: EmployeeLogIn,
    meta: {
      toLogout: true
    },
  },
  {
    path: '/employee/dashboard',
    name: 'EmployeeDashboard',
    component: EmployeeDashboard,
    meta: {
      requireAuth: true,
      // employee: true
    },
  },
  {
    path: '/employee/personal',
    name: 'EmployeePersonal',
    component: EmployeePersonal,
    meta: {
      requireAuth: true
    },
  },
  {
    path: '/discussion',
    name: 'Discussion',
    component: Discussion
  }
]

const router = new VueRouter({
  // mode: 'history',
  base: process.env.BASE_URL,
  routes
})

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (token == null) {
      next({
        name: 'LogIn',
        query: {
          message: "In order to complete this operation, you must log in",
          from: to.path
        }
      });
    } else {
      let _token = token;
      axios({
        method: 'post',
        url: global.request("verifyToken"),
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
          "Authorization": "bearer " + token.getToken(1)
        },
        data: qs.stringify({
          token: token.getToken(0)
        })
      })
        .then(function (response) {
          if (response.data.code == 200) {
            if (to.meta.employee) {
              if (_token.isEmployee() == "true") next("/employee/dashboard");
              else next();
            } else next();
          } else {
            next("/");
          }
        })
        .catch(function (error) {
          if (error.response) {
            if (error.response.status == 401) {
              if(_token.isEmployee()=="true"){
                token.removeToken();
                next({
                  name: 'EmployeeLogIn',
                  query: {
                    message: "Login status expired, please log in again",
                    from: to.path
                  }
                });
              }else if(_token.isEmployee()=="false"){
                token.removeToken();
                next({
                  name: 'LogIn',
                  query: {
                    message: "Login status expired, please log in again",
                    from: to.path
                  }
                });
              }
            } else {
              console.log(error);
            }
          } else {
            console.log(error);
          }
        });
    }
  } else if (to.meta.toLogout) {
    if (token.getToken(0) == null) {
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
