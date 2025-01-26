<template>
  <div class="flex flex-col max-w-md mx-auto mt-10 p-4 border rounded-xl shadow-lg">
    <div class="flex-1 overflow-y-auto mb-4 bg-gray-100 p-2 rounded-lg" style="max-height: 400px;">
      <div
        v-for="(msg, index) in messages"
        :key="index"
        class="my-2 p-2 rounded-lg max-w-sm"
        :class="msg.sender === 'user' ? 'bg-blue-500 text-white self-end' : 'bg-gray-300 text-black self-start'"
      >
        {{ msg.text }}
      </div>
    </div>
    <div class="flex items-center space-x-2">
      <input
        type="text"
        class="flex-1 border p-2 rounded-lg focus:outline-none"
        placeholder="Type a message..."
        v-model="input"
      />
      <button
        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700"
        @click="sendMessage"
      >
        Send
      </button>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue';

export default {
  setup() {
    const messages = ref([]); // Stores chat messages
    const input = ref(''); // User input field

    const apiKey = 'VF.DM.6795c19d12f08bcbb5f778d8.O9aqxLFyvDwdACM8'; // Replace with your Voiceflow API key

    const sendMessage = async () => {
      if (!input.value.trim()) return;

      // Append user message to chat
      const userMessage = { sender: 'user', text: input.value };
      messages.value.push(userMessage);


      try {
        // Make API call to Voiceflow runtime
        const response = await fetch(`https://general-runtime.voiceflow.com/state/user/user_id/interact`, {
          method: 'POST',
          headers: {
            'Authorization': apiKey,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            request: {
              type: 'text',
              payload: input.value,
            },
          }),
        });

        const data = await response.json();

        data.forEach((trace) => {
          if (trace.type === 'speak' || trace.type === 'text') {
            const botMessage = { sender: 'bot', text: trace.payload.message };
            messages.value.push(botMessage);
          } else if (trace.type === 'end') {
            const endMessage = { sender: 'bot', text: 'The conversation has ended.' };
            messages.value.push(endMessage);
          }
        });
      } catch (error) {
        console.error('Error communicating with Voiceflow API:', error);
        messages.value.push({ sender: 'bot', text: 'Error processing your request. Please try again.' });
      }

      // Clear input field
      input.value = '';
    };

    return {
      messages,
      input,
      sendMessage,
    };
  },
};
</script>

<style scoped>
/* Optional: Add some custom styles */
</style>
