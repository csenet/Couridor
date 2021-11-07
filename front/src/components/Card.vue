<template>
  <v-card
      :loading="loading"
      class="mx-auto my-12"
      max-width="500"
  >
    <template slot="progress">
      <v-progress-linear
          color="deep-purple"
          height="10"
          indeterminate
      ></v-progress-linear>
    </template>

    <v-img
        height="250"
        :src="image"
    ></v-img>
    <v-row justify="space-around">
      <v-btn
          class="mx-2"
          fab
          dark
          small
          color="pink"
          @click="$emit('like')"
      >
        <v-icon dark>
          mdi-thumb-up
        </v-icon>
      </v-btn>

      <v-btn
          class="mx-2"
          fab
          dark
          small
          color="pink"
          @click="$emit('bad')"
      >
        <v-icon dark>
          mdi-thumb-down
        </v-icon>
      </v-btn>
    </v-row>
    <v-card-title>{{ title }}</v-card-title>
    <v-divider></v-divider>
    <v-card-title class="black--text">
      <router-link :to="`/profile/${creator}`">
        <v-avatar size="32">
          <img
              alt="user"
              :src="creatorImg"
          >
        </v-avatar>
      </router-link>
      <p class="ml-3 mt-3">
        {{ creator }}
      </p>
    </v-card-title>
    <v-sheet
        id="scrolling-techniques-2"
        max-height="300"
    >
      <v-divider></v-divider>
      <v-card-text class="text-left">
        {{ description }}
      </v-card-text>
    </v-sheet>
  </v-card>
</template>

<script>
export default {
  name: 'Card',
  props: ['title', 'description', 'image', 'creator', 'creatorImg'],
  data: () => ({
    loading: false,
    selection: 1,
  }),
  methods: {
    reserve() {
      this.loading = true
      setTimeout(() => (this.loading = false), 2000)
    },
  },
}
</script>
