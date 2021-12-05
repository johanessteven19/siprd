<template>
  <div>
    <div style="position: fixed; top: 0; z-index: 100">
      <Navigation />
    </div>
    <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
      <validation-observer ref="observer">
        <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
          <v-row>
            <v-col>
              <h1>Daftar Karya Ilmiah</h1>
            </v-col>
            <template v-if="userData.role === 'Reviewer'">
              <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="blue"
                  width="100%"
                  v-on:click="downloadExcel()"
                  > Download to Excel
                </v-btn>
              </v-col>
              <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="purple"
                  v-on:click="reviewKaril(karilData.karil_id)"
                  width="100%"
                  > Review
                </v-btn>
              </v-col>
              <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="success"
                  width="100%"
                  > Upload From Excel
                </v-btn>
              </v-col>
            </template>
            <template v-else>
              <v-col md="2" class="mr-auto">
                <v-btn
                  v-if="userData.role === 'Admin'"
                  class="mr-4 white--text"
                  v-on:click="assignReviewer(karilData.karil_id)"
                  color="success"
                  width="100%"
                  > Assign Reviewer
                </v-btn>
                <v-btn
                  v-if="userData.role === 'SDM PT'"
                  class="mr-4 white--text"
                  v-on:click="assignReviewer(karilData.karil_id)"
                  color="success"
                  width="100%"
                  > Assign Reviewer
                </v-btn>
              </v-col>
              <v-col md="2" class="mr-auto">
                <v-btn
                  class="mr-4 white--text"
                  color="blue"
                  width="100%"
                  > Download to Excel
                </v-btn>
              </v-col>
              <v-col md="2" class="mr-auto"
              v-if="karilData.status !== 'Done' && karilData.status !== 'In Review'">
                <v-btn
                  class="mr-4 white--text"
                  color="purple"
                  v-on:click="editKaril(karilData.karil_id)"
                  width="100%"
                  > <i class="far fa-edit"></i> Edit Karya Ilmiah
                </v-btn>
              </v-col>
            </template>
          </v-row>
          <v-row>
            <v-col md="2" class="mr-auto" v-if="userData.role === 'Admin'">
              <v-btn
                class="mr-auto white--text"
                @click="dialog = true"
                color="error"
                width="100%"
              > Hapus
              </v-btn>
            </v-col>

            <v-col md="2" class="mr-auto"  v-if="userData.role === 'Dosen'">
              <v-btn
                class="mr-auto white--text"
                @click="dialog = true"
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
                    <v-btn
                      v-if="karilData.link_origin != null"
                      outlined
                      color="black"
                      v-on:click="link(karilData.link_origin)"
                      width="100%"
                    > <i class="fas fa-link"></i> Link
                    </v-btn>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Repository
                  </v-col>
                  <v-col md="2">
                      <v-btn
                      v-if="karilData.link_repo != null"
                      outlined
                      color="black"
                      v-on:click="link(karilData.link_repo)"
                      width="100%"
                    > <i class="fas fa-link"></i>  Link
                    </v-btn>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Indexer
                  </v-col>
                  <v-col md="2">
                    <v-btn
                      v-if="karilData.link_indexer != null"
                      outlined
                      color="black"
                      v-on:click="link(karilData.link_indexer)"
                      width="100%"
                    > <i class="fas fa-link"></i>  Link
                    </v-btn>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Check Similarity
                  </v-col>
                  <v-col md="2">
                    <v-btn
                      v-if="karilData.link_simcheck != null"
                      outlined
                      color="black"
                      v-on:click="link(karilData.link_simcheck)"
                      width="100%"
                    > <i class="fas fa-link"></i> Link
                    </v-btn>
                  </v-col>
              </v-row>

              <v-row align="center" justify="center">
                  <v-col md="3" align="right">
                      Link Bukti Korespondensi
                  </v-col>
                  <v-col md="2">
                    <v-btn
                      v-if="karilData.link_correspondence != null"
                      outlined
                      color="black"
                      v-on:click="link(karilData.link_correspondence)"
                      width="100%"
                    > <i class="fas fa-link"></i> Link
                    </v-btn>
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
          <div class="identitas" style="margin-top: 2rem; width: 100%;" justify="center">
            <v-row align="center" justify="center">
              <v-col md="1" align="right">
                Reviewer
              </v-col>
              <v-col md="2">
                <v-select
                v-model="reviewer"
                :items="karilData.reviewers"
                label="Select"
                single-line
                @input="revSelect"></v-select>
              </v-col>
            </v-row>
          </div>
          <div v-if="reviewData != null">
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
                  <v-row style="margin-top: 1rem" row-gap="3px">
                    <v-col cols="6" align="right">
                      Indikasi Plagiasi
                    </v-col>
                    <v-col md="4" cols="8">
                      {{ reviewData.plagiarism_percentage }}%
                    </v-col>
                  </v-row>
                  <v-row style="margin-top: 1rem;margin-bottom: 1rem" row-gap="3px">
                      <v-col cols="6" align="right">
                          Linearitas
                      </v-col>
                      <v-col md="4" cols="8">
                        {{ reviewData.linearity }}
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
                        <h1>Hasil Penilaian Peer Review</h1>
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
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.comment_1 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.comment_2 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.comment_3 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.comment_4 }}
                    </v-col>
                    <v-col></v-col>
                </v-row>
                <v-row align="center" justify="center" row-gap="3px">
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        Nilai Akhir
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.score_1 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.score_2 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.score_3 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                      {{ reviewData.score_4 }}
                    </v-col>
                    <v-col align="center" style="margin-bottom: 1.5rem;">
                        <strong>{{ reviewData.score_1
                          + reviewData.score_2
                          + reviewData.score_3
                          + reviewData.score_4}}</strong>
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
                  <v-row style="margin-top: 1rem;margin-bottom: 1rem" row-gap="3px">
                      <v-col cols="6" align="right">
                          Nilai Pengusul
                      </v-col>
                      <v-col md="4" cols="8">
                        {{ reviewData.score_proposer }}
                      </v-col>
                  </v-row>
              </div>
            </v-card>
          </div>
          <div v-if="reviewData != null || reviewerData != null">
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
                    <v-col style="margin-top: 1rem" cols="6" align="right">
                        Nama:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ reviewerData.full_name }}
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="6" align="right">
                        NIP:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ reviewerData.nip }}
                    </v-col>
                </v-row>
                <v-row row-gap="3px">
                    <v-col style="margin-top: 1rem" cols="6" align="right">
                        Unit Kerja:
                    </v-col>
                    <v-col style="margin-top: 1rem" md="4" cols="8">
                        {{ reviewerData.field_of_study }}, {{ reviewerData.university }}
                    </v-col>
                </v-row>
              </div>
            </v-card>
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
                  Anda yakin ingin menghapus akun?
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
                  @click="deleteKaril(karilData.karil_id);dialog = false"
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
      reviewerData: null,
      reviewer: null,
      reviewData: null,
      reviews: null,
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
      status: 'Not Reviewed Yet',
      karilId: null,
      dialog: false,
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

    reviewKaril(karilId) {
      this.$router.push(`/add-karil-review?id=${karilId}`);
    },

    assignReviewer(karilId) {
      this.$router.push(`/assign-reviewer?id=${karilId}`);
    },

    link(link) {
      window.open(link);
    },
    revSelect() {
      if (localStorage.access) {
        this.reviewerData = null;
        this.reviewData = null;
        const accessToken = localStorage.access;
        const data = {
          username: this.reviewer,
        };
        const config = {
          headers: { Authorization: `Bearer ${accessToken}` },
        };
        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, data, config).then((res) => {
          if (res.status === 200) {
            this.reviewerData = res.data;
          } else {
            this.$router.push('/');
          }
        });
        this.reviews.forEach((element) => {
          if (element.reviewer === this.reviewer) {
            this.reviewData = element;
          }
        });
      }
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
            this.$router.push('/karil-list');
          }
        })
          .catch((err) => {
            console.log(err.response);
          });
      }
    },

    downloadExcel() {
      console.log('downloading!');
      if (localStorage.access) {
        const accessToken = localStorage.access;

        Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}api/download-review-form`, {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
          data: {
            karil_id: this.karilId,
          },
        }).then((res) => {
          if (res.status === 200) {
            console.log('download success');
          }
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
          Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-linked-reviews?id=${this.karilId}`, config).then((res5) => {
            if (res5.status === 200) {
              this.reviews = res5.data;
            }
          });
        }
      });
      Vue.axios.get(`${process.env.VUE_APP_BACKEND_URL || ''}/api/user`, config).then((res) => {
        if (res.status === 200) {
          this.userData = res.data;
        }
      });
    } else {
      this.$router.push('/');
    }
  },

};
</script>
