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
          <h1>Detail Karya Ilmiah</h1>
          </v-col>
          <v-col md="1" class="mr-auto">
            <v-btn
              class="mr-4 white--text"
              :disabled="invalid"
              type=""
              color="success"
              width="100%"
            >
            </v-btn>
          </v-col>
          <v-col md="1" class="mr-auto">
            <v-btn
              class="mr-4 white--text"
              :disabled="false"
              color="red"
              width="100%"
            > Cancel
            </v-btn>
          </v-col>
          </v-row>

          <v-row >
              <v-col md="3" class="mr-auto">
                  Dosen:Doni <br>
                  Jabatan:Lektor <br>
                  Kenaikan Jabatan: Lektor Kepala
              </v-col>
          </v-row>
          <br>

          <div class="identitas" style="margin-top: 2rem; width: 100%;" justify="center">
              <v-row align="center" justify="center" row-gap="10px">
                  <v-col md="5" align="right">
                      <h1>Identitas Karya Ilmiah</h1> <br>
                  </v-col>
              </v-row>
              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Nama Penulis
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="namaPenulis" placeholder="Nama Penulis" readonly>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Judul Karya Ilmiah
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="judulKaril" placeholder="Judul Karil" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Data Jurnal
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="dataJurnal" placeholder="Data Jurnal" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Asli Jurnal
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="linkAsli" placeholder="Link Asli" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Repository
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="linkRepo" placeholder="Link Repository" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Indexer
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="linkIndexer" placeholder="Link Indexer" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Check Similarity
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="linkCheck" placeholder="Link Check" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Bukti Korespondensi
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="linkBukti" placeholder="Link Bukti" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Peng-index
                  </v-col>
                  <v-col md="2">
                      <v-text-field v-model="pengIndex" placeholder="Peng-Index" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Kategori Karya Ilmiah
                  </v-col>
                  <v-col md="2">
                    <v-select
                      v-model="kategori"
                      :items="kategoriSelect"
                      label="Kategori Karil"
                      data-vv-name="select"
                      outlined
                    >
                    </v-select>
                  </v-col>
              </v-row>

          </div>

          <div class="reviewer" style="margin-top: 2rem; width: 100%;" justify="center">
              <v-row align="center" justify="center" row-gap="10px">
                  <v-col md="3" align="right">
                      <h1>Reviewer</h1> <br>
                  </v-col>
              </v-row>
              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Nama Reviewer 1
                  </v-col>
                  <v-col md="2">
                    <v-select
                      v-model="reviewer"
                      :items="reviewerSelect"
                      label="Reviewer"
                      data-vv-name="select"
                      outlined
                    >
                    </v-select>
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
  name: 'ViewKaril',
  components: {
    ValidationObserver,
    Navigation,
  },
  data() {
    return {
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
    submitForm() {
      const data = {

        pemilik: this.namaPenulis,
        judul: this.judulKaril,
        journal_data: this.dataJurnal,
        link_origin: this.linkAsli,
        link_repo: this.linkRepo,
        link_indexer: this.linkIndexer,
        link_simcheck: this.linkCheck,
        link_correspondence: this.linkBukti,
        indexer: this.pengIndex,
        category: this.kategori,
        status: this.status,
      };
      if (localStorage.access) {
        const accessToken = localStorage.access;
        console.log('something');
        const config = {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        };
        Vue.axios
          .put(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, data, config)
          .then((res) => {
            console.log(res.data);
            if (res.status === 200) {
              this.$router.push('/Success');
            } else {
              alert('Gagal');
            }
          })

          .catch((err) => {
            // TODO: Make this output more user-friendly!!!
            // Clean string up with a function?
            console.log(err);
            // var responseErrors = JSON.stringify(err.response.data);
            // console.log(responseErrors);
            // var errMsg = "Edit gagal, errors: " + responseErrors;
            // alert(errMsg);
          });
      }
    },

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

  },

  beforeMount() {
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const data = {
        karil_id: this.karilId,
      };
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-review-form/`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          // this.namaPenulis = res.data.pemilik;
          // this.position = res.data.position;
        }
      });
    } else {
      this.$router.push('/');
    }
  },

};
</script>
