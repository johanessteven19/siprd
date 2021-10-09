<template>
  <v-container>
    <h1>Hello {{ userData.full_name }}</h1>
    <v-btn depressed color="error" v-on:click="logoutUser"> Logout </v-btn>
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
// import Vuetify from "vuetify";

Vue.use(VueAxios, axios);

export default {
  name: "Success",
  data() {
    return {
      userData: "",
    };
  },
  methods: {
    logoutUser() {
      console.log("enter");
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      this.$router.push("/");
    },
  },
  beforeMount() {
    if (localStorage.access) {
      console.log(localStorage.access);
      console.log(localStorage.refresh);
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: "Bearer " + accessToken },
      };
      Vue.axios.get(process.env.VUE_BACKEND_URL+"/api/user", config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.userData = res.data;
        }
      });
    } else {
      this.$router.push("/");
    }
  },
};
</script>
