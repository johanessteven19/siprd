<template>
  <v-container style="margin: auto; width: 60%; padding: 70px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <h3>Back</h3>
      <h2>Edit Akun</h2>
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
                name="email"
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

            <validation-provider
              v-slot="{ errors }"
              name="university"
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

            <validation-provider v-slot="{ errors }" name="fieldOfStudy">
              <v-text-field
                v-model="fieldOfStudy"
                :error-messages="errors"
                label="Bidang Keahlian"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider v-slot="{ errors }" name="position">
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
              name="fullname"
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
              name="password"
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

            <validation-provider v-slot="{ errors }" name="nip">
              <v-text-field
                v-model="nip"
                :error-messages="errors"
                label="NIP"
                required
              >
              </v-text-field>
            </validation-provider>

            <validation-provider
              v-slot="{ errors }"
              name="role"
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
              Buat Akun
            </v-btn>
          </v-col>
          <v-col md="5" class="ml-auto">
            <v-btn
              class="ml-auto white--text"
              :disabled="invalid"
              type="submit"
              color="#8D38E3"
              width="100%"
            >
              Cancel
            </v-btn>
          </v-col>
        </v-row>
      </v-form>
    </validation-observer>
  </v-container>
</template>

<script>
    import Vue from "vue";
    import { required, email} from 'vee-validate/dist/rules'
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
        name: "EditAccount",
        components: {
            ValidationProvider,
            ValidationObserver
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
                    "field_of_study": this.fieldOfStudy,
                    "position": this.position,
                    "role": this.role
                }
                Vue.axios.post(( process.env.VUE_APP_BACKEND_URL || "" )+"/api/register",data).then((res)=>{
                    if(res.status===201){
                        alert("Akun berhasil dibuat.")
                        console.log("YES")
                        this.$router.push("/welcome")
                    }else{
                        alert("Gagal")
                    }
                }).catch(err => {
                    console.log(err.response);
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

            isEmpty (obj) {
                return Object.keys(obj).length === 0
            }
        },

        beforeMount(){
            console.log("test")
            Vue.axios.post(( process.env.VUE_APP_BACKEND_URL || "" )+"/api/register").then((res)=>{
                this.register = res.data
                console.log(res)
            })
        }
        
    }
</script>
