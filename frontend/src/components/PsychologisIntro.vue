<template>
    <div>
      <h1>{{ psychologist.name }}</h1>
      <p>{{ psychologist.bio }}</p>
      
      <button @click="goBack">Back to Home</button>
      <button @click="startChat">Chat with {{ psychologist.name }}</button>
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
      // Get the psychologist ID from the route parameters and load the corresponding psychologist's data
      const psychologistId = parseInt(this.$route.params.id);
      this.psychologist = this.psychologists.find(p => p.id === psychologistId);
    },
    methods: {
      // Navigate back to the home page
      goBack() {
        this.$router.push('/');
      },
      // Navigate to the chat page with the selected psychologist
      startChat() {
        this.$router.push(`/psychologist/${this.psychologist.id}/chat`);
      }
    }
  };
  </script>
  