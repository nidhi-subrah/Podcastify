<template>
  <div>
    <nav>
      <ul>
        <li><router-link to="/">Home</router-link></li>
        <li><router-link to="/upload">Upload</router-link></li>
        <li><router-link to="/feedback">Feedback</router-link></li>
      </ul>
    </nav>
    <router-view />
  </div>
</template>

<style>
nav {
  background: #333;
  color: white;
  padding: 1rem;
}
nav ul {
  list-style: none;
  display: flex;
  gap: 1rem;
}
nav ul li a {
  color: white;
  text-decoration: none;
}
</style>
