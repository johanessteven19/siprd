<template>
  <v-container fill-height>
    <v-row>
      <v-layout column align-center justify-center>
        <div style="padding-left: 320px">
          <v-img
            :src="require('@/assets/asterisk.svg')"
            class="asterisk"
            contain
            height="48px"
            width="48px"
          />
        </div>
        <h1 class="text-center">Token Error</h1>
        <p class="text-center">
         Silahkan kembali lagi untuk mengulang proses mengatur ulang kata sandi.
        </p>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
            @click.stop="proceed()"
          >
            Kembali ke SIPEERKI
          </v-btn>
        </div>
      </v-layout>
    </v-row>
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
    return null;
  },
  methods: {
    proceed() {
      this.$router.push('/login');
    },
  },
};
</script>
