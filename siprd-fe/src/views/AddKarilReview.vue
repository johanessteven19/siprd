<template>
  <div>
    <div style="position: fixed; top: 0;">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <validation-observer ref="observer">
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid" lazy-validation>
          <v-row>
            <v-col>
              <h1>Daftar Karya Ilmiah</h1>
            </v-col>
            <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="success"
                  width="100%"
                  @click="dialog = true"
                  > Submit
                </v-btn>
            </v-col>
            <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="red"
                  v-on:click="cancel"
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

          <v-card elevation="2" outlined>
            <div
            class="identitas"
            style="margin-top: 2rem; margin-bottom: 2rem; width: 100%;"
            justify="center">
                <v-row align="center" justify="center" row-gap="10px">
                    <v-col md="5" align="center">
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
          </v-card>
          <v-card>
              <div
              class="identitas"
              style="margin-top: 2rem; margin-bottom: 2rem; width: 100%;"
              justify="center">
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col md="5" align="center">
                        <h1>Hasil Penilaian Validasi</h1>
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        Indikasi Plagiasi
                    </v-col>
                    <v-col md="4" cols="8">
                        <validation-provider
                        v-slot="{ errors }"
                        name="Indikasi Plagiasi"
                        rules="required|double:2,dot|max_value:100|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="plagiasi"
                            placeholder="0-100"
                            suffix="%"
                            required
                            numeric
                            outlined></v-text-field>
                        </validation-provider>
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        Linearitas
                    </v-col>
                    <v-col md="4" cols="8">
                        <validation-provider
                        v-slot="{ errors }"
                        name="Linearitas"
                        rules="required|max:254"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="linearitas"
                            required
                            placeholder="max char: 254"
                            outlined></v-text-field>
                        </validation-provider>
                    </v-col>
                </v-row>
            </div>
          </v-card>
          <v-card>
              <div
              class="identitas"
              style="margin-top: 2rem; margin-bottom: 2rem; width: 100%;"
              justify="center">
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col md="5" align="center">
                        <h1>Hasil Penilaian Peer Review
                          <v-tooltip bottom
                          outlined
                          color="#F5F5F5"
                          content-class="black--text">
                            <template v-slot:activator="{ on, attrs }">
                              <v-icon
                                color="grey"
                                dark
                                v-bind="attrs"
                                v-on="on"
                              >
                                mdi-information
                              </v-icon>
                            </template>
                            <strong>
                              Petunjuk Pengisian Kolom Uraian untuk Penilaian Peer Review<br>
                              1. Kelengkapan dan Kesesuaian Unsur Publikasi (10%)
                            </strong>
                            <ol type="a">
                              <li>
                                Kelengkapan: Sistematika sesuai penulisan Intruction for Authors
                              </li>
                              <li>
                                Kesesuaian: Ada tidak benang merah antara TITLE dengan IMRaDC
                              </li>
                            </ol>
                            <strong>
                              Ruang lingkup,  kedalaman pembahasan, keterbaruan (30%)
                            </strong>
                            <ol type="a">
                              <li>
                                Ruang Lingkup: Kesesuaian Bidang Ilmu Penulis
                              </li>
                              <li>
                                Kedalaman: % (persentase) yang dilibatkan dalam proses membahas
                              </li>
                              <li>
                                Keterbaruan: Keterbaruan artikel yang dibahas
                              </li>
                            </ol>
                            <strong>
                              Kecukupan dan kemutakhiran data/informasi dan metodologi (30%)
                            </strong>
                            <ol type="a">
                              <li>
                                Kecukupan/Kemuktahiran: Tinjauan Pustaka Primer dan masa
                                 (misalnya 5 - 10 tahun terakhir)
                              </li>
                              <li>
                                Metodology: Adakah unsur novelty (inovasi dan invensi)
                              </li>
                            </ol>
                            <strong>
                              Kelengkapan unsur dan kualitas penerbit,  hasil dan manfaat(30%)
                            </strong>
                            <ol type="a">
                              <li>
                                Cek Online Artikel: ada/tidak
                              </li>
                              <li>
                                Cek Kebenaran ISSN/ISBN
                              </li>
                              <li>
                                Cek Apakah termasuk "Predatory"/tidak (baik jurnal maupun penerbit)
                              </li>
                              <li>
                                Cek Konsistensi penulisan antara "Instruction for Author"
                                 dengan fakta artikel
                              </li>
                              <li>
                                Cek Kategori Nasional atau Internasional
                              </li>
                              <li>
                                Cek Indexing Jurnal
                              </li>
                              <li>
                                Cek syarat komposisi "Editor Board"
                              </li>
                              <li>
                                Cek syarat kontributor penulis artikel
                              </li>
                              <li>
                                Cek keberkalaan penerbitan
                              </li>
                            </ol>
                          </v-tooltip>
                        </h1>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col></v-col>
                    <v-col align="center">
                        Kelengkapan dan<br>
                        Kesesuaian Unsur<br>
                        Publikasi
                        <br>(10%)
                    </v-col>
                    <v-col align="center">
                        Ruang lingkup,<br>
                        kedalaman<br>
                        pembahasaan,<br>
                        kebaruan
                        <br>(30%)
                    </v-col>
                    <v-col align="center">
                        Kecupukuan dan<br>
                        kemutakhiran<br>
                        data/infromasi<br>
                        dan metodologi
                        <br>(30%)
                    </v-col>
                    <v-col align="center">
                        Kelengkapan unsur<br>
                        dan kualitas penerbit,<br>
                        hasil dan manfaat
                        <br>(30%)
                    </v-col>
                    <v-col align="center" style="margin-top: 2rem">
                        Total
                    </v-col>
                </v-row>
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        Komentar
                    </v-col>
                    <v-col>
                      <validation-provider
                        v-slot="{ errors }"
                        name="Komen 1"
                        rules="max:254"
                        >
                        <v-textarea
                        :error-messages="errors"
                        placeholder="max char: 254"
                        v-model="komen1"
                        outlined></v-textarea>
                      </validation-provider>
                    </v-col>
                    <v-col>
                      <validation-provider
                        v-slot="{ errors }"
                        name="Komen 2"
                        rules="max:254"
                        >
                        <v-textarea
                        :error-messages="errors"
                        placeholder="max char: 254"
                        v-model="komen2"
                        outlined></v-textarea>
                      </validation-provider>
                    </v-col>
                    <v-col>
                      <validation-provider
                        v-slot="{ errors }"
                        name="Komen 3"
                        rules="max:254"
                        >
                        <v-textarea
                        :error-messages="errors"
                        placeholder="max char: 254"
                        v-model="komen3"
                        outlined></v-textarea>
                      </validation-provider>
                    </v-col>
                    <v-col>
                      <validation-provider
                        v-slot="{ errors }"
                        name="Komen 4"
                        rules="max:254"
                        >
                        <v-textarea
                        :error-messages="errors"
                        placeholder="max char: 254"
                        v-model="komen4"
                        outlined></v-textarea>
                      </validation-provider>
                    </v-col>
                    <v-col></v-col>
                </v-row>
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        Nilai Akhir
                    </v-col>
                    <v-col>
                        <validation-provider
                        v-slot="{ errors }"
                        name="Score 1"
                        rules="required|numeric|max_value:4|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="score1"
                            placeholder="0-4"
                            required
                            numeric
                            outlined
                            @change="numberChange"></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider
                        v-slot="{ errors }"
                        name="Score 2"
                        rules="required|numeric|max_value:12|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="score2"
                            placeholder="0-12"
                            required
                            numeric
                            outlined
                            @change="numberChange"></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider
                        v-slot="{ errors }"
                        name="Score 3"
                        rules="required|numeric|max_value:12|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="score3"
                            placeholder="0-12"
                            required
                            numeric
                            outlined
                            @change="numberChange"></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col>
                        <validation-provider
                        v-slot="{ errors }"
                        name="Score 4"
                        rules="required|numeric|max_value:12|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="score4"
                            placeholder="0-12"
                            required
                            numeric
                            outlined
                            @change="numberChange"></v-text-field>
                        </validation-provider>
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>{{ totalscore }}</strong>
                    </v-col>
                </v-row>
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        Nilai Maksimum
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>4</strong>
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>12</strong>
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>12</strong>
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>12</strong>
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>40</strong>
                    </v-col>
                </v-row>
              </div>
          </v-card>
          <v-card>
              <div
              class="identitas"
              style="margin-top: 2rem; margin-bottom: 2rem; width: 100%;"
              justify="center">
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col md="5" align="center">
                        <h1>Nilai Pengusul</h1>
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        Nilai Pengusul
                    </v-col>
                    <v-col md="4" cols="8">
                        <validation-provider
                        v-slot="{ errors }"
                        name="Nilai Pengusul"
                        rules="required|double:2,dot|max_value:40|min_value:0"
                        >
                            <v-text-field
                            :error-messages="errors"
                            v-model="proposer_score"
                            placeholder="0-40"
                            required
                            numeric
                            outlined></v-text-field>
                        </validation-provider>
                    </v-col>
                </v-row>
            </div>
          </v-card>
          <v-card>
              <div
              class="identitas"
              style="margin-top: 2rem; margin-bottom: 2rem; width: 100%;"
              justify="center">
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col md="5" align="center">
                        <h1>Reviewer</h1>
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        Nama:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ userData.full_name }}
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        NIP:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ userData.nip }}
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="5" align="right">
                        Unit Kerja:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ userData.field_of_study }}, {{ userData.university }}
                    </v-col>
                </v-row>
            </div>
          </v-card>
          <v-dialog
          v-model="dialog"
          persistent
          max-width="350">
            <v-card class="mx-auto my-0" max-width="350">
              <v-card-title class="justify-center text-h5 ">
                Izin Diperlukan
              </v-card-title>
              <v-card-text style="text-align:center">
                Anda yakin selesai review karya ilmiah?
              </v-card-text>
              <v-card-actions class="justify-center">
                <v-btn
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
import {
  required,
  numeric,
  max_value,
  min_value,
  double,
  max,
} from 'vee-validate/dist/rules';
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

