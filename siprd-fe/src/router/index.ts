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
import EditKaril from '../views/EditKaril.vue';
import AssignReviewer from '../views/AssignReviewer.vue';
import KarilList from '../views/KarilList.vue';
import ViewKaril from '../views/ViewKaril.vue';

Vue.use(VueRouter);
Vue.use(VueAxios, axios);

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Landing',
    redirect: () => {
      if (localStorage.access) {
        return '/dashboard';
      }
      return '/login';
    },
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
    path: '/karil-list',
    name: 'KarilList',
    component: KarilList,
  },
  {
    path: '/view-karil',
    name: 'ViewKaril',
    component: ViewKaril,
  },
  {
    path: '/add-karil',
    name: 'AddKaril',
    component: AddKaril,
  },
  {
    path: '/edit-karil',
    name: 'EditKaril',
    component: EditKaril,
  },
  {
    path: '/assign-reviewer',
    name: 'AssignReviewer',
    component: AssignReviewer,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

// async function isAuthenticated(): Promise<boolean> {
//   let authenticated = false;
//   if (localStorage.access) {
//     const config = {
//       headers: {
//         Authorization: `Bearer ${localStorage.access}`,
//       },
//     };
//     await Vue.axios
//       .get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/ping`, config)
//       .then((res: { status: number; }) => {
//         if (res.status === 200) {
//           console.log('Authenticated!');
//           authenticated = true;
//         }
//       }).catch(() => false);
//   }
//   console.log(`Authenticated = ${authenticated}`);
//   return authenticated;
// }

// // No need to check authentication when redirecting from here
// const authExceptions = [
//   '/', '/login', '/register', '/welcome',
// ];
// router.beforeEach(async (to, from, next) => {
//   console.log(`Going from ${from.path}`);
//   console.log(`Going to ${to.name}`);
//   if (from.path !== null && from.path !== undefined && authExceptions.includes(from.path)) {
//     next();
//   } else if (to.name !== 'Login') {
//     const authenticated = await isAuthenticated();
//     if (authenticated) {
//       next();
//     } else {
//       next('/login');
//     }
//   } else next();
// });

export default router;
