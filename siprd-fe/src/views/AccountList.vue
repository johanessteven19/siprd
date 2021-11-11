<template>
  <div>
    <div style="position: fixed; top: 0;">
    <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <v-row>
        <v-col md="2">
        <h1>Daftar Akun</h1>
        </v-col>
        <v-col md="2">
          <v-btn
            class="mr-4 white--text"
            :disabled="false"
            color="blue"
            width="100%"
            v-on:click="addRedir"
          > + Tambah Akun
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col md="2">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': !show_only_unapproved,
              'white--text': !show_only_unapproved
              }"
            :outlined="show_only_unapproved"
            color="#8D38E3"
            width="100%"
            v-on:click="toggleListTab"
          > Belum Disetujui
          </v-btn>
        </v-col>
        <v-col md="2">
          <v-btn
            class="mr-4"
            :class="{
              'disable-events': show_only_unapproved,
              'white--text': show_only_unapproved
              }"
            :outlined="!show_only_unapproved"
            color="#8D38E3"
            width="100%"
            v-on:click="toggleListTab"
          > Semua Akun
          </v-btn>
        </v-col>
      </v-row>
      <br>
      <v-data-table
        :page="page"
        :headers="headers"
        :items="users"
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

      <template v-slot:item.action="{ item }">
        <template v-if="show_only_unapproved">
          <v-btn
            depressed
            color="success"
          >
            Ubah
          </v-btn>
        </template>
        <template v-else>
          <v-btn
            depressed
            color="success"
          >
            Setujui
          </v-btn>
        </template>
        <template v-if="item.username != userData.username">
          <v-btn
          color="error"
          dark
          @click="setItem(item); dialog = true"
          >
            Hapus
          </v-btn>
        </template>
        <template v-else>
          <v-btn
          color="error"
          disabled>
            Hapus
          </v-btn>
        </template>
      </template>
      </v-data-table>
      <v-dialog
      v-model="dialog"
      persistent>
        <v-card>
          <v-card-title class="text-h5">
            Izin Diperlukan
          </v-card-title>
          <v-card-text>Anda yakin ingin menghapus akun?</v-card-text>
          <v-card-actions>
            <v-btn
            text
            @click="cancelItem(); dialog = false"
            >
              Kembali
            </v-btn>
            <v-btn
            color="blue"
            text
            @click="deleteUser(item);dialog = false"
            >
              Iya
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
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
        { text: 'Email', value: 'email', sortable: false },
        { text: 'Username', value: 'username', sortable: false },
        { text: 'Nama', value: 'full_name', sortable: false },
        { text: 'Universitas', value: 'university', sortable: false },
        { text: 'NIP', value: 'nip', sortable: false },
        { text: 'Bidang Keahlian', value: 'field_of_study', sortable: false },
        { text: 'Jabatan Akademik', value: 'position', sortable: false },
        { text: 'Role', value: 'role', sortable: false },
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
      users: [],
      search: '',
      show_only_unapproved: false,
      userData: '',
      dialog: false,
      item: '',
    };
  },
  methods: {
    addRedir() {
      this.$router.push('/add-account');
    },
    toggleListTab() {
      this.show_only_unapproved = !this.show_only_unapproved;
    },
    deleteUser(item) {
      console.log(item);
      // const data = {
      //   username: item.username,
      // };
      if (localStorage.access) {
        const accessToken = localStorage.access;
        // const config = {
        //   headers: { Authorization: `Bearer ${accessToken}` },
        // };
        Vue.axios.delete(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-users/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
          data: {
            username: item.username,
          },
        }).then((res) => {
          if (res.status === 200) {
            alert(
              'Akun berhasil dihapus!',
            );
            this.$router.push('/account-list');
          } else if (res.status === 404) {
            alert(
              'Akun tidak ada di database',
            );
          }
        })
          .catch((err) => {
            // something went horribly wrong!
            console.log(err.response);
            alert('Maaf, server SIPEERKI tidak dapat dihubungi.');
          });
      }
    },
    setItem(item) {
      this.item = item;
    },
    cancelItem() {
      this.item = '';
    },
  },
  beforeMount() {
    if (localStorage.access) {
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
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-users/`, config).then((res) => {
        if (res.status === 200) {
          console.log(res.data);
          this.users = res.data;
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
