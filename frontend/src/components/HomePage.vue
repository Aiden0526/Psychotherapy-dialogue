<template>
  <div class="home-page">
    <h1>Explore the Minds of History's Greatest Psychologists</h1>
    <p class="subtitle">Choose a psychologist below and start a conversation</p>
    <div class="psychologists-container">
      <button @click="selectPsychologist(1)" class="psychologist-button">Sigmund Freud</button>
      <button @click="selectPsychologist(2)" class="psychologist-button">Carl Jung</button>
      <button @click="selectPsychologist(3)" class="psychologist-button">Alfred Adler</button>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    selectPsychologist(id) {
      this.$router.push(`/psychologist/${id}/intro`);
    }
  }
};
</script>

<style scoped>
/* General styling for the page */
.home-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  background-color: #f0f4f8;
  font-family: 'Arial', sans-serif;
}

/* Styling for the page heading */
h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 2rem;
}

/* Styling for the page subtitle */
.subtitle {
  font-size: 1.5rem;  /* Increased font size from 1.2rem to 1.5rem */
  color: #555;
  margin-bottom: 2rem;
  text-align: center;
}

/* Container for the psychologist buttons */
.psychologists-container {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

/* Styling for psychologist buttons */
.psychologist-button {
  background-color: #4caf50;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.psychologist-button:hover {
  background-color: #45a049;
}

/* Add some spacing on small screens */
@media (max-width: 600px) {
  .psychologist-button {
    width: 100%;
    font-size: 1rem;
  }
}
</style>
