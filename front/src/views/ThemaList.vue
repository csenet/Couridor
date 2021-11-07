<template>
  <v-container>

    <MyProfile
        :renderButton="isUser"
        :bio="true"
        :facebook="facebook"
        :bio-img="bioImg"
        :github="github"
        :name="title"
        :twitter="twitter"
        :cards="cards"
        @openDetail="openDetail"
    ></MyProfile>
    <v-dialog
        v-model="card.show"
        width="90%"
        v-for="(card, index) in cards" v-bind:key="index"
    >
      <Detail
          class="py-5"
          :mainImg="card.src"
          :title="card.title"
          :detail="card.detail"
          :bio-img="card.bioImg"
          :name="card.creator"
          :github="github"
          :twitter="twitter"
          :facebook="facebook">
      </Detail>
    </v-dialog>
  </v-container>
</template>

<script>
import MyProfile from "@/components/MyProfile";
import {getAuth} from "firebase/auth";
import {collection, getDocs, getFirestore, query, where} from "firebase/firestore";
import Detail from "@/components/Detail";

export default {
  name: "ThemeList",
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
      title: "",
      dialog: false,
      themes: [
        {
          id: 0,
          title: "エンジニアの技術力を可視化するアプリケーション",
          description: "エンジニアの技術力を可視化するアプリケーションを可視化する"
        },
        {
          id: 1,
          title: "今まで参加してきたハッカソンで作った作品",
          description: "プログラミングを始めた時はみんな同じスタートライン"
        },
        {
          id: 2,
          title: "自分を象徴する作品",
          description: "自分といったらこれ、といった作品をみんなに共有してください"
        },
        {
          id: 3,
          title: "はじめてgithubにあげた作品",
          description: "そこからどうやって言語選択をしていくのか、同じスタートからの成長をみなさんで共有してください"
        }
      ]
    }
  },
  async mounted() {
    this.getName()
    let theme = this.$route.params.theme;
    const db = getFirestore();
    const q = query(collection(db, 'works'), where('theme_id', '==', theme))
    const querySnapshot = await getDocs(q)
    const rowData = querySnapshot.docs.map(doc => doc.data())
    console.log(rowData)
    rowData.map(data => this.cards.push({
      title: data.title,
      src: data.thumnail,
      flex: 6,
      show: false,
      good: data.LIKE_NUM,
      detail: data.explation,
      bioImg: data.creatorImg,
      creator: data.creator
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
    },
    getName() {
      this.themes.map((data) => {
        if (this.$route.params.theme == data.id) {
          this.title = data.title;
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
