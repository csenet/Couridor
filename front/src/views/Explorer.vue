<template>
  <v-container>
    <h1 class="text-center my-2">Explorer</h1>
    <p class="text-center">テーマに沿った作品を投稿しよう</p>
    <ThemeList :themes="themes"></ThemeList>
  </v-container>
</template>

<script>
import ThemeList from "@/components/ThemeList";

export default {
  name: "Explorer",
  components: {ThemeList},
  data(){
    return{
      themes: [
        {
          id: 0,
          title: "エンジニアの技術力を可視化するアプリ",
          description: "これから、開発インターンやアルバイトの予定もないけど、ハッカソンで頑張った証をみんなに見てほしい。そんな方たちに向けたテーマです。"
        },
        {
          id: 1,
          title: "ハッカソンで出した作品",
          description: "プログラミングを始めた時はみんな同じスタートライン。そこからどうやって言語選択をしていくのか、同じスタートからの成長をみなさんで共有してください。"
        },
        {
          id: 2,
          title: "自分を象徴する作品",
          description: "自分といったらこれ、といった作品をみんなに共有してください"
        },
        {
          id: 3,
          title: "はじめてgithubにあげた作品",
          description: "初めてGitHuBを利用した時、なにがなんだかよくわからなくて右往左往した経験はありませんか？遠い昔の初な時を共有したい人向けのテーマです。"
        }
      ]
    }
  }
}
</script>

<style scoped>

</style>
