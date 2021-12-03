<template>
  <v-container style="margin: auto; width: 60%; padding: 70px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <h2>Lupa Kata Sandi</h2>
      <br />
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
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
    <p>Ingat Kata Sandi <a href="/login">Masuk</a></p>
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
  name: 'Forget',
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data() {
    return {
      errors: [],
      username: null,
    };
  },
  methods: {
    submitForm() {
      if (!this.username) {
        this.errors.push('Username required.');
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
      };
      console.log(data);
      axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/request-reset-email/`, data).then(
        (res) => {
          console.log(res.data);
          this.$router.push('/forget-success');
        },
      ).catch((err) => {
        // NOTE: Do not make this more specific, for security reasons.
        console.log(err.response);
        if (typeof err.response !== 'undefined') {
          // Backend accessible, but credentials incorrect
          alert('Username tidak ditemukan.');
        } else {
          // Backend inaccessible (no response)
          alert('Maaf, server SIPEERKI tidak dapat dihubungi.');
        }
      });
    },
    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },
  },
};
</script>