extend('numeric', {
  ...numeric,
  message: '{_field_} hanya berupa angka.',
});

extend('max_value', {
  ...max_value,
  message: 'Angka {_field_} terlalu tinggi.',
});

extend('min_value', {
  ...min_value,
  message: 'Angka {_field_} terlalu rendah.',
});

extend('double', {
  ...double,
  message: 'Angka {_field_} hanya boleh 2 angka desimal.',
});

extend('max', {
  ...max,
  message: '{_field_} maksimal 254 karakter.',
});

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'AddKarilReview',
  components: {
    ValidationObserver,
    ValidationProvider,
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
      userData: '',
      plagiasi: null,
      linearitas: null,
      komen1: null,
      komen2: null,
      komen3: null,
      komen4: null,
      score1: 0,
      score2: 0,
      score3: 0,
      score4: 0,
      totalscore: 0,
      proposer_score: 0,
      dialog: false,
    };
  },
  methods: {

    checkForm() {
      this.$refs.observer.validate();
      this.submitForm();
    },

    cancel() {
      this.$router.push(`/view-karil?id=${this.karilId}`);
    },

    numberChange() {
      this.totalscore = parseInt(this.score1, 10)
      + parseInt(this.score2, 10)
      + parseInt(this.score3, 10)
      + parseInt(this.score4, 10);
    },

    submitForm() {
      const data = {
        karil_id: this.karilId,
        reviewer: this.userData.username,
        plagiarism_percentage: this.plagiasi,
        linearity: this.linearitas,
        score_1: this.score1,
        score_2: this.score2,
        score_3: this.score3,
        score_4: this.score4,
        comment_1: this.komen1,
        comment_2: this.komen2,
        comment_3: this.komen3,
        comment_4: this.komen4,
        score_proposer: this.proposer_score,
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
          .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-karil-reviews/`, data, config)
          .then((res) => {
            if (res.status === 201) {
              alert('Review berhasil dibuat!');
              console.log(res.data);
              console.log('Success');
              this.$router.push('/karil-list');
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

  },

  beforeMount() {
    this.karilId = this.$route.query.id;
    console.log(this.karilId);
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const data = {
        karil_id: this.karilId,
      };
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          this.userData = res.data;
        }
      });
      Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-review-form/`, data, config).then((res) => {
        console.log(res.data);
        if (res.status === 200) {
          console.log(res.data);
          this.karilData = res.data;
          console.log(this.karilData);
        }
      });
    } else {
      this.$router.push('/');
    }
  },

};
</script>
