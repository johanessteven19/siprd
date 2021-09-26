<template>
  <v-container>
    <h1>Login</h1>
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
        <div v-if="password === '' || username === ''">
          <v-btn
            class="mr-4"
            :disabled="true"
            type="submit"
            color="success"
          >
          submit
        </v-btn>
        </div>
        <div v-else>
          <v-btn
            class="mr-4"
            :disabled="false"
            type="submit"
            color="success"
          >
          submit
        </v-btn>
        </div>
      </v-form>
  </v-container>
</template>

<script>
  import Vue from "vue";
  import axios from "axios";
  import VueAxios from "vue-axios";
  import Vuetify from "vuetify";

  import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'

  Vue.use(VueAxios, axios);
  Vue.use(Vuetify)
  
  export default {
    name:"Login",
    data(){
      return {
        errors: [],
        username: '',
        password: '',
        valid:true,
        usernameRules: [
          v => !!v || 'Username is required',
        ],
        passRules: [
          v => !!v || 'Password is required',
        ],
      }
    },
    methods: {
      submitForm(){
        if (!this.username) {
          this.errors.push("Username required.");
        }
        if (!this.password) {
          this.errors.push("Kata sandi required.");
        }
        console.log(this.errors)
        if (this.errors.length) {
          let message = ""
          for (let i = 0; i < this.errors.length; i++) {
            message += this.errors[i] + " ";
          }
          alert(message)
          return
        }
        const data = {
          'username' : this.username,
          'password' : this.password
        }
        Vue.axios.post("http://localhost:8000/api/token/",data).then((res)=>{
          if (res.status === 200){
            window.localStorage.setItem('refresh',res.data.refresh)
            window.localStorage.setItem('access',res.data.access)
            alert("Login berhasil!")
            this.$router.push("/Success")
          }else{
            alert("login gagal, ada masalah pada server")
          }
        })
      }
    }
  }
</script>