<template>
  <v-container style="margin-top: 2rem; width: 100%; padding: 80px 0">
    <validation-observer ref="observer" v-slot="{ invalid }">
      <v-form @submit.prevent="checkForm" ref="form" v-model="valid">
        <v-row>
        <v-col>
        <h1>Tambah Karya Ilmiah</h1>
        </v-col>
        <v-col md="1" class="mr-auto">
          <v-btn
            class="mr-4 white--text"
            :disabled="invalid"
            type="submit"
            color="success"
            width="100%"
          > Submit
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
                Dosen: Doni <br>
                Jabatan: Asisten Ahli <br>
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
                    <v-text-field v-model="namaPenulis" placeholder="Nama Penulis" outlined>
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
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';

Vue.use(Vuetify);
Vue.use(VueAxios, axios);

export default {
  name: 'AddKaril',
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
      kategoriSelect: ['A', 'B', 'C', 'D'],
      revieweer: null,
      reviewerSelect: ['A', 'B', 'C', 'D'],
    };
  },
  methods: {
    submitForm() {
      const data = {
        namaPenulis: this.namaPenulis,
        judulKaril: this.judulKaril,
        dataJurnal: this.dataJurnal,
        linkAsli: this.linkAsli,
        linkRepo: this.linkRepo,
        linkIndexer: this.linkIndexer,
        linkCheck: this.linkCheck,
        linkBukti: this.linkBukti,
        pengIndex: this.pengIndex,
        kategori: this.kategori,
        reviewer: this.reviewer,
      };
      Vue.axios
        .post('http://localhost:8000/api/add-karil/', data)
        .then((res) => {
          if (res.status === 201) {
            alert('Karil berhasil di submit.');
            console.log('YES');
            // this.backRedir;
          } else {
            alert('Gagal');
          }
        })
        .catch((err) => {
          console.log(err.response);
        });
    },

  },

};
</script>
