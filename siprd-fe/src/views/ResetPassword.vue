<template>
  <v-container style="margin: auto; width: 60%; padding: 70px 0">
    <h1>Lupa Kata Sandi</h1>
    <validation-observer ref="observer" v-slot="{ invalid }">
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
          <validation-provider
            v-slot="{ errors }"
            name="Kata Sandi"
            rules="required"
          >
            <v-text-field
              v-model="password"
              :error-messages="errors"
              label="Kata Sandi"
              type="password"
              required
            >
            </v-text-field>
             <br />
          </validation-provider>
          <validation-provider
            v-slot="{ errors }"
            name="Konfirmasi Kata sandi"
            rules="required"
          >
            <v-text-field
              v-model="confirmPassword"
              :error-messages="errors"
              label="Konfirmasi Kata sandi"
              type="password"
              required
            >
            </v-text-field>
          </validation-provider>
        </v-row>
        <v-row>
          <v-col md="5">
            <v-btn
              class="ml-auto white--text"
              :disabled="invalid"
              type="submit"
              color="#8D38E3"
              width="100%"
            >
              Check
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </validation-observer>
  </v-container>
</template>

<script>
import Vue from 'vue';
import { setInteractionMode, ValidationObserver, ValidationProvider } from 'vee-validate';
import VueAxios from 'vue-axios';
import axios from 'axios';
import Vuetify from 'vuetify';

Vue.use(VueAxios, axios);
Vue.use(Vuetify);
setInteractionMode('eager');
export default {
  name: 'Reset Password',
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      password: null,
      confirmPassword: null,
    };
  },
  methods: {
    submitForm() {
      if (this.password !== this.confirmPassword) {
        alert("Password didn't match");
        return;
      }
      console.log(this.$route.params.token, this.confirmPassword, this.$route.params.uidb);
      const data = {
        password: this.confirmPassword,
        token: this.$route.params.token,
        uidb64: this.$route.params.uidb,
      };
      axios.patch(`${process.env.VUE_APP_BACKEND_URL || ''}/api/password-reset-complete`, data).then(
        (res) => {
          if (res.status === 200) {
            this.$router.push('/reset-success');
          } else {
            alert('terjadi kesalahan pada server');
            this.$router.go();
          }
        },
      );
    },
    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },
  },
};
</script>
