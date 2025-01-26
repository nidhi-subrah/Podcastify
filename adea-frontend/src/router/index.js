import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Upload from "../views/Upload.vue";
import Feedback from "../views/Feedback.vue";
import Chatbot from "../components/Chatbot.vue"; // Import Chatbot component
import Output from "../views/Output.vue"; // Import Output component

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/upload", name: "Upload", component: Upload },
  { path: "/feedback", name: "Feedback", component: Feedback },
  { path: "/chatbot", name: "Chatbot", component: Chatbot }, // Chatbot route
  { path: '/output', name: 'Output', component: Output },

];
const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
