<template>
  <div class="audio-player">
    <h2>Listen to Your Podcast</h2>
    <audio controls :src="audioUrl"></audio>
    <a :href="audioUrl" download="podcast.mp3" class="download-btn">📥 Download Podcast</a>
  </div>
</template>

<script>
export default {
  props: {
    audioUrl: {
      type: String,
      required: true, // The audio URL must be passed as a prop
    },
  },
};
</script>

<style scoped>
.audio-player {
  max-width: 600px;
  margin: 20px auto;
  text-align: center;
}
.download-btn {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
}
.download-btn:hover {
  background-color: #45a049;
}
</style>