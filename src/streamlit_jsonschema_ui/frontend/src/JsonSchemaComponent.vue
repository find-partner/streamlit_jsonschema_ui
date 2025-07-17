<script setup lang="ts">
import Vjsf from '@koumoul/vjsf'
import { VForm } from 'vuetify/components'
import { ref } from 'vue'
import { Streamlit } from "streamlit-component-lib"
import { useStreamlit } from "./streamlit"
import { watch } from 'vue'

const props = defineProps({
  args: {
    type: Object,
    required: true,
  },
})

useStreamlit()

const data = ref({})

const schema = ref(props.args.schema)
const options = ref(props.args.options)


watch(props.args, (newArgs) => {
    schema.value = newArgs.schema
    options.value = newArgs.options
})


</script>
<template>
  <v-form>
    {{ data}}
    <vjsf v-model="data" :schema="schema" :options="options" />
    <button @click="Streamlit.setComponentValue(data)">Submit</button>
  </v-form>
</template>
