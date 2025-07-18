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

console.log('init', props.args)
useStreamlit()
const emit = defineEmits(["dataChange"])
const data = ref(props.args.data)
const formRef = ref(null)
const schema = ref(props.args.schema)
const options = ref(props.args.options)

watch(() => props.args, (newArgs, oldValue) => {
  if (JSON.stringify(oldValue) !== JSON.stringify(newArgs)) {
    schema.value = newArgs.scheme
    options.value = newArgs.options
  }
})

watch(() => data.value, (newArgs) => {
  console.log(formRef.value)
  Streamlit.setFrameHeight()
})

const onSubmit = () => {
  console.log("submit")
  Streamlit.setComponentValue(JSON.parse(JSON.stringify(data.value)))
}

</script>
<template>
  <v-form ref="formRef">
    <button @click="onSubmit">Submit</button>
    <vjsf v-model="data" :schema="schema" :options="options" />
    <button @click="onSubmit">Submit</button>
  </v-form>
</template>

<style>
  button {
    border: solid 1px green;
    background: #9cdcfe;
  }
</style>
