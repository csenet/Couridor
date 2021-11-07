<template>
  <v-card class="mx-auto" max-width="800">
    <v-sheet
        id="scrolling-techniques-3"
        class="overflow-y-auto"
        max-height="800"
    >
      <div v-if="bio">
        <v-card-title class="black--text mt-1">
          <v-avatar size="64" v-if="bioImg">
            <img
                alt="user"
                :src="bioImg"
            />
          </v-avatar>
          <h1 class="ml-4 text-h4 black--text">{{ name }}</h1>

          <v-btn
              v-if="renderButton"
              class="ma-2"
              color="brack"
              dark
          >
            <v-icon dark>
              mdi-wrench
            </v-icon>
          </v-btn>


        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="github">
          GitHub :
          <h1 class="ml-4 text-h4 start">{{ github }}</h1>
        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="twitter">
          Twitter :
          <h1 class="ml-4 text-h4 start">{{ twitter }}</h1>
        </v-card-title>
        <v-divider></v-divider>

        <v-card-title v-if="facebook">
          FaceBook :
          <h1 class="ml-4 text-h4 start">{{ facebook }}</h1>
        </v-card-title>
        <v-divider></v-divider>

      </div>

      <v-container fluid>
        <v-row dense>
          <v-col v-for="card in cards" :key="card.title" :cols="card.flex">
            <v-hover>
              <template v-slot:default="{ hover }">
                <v-card>
                  <v-img
                      :src="card.src"
                      class="white--text align-end"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                      height="300px"
                  >
                    <v-card-title v-text="card.title"></v-card-title>
                  </v-img>

                  <v-card-actions>
                    <v-spacer></v-spacer>
                    <v-icon color="blue" class="mr-1">mdi-thumb-up</v-icon>
                    <b>{{ card.good }}</b>
                  </v-card-actions>

                  <v-fade-transition>
                    <v-overlay v-if="hover" absolute color="#036358">
                      <v-btn @click="$emit('openDetail',card.title)">See more info</v-btn>
                    </v-overlay>
                  </v-fade-transition>
                </v-card>
              </template>
            </v-hover>
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </v-card>
</template>
<script>

export default {
  data: () => ({
    overlay: false,
    cardShow: []
  }),
  props: ['renderButton', 'bio', 'bioImg', 'name', 'github', 'twitter', 'facebook', 'cards'],
};
</script>
