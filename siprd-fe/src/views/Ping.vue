<template>
  <div class="ping">
    <h1>{{ ping }}</h1>
  </div>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
// import Vuetify from "vuetify";

Vue.use(VueAxios, axios);

export default {
  name: "Ping",
  data() {
    return { ping: "" };
  },
  method: {},
  beforeMount() {
    console.log("test");
    Vue.axios.get(process.env.VUE_BACKEND_URL+"/ping").then((res) => {
      this.ping = res.data;
      console.log(res);
    });
  },
};
</script>
