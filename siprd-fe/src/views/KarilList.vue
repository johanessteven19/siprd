<template>
  <div>
    <div style="position: fixed; top: 0;">
    <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <v-row>
        <v-col md="5">
          <template v-if="dosen === true">
            <h1>Daftar Karya Ilmiah oleh {{ ownerName }}</h1>
          </template>
          <template v-else-if="reviewer === true">
            <h1>Daftar Karya Ilmiah di Assign ke {{ ownerName }}</h1>
          </template>
          <template v-else>
            <h1>Daftar Karya Ilmiah</h1>
          </template>
        </v-col>
        <v-col md="3" v-if="profile !== 1">
          <v-btn
            class="mr-4 white--text"
            :disabled="false"
            color="blue"
            width="100%"
            v-on:click="addRedir"
          > + Tambah Karya Ilmiah
          </v-btn>
        </v-col>
        <template v-if="dosen === true || reviewer === true">
          <v-col md="1">
            <v-btn
            class="mr-4 white--text"
            :disabled="false"
            color="red"
            v-on:click="back"
            > back
            </v-btn>
          </v-col>
        </template>
      </v-row>
      <v-row>
        <v-col md="2" v-if="profile !== 1">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': tab === 0,
              'white--text': tab === 0
              }"
            :outlined="tab !== 0"
            color="#8D38E3"
            width="100%"
            v-on:click="setTab(0)"
          > Belum Diassign
          </v-btn>
        </v-col>
        <v-col md="2">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': tab === 1,
              'white--text': tab === 1
              }"
            :outlined="tab !== 1"
            color="#8D38E3"
            width="100%"
            v-on:click="setTab(1)"
          > Belum Direview
          </v-btn>
        </v-col>
        <v-col md="2">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': tab === 2,
              'white--text': tab === 2
              }"
            :outlined="tab !== 2"
            color="#8D38E3"
            width="100%"
            v-on:click="setTab(2)"
          > Telah Direview
          </v-btn>
        </v-col>
      <v-col md="2">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': tab === 3,
              'white--text': tab === 3
              }"
            :outlined="tab !== 3"
            color="#8D38E3"
            width="100%"
            v-on:click="setTab(3)"
          > Semua
          </v-btn>
        </v-col>
        <template v-if="tab === 2">
          <v-col md="2"></v-col>
          <v-col
          md="2">
            <v-btn
            color="primary"
            width="100%"
            v-on:click="donePDF">
              <v-icon>
                mdi-download
              </v-icon>
              Download to PDF
            </v-btn>
          </v-col>
        </template>
      </v-row>
      <br>
      <v-data-table
        :page="page"
        :headers="headers"
        :items="karilList"
        :item-key="karil_id"
        :search="search"
        class="elevation-1"
      >

      <template v-slot:top>
      <v-container>
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          single-line
          hide-details
        >
        </v-text-field>
      </v-container>

      </template>

      <template v-slot:item.no="{ index }">
        {{ index + 1 }}
      </template>

      <template v-slot:item.action="row">
        <v-btn
        depressed
        color="success"
        v-on:click="assign(row.item.karil_id)"
        >
        Lihat
        </v-btn>
      </template>
      <template v-if="profile === 0" v-slot:item.pemilik="row">
        <a
        v-on:click="userKarils(row.item.pemilik)">
          {{ row.item.pemilik }}
        </a>
      </template>
      <template v-if="profile === 0" v-slot:item.reviewers="row">
        <span
        v-for="(reviewer,index) in row.item.reviewers"
        :key="reviewer">
        <a
        v-on:click="reviewerKarils(row.item.reviewers[index])">
          {{ row.item.reviewers[index] }}
        </a>
        </span>
      </template>
      </v-data-table>
      </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';
