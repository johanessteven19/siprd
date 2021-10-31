<template>
  <v-container style="margin: auto; width: 60%; padding: 70px 0">
    <h1> Token error, silahkan lakukan reset password ulang </h1>
  </v-container>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
// import Vuetify from "vuetify";

Vue.use(VueAxios, axios);

export default {
  name: 'TokenError',
  data() {
    return { ping: '' };
  },
  method: {},
};
</script>
