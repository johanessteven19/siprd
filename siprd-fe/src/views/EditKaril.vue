<template>
  <div>
        <div style="position: fixed; top: 0;">
          <Navigation />
        </div>
  <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid" lazy-validation>
        <v-row>
        <v-col>
        <h1>Edit Karya Ilmiah</h1>
        </v-col>
        <v-col md="1" class="mr-auto">
          <v-btn
            class="mr-4 white--text"
            :disabled="invalid"
            type="submit"
            color="success"
            width="100%"
          > Edit
          </v-btn>
        </v-col>
        <v-col md="1" class="mr-auto">
          <v-btn
            class="mr-4 white--text"
            :disabled="false"
            color="red"
            v-on:click="cancel"
            width="100%"
          > Cancel
          </v-btn>
        </v-col>
        </v-row>

        <v-row>
            <v-col md="3" class="mr-auto">
              <validation-provider
                v-slot="{ errors }"
                name="Jabatan"
                rules="required"
              >
                  <v-select
                    v-model="promotion"
                    :items="promotionSelect"
                    :error-messages="errors"
                    label="Pilih jabatan yang dituju*"
                    data-vv-name="select"
                    required
                    outlined
                  >
                  </v-select>
              </validation-provider>
            </v-col>
        </v-row>

        <div class="identitas" justify="center">
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
                  <validation-provider
                    v-slot="{ errors }"
                    name="Nama penulis"
                    rules="required"
                  >
                    <v-text-field v-model="namaPenulis"
                      :error-messages="errors"
                      placeholder="Nama Penulis*"
                      required
                      outlined>
                    </v-text-field>
                  </validation-provider>
                </v-col>
            </v-row>

            <v-row align="center" justify="center">
                <v-col md="3" align="right">
                    Judul Karya Ilmiah
                </v-col>
                <v-col md="2">
                  <validation-provider
                    v-slot="{ errors }"
                    name="Judul karil"
                    rules="required"
                  >
                    <v-text-field v-model="judulKaril"
                    :error-messages="errors"
                    placeholder="Judul Karil*"
                    required
                    outlined>
                    </v-text-field>
                  </validation-provider>
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
                  <validation-provider
                    v-slot="{ errors }"
                    name="Kategori Karil"
                    rules="required"
                  >
                    <v-select
                      v-model="kategori"
                      :error-messages="errors"
                      :items="kategoriSelect"
                      label="Kategori Karil*"
                      data-vv-name="select"
                      outlined
                    >
                    </v-select>
                  </validation-provider>
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
import { required } from 'vee-validate/dist/rules';
import {
  extend,
  ValidationObserver,
  ValidationProvider,
} from 'vee-validate';
import Navigation from '../components/Navigation.vue';

extend('required', {
  ...required,
  message: '{_field_} harap diisi.',
});

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'EditKaril',
  components: {
    ValidationProvider,
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
      kategoriSelect: ['Buku', 'Jurnal'],
      promotion: null,
      promotionSelect: ['Asisten Ahli', 'Lektor', 'Lektor Kepala', 'Guru Besar/Professor'],
      status: 'Not Reviewed Yet',
      karilId: null,
    };
  },
  methods: {
    submitForm() {
      const data = {
        karil_id: this.karilId,
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
        promotion: this.promotion,
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
        console.log(data);
        Vue.axios
          .put(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, data, config)
          .then((res) => {
            if (res.status === 200) {
              alert('Karil berhasil diedit!');
              console.log(res.data);
              console.log('Success');
              this.$router.push(`/view-karil?id=${this.karilId}`);
            } else {
              console.log(res.data);
              console.log(res.status);
              alert('Try Again.');
            }
          })
          .catch((err) => {
            console.log(err.response);
          });
      }
    },

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    cancel() {
      this.$router.push(`/view-karil?id=${this.karilId}`);
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
          console.log(res.data);
          this.karilData = res.data;
          console.log(this.karilData);
          this.namaPenulis = this.karilData.pemilik;
          this.judulKaril = this.karilData.judul;
          this.dataJurnal = this.karilData.journal_data;
          this.linkAsli = this.karilData.linkAsli;
          this.linkRepo = this.karilData.link_repo;
          this.linkIndexer = this.karilData.link_indexer;
          this.linkCheck = this.karilData.link_simcheck;
          this.linkBukti = this.karilData.link_correspondence;
          this.pengIndex = this.karilData.indexer;
          this.kategori = this.karilData.category;
          this.promotion = this.karilData.promotion;
          this.status = this.karilData.status;
        }
      });
    } else {
      this.$router.push('/');
    }
  },

};
</script>
