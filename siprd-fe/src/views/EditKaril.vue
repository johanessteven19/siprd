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
                <v-col md="5" align="center">
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
                <v-col md="2" align="right">
                    Kategori Karya Ilmiah
                </v-col>
            </v-row>
            <v-row align="center" justify="center">
                <v-col md="10">
                    <treeselect v-model="kategori" :multiple="false"
                     :options="options" :disable-branch-nodes="true"
                     :show-count="true" placeholder="Kategori*">
                     <div slot="value-label" slot-scope="{ node }">{{ node.raw.customLabel }}</div>
                    </treeselect>
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
  name: 'EditKaril',
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
      kategoriSelect: ['Buku', 'Jurnal'],
      promotion: null,
      promotionSelect: ['Asisten Ahli', 'Lektor', 'Lektor Kepala', 'Guru Besar/Professor'],
      status: 'Not Reviewed Yet',
      karilId: null,
      // define options
      options: [{
        id: 'Buku',
        label: 'Buku',
        children: [{
          id: 'Buku referensi',
          label: 'Buku referensi',
          customLabel: 'Buku referensi',
        }, {
          id: 'Buku monograph',
          label: 'Buku monograph',
          customLabel: 'Buku monograph',
        }, {
          id: 'Book chapter',
          label: 'Book chapter',
          children: [{
            id: 'Book chapter-nasional',
            label: 'Nasional',
            customLabel: 'Book Chapter - Nasional',
          }, {
            id: 'Book chapter-internasional',
            label: 'Internasional',
            customLabel: 'Book chapter - Internasional',
          }],
        }],
      },
      {
        id: 'Jurnal',
        label: 'Jurnal',
        children: [{
          id: 'Internasional',
          label: 'Internasional',
          children: [
            {
              id: 'Jurnal internasional bereputasi (terindeks pada database internasional bereputasi dan berfaktor dampak)',
              label: 'Bereputasi (terindeks pada database internasional bereputasi dan berfaktor dampak)',
            },
            {
              id: 'Terindex',
              label: 'Terindex',
              children: [
                {
                  id: 'Jurnal Internasional Terindex di DB bereputasi',
                  label: 'Pada database bereputasi',
                  customLabel: 'Jurnal Internasional Terindex di DB bereputasi',
                },
                {
                  id: 'Jurnal Internasional Terindex di DB non-reputasi',
                  label: 'Pada database tidak bereputasi',
                  customLabel: 'Jurnal Internasional Terindex di DB non-reputasi',
                }],
            }, {
              id: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan - Internasional',
              label: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan',
              customLabel: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan - Internasional',
            }, {
              id: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional',
              label: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN)',
              customLabel: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional',
              children: [{
                id: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional - terindeks pada Scimagojr dan Scopus',
                label: 'Terindeks pada Scimagojr dan Scopus',
                customLabel: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional - terindeks pada Scimagojr dan Scopus',
              }, {
                id: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional - terindeks pada Scopus/IEEE Explore/SPIE',
                label: 'Terindeks pada Scopus/IEEE Explore/SPIE',
                customLabel: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Internasional - terindeks pada Scopus/IEEE Explore/SPIE',
              }],
            }, {
              id: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan - Internasional',
              label: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan (bukti sertifikat)',
              customLabel: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan - Internasional',
            }, {
              id: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding - Internasional',
              label: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding ',
              customLabel: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding - Internasional',
            }, {
              id: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Internasional',
              label: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda',
              customLabel: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Internasional',
            }, {
              id: 'HAKI - Membuat rancangan dan karya teknologi yang dipatenkan atau seni yang terdaftar di HAKI - Internasional',
              label: 'HAKI - Membuat rancangan dan karya teknologi yang dipatenkan atau seni yang terdaftar di HAKI (diakui min. 4 negara)',
              customLabel: 'HAKI - Membuat rancangan dan karya teknologi yang dipatenkan atau seni yang terdaftar di HAKI - Internasional',
            },
          ],
        }, {
          id: 'Nasional',
          label: 'Nasional',
          children: [
            {
              id: 'Terakreditasi',
              label: 'Terakreditasi',
              children: [
                {
                  id: 'Jurnal Nasional Terakreditasi oleh Kemenristekdikti',
                  label: 'Oleh Kemenristekdikti',
                  customLabel: 'Jurnal Nasional Terakreditasi oleh Kemenristekdikti',
                },
                {
                  id: 'Jurnal Nasional Terakreditasi oleh Kemenristekdikti peringkat 1 dan 2',
                  label: 'Oleh Kemenristekdikti peringkat 1 dan 2',
                  customLabel: 'Jurnal Nasional Terakreditasi oleh Kemenristekdikti peringkat 1 dan 2',
                }],
            },
            {
              id: 'Jurnal Nasional',
              label: 'Jurnal Nasional',
              customLabel: 'Jurnal Nasional',
            },
            {
              id: 'Jurnal nasional terindex di Kemenristekdikti approved DB ',
              label: 'Jurnal nasional terindex pada basis data yang diakui Kemenristekdikti',
              children: [
                {
                  id: 'Jurnal nasional berbahasa Inggris atau bahasa resmi (PBB) terindeks pada basis data yang diakui Kemenristekdikti',
                  label: 'Bahasa Inggris',
                  customLabel: 'Jurnal nasional berbahasa Inggris atau bahasa resmi (PBB) terindeks pada basis data yang diakui Kemenristekdikti',
                },
                {
                  id: 'Jurnal nasional berbahasa Indonesia terindeks pada basis data yang diakui Kemenristekdikti',
                  label: 'Bahasa Indonesia',
                  customLabel: 'Jurnal nasional berbahasa Indonesia terindeks pada basis data yang diakui Kemenristekdikti',
                }],
            },
            {
              id: 'Jurnal ilmiah yang ditulis dalam Bahasa Resmi PBB namun tidak memenuhi syarat syarat sebagai jurnal ilmiah internasional',
              label: 'Jurnal ilmiah yang ditulis dalam Bahasa Resmi PBB namun tidak memenuhi syarat syarat sebagai jurnal ilmiah internasional',
              customLabel: 'Jurnal ilmiah yang ditulis dalam Bahasa Resmi PBB namun tidak memenuhi syarat syarat sebagai jurnal ilmiah internasional',
            }, {
              id: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Nasional',
              label: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN)',
              customLabel: 'Dipresentasikan secara oral dan dimuat dalam prosiding yang dipublikasikan (ber ISSN/ISBN) - Nasional',
            }, {
              id: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan - Nasional',
              label: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan',
              customLabel: 'Disajikan dalam bentuk poster dan dimuat dalam prosiding yang dipublikasikan - Nasional',
            }, {
              id: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan - Nasional',
              label: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan (bukti sertifikat)',
              customLabel: 'Disajikan dalam seminar/simposium/lokakarya, tetapi tidak dimuat dalam prosiding yang dipublikasikan - Nasional',
            }, {
              id: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding - Nasional',
              label: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding',
              customLabel: 'Hasil penelitian/pemikiran yang tidak disajikan dalam seminar/simposium/lokakarya tetapi dimuat dalam prosiding - Nasional',
            }, {
              id: 'HAKI',
              label: 'HAKI - Membuat rancangan dan karya teknologi yang dipatenkan atau seni yang terdaftar di HAKI',
              children: [{
                id: 'Nasional',
                label: 'Nasional',
                customLabel: 'HKI - Nasional',
              }, {
                id: 'HAKI- Nasional, dalam bentuk paten sederhana yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham',
                label: 'Nasional, dalam bentuk paten sederhana yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham',
                customLabel: 'HKI - Nasional - Paten sederhana yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham',
              }, {
                id: 'HAKI - Karya ciptaan desain industri, indikasi geografis yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham ',
                label: 'Karya ciptaan desain industri, indikasi geografis yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham ',
                customLabel: 'HKI - Karya ciptaan desain industri, indikasi geografis yang telah memiliki sertifikat dari Direktorat Jenderal Kekayaan Intelektual, Kemenkumham',
              }],
            }, {
              id: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Nasional',
              label: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda',
              customLabel: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Nasional',
            },
          ],
        }, {
          id: 'Hasil penelitian/pemikiran yang disajikan dalam koran/majalah populer/umum',
          label: 'Hasil penelitian/pemikiran yang disajikan dalam koran/majalah populer/umum',
          children: [{
            id: 'Hasil penelitian atau pemikiran atau kerjasama industri yang tidak dipublikasikan (tersimpan dalam perpustakaan) yang dilakukan secara melembaga',
            label: 'Tidak dipublikasikan (tersimpan dalam perpustakaan) yang dilakukan secara melembaga',
            customLabel: 'Hasil penelitian atau pemikiran atau kerjasama industri yang tidak dipublikasikan (tersimpan dalam perpustakaan) yang dilakukan secara melembaga',
          }, {
            id: 'Menerjemahkan/menyadur buku ilmiah, Diterbitkan dan diedarkan secara nasional',
            label: 'Menerjemahkan/menyadur buku ilmiah, Diterbitkan dan diedarkan secara nasional',
            customLabel: 'Menerjemahkan/menyadur buku ilmiah, Diterbitkan dan diedarkan secara nasional',
          }, {
            id: 'Mengedit/menyunting karya ilmiah, Diterbitkan dan diedarkan secara nasional',
            label: 'Mengedit/menyunting karya ilmiah, Diterbitkan dan diedarkan secara nasional',
            customLabel: 'Mengedit/menyunting karya ilmiah, Diterbitkan dan diedarkan secara nasional',
          }],
        }, {
          id: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda',
          label: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda',
          children: [{
            id: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Lokal',
            label: 'Lokal',
            customLabel: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda - Lokal',
          }, {
            id: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda -Rancangan dan karya seni yang tidak terdaftar HAKI',
            label: 'Rancangan dan karya seni yang tidak terdaftar HAKI',
            customLabel: 'Membuat rancangan dan karya teknologi yang tidak dipatenkan tetapi telah dipresentasikan pada forum yang teragenda -Rancangan dan karya seni yang tidak terdaftar HAKI',
          }],
        }],
      },
      ],
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
