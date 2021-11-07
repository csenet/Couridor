<template>
  <v-container>
    <v-card
        max-width="800"
        class="mx-auto"
    >
      <v-expansion-panels>
        <v-expansion-panel v-for="theme in themes" :key="theme.title">
          <v-expansion-panel-header>
            <v-card-text
                class="text-center"
            >
              <v-btn
                  absolute
                  left
                  top
                  color="primary"
                  :to="`/themelist/${theme.id}`"
              >
                {{ theme.title }}
              </v-btn>
            </v-card-text>
          </v-expansion-panel-header>
          <v-expansion-panel-content>
            {{ theme.description }}
          </v-expansion-panel-content>
        </v-expansion-panel>
      </v-expansion-panels>
    </v-card>
  </v-container>
</template>

<script>
export default {
  data: () => ({
    panel: [0, 1],
    readonly: false
  }),
  props: ['themes']
}
</script>
