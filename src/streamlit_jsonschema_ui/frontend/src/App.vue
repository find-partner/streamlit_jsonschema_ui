<template>
  <div id="app">
    <WithStreamlitConnection v-slot="{ args }">
      <JsonSchemaComponent :args="args" />
    </WithStreamlitConnection>
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue"
import JsonSchemaComponent from "./JsonSchemaComponent.vue"


import WithStreamlitConnection from "./streamlit/WithStreamlitConnection.vue"

export default defineComponent({
  name: "App",
  components: {
    JsonSchemaComponent,
    WithStreamlitConnection,
  },
})
</script>

<style>
body {
  margin: 0px;
}
#app {
  color: var(--text-color);
  font-family: var(--font);
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>
