<template>
  <v-container class="justify-center text-center" style="max-width: 500px;">
    <h1>LOGIN</h1>
    <p>GitHubを使用してログインします<br>
      新規登録の方は<router-link to="/">こちら</router-link>から</p>
    <v-btn @click="login" color="primary">Login with GitHub</v-btn>
  </v-container>
</template>

<script>
import {getAuth, signInWithPopup, GithubAuthProvider} from 'firebase/auth';

export default {
  name: "Login.vue",
  methods: {
    login() {
      const auth = getAuth();
      const provider = new GithubAuthProvider()
      signInWithPopup(auth, provider)
          .then((result) => {
            console.log(result.user)
            this.$router.push('/')
          }).catch((error) => {
        console.log(error)
      });
    }
  }
}
</script>

<style scoped>

</style>
