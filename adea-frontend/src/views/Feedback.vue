<template>
  <div class="feedback">
    <h1>Submit Feedback</h1>
    <textarea v-model="feedback" placeholder="Enter feedback here"></textarea>
    <button class="btn-primary" @click="submitFeedback">Submit</button>
  </div>
</template>

<script>
import { ref } from 'vue';
export default {
  setup() {
    const feedback = ref('');
    const submitFeedback = async () => {
      alert(`Feedback submitted: ${feedback.value}`);
      feedback.value = '';
    };
    return { feedback, submitFeedback };
  },
};
</script>

<style scoped>
.feedback {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  text-align: center;
}
textarea {
  width: 100%;
  height: 100px;
  margin-bottom: 10px;
}
</style>
