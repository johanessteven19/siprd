<template>
  <div>
    <div style="position: fixed; top: 0;">
    <Navigation />
    </div>
    <v-container style="margin: auto; width: 60%; padding: 70px 0">
      <h1>Welcome, {{ userData.full_name }}</h1><br><br>
      <v-btn outlined class="blue--text" v-on:click="editUser"> Edit Akun </v-btn><br><br>
      <v-btn outlined class="blue--text" v-on:click="addKaril"> Submit Karil </v-btn><br><br>
      <v-btn outlined class="blue--text" v-on:click="editKaril"> Edit Karil </v-btn><br><br>
      <v-btn outlined class="red--text" v-on:click="logoutUser"> Logout </v-btn>
    </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Navigation from '../components/Navigation.vue';

// import Vuetify from "vuetify";

Vue.use(VueAxios, axios);

export default {
  name: 'Success',
  components: {
    Navigation,
  },
  data() {
    return {
      userData: '',
    };
  },
  methods: {
    logoutUser() {
      console.log('enter');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      this.$router.push('/');
    },
    editUser() {
      this.$router.push('/edit-account');
    },

    addKaril() {
      this.$router.push('/add-karil');
    },

    editKaril() {
      this.$router.push('/edit-karil');
    },
  },
  beforeMount() {
    if (localStorage.access) {
      console.log(localStorage.access);
      console.log(localStorage.refresh);
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.userData = res.data;
        }
      });
    } else {
      this.$router.push('/');
    }
  },
};
</script>
