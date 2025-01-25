<template>
  <div class="upload">
    <h1>Upload Material</h1>
    <input type="file" @change="handleFile" />
    <button class="btn-primary" @click="uploadFile">Upload</button>
    <div v-if="summary">
      <h2>Summary:</h2>
      <p>{{ summary }}</p>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';
export default {
  setup() {
    const file = ref(null);
    const summary = ref('');
    const handleFile = (e) => {
      file.value = e.target.files[0];
    };
    const uploadFile = async () => {
      summary.value = 'Sample summary generated from backend.';
    };
    return { file, summary, handleFile, uploadFile };
  },
};
</script>

<style scoped>
.upload {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}
input {
  margin: 20px 0;
  display: block;
  width: 100%;
}
</style>
