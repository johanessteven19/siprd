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
            label="username"
            :rules="usernameRules"
            required
          ></v-text-field>

          <v-text-field
            v-model="password"
            label="password"
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
            <v-card-text> Test </v-card-text>

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
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import Vuetify from "vuetify";

import { required, digits, email, max, regex } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import { GoogleLogin, LoaderPlugin } from "vue-google-login";

Vue.use(VueAxios, axios);
Vue.use(Vuetify);
Vue.use(LoaderPlugin, {
  client_id:
    "7984133184-8qrtflgutpulc7lsb5ml0amv8u58qdu3.apps.googleusercontent.com",
});

export default {
  name: "Login",
  components: {
    GoogleLogin,
  },
  beforeMount() {
    Vue.GoogleAuth.then((auth2) => {
      if (auth2.isSignedIn.get()) {
        // TODO: Display select user dialog
        console.log("Signed in via Google.");
      } else {
        console.log("Not signed in via Google");
      }
    });
    if (Vue.isLoggedIn("http://localhost:8000/api/token/refresh/")) {
      this.$router.push("/success");
    } else {
      console.log("No valid auth token found");
    }
  },
  data() {
    return {
      errors: [],
      username: "",
      password: "",
      valid: true,
      usernameRules: [(v) => !!v || "Username is required"],
      passRules: [(v) => !!v || "Kata sandi tidak sesuai"],
      params: {
        client_id:
          "7984133184-8qrtflgutpulc7lsb5ml0amv8u58qdu3.apps.googleusercontent.com",
      },
      renderParams: {
        width: 460,
        height: 40,
        longtitle: true,
      },
      dialog: false,
    };
  },
  methods: {
    submitForm() {
      if (!this.username) {
        this.errors.push("Username required.");
      }
      if (!this.password) {
        this.errors.push("Kata sandi tidak sesuai");
      }
      console.log(this.errors);
      if (this.errors.length) {
        let message = "";
        for (let i = 0; i < this.errors.length; i++) {
          message += this.errors[i] + " ";
        }
        alert(message);
        return;
      }
      const data = {
        username: this.username,
        password: this.password,
      };
      Vue.axios.post("http://localhost:8000/api/token/", data).then((res) => {
        if (res.status === 200) {
          window.localStorage.setItem("refresh", res.data.refresh);
          window.localStorage.setItem("access", res.data.access);
          alert("Login berhasil!");
          this.$router.push("/Success");
        } else {
          alert("login gagal, ada masalah pada server");
        }
      });
    },
    onSuccess(googleUser) {
      console.log(googleUser);
      // This only gets the user information: id, name, imageUrl and email
      console.log(googleUser.getBasicProfile());
      const data = {
        provider: "google-oauth2",
        code: googleUser.getBasicProfile["fT"],
      };
      // TODO: Add account selector for Google login

      Vue.axios
        .post("http://localhost:8000/api/google/social/jwt-pair/", data)
        .then((res) => {
          if (res.status === 200) {
            window.localStorage.setItem("refresh", res.data.refresh);
            window.localStorage.setItem("access", res.data.access);
            alert("Login berhasil!");
            this.$router.push("/Success");
          } else {
            alert("login gagal, ada masalah pada server");
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    onFailure(googleUser) {
      console.log("Google Login failed!");
    },
  },
};
</script>
