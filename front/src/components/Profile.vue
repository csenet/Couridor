<template>
  <v-card
      class="mx-auto"
      max-width="800"
  >

    <v-sheet
        id="scrolling-techniques-3"
        class="overflow-y-auto"
        max-height="800"
    >

      <template v-slot:img="{ props }">
        <v-img
            v-bind="props"
            gradient="to top right, rgba(100,115,201,.7), rgba(25,32,72,.7)"
        ></v-img>
      </template>

      <v-card-title class="black--text mt-1">
        <v-avatar size="64">
          <img
              alt="user"
              src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
          >
        </v-avatar>
        <h1 class="ml-4 text-h4 black--text">
          John Doe
        </h1>

      </v-card-title>
      <v-divider></v-divider>

      <v-card-title>
        GitHub :
        <h1 class="ml-4 text-h4 start">
          aaaaa
        </h1>
      </v-card-title>
      <v-divider></v-divider>

      <v-card-title>
        Slack :
        <h1 class="ml-4 text-h4 start">
          aaaaa
        </h1>
      </v-card-title>
      <v-divider></v-divider>

      <v-card-title>
        FaceBook :
        <h1 class="ml-4 text-h4 start">
          aaaaa
        </h1>
      </v-card-title>
      <v-divider></v-divider>

      <v-container fluid>
        <v-row dense>
          <v-col
              v-for="card in cards"
              :key="card.title"
              :cols="card.flex"
          >


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
                  </v-card-actions>

                  <v-fade-transition>
                    <v-overlay
                        v-if="hover"
                        absolute
                        color="#036358"
                    >
                      <v-btn>See more info</v-btn>
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
    cards: [
      {title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 6},
      {title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
      {title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6},
    ],
    overlay: false,
  }),

}
</script>