import { jsPDF as JsPDF } from 'jspdf';
import Navigation from '../components/Navigation.vue';

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'table-list',
  components: {
    Navigation,
  },
  data() {
    return {
      headers: [
        { text: 'No.', sortable: false, value: 'no' },
        { text: 'Nama Dosen', value: 'pemilik', sortable: false },
        { text: 'Nama Penulis', value: 'pemilik', sortable: false },
        { text: 'Judul Karya Ilmiah', value: 'judul', sortable: false },
        { text: 'Data Jurnal', value: 'journal_data', sortable: false },
        { text: 'Repository', value: 'link_repo', sortable: false },
        { text: 'Indexer', value: 'indexer', sortable: false },
        { text: 'Check Similarity', value: 'link_simcheck', sortable: false },
        { text: 'Reviewer', value: 'reviewers', sortable: false },
        {
          text: 'Reviewed',
          value: 'status',
          filter: (value) => {
            // not shown if tab is
            switch (this.tab) {
              case 0:
                return value === 'Not Assigned Yet';
              case 1:
                return value === 'Not Reviewed Yet';
              case 2:
                return value === 'Done';
              case 3:
                return true;
              default:
                return true;
            }
          },
        },
        {
          text: 'Karil Id',
          value: 'karilId',
          align: ' d-none',
        },
        { text: 'Action', value: 'action', sortable: false },
      ],
      karilList: [],
      search: '',
      // Tabs:
      // 0: Not Assigned Yet
      // 1: Not Reviewed Yet
      // 2: Done
      // 3: All
      tab: 3,
      dosen: false,
      reviewer: false,
      username: null,
      ownerName: '',
      // Who's using it?
      // Admin/SDMPT: 0
      // Reviewer: 1
      // Dosen: 2
      profile: '',
    };
  },
  methods: {
    addRedir() {
      this.$router.push('/add-karil');
    },
    back() {
      this.$router.push('/karil-list');
      this.$router.go();
    },
    setTab(tabNo) {
      this.tab = tabNo;
    },
    assign(karilId) {
      console.log(karilId);
      this.$router.push(`/view-karil?id=${karilId}`);
    },
    userKarils(pemilik) {
      this.$router.push(`/karil-list?username=${pemilik}`);
      this.$router.go();
    },
    reviewerKarils(reviewer) {
      this.$router.push(`/karil-list?reviewer=${reviewer}`);
      this.$router.go();
    },
    donePDF() {
      const doc = new JsPDF({ putOnlyUsedFonts: true, orientation: 'landscape' });
      const label = [
        'no',
        'pemilik',
        'judul',
        'journal_data',
        'link_repo',
        'indexer',
        'link_simcheck',
        'reviewers',
      ];
      const headers = [];
      const doneData = [];
      label.forEach((i) => {
        headers.push({
          id: i,
          name: i,
          prompt: i,
          width: 80,
          align: 'center',
          padding: 0,
        });
      });
      let numb = 1;
      this.karilList.forEach((j) => {
        if (j.status.includes('Done')) {
          doneData.push({
            no: String(numb++),
            pemilik: j.pemilik,
            judul: j.judul,
            journal_data: j.journal_data,
            link_repo: j.link_repo,
            indexer: j.indexer,
            link_simcheck: j.link_simcheck,
            reviewers: j.reviewers,
          });
        }
      });
      console.log(doneData);
      doc.table(1, 1, doneData, headers, { autoSize: true });
      doc.save('DoneKarils.pdf');
    },
  },
  async beforeMount() {
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };

      console.log('First get!');
      await Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          if (res.data.role === 'Reviewer') {
            console.log('First result get!');
            this.profile = 1;
          } else if (res.data.role === 'Dosen') {
            this.profile = 2;
          } else {
            this.profile = 0;
          }
        }
      });

      console.log('Second get!');
      if (this.profile === 1) {
        Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-assigned-karils/`, config).then((res) => {
          if (res.status === 200) {
            console.log('Reviewer get success!');
            console.log(res.data);
            this.karilList = res.data;
          } else {
            this.$router.push('/');
          }
        }).catch((err) => {
          console.log(err);
        });
      } else if (this.profile === 2) {
        Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-karil-summary/`, config).then((res) => {
          if (res.status === 200) {
            console.log('Dosen get success!');
            console.log(res.data);
            this.karilList = res.data;
          } else if (res.status === 204) {
            this.karilList = [];
          } else {
            this.$router.push('/');
          }
        }).catch((err) => {
          console.log(err);
        });
      } else if (this.$route.query.username != null) {
        this.username = this.$route.query.username;
        this.dosen = true;
        const data = {
          username: this.username,
        };
        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-karil-summary/`, data, config).then((res) => {
          if (res.status === 200) {
            console.log(res.data);
            this.karilList = res.data;
          } else {
            this.$router.push('/');
          }
        }).catch((err) => {
          console.log(err);
        });
        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, data, config).then((res) => {
          if (res.status === 200) {
            this.ownerName = res.data.full_name;
          }
        });
      } else if (this.$route.query.reviewer != null) {
        this.username = this.$route.query.reviewer;
        this.reviewer = true;
        const data = {
          username: this.username,
        };
        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-assigned-karils/`, data, config).then((res) => {
          if (res.status === 200) {
            console.log(res.data);
            this.karilList = res.data;
          } else {
            this.$router.push('/');
          }
        }).catch((err) => {
          console.log(err);
        });
        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, data, config).then((res) => {
          if (res.status === 200) {
            this.ownerName = res.data.full_name;
          }
        });
      } else {
        Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, config).then((res) => {
          if (res.status === 200) {
            console.log('Admin get success!');
            console.log(res.data);
            this.karilList = res.data;
          } else {
            this.$router.push('/');
          }
        }).catch((err) => {
          console.log(err);
        });
      }
    }
  },
};
</script>
<style>
  @import '../assets/styles/button.css';
</style>
