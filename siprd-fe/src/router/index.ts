import Vue from "vue";
import VueRouter, { RouteConfig } from "vue-router";
import Ping from "../views/Ping.vue";
import Login from "../views/Login.vue";
import Register from "../views/Register.vue";
import AddAccount from "../views/AddAccount.vue";
import EditAccount from "../views/EditAccount.vue";
import Success from "../views/Success.vue";
import Dashboard from "../views/Dashboard.vue";
import RegisterSuccess from "../views/RegisterSuccess.vue";
import AccountList from "../views/AccountList.vue";
import ForgetPasswordRequest from "../views/ForgetPasswordRequest.vue";
import ResetPassword from "../views/ResetPassword.vue";
import TokenError from "../views/TokenError.vue";

Vue.use(VueRouter);

const routes: Array<RouteConfig> = [
  {
    path: "/",
    redirect: (to) => {
      if(localStorage.access){
        return "/dashboard";
      } else{
        return "/login";
      }
      // TODO: check if user is logged in
      // If not, then
      //return "/login";
      // Else display their home screen
    },
    //name: "Dashboard",
    //component: Dashboard,
  },
  {
    path: "/about",
    name: "About",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/ping",
    name: "Ping",
    component: Ping,
  },
  {
    path: "/login",
    name: "Login",
    component: Login,
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
  {
    path: "/add-account",
    name: "AddAccount",
    component: AddAccount,
  },
  {
    path: "/edit-account",
    name: "EditAccount",
    component: EditAccount,
  },
  {
    path: "/success",
    name: "Success",
    component: Success,
  },
  {
    path: "/welcome",
    name: "Welcome",
    component: RegisterSuccess,
  },
  {
    path: "/forget",
    name: "Forget",
    component: ForgetPasswordRequest,
  },
  {
    path: "/token-error",
    name: "Token Error",
    component: TokenError,
  },
  {
    path: "/reset-password/:token/:username/:uidb",
    name: "Reset Password",
    component: ResetPassword,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
  },
  {
    path: "/account-list",
    name: "AccountList",
    component: AccountList,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
