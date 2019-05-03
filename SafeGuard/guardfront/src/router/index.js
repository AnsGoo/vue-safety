import Vue from 'vue'
import Router from 'vue-router'
import Content from '@/pages/common/Content'
import Login from '@/pages/common/Login'
import CommonBody from '@/pages/common/CommonBody'
import user from './models/user'
import cmdb from './models/cmdb'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/login',
      name: 'HelloWorld',
      component: Login
    },
    {
      path: '/',
      component: Content,
      children:[
        {
          path: 'user/',
          component: CommonBody,
          children:[
            ...user
          ]
        },
        {
          path: 'cmdb/',
          component: CommonBody,
          children:[
            ...cmdb
          ]
        },
      ]
    }
  ]
})
