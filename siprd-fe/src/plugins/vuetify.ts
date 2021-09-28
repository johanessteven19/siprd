import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import GoogleIcon from "../components/GoogleIcon.vue"

Vue.use(Vuetify);

export default new Vuetify({
    theme: {/**/},
    icons: {
        values: {
            custom: {
                component: GoogleIcon
            },
        },
    },
});
