<template>
    <div class="chatbot">
      <h1>Ask About the File</h1>
      <div class="chat-window">
        <div v-for="(message, index) in chatHistory" :key="index" class="message">
          <div :class="message.role === 'user' ? 'user-message' : 'bot-message'">
            <p>{{ message.content }}</p>
          </div>
        </div>
      </div>
      <div class="chat-input">
        <input
          v-model="question"
          type="text"
          placeholder="Type your question here..."
          @keydown.enter="sendQuestion"
        />
        <button class="btn-primary" @click="sendQuestion">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  import { ref } from "vue";
  import axios from "axios";
  
  export default {
    name: "Chatbot",
    setup() {
      const chatHistory = ref([
        { role: "bot", content: "Hi! Ask me anything about the uploaded file." },
      ]);
      const question = ref("");
  
      const sendQuestion = async () => {
        if (!question.value.trim()) return;
  
        // Add the user question to chat history
        chatHistory.value.push({ role: "user", content: question.value });
  
        try {
          const response = await axios.post("/chat", { question: question.value });
  
          // Add the bot's response to chat history
          chatHistory.value.push({ role: "bot", content: response.data.answer });
        } catch (error) {
          chatHistory.value.push({
            role: "bot",
            content: "Oops! Something went wrong. Please try again later.",
          });
        }
  
        question.value = ""; // Clear input field
      };
  
      return { chatHistory, question, sendQuestion };
    },
  };
  </script>
  
  <style scoped>
  .chatbot {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    background: #2c2c3c; /* Darker background */
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
  }
  
  .chat-window {
    max-height: 300px;
    overflow-y: auto;
    padding: 10px;
    background: #1e1e2f; /* Slightly darker than main background */
    border-radius: 8px;
    margin-bottom: 20px;
    border: 1px solid #8e44ad;
  }
  
  .message {
    margin-bottom: 10px;
  }
  
  .user-message {
    text-align: right;
    color: #ffffff;
  }
  
  .bot-message {
    text-align: left;
    color: #8e44ad; /* Bot response color */
  }
  
  .chat-input {
    display: flex;
    gap: 10px;
  }
  
  input {
    flex-grow: 1;
    border: 1px solid #8e44ad;
    border-radius: 6px;
    padding: 10px;
    background: #2c2c3c;
    color: #ffffff;
  }
  
  input::placeholder {
    color: #cccccc;
  }
  
  button {
    background: linear-gradient(90deg, #8e44ad, #3498db);
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 6px;
    transition: 0.3s ease;
    cursor: pointer;
  }
  
  button:hover {
    background: linear-gradient(90deg, #e91e63, #8e44ad);
    transform: scale(1.05);
  }
  </style>
  