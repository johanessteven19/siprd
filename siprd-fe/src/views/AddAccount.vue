<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 60%; padding: 80px 0">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <h3><a v-on:click="backRedir" style="color:black">Back</a></h3>
        <h2>Tambah Akun Baru</h2>
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
                v-slot="{ errors }"
                name="Universitas"
              >
                <v-text-field
                  v-model="university"
                  :error-messages="errors"
                  label="Universitas*"
                >
                </v-text-field>
              </validation-provider>

              <validation-provider v-slot="{ errors }" name="Bidang Keahlian">
                <v-text-field
                  v-model="fieldOfStudy"
                  :error-messages="errors"
                  label="Bidang Keahlian"
                  required
                >
                </v-text-field>
              </validation-provider>

              <validation-provider v-slot="{ errors }" name="Jabatan">
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
              <validation-provider
                v-slot="{ errors }"
                name="Nama Lengkap"
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
                @click="dialog = true"
                color="#8D38E3"
                width="100%"
              >
                Buat Akun
              </v-btn>
            </v-col>
            <v-col md="5" class="ml-auto">
              <v-btn
                class="ml-auto white--text"
                color="#2D3748"
                width="100%"
                v-on:click="backRedir"
              >
                Cancel
              </v-btn>
            </v-col>
          </v-row>
          <v-dialog
          v-model="dialog"
          persistent
          max-width="350">
            <v-card class="mx-auto my-0" max-width="350">
              <v-card-title class="justify-center text-h5 ">
                Izin Diperlukan
              </v-card-title>
              <v-card-text style="text-align:center">Anda yakin ingin menambah akun?</v-card-text>
              <v-card-actions class="justify-center">
                <v-btn
                text
                @click="dialog = false"
                >
                  Kembali
                </v-btn>
                <v-btn
                color="blue"
                text
                type="submit"
                 @click="checkForm();dialog = false"
                >
                  Iya
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
        </v-form>
      </validation-observer>
    </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import { required, email, numeric } from 'vee-validate/dist/rules';
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from 'vee-validate';
import Navigation from '../components/Navigation.vue';

setInteractionMode('eager');

extend('required', {
  ...required,
  message: '{_field_} tidak boleh kosong',
});

extend('email', {
  ...email,
  message: 'Email harus valid',
});

extend('numeric', {
  ...numeric,
  message: '{_field_} hanya berupa angka.',
});

export default {
  name: 'AddAccount',
  components: {
    ValidationProvider,
    ValidationObserver,
    Navigation,
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
      dialog: false,
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
        approved: true,
      };
      if (localStorage.access) {
        const accessToken = localStorage.access;
        const config = {
          headers: { Authorization: `Bearer ${accessToken}` },
        };
        Vue.axios
          .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-users/`, data, config)
          .then((res) => {
            if (res.status === 201) {
              alert('Akun berhasil dibuat.');
              console.log('YES');
              this.backRedir();
            } else {
              alert('Gagal');
            }
          })
          .catch((err) => {
            alert('Username is taken.');
            console.log(err.response);
          });
      }
    },
    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    backRedir() {
      this.$router.push('/account-list');
    },

    isEmpty(obj) {
      return Object.keys(obj).length === 0;
    },
  },
};
</script>
