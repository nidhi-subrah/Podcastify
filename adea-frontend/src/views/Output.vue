<template>
  <div class="output">
    <h1>Podcast Generated</h1>
    <p>Your text has been converted into a podcast! Click play to listen.</p>

    <!-- Pass the audio file URL as a prop -->
    <AudioPlayer :audioUrl="audioUrl" />
  </div>
</template>

<script>
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import AudioPlayer from "../components/AudioPlayer.vue";

export default {
  components: { AudioPlayer },
  setup() {
    const route = useRoute();
    const audioUrl = ref("");

    onMounted(() => {
      audioUrl.value = route.query.audioUrl;
    });

    return { audioUrl };
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