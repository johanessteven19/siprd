<template>
  <v-app>
    <v-main>
      <Navigation />
      <router-view />
    </v-main>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue';
import Navigation from './components/Navigation.vue';

export default Vue.extend({
  name: 'App',
  components: {
    Navigation,
  },
  data: () => ({
    //
  }),
});
</script>
