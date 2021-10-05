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
        <h1 class="text-center">Selamat Datang!</h1>
        <p class="text-center">
          Anda akan dapat mengakses keseluruhan sistem setelah admin menyetujui
          akun Anda.
          <br />Sekarang, Anda dapat mengakses sistem sebagai Guest.
        </p>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
            @click.stop="proceed()"
          >
            Masuk ke SIPEERKI
          </v-btn>
        </div>
      </v-layout>
    </v-row>
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import Vuetify from "vuetify";

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

export default {
  name: "Success",
  data() {
    return null;
  },
  methods: {
    proceed() {
      this.$router.push("/");
    },
  },
};
</script>
