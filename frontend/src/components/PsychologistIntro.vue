<template>
  <div class="psychologist-intro">
    <h1>{{ psychologist.name }}</h1>
    <p class="bio">{{ psychologist.bio }}</p>
    
    <div class="buttons-container">
      <button @click="goBack" class="back-button">Back to Home</button>
      <button @click="startChat" class="chat-button">Chat with {{ psychologist.name }}</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      psychologists: [
        {
          id: 1,
          name: "Sigmund Freud",
          bio: "Sigmund Freud was an Austrian neurologist and the founder of psychoanalysis. His theories on the unconscious mind and the mechanisms of repression are some of the most well-known in psychology."
        },
        {
          id: 2,
          name: "Carl Jung",
          bio: "Carl Jung was a Swiss psychiatrist and psychoanalyst who founded analytical psychology. His work has been influential not only in psychiatry but also in philosophy, anthropology, and religious studies."
        },
        {
          id: 3,
          name: "Alfred Adler",
          bio: "Alfred Adler was an Austrian medical doctor, psychotherapist, and founder of the school of individual psychology. His emphasis on the importance of feelings of inferiority is recognized as an isolating element which plays a key role in personality development."
        }
      ],
      psychologist: {}
    };
  },
  created() {
    const psychologistId = parseInt(this.$route.params.id);
    this.psychologist = this.psychologists.find(p => p.id === psychologistId);
  },
  methods: {
    goBack() {
      this.$router.push('/');
    },
    startChat() {
      this.$router.push(`/psychologist/${this.psychologist.id}/chat`);
    }
  }
};
</script>

<style scoped>
/* Container for the introduction page */
.psychologist-intro {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 2rem;
  background-color: #f9f9f9;
  min-height: 100vh;
  font-family: 'Arial', sans-serif;
}

/* Styling for the psychologist's name */
h1 {
  font-size: 2.5rem;
  color: #333;
  margin-bottom: 1.5rem;
}

/* Styling for the bio/description */
.bio {
  font-size: 1.2rem;
  color: #555;
  max-width: 600px;
  text-align: center;
  margin-bottom: 2rem;
}

/* Container for the buttons */
.buttons-container {
  display: flex;
  gap: 1.5rem;
}

/* Back to Home button styling */
.back-button {
  background-color: #f44336;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.back-button:hover {
  background-color: #d32f2f;
}

/* Chat button styling */
.chat-button {
  background-color: #4caf50;
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 8px;
  font-size: 1.2rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.chat-button:hover {
  background-color: #45a049;
}
</style>
