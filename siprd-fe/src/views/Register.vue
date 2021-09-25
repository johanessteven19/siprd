<template>
    <v-container>
    <validation-observer ref="observer" v-slot="{ invalid }">
        <h2>Buat akun baru</h2>
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
            <v-col md="5">
            <validation-provider v-slot="{ errors }" name="email" rules="required|email">
                <v-text-field
                    v-model="email"
                    :error-messages="errors"
                    label="Email"
                    required>  
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="username" rules="required">
                <v-text-field
                    v-model="username"
                    :error-messages="errors"
                    label="Username"
                    required>   
                </v-text-field>
            </validation-provider>

           <validation-provider v-slot="{ errors }" name="university" rules="required">
                <v-text-field
                    v-model="university"
                    :error-messages="errors"
                    label="Universitas"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="field_of_study" rules="required">
                <v-text-field
                    v-model="field_of_study"
                    :error-messages="errors"
                    label="Bidang Keahlian"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="position" rules="required">
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
                    v-model="full_name"
                    :error-messages="errors"
                    label="Nama Lengkap"
                    required>   
                </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="password" rules="required">
                <v-text-field
                    v-model="password"
                    :error-messages="errors"
                    label="Password"
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

            <validation-provider v-slot="{ errors }" name="role">
                <v-select
                    v-model="role"
                    :items="roleSelect"
                    :error-messages="errors"
                    label="Role"
                    data-vv-name="select"
                    required>
                </v-select>
            </validation-provider>
            </v-col>
        </v-row>
        <v-row>
            <v-col md="6">
            <v-btn
                class="mr-6"
                :disabled="invalid"
                type="submit"
                color="success"
            >
                Daftar
            </v-btn>
            </v-col>

            <v-col md="5" class="ml-auto">
            <v-btn
                :disabled="valid"
                type="button"
                color="success"
            >
                Masuk dengan Google
            </v-btn>
            </v-col>
        </v-row>
        </v-form>
    </validation-observer>
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
        ValidationProvider,
        ValidationObserver,
        },
        data(){
            return {
            errors: [],
            email: null,
            username: null,
            full_name: null,
            password: null,
            nip: null,
            university: null,
            field_of_study: null,
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
            }
        },
        methods: {
            submitForm(){
                const data={
                    "username": this.username,
                    "email": this.email,
                    "password": this.password,
                    "full_name": this.full_name,
                    "university": this.university,
                    "nip": this.nip,
                    "field_of_study": this.field_of_study,
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
