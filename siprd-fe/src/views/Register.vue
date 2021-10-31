<template>
  <v-container style="margin-top: 2rem; width: 60%; padding: 80px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <h2>Buat Akun Baru</h2>
      <br />
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid" lazy-validation>
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
                name="Email"
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
              name="Username"
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
              name="Universitas"
            >
              <v-text-field
                v-model="university"
                label="Universitas"
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="Bidang Keahlian">
              <v-text-field
                v-model="fieldOfStudy"
                :error-messages="errors"
                label="Bidang Keahlian"
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="Jabatan" rules="required">
              <v-select
                v-model="position"
                :items="posSelect"
                :error-messages="errors"
                label="Jabatan*"
                data-vv-name="select"
                required
              >
              </v-select>
            </validation-provider>
          </v-col>

          <v-col md="5" class="ml-auto">
              <validation-provider
                v-slot="{ errors }"
                name="Nama Lengkap"
                rules="required"
              >
                <v-text-field
                  v-model="fullName"
                  :error-messages="errors"
                  label="Nama Lengkap*"
                  required
                >
                </v-text-field>
              </validation-provider>

            <validation-provider
              v-slot="{ errors }"
              name="Password"
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

            <validation-provider v-slot="{ errors }" name="NIP" rules="numeric">
              <v-text-field
                v-model="nip"
                :error-messages="errors"
                label="NIP"
                numeric
              >
              </v-text-field>
            </validation-provider>

            <validation-provider
              v-slot="{ errors }"
              name="Role"
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
              v-on:click="submitForm"
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
                &nbsp; Daftar dengan Google
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
import Vue from 'vue';
import axios from 'axios';
import { required, email, numeric } from 'vee-validate/dist/rules';
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from 'vee-validate';
import GoogleLogin from 'vue-google-login';

setInteractionMode('eager');

extend('required', {
  ...required,
  message: '{_field_} tidak boleh kosong',
});

extend('email', {
  ...email,
  message: 'Pastikan Email anda benar',
});

extend('numeric', {
  ...numeric,
  message: '{_field_} hanya berupa angka.',
});
export default {
  name: 'Register',
  components: {
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
        'Asisten Ahli',
        'Lektor',
        'Lektor Kepala',
        'Guru Besar/Professor',
      ],
      role: null,
      roleSelect: ['Dosen', 'Reviewer', 'SDM PT', 'Admin'],
      user: {},
      params: {
        client_id:
          '7984133184-8qrtflgutpulc7lsb5ml0amv8u58qdu3.apps.googleusercontent.com',
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
        full_name: this.fullName,
        university: this.university,
        nip: this.nip,
        field_of_study: this.fieldOfStudy,
        position: this.position,
        role: this.role,
      };
      Vue.axios
        .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/register`, data)
        .then((res) => {
          if (res.status === 201) {
            console.log('YES');
            this.$router.push('/welcome');
          } else {
            alert('Gagal');
          }
        })
        .catch((err) => {
          // TODO: Make this output more user-friendly!!!
          // Clean string up with a function?
          console.log(err.response);
          const responseErrors = JSON.stringify(err.response.data);
          console.log(responseErrors);
          const errMsg = `Register gagal, errors: ${responseErrors}`;
          alert(errMsg);
        });
    },

    checkForm() {
      this.$refs.observer.validate();
      // this.submitForm();
    },

    loginRedir() {
      this.$router.push('/login');
    },

    onSuccess(googleUser) {
      console.log(googleUser);

      // This only gets the user information: id, name, imageUrl and email
      console.log(googleUser.getBasicProfile());
      this.google_signed = 'true';
      this.fullName = googleUser.getBasicProfile().getName();
      this.email = googleUser.getBasicProfile().getEmail();
    },
    onGoogleSignInSuccess(resp) {
      const token = resp.Zi.access_token;
      axios
        .post(`${process.env.VUE_APP_BACKEND_URL || ''}/auth/google/`, {
          access_token: token,
        })
        .then((res) => {
          this.user = res.data.user;
        })
        .catch((err) => {
          console.log(err.response);
        });
    },
    onGoogleSignInError(error) {
      console.log('OH NOES', error);
      alert('Maaf, layanan Google tidak dapat dihubungi.');
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
  },

  beforeMount() {
    console.log('test');
    Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/register`).then((res) => {
      this.register = res.data;
      console.log(res);
    });
  },
};
</script>
