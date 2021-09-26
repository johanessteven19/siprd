<template>
  <div
  class="d-flex align-center "
  v-bind:style="{ width:'100%', height:'100%'}"
  >
    <v-card
      flat
      v-bind:style="{ width:'50%', 'background-color':'#8D38E3'}"
      class="d-flex justify-center align-center"
      height="100%"
    >
        <v-img
          :src="require('../assets/bunderan.svg')"
          class="bunderan"
          contain
          height="100%"
          width="50%"
        />
    </v-card>
    <v-card
      flat
      v-bind:style="{ width:'50%'}"
    >
          <v-container
        style=
        "margin: auto;
        width: 60%;
        padding: 150px 0;">
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
                
                <div style="margin-top: 10px;" v-if="password === '' || username === ''">
                  <v-btn
                    class="mr-4"
                    :disabled="true"
                    type="submit"
                    color="#8D38E3"
                    width= '100%'
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
                    width= '100%'
                    
                  >
                  masuk
                </v-btn>
                
              </div>
            </v-form>
            <p style="margin-top: 20px;" class="register">Tidak memiliki akun? <span> <a href="/Register" >Daftar</a></span></p>
        </v-container>
    </v-card>
  </div>

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
          v => !!v || 'Kata sandi tidak sesuai',
        ],
      }
    },
    methods: {
      submitForm(){
        if (!this.username) {
          this.errors.push("Username required.");
        }
        if (!this.password) {
          this.errors.push("Kata sandi tidak sesuai");
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

