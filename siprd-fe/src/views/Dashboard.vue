<template>
  <div>
    <div style="position: fixed; top: 0; z-index: 100">
      <Navigation />
    </div>
  <v-container style="padding: 140px 50px 0px;">
    <v-row >
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
        <div>
          <div v-if="userData.role === 'Admin'">
            <h1 class="text-left" ><strong>Admin<br>Dashboard</strong></h1>
          </div>
          <div v-else>
            <h1 class="text-left" ><strong>Your<br>Dashboard</strong></h1>
          </div>
          <p class="text-center">
          Sistem Informasi Peer Review Karya Ilmiah
          </p>
          <div class="txt-xs-center">
            <v-btn
              class="ml-auto white--text"
              color="#8D38E3"
              width="80%"
              v-on:click="karilList"
            >
              Daftar Karya Ilmiah
            </v-btn>
          </div>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
      </v-layout>
    </v-row>
  </v-container>
  <div style="background-color: #F9F9F9">
    <v-container style="padding: 50px 140px 100px 140px;">
    <v-row >
      <v-layout column align-center justify-center>
        <h1 class="text-center"><strong>Summary Karya Ilmiah {{ userData.full_name }}</strong></h1>
        <br>
        <v-row  style="padding-bottom: 0px">
            <v-col>
              <!-- eslint-disable no-trailing-spaces -->
                <v-card 
                outlined
                :min-height="300"
                :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Assigned</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "assigned"
                        color="blue"
                        >
                            <strong>{{assigned}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined :min-height="300" :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Reviewed</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "reviewed"
                        color="blue"
                        >
                            <strong>{{reviewed}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined :min-height="300" :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Done</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "done"
                        color="amber"
                        >
                            <strong>{{done}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
          <div
          v-for="(karil,index) in karils"
          :key="karil.karil_id">
          <v-col v-if="index < 3" class="mt-n9">
              <v-card elevation="1"
                  outlined
                  :loading="loading"
                  class="mx-auto my-12"
                  min-height="280"
                  min-width="280">
                  <v-card-title>
                      {{karil.judul}}
                  </v-card-title>
                  <v-card-text class="pb-1">
                      <strong >Pemilik:</strong> {{ userData.full_name }}<br>
                  </v-card-text>
                  <v-card-text class="pb-0 pt-1">
                      <strong>Data:</strong>  {{karil.journal_data}}<br>
                  </v-card-text>
                  <v-card-text class="pb-1 pt-1">
                      <strong>Indexer:</strong>  {{karil.indexer}}<br>
                  </v-card-text>
                  <v-card-text class="pb-1 pt-1">
                      <v-btn
                      v-if="karil.link_repo != null"
                      outlined
                      color="#8D38E3"
                      v-on:click="link(karil.link_repo)"
                      width="80%"
                    >Repository
                    </v-btn>
                  </v-card-text>
                  <v-card-text class="pb-0 pt-1">
                      <v-btn
                      v-if="karil.link_correspondence != null"
                      outlined
                      color="#8D38E3"
                      v-on:click="link(karil.link_correspondence)"
                      width="80%"
                    >Bukti Korespondensi
                    </v-btn>
                  </v-card-text>
                  <v-card-text>
                    <v-card color="#8D38E3" dark class="pb-2 pt-2 pl-2 mx-auto my-auto">
                        <div v-if="karil.reviewers.length > 0">
                          <strong>Reviewer:</strong>
                          <span
                          v-for="reviewer in karil.reviewers"
                          :key="reviewer">
                            <br>{{reviewer}}
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
            width="200px"
            v-on:click="karilList"
          >
            Lihat Semua List <span> <i class="fas fa-arrow-right"></i></span>
          </v-btn>
        </div>
      </v-layout>
    </v-row>
  </v-container>
  </div>
  <div v-if="userData.role === 'Admin'" >
    <v-container style="padding: 60px 50px 50px;">
      <v-row >
      <v-layout column align-center justify-center>
        <h1 class="text-center"><strong>Summary Akun</strong></h1>
        <br>
        <v-row  style="padding-bottom: 0px">
            <v-col>
              <!-- eslint-disable no-trailing-spaces -->
                <v-card 
                outlined
                :min-height="300"
                :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Need Approval</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "need"
                        color="blue"
                        >
                            <strong>{{need}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined :min-height="300" :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Approved</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "approved"
                        color="blue"
                        >
                            <strong>{{approved}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined :min-height="300" :min-width="280">
                    <v-card-text class="text-center black--text font-weight-black">
                      <h2>Total Account</h2>
                      <br>
                        <v-progress-circular
                        :rotate="-90"
                        :size="190"
                        :width="25"
                        :value= "total"
                        color="amber"
                        >
                            <strong>{{total}}%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
          <div
          v-for="(karil,index) in karils"
          :key="karil.karil_id">
          <v-col v-if="index < 3" class="mt-n9">
              <v-card elevation="1"
                  outlined
                  :loading="loading"
                  class="mx-auto my-12"
                  min-height="280"
                  min-width="280">
                  <v-card-title>
                      {{userData.full_name}}
                  </v-card-title>
                  <v-card-text class="pb-1">
                      <strong >Pemilik:</strong> {{ userData.full_name }}<br>
                  </v-card-text>
                  <v-card-text class="pb-0 pt-1">
                      <strong>Data:</strong>  {{karil.journal_data}}<br>
                  </v-card-text>
                  <v-card-text class="pb-1 pt-1">
                      <strong>Indexer:</strong>  {{karil.indexer}}<br>
                  </v-card-text>
                  <v-card-text class="pb-1 pt-1">
                      <v-btn
                      v-if="karil.link_repo != null"
                      outlined
                      color="#8D38E3"
                      v-on:click="link(karil.link_repo)"
                      width="80%"
                    >Repository
                    </v-btn>
                  </v-card-text>
                  <v-card-text class="pb-0 pt-1">
                      <v-btn
                      v-if="karil.link_correspondence != null"
                      outlined
                      color="#8D38E3"
                      v-on:click="link(karil.link_correspondence)"
                      width="80%"
                    >Bukti Korespondensi
                    </v-btn>
                  </v-card-text>
                  <v-card-text>
                    <v-card color="#8D38E3" dark class="pb-2 pt-2 pl-2 mx-auto my-auto">
                        <div v-if="karil.reviewers.length > 0">
                          <strong>Reviewer:</strong>
                          <span
                          v-for="reviewer in karil.reviewers"
                          :key="reviewer">
                            <br>{{reviewer}}
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
            width="200px"
            v-on:click="AccountList"
          >
            Lihat Semua List <span> <i class="fas fa-arrow-right"></i></span>
          </v-btn>
        </div>
      </v-layout>
    </v-row>
    </v-container>
  </div>
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
      users: [],
      userData: '',
      karils: '',
      assigned: 0,
      reviewed: 0,
      done: 0,
      need: 0,
      approved: 0,
      total: 0,
    };
  },
  methods: {
    proceed() {
      this.$router.push('/');
    },
    karilList() {
      this.$router.push('/karil-list');
    },
    link(link) {
      window.open(link);
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
            }
            if (element.reviews.length !== 0) {
              rsum += 1;
            }
            if (element.reviewers.length !== 0) {
              asum += 1;
            }
          });
          this.assigned = Math.round((asum / this.karils.length) * 100);
          this.reviewed = Math.round((rsum / this.karils.length) * 100);
          this.done = Math.round((dsum / this.karils.length) * 100);
        } else {
          console.log('fetch failed or no karil');
        }
      });
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-users/`, config).then((res) => {
        if (res.status === 200) {
          console.log(res.data);
          this.users = res.data;
          let needSum = 0;
          let approvedSum = 0;
          let totalSum = 0;
          this.users.forEach((item) => {
            console.log(item.status);
            if (item.status.includes('Done')) {
              needSum += 1;
            }
            if (item.reviews.length !== 0) {
              approvedSum += 1;
            }
            if (item.reviewers.length !== 0) {
              totalSum += 1;
            }
          });
          this.need = Math.round((needSum / this.users.length) * 100);
          this.approved = Math.round((approvedSum / this.users.length) * 100);
          this.total = Math.round((totalSum / this.users.length) * 100);
        } else {
          console.log('fetch failed or no user');
        }
      });
    } else {
      this.$router.push('/');
    }
  },
};
</script>
