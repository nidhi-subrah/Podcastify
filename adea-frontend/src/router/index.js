import { createRouter, createWebHistory } from "vue-router";

import Home from "../views/Home.vue";
import Upload from "../views/Upload.vue";
import Feedback from "../views/Feedback.vue";

const routes = [
  { path: "/", name: "Home", component: Home },
  { path: "/upload", name: "Upload", component: Upload },
  { path: "/feedback", name: "Feedback", component: Feedback },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
