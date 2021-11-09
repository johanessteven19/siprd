<template>
  <div>
  <div style="position: fixed; top: 0;">
  <Navigation />
  </div>
  <v-container style="padding: 140px 0">
    <v-row>
      <v-layout column align-center justify-center>
        <div style="padding-left: 320px">
          <v-img
            :src="require('@/assets/asterisk.svg')"
            class="asterisk"
            contain
            height="48px"
            width="48px"
          />
        </div>
        <h1 class="text-left"><strong>Your<br>Dashboard</strong></h1>
        <p class="text-left">
          Sistem Informasi Peer Review Karya Ilmiah
        </p>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
          >
            Daftar Karya Ilmiah
          </v-btn>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <h2 class="text-center"><strong>Summary Karya Ilmiah {{ userData.full_name }}</strong></h2>
        <br>
        <v-row>
            <v-col>
                <v-card outlined>
                    <v-card-text class="text-center black--text font-weight-black">
                      ASSIGNED
                      <br><br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="140"
                        :width="15"
                        :value= "assigned"
                        color="blue"
                        >
                            <strong>{{assigned}}</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-text class="text-center black--text font-weight-black">
                      REVIEWED
                      <br><br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="140"
                        :width="15"
                        :value= "reviewed"
                        color="blue"
                        >
                            <strong>{{reviewed}}</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-text class="text-center black--text font-weight-black">
                      DONE
                      <br><br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="140"
                        :width="15"
                        :value= "done"
                        color="amber"
                        >
                            <strong>{{done}}</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
          <div
            v-for="(karil,index) in karils"
            :key="karil.karil_id">
            <v-col v-if="index < 3">
                <v-card outlined>
                    <v-card-title>
                        {{karil.judul}}
                    </v-card-title>
                    <v-card-text>
                        Pemilik: {{ userData.full_name }}<br>
                        Data: {{karil.journal_data}}<br>
                        Indexer: {{karil.indexer}}<br>
                        <a :href="karil.link_repo">Repository</a><br>
                        <a :href="karil.link_correspondence">Bukti Korespondensi</a>
                        <v-card color="#8D38E3" dark>
                          <div v-if="karil.reviewers.length > 0">
                            <strong>Reviewer:</strong>
                            <span
                            v-for="reviewer in karil.reviewers"
                            :key="reviewer.username">
                              {{reviewer.full_name}},
                            </span>
                          </div>
                          <div v-else>
                            <strong>Reviewer:</strong>   Not assigned
                          </div>
                        </v-card>
                    </v-card-text>
                </v-card>
            </v-col>
          </div>
        </v-row>
        <br>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
            v-on:click="karilList"
          >
            See All List
          </v-btn>
        </div>
      </v-layout>
    </v-row>
  </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';
import Navigation from '../components/Navigation.vue';

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

export default {
  name: 'Success',
  components: {
    Navigation,
  },
  data() {
    return {
      userData: '',
      karils: '',
      assigned: 0,
      reviewed: 0,
      done: 0,
    };
  },
  methods: {
    proceed() {
      this.$router.push('/');
    },
    karilList() {
      this.$router.push('/karil-list');
    },
  },
  beforeMount() {
    if (localStorage.access) {
      console.log(localStorage.access);
      console.log(localStorage.refresh);
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.userData = res.data;
        }
      });
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-karil-summary/`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.karils = res.data;
          let asum = 0;
          let rsum = 0;
          let dsum = 0;
          this.karils.forEach((element) => {
            console.log(element.status);
            if (element.status.includes('Done')) {
              dsum += 1;
            } else if (element.status.includes('In_Review')) {
              rsum += 1;
            } else if (element.status.includes('Reviewed')) {
              asum += 1;
            }
          });
          this.assigned = (asum / this.karils.length) * 100;
          this.reviewed = (rsum / this.karils.length) * 100;
          this.done = (dsum / this.karils.length) * 100;
        } else {
          console.log('fetch failed or no karil');
        }
      });
    } else {
      this.$router.push('/');
    }
  },
};
</script>
