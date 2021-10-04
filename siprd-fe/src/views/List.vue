<template>
  <v-data-table
    :headers="headers"
    :items="users"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>

<script>
    import Vue from "vue";
    import axios from "axios";
    import VueAxios from "vue-axios";
    import Vuetify from "vuetify";
    import { required, digits, email, max, regex } from 'vee-validate/dist/rules'
    import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  export default {
    name:"List",
    data () {
      return {
        headers: [  
          {
            text: 'Email',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        users: [],
        error: "",
        state: "loading"
      }
    },
    created () {
      this.loadAllUsers();
    },
    methods: {
      loadAllUsers(){
          Vue.axios.get("http://localhost:8000/api/alluser").then((res)=>{
              console.log("masuk")
              console.log(res.data[0])
              this.users = res.data;
              this.state = "ready";
                })
            },
      }
  }
</script>