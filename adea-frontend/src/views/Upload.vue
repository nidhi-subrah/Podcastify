<template>
    <div class="upload">
      <h1>Upload Material</h1>
      <input type="file" @change="handleFile" />
      <button @click="uploadFile">Upload</button>
      <div v-if="summary">
        <h2>Summary:</h2>
        <p>{{ summary }}</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import axios from "axios";
  
  export default {
    setup() {
      const file = ref(null);
      const summary = ref("");
  
      const handleFile = (event) => {
        file.value = event.target.files[0];
      };
  
      const uploadFile = async () => {
        const formData = new FormData();
        formData.append("file", file.value);
  
        const response = await axios.post("http://localhost:5000/process-text", formData);
        summary.value = response.data.summary;
      };
  
      return { file, summary, handleFile, uploadFile };
    },
  };
  </script>
  