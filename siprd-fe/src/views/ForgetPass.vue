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
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import { required } from "vee-validate/dist/rules";
import {
  extend,
  ValidationObserver,
  ValidationProvider,
  setInteractionMode,
} from "vee-validate";

setInteractionMode("eager");
export default {
  name: "Forget",
  components: {
    ValidationProvider,
    ValidationObserver,
  },
  data(){
    return{
      errors:[],
      username:null,
    }
  },
  methods: {
    submitForm(){
      console.log("cek")
      const data = this.username;
      Vue.axios
        .post("http://localhost:8000/api/pings")
        .then((res) => {
          if (res.status === 201) {
            alert("Akun berhasil dibuat.");
            console.log("YES");
            // this.$router.push("/welcome");
          } else {
            alert("Gagal");
          }
        })
        .catch((err) => {
          console.log(err.response);
          var responseErrors = JSON.stringify(err.response.data);
          console.log(responseErrors)
        });
    },
    checkForm: function (e) {
      this.$refs.observer.validate();
      this.submitForm();
      return;
    },
  }

}
</script>
