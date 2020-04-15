import Vue from 'vue'
import App from './App.vue'
import router from './router'
import VueI18n from 'vue-i18n'

import '../public/css/bootstrap.min.css'
import '../public/css/bootstrap-font.css'

Vue.config.productionTip = false
Vue.use(VueI18n)


const i18n = new VueI18n({
  locale: 'en-US',
  messages: {
    'zh-CN': require('./lang/zh-CN'),
    'en-US': require('./lang/en-US')
  }
})


new Vue({
  router,
  i18n,
  render: h => h(App)
}).$mount('#app')
