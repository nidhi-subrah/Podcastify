<template>
    <div class="audio-player">
      <h2>Listen to Your Podcast</h2>
      <div class="controls">
        <button @click="playAudio">▶️ Play</button>
        <button @click="pauseAudio">⏸️ Pause</button>
        <input
          type="range"
          min="0"
          max="100"
          step="1"
          v-model="volume"
          @input="setVolume"
        />
        <span>{{ volume }}%</span>
  
        <!-- Download Button -->
        <a
          :href="audioSource"
          download
          class="download-btn"
          v-if="audioSource"
          >📥 Download Podcast</a
        >
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      audioSource: {
        type: String,
        required: true,
      },
    },
    data() {
      return {
        volume: 50, // Default volume
      };
    },
    mounted() {
      this.audio = new Audio(this.audioSource);
      this.audio.volume = this.volume / 100; // Initialize volume
    },
    methods: {
      playAudio() {
        this.audio.play();
      },
      pauseAudio() {
        this.audio.pause();
      },
      setVolume() {
        this.audio.volume = this.volume / 100;
      },
    },
  };
  </script>
  
  <style scoped>
  .audio-player {
    text-align: center;
    margin: 20px;
  }
  
  .controls {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
  }
  
  input[type="range"] {
    cursor: pointer;
  }
  
  /* Styling for download button */
  .download-btn {
    background-color: #4caf50;
    color: white;
    padding: 10px;
    text-decoration: none;
    border-radius: 5px;
    cursor: pointer;
  }
  
  .download-btn:hover {
    background-color: #45a049;
  }
  </style>
  