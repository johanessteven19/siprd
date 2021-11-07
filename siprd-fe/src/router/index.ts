import Vue from 'vue';
import VueRouter, { RouteConfig } from 'vue-router';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Ping from '../views/Ping.vue';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import AddAccount from '../views/AddAccount.vue';
import EditAccount from '../views/EditAccount.vue';
import Success from '../views/Success.vue';
import Dashboard from '../views/Dashboard.vue';
import RegisterSuccess from '../views/RegisterSuccess.vue';
import AccountList from '../views/AccountList.vue';
import AddKaril from '../views/AddKaril.vue';
import AssignReviewer from '../views/AssignReviewer.vue';

Vue.use(VueRouter);
Vue.use(VueAxios, axios);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Landing',
    redirect: 'Dashboard',
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue'),
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
  {
    path: '/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/register',
    name: 'Register',
    component: Register,
  },
  {
    path: '/add-account',
    name: 'AddAccount',
    component: AddAccount,
  },
  {
    path: '/edit-account',
    name: 'EditAccount',
    component: EditAccount,
  },
  {
    path: '/success',
    name: 'Success',
    component: Success,
  },
  {
    path: '/welcome',
    name: 'Welcome',
    component: RegisterSuccess,
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
  },
  {
    path: '/account-list',
    name: 'AccountList',
    component: AccountList,
  },
  {
    path: '/add-karil',
    name: 'AddKaril',
    component: AddKaril,
  },
  {
    path: "/assign-reviewer",
    name: "AssignReviewer",
    component: AssignReviewer,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

function isAuthenticated(): boolean {
  if (localStorage.access) {
    const config = {
      headers: {
        Authorization: `Bearer ${localStorage.access}`,
      },
    };
    Vue.axios
      .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/ping`, config)
      .then((res: { status: number; }) => {
        if (res.status === 401) {
          return false;
        }
        return true;
      }).catch(() => false);
  }
  return false;
}

router.beforeEach((to, from, next) => {
  if (to.name !== 'Login' && !isAuthenticated()) next({ name: 'Login' });
  else next();
});

export default router;
