<template>
  <div
    class="d-flex align-center"
    v-bind:style="{ width: '100%', height: '100%' }"
  >
    <v-card
      flat
      v-bind:style="{ width: '50%', 'background-color': '#8D38E3' }"
      class="d-flex justify-center align-center"
      height="100%"
    >
      <v-img
        :src="require('@/assets/bunderan.svg')"
        class="bunderan"
        contain
        height="100%"
        width="50%"
      />
    </v-card>
    <v-card flat v-bind:style="{ width: '50%' }">
      <v-container style="margin: auto; width: 60%; padding: 150px 0">
        <h2>Masuk Dengan Akun Anda</h2>
        <v-form
          @submit.prevent="submitForm"
          ref="form"
          v-model="valid"
          lazy-validation
        >
          <v-text-field
            v-model="username"
            label="Username"
            :rules="usernameRules"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="Password"
            :type="'password'"
            :rules="passRules"
            required
          ></v-text-field>

          <div
            style="margin-top: 10px"
            v-if="password === '' || username === ''"
          >
            <v-btn
              class="mr-4"
              :disabled="true"
              type="submit"
              color="#8D38E3"
              width="100%"
            >
              masuk
            </v-btn>
          </div>
          <div v-else>
            <v-btn
              class="mr-4 white--text"
              :disabled="false"
              type="submit"
              color="#8D38E3"
              width="100%"
            >
              masuk
            </v-btn>
          </div>
        </v-form>
        <br />
        <v-dialog v-model="dialog" max-width="600px">
          <template v-slot:activator="{ on }">
            <v-btn
              class="mr-4 white--text"
              :disabled="false"
              color="#2D3748"
              width="100%"
              v-on="on"
            >
              <v-icon small> $custom </v-icon>
              <GoogleLogin
                :params="params"
                :onSuccess="onSuccess"
                :onFailure="onFailure"
              >
                &nbsp; Masuk dengan Google
              </GoogleLogin>
            </v-btn>
          </template>

          <v-card>
            <v-card-title class="text-justify"> Silahkan pilih akun </v-card-title>
            <v-layout column align-center justify-center>
              <div class="text-center" v-if="usernameList === undefined">
                <v-progress-circular
                  indeterminate
                  color="primary"
                ></v-progress-circular>
              </div>

              <div
                class="options"
                v-for="option in usernameList"
                :key="option"
                style="padding-bottom: 10px;"
              >
                <v-btn
                  @click.stop="
                    username = option;
                    dialog = false
                  "
                >
                  {{ option }}
                </v-btn>
              </div>
            </v-layout>

            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn color="primary" text @click="dialog = false">
                Tutup
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
        <p style="margin-top: 20px" class="register">
          Tidak memiliki akun? <span> <a href="/Register">Daftar</a></span>
        </p>
      </v-container>
    </v-card>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';

import { GoogleLogin } from 'vue-google-login';

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

export default {
  name: 'Login',
  components: {
    GoogleLogin,
  },
  // TODO: auto redirect to home page if already authenticated
  data() {
    return {
      errors: [],
      username: '',
      password: '',
      valid: true,
      usernameRules: [(v) => !!v || 'Username is required'],
      passRules: [(v) => !!v || 'Kata sandi tidak sesuai'],
      params: {
        client_id:
          '7984133184-8qrtflgutpulc7lsb5ml0amv8u58qdu3.apps.googleusercontent.com',
      },
      renderParams: {
        width: 460,
        height: 40,
        longtitle: true,
      },
      dialog: false,
      usernameList: undefined,
    };
  },
  methods: {
    submitForm() {
      if (!this.username) {
        this.errors.push('Username required.');
      }
      if (!this.password) {
        this.errors.push('Kata sandi tidak sesuai');
      }
      console.log(this.errors);
      if (this.errors.length) {
        let message = '';
        for (let i = 0; i < this.errors.length; i++) {
          message += `${this.errors[i]} `;
        }
        alert(message);
        return;
      }
      const data = {
        username: this.username,
        password: this.password,
      };
      Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/token/`, data).then((res) => {
        if (res.status === 200) {
          window.localStorage.setItem('refresh', res.data.refresh);
          window.localStorage.setItem('access', res.data.access);
          // alert("Login berhasil!");
          this.$router.push('/dashboard');
        } else {
          alert('Login gagal');
        }
      })
        .catch((err) => {
        // NOTE: Do not make this more specific, for security reasons.
          console.log(err.response);
          if (typeof err.response !== 'undefined') {
          // Backend accessible, but credentials incorrect
            alert('Login gagal! Username atau Password salah.');
          } else {
          // Backend inaccessible (no response)
            alert('Maaf, server SIPEERKI tidak dapat dihubungi.');
          }
        });
    },
    onSuccess(googleUser) {
      console.log(googleUser);
      // This only gets the user information: id, name, imageUrl and email
      const userProfile = googleUser.getBasicProfile();
      console.log(userProfile);
      const config = {
        params: {
          email: userProfile.getEmail(),
        },
      };
      // Get users linked to this Google account
      console.log(config);
      Vue.axios
        .get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-linked-users/`, config)
        .then((res) => {
          if (res.status === 200) {
            // usernames found
            this.usernameList = res.data.usernames;
            console.log(this.usernameList);
          } else if (res.status === 204) {
            // usernames not found
            alert(
              'Maaf, tidak ada akun yang terhubung dengan email tersebut. Apakah anda sudah daftar?',
            );
          }
        })
        .catch((err) => {
          // something went horribly wrong!
          console.log(err.response);
          alert('Maaf, server SIPEERKI tidak dapat dihubungi.');
        });
    },
    onFailure() {
      console.log('Google Login failed!');
    },
  },
};
</script>
