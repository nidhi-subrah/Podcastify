<template>
  <div class="output">
    <h1>Podcast Generated</h1>
    <p>Your text has been converted into a podcast! Click play to listen.</p>

    <!-- Audio Player Component -->
    <AudioPlayer :audioSource="audioFile" />
  </div>
</template>

<script>
import AudioPlayer from "../components/AudioPlayer.vue";

export default {
  components: { AudioPlayer },
  data() {
    return {
      audioFile: "http://localhost:5000/output/audio.mp3", // Replace with actual URL or dynamic data
    };
  },
};
</script>

<style scoped>
.output {
  text-align: center;
  margin: 30px;
}

.output h1 {
  font-size: 2rem;
  color: #4caf50;
}

.output p {
  margin-bottom: 20px;
  font-size: 1.2rem;
  color: #555;
}
</style>

