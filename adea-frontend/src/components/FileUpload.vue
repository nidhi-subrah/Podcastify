<template>
  <div class="upload">
    <h1>Upload Material</h1>
    <input type="file" @change="handleFile" />
    <button class="btn-primary" @click="uploadFile">Upload</button>
    <h3>
      {{ status }}
    </h3>
  </div>
</template>

<script>
import { ref } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";

export default {
  setup() {
    const file = ref(null);
    const status = ref('');
    const router = useRouter();

    const handleFile = (e) => {
      file.value = e.target.files[0];
    };

    const uploadFile = async () => {
      if (!file.value) {
        alert("Please select a file to upload.");
        return;
      }

      const formData = new FormData();
      formData.append("file", file.value);

      try {
        console.log("Uploading file...");
        status.value = 'Uploading file...';
        const response = await axios.post(
          "http://localhost:5000/upload",
          formData,
          {
            headers: {
              Authorization: "Bearer: oypkN4D9Nh2AcsEmw66ug0nWdk-XS1unprMocyg0yPE=",
              "Content-Type": "multipart/form-data",
            },
          }
        );
        console.log("File uploaded:", response.data);
        status.value = 'File uploaded';
        const audioUrl = `http://localhost:5000${response.data.audio_file}`;

        // Pass audioUrl to Output.vue
        router.push({ name: "Output", query: { audioUrl } });
      } catch (error) {
        console.error("Error uploading file:", error);
        status.value = 'Failed to upload the file.';
        alert("Failed to upload the file.");
      }
    };

    return { file, status, handleFile, uploadFile };
  }
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
button {
  margin-top: 10px;
}
</style>