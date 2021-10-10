<template>
  <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
    <v-row>
    <v-col>
    <h1>Daftar Akun</h1>
    </v-col>
    <v-col md="2" class="mr-auto">
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

      <template v-slot:item.action>
    <v-btn
      depressed
      color="success"
    >
      Approve
    </v-btn>
        <v-btn
      depressed
      color="error"
      @click.stop=""
    >
      Delete
    </v-btn>
      </template>
    
    </v-data-table>
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import Vuetify from "vuetify";


Vue.use(Vuetify);
Vue.use(VueAxios, axios)

export default {
  name: "table-list",
  data() {
    return {
      headers: [
        { text: "No.", sortable: false, value: "no" },
        { text: "Email", value: "email", sortable: false },
        { text: "Username", value: "username", sortable: false },
        { text: "Nama", value: "full_name", sortable: false },
        { text: "Universitas", value: "university", sortable: false },
        { text: "NIP", value: "nip", sortable: false },
        { text: "Bidang Keahlian", value: "field_of_study", sortable: false },
        { text: "Jabatan Akademik", value: "position", sortable: false },
        { text: "Role", value: "role", sortable: false },
        { text: "Action", value: "action", sortable: false },
      ],
      users:[],
      search:""
    }
  },
  methods:{
    addRedir: function (e) {
      this.$router.push("/add-account");
    },
  },
  beforeMount() {
    if (localStorage.access){
      const accessToken = localStorage.access;
      const config = {
        headers : { Authorization: "Bearer " + accessToken },
      };

      Vue.axios.get(( process.env.VUE_APP_BACKEND_URL || "" )+"/api/manage-users/", config).then((res) => {
        if (res.status === 200){
          console.log(res.data)
          this.users = res.data;
        }else{
          this.$router.push("/");
        }

      }).catch((err) => {
        console.log(err);
      });

    }
    
    
  },
  
}
</script>