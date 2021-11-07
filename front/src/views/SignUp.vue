<template>
  <v-container>
    <h1 class="text-center">Sign Up</h1>
    <v-stepper v-model="e1">
      <v-stepper-header>
        <v-stepper-step
            :complete="e1 > 1"
            step="1"
        >
          GitHubを連携
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step
            :complete="e1 > 2"
            step="2"
        >
          レポジトリを選択
        </v-stepper-step>

        <v-divider></v-divider>

        <v-stepper-step step="3">
          登録完了
        </v-stepper-step>
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <p class="text-center">
            <v-btn @click="login" color="primary" class="flex ju">Login with GitHub</v-btn>
          </p>
        </v-stepper-content>

        <v-stepper-content step="2">
          公開する作品を選択してください（{{ userName }}）
          <v-container>
            <v-checkbox
                v-for="work in works" v-bind:key="work"
                v-model="addWorks"
                :label="work"
                :value="work"
            ></v-checkbox>
          </v-container>

          <v-btn
              color="primary"
              @click="register()"
          >
            Continue
          </v-btn>

          <v-btn text>
            Cancel
          </v-btn>
        </v-stepper-content>

        <v-stepper-content step="3">
          <h1>登録完了</h1>
          <p>作品が正常に登録されました<br>詳細は各自のProfileから確認してください</p>

          <v-btn
              color="primary"
              @click="e1 = 1"
          >
            Getting Started
          </v-btn>
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </v-container>
</template>

<script>
import {getAuth, GithubAuthProvider, signInWithPopup} from "firebase/auth";
import axios from "axios"

export default {
  name: "Signin.vue",
  data() {
    return {
      e1: 1,
      works: [],
      addWorks: [],
      userName: ""
    }
  },
  methods: {
    login() {
      const auth = getAuth();
      const provider = new GithubAuthProvider()
      signInWithPopup(auth, provider)
          .then(async (result) => {
            this.userName = result._tokenResponse.screenName
            this.works = (await axios.get('http://os3-359-12725.vs.sakura.ne.jp/getRepo/' + this.userName)).data
            this.e1 = 2;
          }).catch((error) => {
        console.log(error)
      });
    },
    register() {
      // レポジトリを登録する
      axios.post('http://os3-359-12725.vs.sakura.ne.jp/post_data', {
        username: this.username,
        repository: this.addWorks
      })
      this.e1 = 3;
    }
  }
}
</script>

<style scoped>

</style>
