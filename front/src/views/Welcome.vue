<template>
  <v-container class="justify-center text-center" style="max-width: 500px;">
    <v-img
        :src="require('../assets/logo.png')"
        class="my-3"
        contain
        height="500"
    />
    <p class="text-justify">
      Couridorは、Github APIを使い、GitHubのレポジトリーを読み取り作品として公開します。
      Couridorには、ここから広がるかもしれない繋がりの可能性があふれています。新しいコードたちに出会いたい。言語の幅を広げたい。異言語のプログラマーに会ってみたい。あるいはただ、いまここで楽しみたい。Couridorはそんなあなたに、ぴったりのWEBサイトです。
    </p>
    <h3>Privacy</h3>
    <p class="text-justify">
      Couridorは、お客様のプライバシーの保護に努めています。お客様には良縁の獲得に専念していただけるよう、当社は信頼性の高い業界最高水準の製品・サービスの提供を目指します。プライバシーの保護に向けて、当社のデータ活用に関してお客様にわかりやすい情報をお届けする所存です。
    </p>
    <v-divider class="my-2"></v-divider>
    <h3>新規登録はこちらから</h3>
    <v-btn to="/signup" class="mt-1" color="primary">新規登録</v-btn>
  </v-container>
</template>

<script>
export default {
  name: "Welcome.vue"
}
</script>

<style scoped>

</style>
