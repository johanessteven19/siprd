<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <validation-observer ref="observer" v-slot="{ invalid }">
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
          <v-row>
          <v-col>
          <h1>Daftar Karya Ilmiah</h1>
          </v-col>
            <v-col md="1" class="mr-auto">
              <v-btn
                class="mr-4 white--text"
                :disabled="invalid"
                type="submit"
                color="success"
                width="100%"
              > Accept
              </v-btn>
            </v-col>
            <v-col md="1" class="mr-auto">
              <v-btn
                class="mr-4 white--text"
                :disabled="false"
                v-on:click="cancel"
                color="red"
                width="100%"
              > Cancel
              </v-btn>
            </v-col>
          </v-row>

          <v-row >
              <v-col md="3" class="mr-auto">
                  Dosen : {{ karilData.pemilik }} <br>
                  Jabatan: {{ karilData.position }} <br>
                  Kenaikan Jabatan: {{ karilData.promotion }}
              </v-col>
          </v-row>

          <div class="identitas" style="margin-top: 2rem; width: 100%;" justify="center">
              <v-row align="center" justify="center" row-gap="10px">
                  <v-col md="5" align="right">
                      <h1>Identitas Karya Ilmiah</h1>
                  </v-col>
              </v-row>
              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Nama Penulis
                  </v-col>
                  <v-col md="2">
                      {{ karilData.pemilik }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Judul Karya Ilmiah
                  </v-col>
                  <v-col md="2">
                      {{ karilData.judul }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Data Jurnal
                  </v-col>
                  <v-col md="2">
                      {{karilData.journal_data}}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Asli Jurnal
                  </v-col>
                  <v-col md="2">
                      {{ karilData.link_origin }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Repository
                  </v-col>
                  <v-col md="2">
                      {{ karilData.link_repo }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Indexer
                  </v-col>
                  <v-col md="2">
                      {{ karilData.link_indexer }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Check Similarity
                  </v-col>
                  <v-col md="2">
                      {{ karilData.link_simcheck }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Bukti Korespondensi
                  </v-col>
                  <v-col md="2">
                      {{ karilData.link_correspondence }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Peng-index
                  </v-col>
                  <v-col md="2">
                      {{ karilData.indexer }}
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Kategori Karya Ilmiah
                  </v-col>
                  <v-col md="2">
                    {{ karilData.category }}
                  </v-col>
              </v-row>

          </div>

          <div class="reviewers" style="margin-top: 2rem; width: 100%;" justify="center">
              <v-row align="center" justify="center" row-gap="10px">
                  <v-col md="3" align="right">
                      <h1>Reviewer</h1> <br>
                  </v-col>
              </v-row>

              <div class="reviewArea" v-for="reviewer in reviewers" :key="reviewer.id">
              <v-row align="center" justify="center">
                  <v-col md="3" align="right" :for="reviewer.id">
                      {{reviewer.label}}
                  </v-col>
                  <v-col md="2">
                    <v-select
                      :id="reviewer.id"
                      v-model="reviewer.value"
                      :items="reviewerSelect"
                      label="Reviewer"
                      data-vv-name="select"
                      outlined
                    >
                    </v-select>
                  </v-col>
              </v-row>
              </div>

              <v-row align="center" justify="center">
                  <v-col md="4" align="right">
                    <v-btn
                      class="mr-5 white--text"
                      v-on:click="addNew"
                      color="purple"
                    > + Tambah Reviewer
                    </v-btn>
                  </v-col>
              </v-row>

          </div>
        </v-form>

      </validation-observer>

    </v-container>
  </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';
import {
  ValidationObserver,
} from 'vee-validate';
import Navigation from '../components/Navigation.vue';

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'AssignReviewer',
  components: {
    ValidationObserver,
    Navigation,
  },
  data() {
    return {
      karilData: '',
      namaPenulis: null,
      judulKaril: null,
      dataJurnal: null,
      linkAsli: null,
      linkRepo: null,
      linkIndexer: null,
      linkCheck: null,
      linkBukti: null,
      pengIndex: null,
      kategori: null,
      status: 'Requested',
      karilId: null,
      counter: 0,
      reviewers: [{
        id: 'reviewer0',
        label: 'Nama Reviewer',
        value: '',
      }],
    };
  },
  methods: {
    // submitForm() {
    //   const data = {

    //     pemilik: this.namaPenulis,
    //     judul: this.judulKaril,
    //     journal_data: this.dataJurnal,
    //     link_origin: this.linkAsli,
    //     link_repo: this.linkRepo,
    //     link_indexer: this.linkIndexer,
    //     link_simcheck: this.linkCheck,
    //     link_correspondence: this.linkBukti,
    //     indexer: this.pengIndex,
    //     category: this.kategori,
    //     status: this.status,
    //   };
    //   if (localStorage.access) {
    //     const accessToken = localStorage.access;
    //     console.log('something');
    //     const config = {
    //       headers: {
    //         Authorization: `Bearer ${accessToken}`,
    //       },
    //     };
    //     Vue.axios
    //       .put(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, data, config)
    //       .then((res) => {
    //         console.log(res.data);
    //         if (res.status === 200) {
    //           this.$router.push('/your-account');
    //         } else {
    //           alert('Gagal');
    //         }
    //       })

    //       .catch((err) => {
    //         // TODO: Make this output more user-friendly!!!
    //         // Clean string up with a function?
    //         console.log(err);
    //         // var responseErrors = JSON.stringify(err.response.data);
    //         // console.log(responseErrors);
    //         // var errMsg = "Edit gagal, errors: " + responseErrors;
    //         // alert(errMsg);
    //       });
    //   }
    // },

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    editKaril() {
      this.$router.push('/edit-karil');
    },

    cancel() {
      this.$router.push(`/view-karil?id=${this.karilId}`);
    },

    addNew() {
      this.reviewers.push({
        id: `reviewer${++this.counter}`,
        label: 'Nama Reviewer',
        value: '',
      });
    },

  },

  beforeMount() {
    this.karilId = this.$route.query.id;
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const data = {
        karil_id: this.karilId,
      };
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-review-form/`, data, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.karilData = res.data;
        }
      });
    } else {
      this.$router.push('/');
    }
  },

};
</script>
