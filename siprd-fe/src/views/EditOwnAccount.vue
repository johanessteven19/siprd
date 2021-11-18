<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 60%; padding: 80px 0">
      <h3> <a v-on:click="backRedir" style="color:black">Back </a></h3> <br>
      <validation-observer ref="observer" v-slot="{ invalid }">
        <h2>Edit Akun</h2> <br>
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
          <v-row>
            <v-col md="5">
                <validation-provider
                  v-slot="{ errors }"
                  name="Email"
                  rules="required|email"
                >
                  <v-text-field
                    v-model="email"
                    :error-messages="errors"
                    label="Email*"
                    :value="email"

                    required
                  >
                  </v-text-field>
                </validation-provider>

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
                    v-model="fullName"
                    :error-messages="errors"
                    label="Nama Lengkap*"
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
              >
                Edit Akun
              </v-btn>
            </v-col>
            <v-col md="5" class="ml-auto">
              <v-btn
                class="mr-4 white--text"
                :disabled="false"
                color="#2D3748"
                width="100%"
                v-on:click="backRedir"
              > Cancel
              </v-btn>
            </v-col>
          </v-row>
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
  name: 'EditOwnAccount',
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
      userData: '',
      config: null,
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
      if (localStorage.access) {
        const accessToken = localStorage.access;
        console.log('something');
        const config = {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        };

        Vue.axios
          .put(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-users/`, data, config)
          .then((res) => {
            console.log(res.data);
            if (res.status === 200) {
              // alert("Akun berhasil diedit.");
              this.$router.push('/your-account');
            } else {
              alert('Gagal');
            }
          })

          .catch((err) => {
            // TODO: Make this output more user-friendly!!!
            // Clean string up with a function?
            console.log(err);
            // var responseErrors = JSON.stringify(err.response.data);
            // console.log(responseErrors);
            // var errMsg = "Edit gagal, errors: " + responseErrors;
            // alert(errMsg);
          });
      }
    },

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    backRedir() {
      this.$router.push('/your-account');
    },
  },

  beforeMount() {
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        if (res.status === 200) {
          this.userData = res.data;
          this.email = res.data.email;
          this.username = res.data.username;
          this.fullName = res.data.full_name;
          this.password = res.data.password;
          this.university = res.data.university;
          this.nip = res.data.nip;
          this.fieldOfStudy = res.data.field_of_study;
          this.role = res.data.role;
          this.position = res.data.position;
        }
      });
    } else {
      this.$router.push('/');
    }
  },
};
</script>
