<template>
  <v-card
    :loading="loading"
    class="mx-auto my-12"
    max-width="374"
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
      src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
    ></v-img>

    <!-- <v-card-title>Cafe Badilico</v-card-title> -->

    <!-- <v-row justify="space-around"> -->

    <v-row justify="space-around">
      <v-btn
       class="mx-2"
        fab
        dark
        small
        color="pink"
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
      >
        <v-icon dark>
          mdi-thumb-down
        </v-icon>
      </v-btn>
    </v-row>
      
<!-- 
    <v-card-text>
      <v-row
        align="center"
        class="mx-0"
      >
        <v-rating
          :value="4.5"
          color="amber"
          dense
          half-increments
          readonly
          size="14"
        ></v-rating>

        <div class="grey--text ms-4">
          4.5 (413)
        </div>
      </v-row>

      <div class="my-4 text-subtitle-1">
        $ • Italian, Cafe
      </div>

      <div>Small plates, salads & sandwiches - an intimate setting with 12 indoor seats plus patio seating.</div>
    </v-card-text>

    <v-divider class="mx-4"></v-divider> -->

    <v-card-title>おいしそうなパンを眺めるアプリ</v-card-title>
    <v-divider></v-divider>
  <!-- <v-row class="pa-md-6 mx-lg-auto">

    <v-avatar
      color="red"
      size="36"
    >
      <img
        src="https://cdn.vuetifyjs.com/images/john.jpg"
        alt="John"
      >
    </v-avatar>

    <v-card-title>
      ジョン・F・ケネディ
    </v-card-title>

  </v-row> -->


<!-- 
  <v-row
    align="center"
    class="spacer"
    no-gutters
  >
    <v-avatar
      size="36px"
    >
      <img
        src="https://cdn.vuetifyjs.com/images/john.jpg"
        alt="John"
      >
     </v-avatar>

  </v-row>
  
<v-card-text v-text="lorem"></v-card-text> -->

    <v-sheet
      id="scrolling-techniques-2"
      class="overflow-y-auto"
      max-height="300"
    >

          <v-card-title class="black--text mt-1">
            <v-avatar size="32">
              <img
                alt="user"
                src="https://cdn.pixabay.com/photo/2020/06/24/19/12/cabbage-5337431_1280.jpg"
              >
            </v-avatar>
            <p class="ml-3">
              John Doe
            </p>
          </v-card-title>
    <v-divider></v-divider>


    <!-- <v-card-title>工夫した点</v-card-title> -->
    
    <v-card-title>
      項目1
    </v-card-title>
        <v-card-text class="text-left">
          項目1の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider> 
    <v-card-title>
      項目2
    </v-card-title>
        <v-card-text class="text-left">
          項目2の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider> 
    <v-card-title>
      項目3
    </v-card-title>
        <v-card-text class="text-left">
          項目3の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider>
    <v-card-title>
      項目4
    </v-card-title>
        <v-card-text class="text-left">
          項目4の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider>
    <v-card-title>
      項目5
    </v-card-title>
        <v-card-text class="text-left">
          項目5の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider>
    <v-card-title>
      項目6
    </v-card-title>
        <v-card-text class="text-left">
          項目6の内容。あああああああああああああああああああああああ
        </v-card-text>
    <v-divider></v-divider>
    </v-sheet>

<!-- 
    <v-card-text>
      <v-chip-group
        v-model="selection"
        active-class="deep-purple accent-4 white--text"
        column
      >
        <v-chip>5:30PM</v-chip>

        <v-chip>7:30PM</v-chip>

        <v-chip>8:00PM</v-chip>

        <v-chip>9:00PM</v-chip>
      </v-chip-group>
    </v-card-text>

    <v-card-actions>
      <v-btn
        color="deep-purple lighten-2"
        text
        @click="reserve"
      >
        Reserve
      </v-btn>
    </v-card-actions> -->
  </v-card>
</template>

<script>
  export default {
    data: () => ({
      loading: false,
      selection: 1,
    }),
    methods: {
      reserve () {
        this.loading = true
        setTimeout(() => (this.loading = false), 2000)
      },
    },
  }
</script>