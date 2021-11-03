<template>
  <v-container fill-height>
    <v-row>
      <v-layout column align-center justify-center>
        <div style="padding-left: 320px">
          <v-img
            :src="require('@/assets/asterisk.svg')"
            class="asterisk"
            contain
            height="48px"
            width="48px"
          />
        </div>
        <h1 class="text-left"><strong>Your<br>Dashboard</strong></h1>
        <p class="text-left">
          Sistem Informasi Peer Review Karya Ilmiah
        </p>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
          >
            Daftar Karya Ilmiah
          </v-btn>
        </div>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <br>
        <h2 class="text-center"><strong>Summary Karya Ilmiah</strong></h2>
        <v-row>
            <v-col>
                <v-card outlined>
                    <v-card-text>
                        <v-progress-circular
                        :rotate="-90"
                        :size="100"
                        :width="15"
                        :value="10"
                        color="blue"
                        >
                            <strong>10%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-text>
                        <v-progress-circular
                        :rotate="-90"
                        :size="100"
                        :width="15"
                        :value="33"
                        color="blue"
                        >
                            <strong>33%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-text>
                        <v-progress-circular
                        :rotate="-90"
                        :size="100"
                        :width="15"
                        :value="75"
                        color="amber"
                        >
                            <strong>75%</strong>
                        </v-progress-circular>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <v-row>
            <v-col>
                <v-card outlined>
                    <v-card-title>
                        Judul Karya 1
                    </v-card-title>
                    <v-card-text>
                        penulis 1, penulis 2<br>
                        data jurnal<br>
                        Indexer 1, Indexer 2<br>
                        Repository<br>
                        Bukti Korespondensi
                        <v-card color="#8D38E3" dark>
                            <strong>Reviewer:</strong>     Finding...
                        </v-card>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-title>
                        Judul Karya 2
                    </v-card-title>
                    <v-card-text>
                        penulis 1, penulis 2<br>
                        data jurnal<br>
                        Indexer 1, Indexer 2<br>
                        Repository<br>
                        Bukti Korespondensi
                        <v-card color="#8D38E3" dark>
                            <strong>Reviewer:</strong>     Revi W
                        </v-card>
                    </v-card-text>
                </v-card>
            </v-col>
            <v-col>
                <v-card outlined>
                    <v-card-title>
                        Judul Karya 3
                    </v-card-title>
                    <v-card-text>
                        penulis 1, penulis 2<br>
                        data jurnal<br>
                        Indexer 1, Indexer 2<br>
                        Repository<br>
                        Bukti Korespondensi
                        <v-card color="#8D38E3" dark>
                            <strong>Reviewer:</strong>     Revi W
                        </v-card>
                    </v-card-text>
                </v-card>
            </v-col>
        </v-row>
        <br>
        <div class="txt-xs-center">
          <v-btn
            class="ml-auto white--text"
            color="#8D38E3"
            width="100%"
          >
            See All List
          </v-btn>
        </div>
      </v-layout>
    </v-row>
  </v-container>
</template>

<script>
import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";
import Vuetify from "vuetify";

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

export default {
  name: "Success",
  data() {
    return null;
  },
  methods: {
    proceed() {
      this.$router.push("/");
    },
  },
};
</script>
