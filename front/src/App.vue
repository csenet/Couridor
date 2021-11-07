<!-- App.vue -->
<template>
  <v-app>
    <v-app-bar color="white" app>
      <v-spacer></v-spacer>
      <v-btn v-for="item in items" v-bind:key="item.title" class="mx-1 " :to="item.to" color="primary">
        <v-icon>{{ item.icon }}</v-icon>
        <span>{{ item.title }}</span>
      </v-btn>
    </v-app-bar>
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>
    <Footer/>
  </v-app>
</template>
<script>
import Footer from "@/components/Footer";

export default {
  components: {Footer},
  computed: {
    currentRoute() {
      return this.$route.name;
    }
  },
  data() {
    return {
      items: [
        {title: 'About', icon: 'mdi-help', to: '/'},
        {title: 'Home', icon: 'mdi-home', to: '/home'},
        {title: 'Profile', icon: 'mdi-account', to: 'profile/my'},
        {title: 'Explorer', icon: 'mdi-earth', to: '/explorer'},
        {title: 'Notify', icon: 'mdi-bell', to: '/notify'},
      ],
      right: null,
      title: ""
    }
  },
}
</script>
