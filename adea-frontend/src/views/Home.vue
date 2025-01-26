<template>
  <div class="home">
    <div class="hero">
      <h1>Welcome to Podcastify</h1>
      <p> Your digital education assistent making learning fun and accessible.</p>
      <p> Study smarter not harder!</p>
      <router-link to="/upload" class="cta-button">Get Started</router-link>
    </div>
  </div>
</template>

<style scoped>
.hero {
  text-align: center;
  margin: 5rem auto;
  padding: 2rem;
  max-width: 600px;
  background: white;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
}
.hero h1 {
  color: #2c7be5;
  font-size: 2.5rem;
  margin-bottom: 1rem;
}
.hero p {
  font-size: 1.2rem;
  color: #333333;
  margin-bottom: 2rem;
}
.cta-button {
  display: inline-block;
  background: #2c7be5;
  color: white;
  padding: 0.8rem 2rem;
  border-radius: 8px;
  font-weight: bold;
  text-decoration: none;
  transition: background 0.3s;
}
.cta-button:hover {
  background: #ff8a48;
}
</style>
