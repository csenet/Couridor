<template>
  <v-card
      class="mx-auto"
      height="800"
  >
    <v-row>
      <v-col cols="8">

        <v-img
            class="white--text align-end center"
            height="750px"
            :src="mainImg"
        >
        </v-img>
      </v-col>

      <v-col cols="4">


        <h1 class=" text-h4 black--text">{{ title }}</h1>
        <v-divider></v-divider>

        <v-card-title>
          <span class="ml-4 start" style="font-size:1.0em;">{{ detail }}</span>
        </v-card-title>
        <v-divider></v-divider>
        <template v-slot:img="{ props }">
          <v-img
              v-bind="props"
              gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
          ></v-img>
        </template>

        <v-card-title class="black--text mt-1">
          <router-link :to="`/profile/${name}`">
            <v-avatar size="32">
              <img
                  alt="user"
                  :src="bioImg"
              >
            </v-avatar>
          </router-link>
          <h1 class="ml-4 text-h5 black--text">{{ name }}</h1>

        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="github">
          GitHub :
          <h1 class="ml-4 text-h6 start">{{ github }}</h1>
        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="twitter">
          Twitter :
          <h1 class="ml-4 text-h6 start">{{ twitter }}</h1>
        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="facebook">
          FaceBook :
          <h1 class="ml-4 text-h6 start">{{ facebook }}</h1>
        </v-card-title>
        <v-divider></v-divider>

      </v-col>

    </v-row>
  </v-card>
</template>
<script>

export default {
  data: () => ({
    overlay: false,
  }),

  props: ['mainImg', 'title', 'detail', 'bioImg', 'name', 'github', 'twitter', 'facebook'],
};
</script>
