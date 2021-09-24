<template>
  <div class="register">
    <h2>Buat akun baru</h2>
    <form id="register-form" @submit="checkForm" action="http://127.0.0.1:8000/" method="post" novalidate="true">
        <p v-if="errors.length">
         <b>Please correct the following error(s):</b>
            <ul>
                <li v-for="error in errors" v-bind:key="error">{{ error }}</li>
            </ul>
        </p>
        <p>Email*</p>
        <input v-model="email" type="email" placeholder="Email">

        <p>Username*</p>
        <input v-model="username" placeholder="Username">

        <p>Nama Lengkap*</p>
        <input v-model="full_name" placeholder="Nama Lengkap">

        <p>Kata Sandi*</p>
        <input v-model="password" placeholder="Kata Sandi">

        <p>NIP</p>
        <input v-model="nip" placeholder="NIP">

        <p>Universitas*</p>
        <input v-model="university" placeholder="Universitas">

        <p>Bidang Keahlian</p>
        <input v-model="field_of_study" placeholder="Bidang Keahlian">

        <p>Jabatan Akademik</p>
        <select v-model="position">
            <option value="" disabled>Jabatan Akademik</option>
            <option>Asisten Ahli</option>
            <option>Lektor</option>
            <option>Lektor Kepala</option>
            <option>Guru Besar/Professor</option>
        </select>

        <p>Role*</p>
        <select v-model="role">
            <option disabled value="">Role</option>
            <option>Dosen</option>
            <option>Reviewer</option>
            <option>SDM PT</option>
            <option>Admin</option>
        </select>

        <p> 
            <input type="submit" value="Daftar">
        </p>
    </form>
  </div>
</template>

<script>
    import Vue from "vue";
    import axios from "axios";
    import VueAxios from "vue-axios";
    // import Vuetify from "vuetify";
    export default{
        name: "Register",
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
            role: null
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
                        this.$router.push("/")
                    }else{
                        alert("Gagal")
                    }
                })
            },

            checkForm: function (e) {
                console.log("hi")
                e.preventDefault();
                this.errors = [];
                console.log(this.full_name)
                console.log(this.university)

                if (!this.username) {
                    this.errors.push("Username required.");
                }
                if (!this.full_name) {
                    this.errors.push("Name Lengkap required.");
                }
                if (!this.password) {
                    this.errors.push("Kata sandi required.");
                }
                if (!this.university) {
                    this.errors.push("Universitas required.");
                }
                if (!this.role) {
                    this.errors.push("Role required.");
                }
                if (!this.email) {
                    this.errors.push('Email required.');
                } else if (!this.validEmail(this.email)) {
                    this.errors.push('Valid email required.');
                }

                console.log(this.errors)
                if (!this.errors.length) {
                    console.log("error")
                    this.submitForm()
                    return
                }
            },

            validEmail: function (email) {
            var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(email);
            },
        },

        beforeMount(){
            console.log('test')
            Vue.axios.post("http://localhost:8000/api/register").then((res)=>{
                this.register = res.data
                console.log(res)
            })
        }
        
    }
</script>
