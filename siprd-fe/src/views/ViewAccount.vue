<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 60%; padding: 80px 0">
      <h3> <a v-on:click="backRedir" style="color:black">Back </a></h3> <br>
            <v-row>
            <v-col>
                <h1>Hello, {{ userData.full_name }}</h1> <br>
            </v-col>
            <v-col md="2" class="mr-auto">
                <v-btn
                class="mr-4 purple--text"
                v-on:click="editAccount"
                width="100%"
                > Edit Akun
                </v-btn>
            </v-col>
            <v-col md="3" class="mr-auto">
                <v-btn
                class="mr-4 white--text"
                v-on:click="changePass"
                color="#2D3748"
                width="100%"
                > Ganti Password
                </v-btn>
            </v-col>
            </v-row>
            <br><br>

            <v-row >
            <v-col md="5" >
                <v-row style="font-size:15px; color:grey;">
                    Email
                </v-row>
                <v-row style="font-size:20px; border-bottom: 2px solid #8D38E3; padding-left:5px">
                    <div v-if="userData.email != null">
                        {{ userData.email }}
                    </div>
                    <div v-else> - </div>
                </v-row>

                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    Username
                </v-row>
                <v-row style="font-size:20px; border-bottom: 2px solid #8D38E3; padding-left:5px">
                    <div v-if="userData.username != null">
                        {{ userData.username }}
                    </div>
                    <div v-else> - </div>
                </v-row>

                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    Universitas
                </v-row>
                <v-row style="font-size:20px; border-bottom: 2px solid #8D38E3; padding-left:5px">
                    <div v-if="userData.university != null">
                        {{ userData.university }}
                    </div>
                    <div v-else> - </div>

                </v-row>

                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    Bidang Keahlian
                </v-row>
                <v-row style="font-size:20px;border-bottom: 2px solid #8D38E3; padding-left:5px">
                    <div v-if="userData.field_of_study != null">
                        {{ userData.field_of_study }}
                    </div>
                    <div v-else> - </div>
                </v-row>

            </v-col>

            <v-col md="5" class="ml-auto">
                <v-row style="font-size:15px; color:grey;">
                    Nama Lengkap
                </v-row>
                <v-row style="font-size:20px; border-bottom: 2px solid #8D38E3;padding-left:5px">
                    <div v-if="userData.full_name != null">
                        {{ userData.full_name }}
                    </div>
                    <div v-else> - </div>
                </v-row>

                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    NIP
                </v-row>
                <v-row style="font-size:20px;border-bottom: 2px solid #8D38E3;padding-left:5px">
                    <div v-if="userData.nip != null">
                        {{ userData.nip }}
                    </div>
                    <div v-else> - </div>
                </v-row>

                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    Role
                </v-row>
                <v-row style="font-size:20px;border-bottom: 2px solid #8D38E3;padding-left:5px">
                    <div v-if="userData.role != null">
                        {{ userData.role }}
                    </div>
                    <div v-else> - </div>
                </v-row>
                <v-row style="font-size:15px; color:grey; padding-top:40px">
                    Jabatan
                </v-row>
                <v-row style="font-size:20px; border-bottom: 2px solid #8D38E3;padding-left:5px">
                    <div v-if="userData.position != null">
                        {{ userData.position }}
                    </div>
                    <div v-else> - </div>
                </v-row>
            </v-col>
            </v-row>

    </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import Navigation from '../components/Navigation.vue';

export default {
  name: 'ViewAccount',
  components: {
    Navigation,
  },
  data() {
    return {
      userData: '',
    };
  },
  methods: {
    backRedir() {
      this.$router.push('/your-account');
    },

    editAccount() {
      this.$router.push('/edit-account');
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
        }
      });
    } else {
      this.$router.push('/');
    }
  },
};
</script>
