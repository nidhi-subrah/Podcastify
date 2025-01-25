<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/upload">Upload</router-link></li>
        <li><router-link to="/feedback">Feedback</router-link></li>
        <li><router-link to="/chatbot">Chatbot</router-link></li>
        <li><router-link to="/output">Output</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  name: "App",
};
</script>

<style scoped>
nav {
  background: linear-gradient(90deg, #8e44ad, #3498db);
  color: white;
  padding: 10px;
}
nav ul {
  list-style: none;
  display: flex;
  gap: 15px;
  padding: 0;
  justify-content: center;
}
nav ul li {
  display: inline;
}
nav ul li a {
  color: white;
  font-weight: 500;
  text-decoration: none;
  transition: color 0.3s ease;
}
nav ul li a:hover {
  color: #e91e63; /* Pink accent on hover */
}
</style>
