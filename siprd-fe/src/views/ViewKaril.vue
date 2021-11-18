<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <validation-observer ref="observer">
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
          <v-row>
          <v-col>
          <h1>Daftar Karya Ilmiah</h1>
          </v-col>
          <v-col md="2" class="mr-auto">
            <v-btn
              class="mr-4 white--text"
              color="blue"
              width="100%"
            > Download to Excel
            </v-btn>
          </v-col>
          <v-col md="2" class="mr-auto">
            <v-btn
              class="mr-4 white--text"
              color="purple"
              v-on:click="editKaril(karilData.karil_id)"
              width="100%"
            > Edit Karya Ilmiah
            </v-btn>
          </v-col>
          <v-col md="2" class="mr-auto">
            <v-btn
              class="mr-4 white--text"
              v-on:click="assignReviewer(karilData.karil_id)"
              color="success"
              width="100%"
            > Assign Reviewer
            </v-btn>
          </v-col>
          </v-row>
          <v-row>
            <v-col md="2" class="mr-auto">
            <v-btn
              class="mr-auto white--text"
              v-on:click="deleteKaril(karilData.karil_id)"
              color="error"
              width="100%"
            > Hapus
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
      userData: '',
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
    };
  },
  methods: {

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    editKaril(karilId) {
      this.$router.push(`/edit-karil?id=${karilId}`);
    },

    assignReviewer(karilId) {
      this.$router.push(`/assign-reviewer?id=${karilId}`);
    },

    deleteKaril(karilId) {
      console.log(karilId);
      if (localStorage.access) {
        const accessToken = localStorage.access;

        Vue.axios.delete(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
          data: {
            karil_id: this.karilId,
          },
        }).then((res) => {
          console.log(res.data);
          if (res.status === 200) {
            alert(
              ' Karil berhasil dihapus!',
            );
          }
        })
          .catch((err) => {
            console.log(err.response);
          });
      }
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
