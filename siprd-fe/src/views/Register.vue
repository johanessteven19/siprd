<template>
  <v-container style="margin: auto; width: 60%; padding: 70px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <h2>Buat Akun Baru</h2>
      <br />
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
          <v-col md="5">
            <div v-if="google_signed != null">
              <v-text-field
                :value="email"
                label="Email (Filled)"
                filled
                readonly
              >
              </v-text-field>
            </div>
            <div v-else>
              <validation-provider
                v-slot="{ errors }"
                name="email"
                rules="required|email"
              >
                <v-text-field
                  v-model="email"
                  :error-messages="errors"
                  label="Email*"
                  required
                >
                </v-text-field>
              </validation-provider>
            </div>

            <validation-provider
              v-slot="{ errors }"
              name="username"
              rules="required"
            >
              <v-text-field
                v-model="username"
                :error-messages="errors"
                label="Username*"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider
              v-slot="{ errors }"
              name="university"
              rules="required"
            >
              <v-text-field
                v-model="university"
                :error-messages="errors"
                label="Universitas*"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="fieldOfStudy">
              <v-text-field
                v-model="fieldOfStudy"
                :error-messages="errors"
                label="Bidang Keahlian"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="position">
              <v-select
                v-model="position"
                :items="posSelect"
                :error-messages="errors"
                label="Jabatan"
                data-vv-name="select"
                required
              >
              </v-select>
            </validation-provider>
          </v-col>

          <v-col md="5" class="ml-auto">
            <div v-if="google_signed != null">
              <v-text-field
                :value="full_name"
                label="Nama lengkap (Filled)"
                filled
                readonly
              >
              </v-text-field>
            </div>
            <div v-else>
              <validation-provider
                v-slot="{ errors }"
                name="fullname"
                rules="required"
              >
                <v-text-field
                  v-model="full_name"
                  :error-messages="errors"
                  label="Nama Lengkap*"
                  required
                >
                </v-text-field>
              </validation-provider>
            </div>

            <validation-provider
              v-slot="{ errors }"
              name="password"
              rules="required"
            >
              <v-text-field
                v-model="password"
                :error-messages="errors"
                label="Password*"
                :type="'password'"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="nip">
              <v-text-field
                v-model="nip"
                :error-messages="errors"
                label="NIP"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider
              v-slot="{ errors }"
              name="role"
              rules="required"
            >
              <v-select
                v-model="role"
                :items="roleSelect"
                :error-messages="errors"
                label="Role*"
                data-vv-name="select"
                required
              >
              </v-select>
            </validation-provider>
          </v-col>
        </v-row>

        Required*
        <v-row>
          <v-col md="5">
            <v-btn
              class="ml-auto white--text"
              :disabled="invalid"
              type="submit"
              color="#8D38E3"
              width="100%"
            >
              Daftar
            </v-btn>
          </v-col>
          <v-col md="5" class="ml-auto">
            <v-btn
              class="mr-4 white--text"
              :disabled="false"
              color="#2D3748"
              width="100%"
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
          </v-col>
        </v-row>
      </v-form>
    </validation-observer>
    <br />
    <p>Sudah punya akun? <a v-on:click="loginRedir">Masuk</a></p>
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import { required,email} from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";
import GoogleLogin from "vue-google-login";

setInteractionMode("eager");

extend("required", {
  ...required,
  message: "{_field_} can not be empty",
});

extend("email", {
  ...email,
  message: "Email must be valid",
});
export default {
  name: "Register",
  components: {
    // UserPanel,
    ValidationProvider,
    ValidationObserver,
    GoogleLogin,
  },
  data() {
    return {
      errors: [],
      email: null,
      username: null,
      fullName: null,
      password: null,
      nip: null,
      university: null,
      fieldOfStudy: null,
      position: null,
      posSelect: [
        "Asisten Ahli",
        "Lektor",
        "Lektor Kepala",
        "Guru Besar/Professor",
      ],
      role: null,
      roleSelect: ["Dosen", "Reviewer", "SDM PT", "Admin"],
      user: {},
      params: {
        client_id:
          "7984133184-8qrtflgutpulc7lsb5ml0amv8u58qdu3.apps.googleusercontent.com",
      },
      renderParams: {
        width: 357,
        longtitle: true,
      },
      google_signed: null,
    };
  },
  methods: {
    submitForm() {
      const data = {
        username: this.username,
        email: this.email,
        password: this.password,
        full_name: this.full_name,
        university: this.university,
        nip: this.nip,
        field_of_study: this.fieldOfStudy,
        position: this.position,
        role: this.role,
      };
      Vue.axios
        .post(( process.env.VUE_APP_BACKEND_URL || "" )+"/api/register", data)
        .then((res) => {
          if (res.status === 201) {
            alert("Akun berhasil dibuat.");
            console.log("YES");
            this.$router.push("/welcome");
          } else {
            alert("Gagal");
          }
        })
        .catch((err) => {
          // TODO: Make this output more user-friendly!!!
          // Clean string up with a function?
          console.log(err.response);
          var responseErrors = JSON.stringify(err.response.data);
          console.log(responseErrors)
          var errMsg = "Login gagal, errors: " + responseErrors
          alert(errMsg);
        });
    },

    checkForm: function (e) {
      this.$refs.observer.validate();
      this.submitForm();
      return;
    },

    loginRedir: function (e) {
      this.$router.push("/login");
    },

    onSuccess(googleUser) {
      console.log(googleUser);

      // This only gets the user information: id, name, imageUrl and email
      console.log(googleUser.getBasicProfile());
      this.google_signed = "true";
      this.full_name = googleUser.getBasicProfile().getName();
      this.email = googleUser.getBasicProfile().getEmail();
    },
    onGoogleSignInSuccess(resp) {
      const token = resp.Zi.access_token;
      axios
        .post(( process.env.VUE_APP_BACKEND_URL || "" )+"/auth/google/", {
          access_token: token,
        })
        .then((resp) => {
          this.user = resp.data.user;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    onGoogleSignInError(error) {
      console.log("OH NOES", error);
      alert("Maaf, layanan Google tidak dapat dihubungi.")
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
  },

  beforeMount() {
    console.log("test");
    Vue.axios.post(( process.env.VUE_APP_BACKEND_URL || "" )+"/api/register").then((res) => {
      this.register = res.data;
      console.log(res);
    });
  },
};
</script>
