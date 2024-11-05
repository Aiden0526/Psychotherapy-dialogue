<template>
    <div>
      <h2>Chat with {{ psychologist.name }}</h2>
  
      <!-- Dialogue box where messages will be displayed -->
      <div>
        <div v-for="message in messages" :key="message.id">
          <p><strong>{{ message.sender }}:</strong> {{ message.text }}</p>
        </div>
      </div>
  
      <!-- Input box and send button -->
      <div>
        <input v-model="userMessage" type="text" placeholder="Type your message..." />
        <button @click="sendMessage">Send</button>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        userMessage: '',  // Message typed by the user
        messages: [],     // Array to store the dialogue messages
        psychologist: {
          id: this.$route.params.id,
          name: this.$route.query.name || "Psychologist" // Psychologist's name received from the query parameter
        }
      };
    },
    methods: {
      sendMessage() {
        if (this.userMessage.trim() !== '') {
          // Add the user's message to the messages array
          this.messages.push({
            id: Date.now(),
            text: this.userMessage,
            sender: 'User'
          });
  
          // Clear the input box after sending
          this.userMessage = '';
  
          // Placeholder response from the psychologist
          this.messages.push({
            id: Date.now() + 1,
            text: 'Placeholder response from the psychologist.',
            sender: 'Psychologist'
          });
        }
      }
    }
  };
  </script>
  