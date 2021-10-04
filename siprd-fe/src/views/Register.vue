<template>
    <v-container style=
        "margin: auto;
        width: 60%;
        padding: 70px 0;">
    <validation-observer ref="observer" v-slot="{ invalid }">
        <h2>Buat Akun Baru</h2>
        <br>
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
            <v-col md="5">
            <validation-provider v-slot="{ errors }" name="email" rules="required|email">
                <v-text-field
                    v-model="email"
                    :error-messages="errors"
                    label="Email*"
                    required>  
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="username" rules="required">
                <v-text-field
                    v-model="username"
                    :error-messages="errors"
                    label="Username*"
                    required>   
                </v-text-field>
            </validation-provider>

           <validation-provider v-slot="{ errors }" name="university" rules="required">
                <v-text-field
                    v-model="university"
                    :error-messages="errors"
                    label="Universitas*"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="fieldOfStudy">
                <v-text-field
                    v-model="fieldOfStudy"
                    :error-messages="errors"
                    label="Bidang Keahlian"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="position">
                <v-select
                    v-model="position"
                    :items="posSelect"
                    :error-messages="errors"
                    label="Jabatan"
                    data-vv-name="select"
                    required>
                </v-select>
            </validation-provider>
            </v-col>

            <v-col md="5" class="ml-auto">
            <validation-provider v-slot="{ errors }" name="fullname" rules="required">
                <v-text-field
                    v-model="fullName"
                    :error-messages="errors"
                    label="Nama Lengkap*"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="password" rules="required">
                <v-text-field
                    v-model="password"
                    :error-messages="errors"
                    label="Password*"
                    :type="'password'"
                    required>
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="nip">
                <v-text-field
                    v-model="nip"
                    :error-messages="errors"
                    label="NIP"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="role" rules="required">
                <v-select
                    v-model="role"
                    :items="roleSelect"
                    :error-messages="errors"
                    label="Role*"
                    data-vv-name="select"
                    required>
                </v-select>
            </validation-provider>
            </v-col>
        </v-row>

        Required*
            
            <v-col md="5">
            <v-btn
                class="ml-auto white--text"
                :disabled="invalid"
                type="submit"
                color="#8D38E3"
                width= '100%'
            >
                Daftar
            </v-btn>
            </v-col>
        </v-form>
    </validation-observer>
            <v-col md="5" >
            <GoogleLogin 
            :params="params" 
            :renderParams="renderParams" 
            :onSuccess="onSuccess" 
            :onFailure="onFailure"
            ></GoogleLogin>
            </v-col>
            <!-- <user-panel v-else :user="user"></user-panel> -->
    <br>
    <p>Sudah punya akun? <a v-on:click="loginRedir">Masuk</a></p>
    </v-container>
</template>

<script>
    import Vue from "vue";
    import axios from "axios";
    import VueAxios from "vue-axios";
    import Vuetify from "vuetify";
    import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
    import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
    // import UserPanel from '../components/UserPanel.vue'
    import GoogleLogin from 'vue-google-login';

    setInteractionMode('eager')

    extend('required', {
        ...required,
        message: '{_field_} can not be empty',
    })

    extend('email', {
        ...email,
        message: 'Email must be valid',
    })
    export default{
        name: "Register",
        components: {
            // UserPanel,
            ValidationProvider,
            ValidationObserver,
            GoogleLogin
        },
        data(){
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
                'Guru Besar/Professor'
            ],
            role: null,
            roleSelect: [
                'Dosen',
                'Reviewer',
                'SDM PT',
                'Admin'
            ],
            user: {},
            params: {
                client_id: '473901621952-2upinaorbnjbmreeap1mqvb084d8bqpk.apps.googleusercontent.com'
             },
            renderParams: {
                width:357,
                longtitle: true
            }
            }
        },
        methods: {
            submitForm(){
                const data={
                    "username": this.username,
                    "email": this.email,
                    "password": this.password,
                    "full_name": this.fullName,
                    "university": this.university,
                    "nip": this.nip,
                    "field_of_study": this.fieldOfStudy,
                    "position": this.position,
                    "role": this.role
                }

                Vue.axios.post("http://localhost:8000/api/register",data).then((res)=>{
                    if(res.status===201){
                        alert("Akun berhasil dibuat.")
                        console.log("YES")
                        this.$router.push("/login")
                    }else{
                        alert("Gagal")
                    }
                })
            },

            checkForm: function (e) {
                this.$refs.observer.validate()
                this.submitForm()
                return
            },

            loginRedir: function(e){
                this.$router.push("/login")
            },

            onSuccess(googleUser) {
                console.log(googleUser);
 
                // This only gets the user information: id, name, imageUrl and email
                console.log(googleUser.getBasicProfile());
            },
            onGoogleSignInSuccess (resp) {
                const token = resp.Zi.access_token
                axios.post('http://localhost:8000/auth/google/', {
                    access_token: token
                })
                .then(resp => {
                    this.user = resp.data.user
                })
                .catch(err => {
                    console.log(err.response)
                })
            },
            onGoogleSignInError (error) {
                console.log('OH NOES', error)
            },
            isEmpty (obj) {
                return Object.keys(obj).length === 0
            }
        },

        beforeMount(){
            console.log("test")
            Vue.axios.post("http://localhost:8000/api/register").then((res)=>{
                this.register = res.data
                console.log(res)
            })
        }
        
    }
</script>
