<template>
  <div class="audio-player">
    <h2>Listen to Your Podcast</h2>
    <div class="audio-controls">
      <audio controls :src="audioUrl"></audio>
    </div>
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
  background-color: #f9f9f9;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.audio-player h2 {
  font-size: 1.5rem;
  color: #4caf50;
  margin-bottom: 20px;
}

.audio-controls {
  margin-bottom: 20px;
}

audio {
  width: 100%;
  border-radius: 5px;
}

.download-btn {
  display: inline-block;
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #4caf50;
  color: white;
  text-decoration: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.download-btn:hover {
  background-color: #45a049;
}
</style>