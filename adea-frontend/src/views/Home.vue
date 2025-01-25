<template>
    <div class="home">
      <h1>Welcome to ADEA</h1>
      <p>Navigate to upload a file or submit feedback.</p>
    </div>
  </template>

<script>
import { defineComponent, ref } from 'vue';

export default defineComponent({
  setup() {
    const message = ref('Hello, Vue 3!');
    return { message };
  },
});
</script>
