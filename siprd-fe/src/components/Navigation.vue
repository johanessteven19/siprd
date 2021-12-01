<template>
  <header :class="{ 'scrolled-nav': scrolledNav }">
    <nav style='z-index:999'>
      <div class="branding">
        <img src="@/assets/logo.png" style="width: 35px; padding-right: 10px;">
        <a href="">SIPEERKI</a>
      </div>
      <ul v-show="!mobile" class="menu">
        <li>
          <router-link class="link" :to="{ name: 'KarilList' }"
            >Daftar Karya Ilmiah</router-link
          >
        </li>
        <li v-if="userData.role === 'Admin'">
          <router-link class="link" :to="{ name: 'AccountList' }">Daftar Akun</router-link>
        </li>
        <li v-if="userData.role === 'SDM PT'">
          <router-link class="link" :to="{ name: 'AccountList' }">Daftar Akun</router-link>
        </li>
        <li>
          <router-link class="link" :to="{ name: 'Success' }">Panduan</router-link>
        </li>

        <li @mouseover="profileList = true" @mouseleave="profileList = false">
          <img src="@/assets/profile.jpg" alt="User" width="40" height="40">

          <transition name="fade">
            <ul v-if="profileList" @click="profileList = false">
              <li> <router-link class="link"
                    :to="{ name: 'ViewAccount' }">Profile</router-link>
              </li>
              <li> <div class="link" v-on:click="logoutUser"> <a>Logout</a> </div>
              </li>
            </ul>
          </transition>

        </li>
      </ul>
      <div class="icon">
        <em
          @click="toggleMobileNav"
          v-show="mobile"
          class="far fa-bars"
          :class="{ 'icon-active': mobileNav }"
        ></em>
      </div>
      <transition name="mobile-nav">
        <ul v-show="mobileNav" class="dropdown-nav">
          <li>
            <router-link class="link" :to="{ name: 'KarilList' }"
              >Daftar Karya Ilmiah</router-link
            >
          </li>
          <li>
            <router-link class="link" :to="{ name: 'AccountList' }"
              >Daftar Akun</router-link
            >
          </li>
          <li>
            <router-link class="link" :to="{ name: '' }">Panduan</router-link>
          </li>
          <li>
            <router-link class="link" :to="{ name: 'ViewAccount' }">Profil Anda</router-link>
          </li>
        </ul>
      </transition>
    </nav>
  </header>
</template>

<script>
import Vue from 'vue';
import axios from 'axios';
import VueAxios from 'vue-axios';

Vue.use(VueAxios, axios);
export default {
  name: 'navigation',
  data() {
    return {
      userData: '',
      scrolledNav: null,
      mobile: null,
      mobileNav: null,
      windowWidth: null,
      profileList: false,
      role: null,
    };
  },
  created() {
    window.addEventListener('resize', this.checkScreen);
    this.checkScreen();
  },
  mounted() {
    window.addEventListener('scroll', this.updateScroll);
  },
  methods: {
    toggleMobileNav() {
      this.mobileNav = !this.mobileNav;
    },

    updateScroll() {
      const scrollPosition = window.scrollYl;
      if (scrollPosition > 50) {
        this.scrolledNav = true;
        return;
      }
      this.scrolledNav = false;
    },
    checkScreen() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= 750) {
        this.mobile = true;
        return;
      }
      this.mobile = false;
      this.mobileNav = false;
    },

    logoutUser() {
      console.log('enter');
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      this.$router.push('/');
    },
  },
  beforeMount() {
    if (localStorage.access) {
      console.log(localStorage.access);
      console.log(localStorage.refresh);
      const accessToken = localStorage.access;
      const config = {
        headers: { Authorization: `Bearer ${accessToken}` },
      };
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

<style lang="scss" scoped>
header {
  // background-color: rgba(0, 0, 0, 0.8);
  z-index: 9999;
  width: 100%;
  position: fixed;
  transition: 0.5s ease all;
  background-color: white;
  opacity: 100;
  border-bottom: 2px;
  border-bottom: 1px solid transparent;

  nav {
    position: relative;
    z-index: 999;
    display: flex;
    flex-direction: row;
    padding: 2px 0;
    transition: 0.5s ease all;
    width: 90%;
    margin: 0 auto;
    @media (min-width: 1140px) {
      max-width: 1140px;
    }
  .menu {
    // position: sticky;
    display: flex;
    align-items: right;
    flex: 1;
    justify-content: flex-end;
    font-size: 14px;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .menu a {
    display: block;
    padding: 10px;
    font-weight: 500;
    color: black;
    text-decoration: none;
  }

  .menu li {
    display:block;
    float: left;
    position: relative;
    background:white;
    color: black;
    // min-width: 10px;
    text-transform: uppercase;
    padding: 16px;
  }

  .menu li ul {
    position: absolute;
    left: 0;
    top: 61px;
    margin: 0;
    padding: 0;
  }

  .menu li ul li {
    background:white;
    transition: background .2s;
  }

  .menu li ul li:hover {
    color: purple;
    border-color: purple;
  }

  .link {
    font-size: 14px;
    transition: 0.5s ease all;
    padding-bottom: 4px;
    border-bottom: 1px solid transparent;

    &:hover {
      color: purple;
      border-color: purple;
    }
  }

    .branding {
      display: flex;
      align-items: center;

      a {
        color: black;
        text-decoration: none;
        width: 50px;
        transition: 0.5s ease all;
        font-weight: 500;
      }
    }

    .icon {
      display: flex;
      align-items: center;
      position: absolute;
      top: 0;
      right: 24px;
      height: 100%;
      color: black;
      i {
        cursor: pointer;
        font-size: 24px;
        transition: 0.8s ease all;
      }
    }

    .icon-active {
      transform: rotate(180deg);
    }

    .fade-enter-active, .fade-leave-active {
      transition: opacity .2s;
    }

    .fade-enter, .fade-leave-active {
      opacity: 0;
    }

    .dropdown-nav {
      display: flex;
      flex-direction: column;
      position: fixed;
      width: 100%;
      max-width: 250px;
      height: 100%;
      background-color: black;
      top: 0;
      left: 0;

      li {
        margin-left: 0;
        .link {
          color: white;
        }
      }
    }

    .mobile-nav-enter-active,
    .mobile-nav-leave-active {
      transition: 1s ease all;
    }

    .mobile-nav-enter-from,
    .mobile-nav-leave-to {
      transform: translateX(-250px);
    }

    .mobile-nav-enter-to {
      transform: translateX(0);
    }
  }
}

header{
  color: aliceblue;
   -webkit-box-shadow: 0 8px 6px -6px #999;
    -moz-box-shadow: 0 8px 6px -6px #999;
    box-shadow: 0 8px 6px -6px #999;
}

.scrolled-nav {
  background-color: white;
  box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
    0 2px 4px -1px rgba(0, 0, 0, 0.06);

  nav {
    padding: 8px 0;

    .branding {
      a {
        width: 40px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
          0 2px 4px -1px rgba(0, 0, 0, 0.06);
      }
    }
  }
}
</style>
