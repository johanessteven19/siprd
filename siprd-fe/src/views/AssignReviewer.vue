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
                @click="dialog = true"
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
                    > Link
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
                    > Link
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
                    > Link
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
                    > Link
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
                    > Link
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

          <div class="reviewers" style="margin-top: 2rem; width: 100%;" justify="center">
              <v-row align="center" justify="center" row-gap="10px">
                  <v-col md="3" align="right">
                      <h1>Reviewer</h1>
                      <br>
                  </v-col>
              </v-row>

               <v-row align="center" justify="center"
               v-for="(value, index) in selected" :key="index" >
                  <v-col md="3" align="right">
                      Nama Reviewer
                  </v-col>
                  <v-col md="2">
              <v-select
                v-model="selected[index]"
                :items="reviewerProfiles"
                :item-text="'full_name'"
                item-value="reviewerProfiles.username"
                label="Select"
                return-object
                single-line
              >
                <template v-slot:item="{item}">
                  {{item.full_name}} - {{item.position}}
                   - {{item.field_of_study}} - {{item.university}}
                </template>
              </v-select>
                  </v-col>
              </v-row>
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
          <v-dialog
          v-model="dialog"
          persistent
          max-width="350">
            <v-card class="mx-auto my-0" max-width="350">
              <v-card-title class="justify-center text-h5 ">
                Izin Diperlukan
              </v-card-title>
              <v-card-text style="text-align:center">
                Anda yakin ingin assign reviewer?
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
      reviewerData: '',
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
      status: 'Done',
      karilId: null,
      counter: 0,
      dialog: false,
      reviewers: [{
        id: 'reviewer0',
        label: 'Nama Reviewer',
        value: '',
      }],
      reviewerProfiles: null,
      selected: [null, null],
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
        status: this.status,
        reviewers: this.selected.map((r) => r.username),
      };
      if (localStorage.access) {
        const accessToken = localStorage.access;
        const config = {
          headers: {
            Authorization: `Bearer ${accessToken}`,
          },
        };
        console.log(data);
        Vue.axios
          .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/assign-reviewer/`, data, config)
          .then((res) => {
            if (res.status === 200) {
              console.log('berhasil submit!');
              console.log(res.data);

              alert('Reviewers berhasil di assign!');
              this.$router.push('/karil-list');
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

    editKaril() {
      this.$router.push('/edit-karil');
    },

    cancel() {
      this.$router.push(`/view-karil?id=${this.karilId}`);
    },

    addNew() {
      this.selected.push(null);
    },
  },

  async beforeMount() {
    this.karilId = this.$route.query.id;
    if (localStorage.access) {
      const accessToken = localStorage.access;
      const data = {
        karil_id: this.karilId,
      };
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };

      await Vue.axios
        .post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/get-review-form/`, data, config)
        .then((response) => {
          if (response.status === 200) {
            this.karilData = response.data;
            console.log(this.karilData);
          }
        });
      const posData = {
        position: this.karilData.promotion,
      };
      console.log(posData);
      const res = await Vue.axios.post(`${process.env.VUE_APP_BACKEND_URL || ''}/api/manage-reviewers/`, posData, config);
      console.log(res.data);
      if (res.status === 200) {
        this.reviewerSelect = res.data;
        this.reviewerSelect.full_name = res.data.full_name;
        this.reviewerProfiles = res.data;
      }
    } else { this.$router.push('/'); }
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
