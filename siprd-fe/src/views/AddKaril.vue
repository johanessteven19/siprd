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
        <h1>Tambah Karya Ilmiah</h1>
        </v-col>
        <v-col md="1" class="mr-auto">
          <v-btn
            class="mr-4 white--text"
            :disabled="invalid"
            @click="dialog = true"
            color="success"
            width="100%"
          > Submit
          </v-btn>
        </v-col>
        <v-col md="1" class="mr-auto">
          <v-btn
            style='z-index:-0'
            class="mr-4 white--text"
            v-on:click="backRedir"
            :disabled="false"
            color="red"
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
                    class="pb-4"
                    style="z-index: 0"
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
                <v-col md="5" align="center">
                    <h1 class = "Nama pb-4">Identitas Karya Ilmiah</h1>
                </v-col>
            </v-row>
            <v-row align="center" justify="center">
                <v-col md="2" align="center">
                    Nama Penulis
                </v-col>
                <v-col md="3">
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
                <v-col md="2" align="center">
                    Judul Karya Ilmiah
                </v-col>
                <v-col md="3">
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
                  <v-col md="2" align="center">
                      Data Jurnal
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="dataJurnal" placeholder="Data Jurnal" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Link Asli Jurnal
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="linkAsli" placeholder="Link Asli" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Link Repository
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="linkRepo" placeholder="Link Repository" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Link Indexer
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="linkIndexer" placeholder="Link Indexer" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Link Check Similarity
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="linkCheck" placeholder="Link Check" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Link Bukti Korespondensi
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="linkBukti" placeholder="Link Bukti" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="2" align="center">
                      Peng-index
                  </v-col>
                  <v-col md="3">
                      <v-text-field v-model="pengIndex" placeholder="Peng-Index" outlined>
                      </v-text-field>
                  </v-col>
              </v-row>

            <v-row align="center" justify="center">
                <v-col md="2" align="right">
                    Kategori Karya Ilmiah
                </v-col>
                <v-col md="3">
                    <treeselect v-model="kategori" :multiple="false"
                     :options="options" :disable-branch-nodes="true"
                     :show-count="true" placeholder="Kategori*"/>
                </v-col>
            </v-row>
        </div>

          <v-dialog
          v-model="dialog"
          persistent
          max-width="350">
            <v-card class="mx-auto my-0" max-width="350">
              <v-card-title class="justify-center text-h5 ">
                Izin Diperlukan
              </v-card-title>
              <v-card-text style="text-align:center">
                Anda yakin ingin menambah karya ilmiah?
              </v-card-text>
              <v-card-actions class="justify-center">
                <v-btn
                style='z-index:0'
                text
                @click="dialog = false"
                >
                  Kembali
                </v-btn>
                <v-btn
                color="blue"
                text
                type="submit"
                 @click="checkForm();dialog = false"
                >
                  Iya
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-dialog>
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
import Treeselect from '@riophae/vue-treeselect';
import Navigation from '../components/Navigation.vue';
import '@riophae/vue-treeselect/dist/vue-treeselect.css';

extend('required', {
  ...required,
  message: '{_field_} harap diisi.',
});

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'AddKaril',
  components: {
    ValidationProvider,
    ValidationObserver,
    Navigation,
    Treeselect,
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
      promotion: null,
      promotionSelect: ['Asisten Ahli', 'Lektor', 'Lektor Kepala', 'Guru Besar/Professor'],
      status: 'Not Assigned Yet',
      dialog: false,
      // define options
      options: [{
        id: 'Buku',
        label: 'Buku',
        children: [{
          id: 'Buku referensi',
          label: 'Buku referensi',
        }, {
          id: 'Buku monograph',
          label: 'Buku monograph',
        }, {
          id: 'Book chapter (internasional)',
          label: 'Book chapter (internasional)',
        }, {
          id: 'Book chapter (nasional)',
          label: 'Book chapter (nasional)',
        }],
      },
      {
        id: 'Jurnal',
        label: 'Jurnal',
        children: [{
          id: 'Jurnal internasional bereputasi (terindeks pada database internasional bereputasi dan berfaktor dampak)',
          label: 'Jurnal internasional bereputasi (terindeks pada database internasional bereputasi dan berfaktor dampak)',
        }, {
          id: 'Jurnal internasional terindeks pada basis data internasional bereputasi',
          label: 'Jurnal internasional terindeks pada basis data internasional bereputasi',
        }, {
          id: 'Jurnal internasional terindeks pada basis data non bereputasi',
          label: 'Jurnal internasional terindeks pada basis data non bereputasi ',
        }, {
          id: 'Jurnal nasional terakreditasi Kemenristek Dikti',
          label: 'Jurnal nasional terakreditasi Kemenristek Dikti',
        }, {
          id: 'Jurnal nasional terakreditasi Kemenristek Dikti peringkat 1 dan 2',
          label: 'Jurnal nasional terakreditasi Kemenristek Dikti peringkat 1 dan 2',
        }],
      }],
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
          .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviews/`, data, config)
          .then((res) => {
            if (res.status === 201) {
              alert('Karil berhasil disubmit!');
              console.log(res.data);
              console.log('Success');
              this.$router.push('/karil-list');
            }
          })
          .catch((err) => {
            console.log(err.response);
            alert('Masukan nama penulis yang sudah terdaftar.');
          });
      }
    },

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    backRedir() {
      this.$router.push('/karil-list');
    },

  },

};
</script>

<style scoped>
  .identitas{
    background-color: #F9F9F9;
    border-radius: 25px;
    box-shadow: 0 3px 10px rgb(0 0 0 / 0.2);
  }
  .v-btn{
    z-index: 0;
  }
</style>
