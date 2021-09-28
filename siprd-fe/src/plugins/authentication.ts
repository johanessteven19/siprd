import Vue from "vue";
import axios from "axios";
import VueAxios from "vue-axios";

Vue.use(VueAxios, axios);

// Check if current user is logged into backend
export function isLoggedIn(url: string, refresh_token: string) {
    Vue.axios.post(url, refresh_token).then((res) => {
        if (res.status === 200) {
            window.localStorage.setItem('access', res.data.access);
            return true;
        }
        else return false;
    })
}

export function refresh(url: string, refresh_token: string) {
    Vue.axios.post(url, refresh_token).then((res) => {
        window.localStorage.setItem('access', res.data.access);
    })
    return;
}