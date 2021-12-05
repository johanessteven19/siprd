<template>
<!-- eslint-disable max-len -->
    <div id="panduan">
        <div style="position: fixed; top: 0;">
            <Navigation />
        </div>
        <v-container style="padding: 140px 0">
            <div class="title" style="width: '50px">
                <h1 style="font-size: 30px">Panduan</h1>
            </div>
            <br>
            <accordion>
                <accordion-item>
                <!-- This slot will handle the title/header of the accordion and is the part you click on -->
                <template slot="accordion-trigger">
                    <!-- eslint-disable no-trailing-spaces -->
                    <h2><span class="fas fa-caret-down"></span>  Cara Pemakaian Sistem</h2> 
                </template>
                <!-- This slot will handle all the content that is passed to the accordion -->
                <template slot="accordion-content">
                    <br>
                    <span>Jika Anda adalah <strong> Admin</strong>, Anda dapat menambah karya ilmiah untuk direview, mengedit dan menghapus karya ilmiah serta assign reviewer untuk mereview karya ilmiah. Anda juga dapat menerima permintaan approval akun dan hapus akun</span>
                    <br><br>
                    <span>Jika Anda adalah <strong> Dosen</strong>, Anda dapat menambah karya ilmiah untuk direview, mengedit karya ilmiah jika belum di-assign kepada reviewer. Jika Anda mengubah karya ilmiah yang telah selesai, maka karya ilmiah tersebut akan kembali direview oleh Reviewer.</span>
                    <br><br>
                    <span>Jika Anda adalah <strong>SDM PT</strong>, Anda dapat menambah karya ilmiah untuk direview, mengedit karya ilmiah jika belum di-assign kepada reviewer. Anda juga dapat menerima permintaan approval akun</span>
                    <br><br>
                    <span>Jika Anda adalah <strong>Reviewer</strong>, Anda dapat menambah karya ilmiah untuk direview, mengedit karya ilmiah jika belum di-assign kepada reviewer. Anda juga dapat menerima permintaan approval akun</span>
                    <br><br>
                    <span>Jika Anda adalah <strong>Guest</strong>, akun Anda perlu di-approve terlebih dahulu oleh Admin</span>
                </template>
                </accordion-item>

                <accordion-item>
                <!-- This slot will handle the title/header of the accordion and is the part you click on -->
                <template slot="accordion-trigger">
                    <!-- eslint-disable no-trailing-spaces -->
                    <h2><span class="fas fa-caret-down"></span> Macam-macam Karya Ilmiah dan Angka Kredit</h2>
                </template>
                <!-- This slot will handle all the content that is passed to the accordion -->
                <template slot="accordion-content">
                    <br>
                    <span>Informasi rinci mengenai jenis karil yang bisa dinilai serta angka kredit, dapat dilihat pada Pedoman Operasional PAK (Penilaian Angka Kredit) 2019 melalui:</span>
                    <br>
                    <span> <a href="https://pak.kemdikbud.go.id/portalv2/download/2868/">https://pak.kemdikbud.go.id/portalv2/download/2868/</a></span>
                </template>
                </accordion-item>

                <accordion-item>
                <!-- This slot will handle the title/header of the accordion and is the part you click on -->
                <template slot="accordion-trigger">
                    <!-- eslint-disable no-trailing-spaces -->
                    <h2><span class="fas fa-caret-down"></span> Contact Person</h2>
                </template>
                <!-- This slot will handle all the content that is passed to the accordion -->
                <template slot="accordion-content">
                    <br>
                    <span>Jika Anda memiliki pertanyaan seputar SIPEERKI (Sistem Peer Review Karya Ilmiah), Anda dapat menghubungi Dr. Rizal (Manager IT Fasilkom) melalui email rizal@cs.ui.ac.id</span>
                </template>
                </accordion-item>
            </accordion>
        </v-container>
    </div>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';
import Vuetify from 'vuetify';
import Navigation from '../components/Navigation.vue';
import Accordion from '../components/Accordion.vue';
import AccordionItem from '../components/Accordion-item.vue';

Vue.use(VueAxios, axios);
Vue.use(Vuetify);

Vue.use(VueAxios, axios);

export default ({
  name: 'Success',
  components: {
    Navigation,
    Accordion,
    AccordionItem,
  },
});
</script>
<!-- eslint-disable max-len -->
<style scoped>
    .title{ width: 120px; border-bottom: 3px solid  #8D38E3; padding-bottom: 5px; }
    .accordion{ background-color: #F9F9F9; border-radius: 25px;}
</style>
