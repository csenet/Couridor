<template>
  <v-container>

    <MyProfile
        :renderButton="isUser"
        :bio="true"
        :facebook="facebook"
        :bio-img="bioImg"
        :github="github"
        :name="name"
        :twitter="twitter"
        :cards="cards"
        @openDetail="openDetail"
    ></MyProfile>
    <v-dialog
        v-model="card.show"
        width="80%"
        v-for="(card, index) in cards" v-bind:key="index"
    >
      <Detail
          class="py-5"
          :mainImg="card.src"
          :title="card.title"
          :detail="card.detail"
          :bio-img="bioImg"
          :name="name"
          :github="github"
          :twitter="twitter"
          :facebook="facebook"
      ></Detail>
    </v-dialog>
  </v-container>
</template>

<script>
import MyProfile from "@/components/MyProfile";
import {getAuth} from "firebase/auth";
import axios from "axios";
import {collection, getDocs, getFirestore, query, where} from "firebase/firestore";
import Detail from "@/components/Detail";

export default {
  name: "Profile",
  components: {Detail, MyProfile},
  data() {
    return {
      user: getAuth().currentUser,
      isUser: false,
      bioImg: "",
      name: "",
      github: "",
      twitter: "",
      facebook: "",
      cards: [],
      dialog: false
    }
  },
  async mounted() {
    let userName = this.$route.params.username;
    if (userName == "my") {
      if (!this.user) {
        await this.$router.push("/login");
      }
      this.isUser = true
      userName = getAuth().currentUser.reloadUserInfo.screenName;
    }
    const githubData = (await axios.get('http://os3-359-12725.vs.sakura.ne.jp/api/' + userName)).data
    this.bioImg = githubData.avatar_url
    this.name = userName
    this.github = userName
    this.twitter = githubData.twitter_username
    const db = getFirestore();
    const q = query(collection(db, 'works'), where('creator', '==', this.name))
    const querySnapshot = await getDocs(q)
    const rowData = querySnapshot.docs.map(doc => doc.data())
    console.log(rowData)
    rowData.map(data => this.cards.push({
      title: data.title,
      src: data.thumnail,
      flex: 6,
      show: false,
      good: data.LIKE_NUM,
      detail: data.explation
    }))
    console.log(this.cards)
  },
  methods: {
    openDetail(cardName) {
      this.cards.map(card => {
        if (card.title == cardName) {
          card.show = true
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
