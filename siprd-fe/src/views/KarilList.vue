<template>
  <div>
    <div style="position: fixed; top: 0;">
    <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <v-row>
        <v-col md="4">
        <h1>Daftar Karya Ilmiah</h1>
        </v-col>
        <v-col md="4">
          <v-btn
            class="mr-4 white--text"
            :disabled="false"
            color="blue"
            width="100%"
            v-on:click="addRedir"
          > + Tambah Karya Ilmiah
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col md="2">
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
      </v-row>
      <br>
      <v-data-table
        :page="page"
        :headers="headers"
        :items="karilList"
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

      <template v-slot:item.action>
        <template v-if="show_only_unapproved">
          <v-btn
            depressed
            color="success"
          >
            Setujui
          </v-btn>
          <v-btn
            depressed
            color="error"
            @click.stop=""
          >
            Hapus
          </v-btn>
        </template>
        <template v-else>
          <v-btn
            depressed
            color="success"
          >
            Ubah
          </v-btn>
          <v-btn
            depressed
            color="error"
            @click.stop=""
          >
            Hapus
          </v-btn>
        </template>
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
        { text: 'Reviewer', value: 'reviewer', sortable: false },
        { text: 'Reviewed', value: 'status', sortable: false },
        {
          text: 'Disetujui',
          value: 'approved',
          filter: (value) => {
            // not shown if tab is
            if (!this.show_only_unapproved && value) {
              return false;
            } return true;
          },
          // Used to hide column from table
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
    };
  },
  methods: {
    addRedir() {
      this.$router.push('/add-karil');
    },
    setTab(tabNo) {
      this.tab = tabNo;
    },
  },
  beforeMount() {
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };

      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, config).then((res) => {
        if (res.status === 200) {
          console.log(res.data);
          this.karilList = res.data;
        } else {
          this.$router.push('/');
        }
      }).catch((err) => {
        console.log(err);
      });
    }
  },
};
</script>
<style>
  @import '../assets/styles/button.css';
</style>
