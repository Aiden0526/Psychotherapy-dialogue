<template>
    <div class="chat-container">
        <h2>Chat with {{ psychologist.name }}</h2>
  
        <!-- Dialogue box where messages will be displayed -->
        <div class="dialogue-box">
            <div v-for="message in messages" :key="message.id" :class="{'user-message': message.sender === 'User', 'psychologist-message': message.sender === 'Psychologist'}">
                <!-- For psychologist: label on the left -->
                <div v-if="message.sender === 'Psychologist'" class="psychologist-image">
                    <img :src="psychologist.image" :alt="psychologist.name" />
                </div>

                <!-- Message text -->
                <div class="message-text">
                    <p>{{ message.text }}</p>
                </div>

            </div>
        </div>
  
        <!-- Input box and send button -->
        <div class="input-box">
            <input v-model="userMessage" type="text" placeholder="Type your message..." />
            <button @click="sendMessage">Send</button>
        </div>

        <!-- Back button to return to the introduction page -->
        <div class="back-button-container">
            <button @click="goBack" class="back-button">Back to Introduction</button>
        </div>

        <!-- Button to view the psychologist's summary -->
        <div class="summary-button-container">
            <button @click="fetchSummary" class="summary-button">View Summary</button>
        </div>

        <!-- Modal for displaying summary -->
        <div v-if="showSummary" class="modal">
            <div class="modal-content">
                <span @click="closeSummary" class="close-button">&times;</span>
                <h3>Summary from {{ psychologist.name }}</h3>
                <p>{{ summary }}</p>
                <button @click="closeSummary" class="close-button">Close</button>
            </div>
        </div>


    </div>
  </template>
  
  <script>

import { io } from 'socket.io-client';
// import axios from 'axios';

export default {
    data() {
        return {
        userMessage: '', // Message typed by the user
        messages: [], // Array to store the dialogue messages
        psychologist: {
            id: this.$route.params.id,
            name: this.$route.query.name || 'Psychologist', // Psychologist's name received from the query parameter
            image: this.$route.query.image, // Psychologist's image received from the query parameter
        },
        socket: null, // Socket.IO client
        showSummary: false, // Flag to show/hide the summary modal
        summary: '', // Summary text received from the backend
        };
    },
    created() {
        // Initialize the Socket.IO client
        this.socket = io('http://localhost:5000');

        // Listen for 'response_streaming' events
        this.socket.on('response_streaming', (data) => {
        console.log('Received chunk:', data.data);

        // Update the last message from the psychologist
        if (this.messages.length > 0 && this.messages[this.messages.length - 1].sender === 'Psychologist') {
            this.messages[this.messages.length - 1].text += data.data;
        } else {
            // If there is no existing message from the psychologist, create a new one
            this.messages.push({
            id: Date.now() + 1,
            text: data.data,
            sender: 'Psychologist',
            });
        }
        });
    },
    methods: {
        async sendMessage() {
            if (this.userMessage.trim() === '') return;
            // Add the user's message to the messages array
            this.messages.push({
                id: Date.now(),
                text: this.userMessage,
                sender: 'User',
            });

            // Clear the input box after sending
            const userQuestion = this.userMessage;
            this.userMessage = '';

            try {
                // Send the user's message to the backend to initiate streaming
                const response = await fetch('http://localhost:5000/chat/streaming', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    psychologist_name: this.psychologist.name,
                    user_question: userQuestion,
                }),
                });

                // Get the response from the backend
                const data = await response.json();

                if (!response.ok) {
                // Display an error message if the response was not successful
                console.error('Error from backend:', data.error);
                this.messages.push({
                    id: Date.now() + 1,
                    text: 'There was an error processing your request. Please try again later.',
                    sender: 'Psychologist',
                });
                }
            } catch (error) {
                console.error('Error connecting to backend:', error);
                this.messages.push({
                id: Date.now() + 1,
                text: 'Unable to connect to the server. Please check your connection.',
                sender: 'Psychologist',
                });
            }
        },
        beforeDestroy() {
            // Clean up the socket connection when the component is destroyed
            if (this.socket) {
            this.socket.disconnect();
            }
        },
        async fetchSummary() {
            this.summary = 'Generating summary...';
            this.showSummary = true;

            try {
                const response = await fetch('http://localhost:5000/summary', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ psychologist_name: this.psychologist.name }),
                });
                const data = await response.json();

                if (response.ok) {
                this.psychologistSummary = data.summary; //update the summary from backend
                } else {
                console.error('Error fetching summary:', data.error);
                this.psychologistSummary = 'Failed to load summary. Please try again later.';
                this.showSummaryModal = true;
                }
            } catch (error) {
                console.error('Error fetching summary from backend:', error);
                this.psychologistSummary = 'Unable to connect to the server. Please check your connection.';
                this.showSummaryModal = true;
            }
        },
        closeSummary() {
            this.showSummary = false;
        },
        goBack() {
            // Navigate back to the introduction page
            this.$router.push(`/psychologist/${this.psychologist.id}/intro`);
        },
    }
  };
  </script>
  



<style scoped>
/* Container for the chat page */
.chat-container {
display: flex;
flex-direction: column;
justify-content: center;
align-items: center;
padding: 2rem;
font-family: 'Arial', sans-serif;
min-height: 100vh;
background-color: #f4f6f9;
}

/* Title styling */
h2 {
font-size: 1.8rem;
color: #333;
margin-bottom: 1.5rem;
}

/* Dialogue box to display the messages */
.dialogue-box {
width: 100%;
max-width: 1000px;
height: 600px;
border: 1px solid #ddd;
background-color: white;
overflow-y: auto;
padding: 1rem;
margin-bottom: 1rem;
border-radius: 8px;
}

/* Styling for user and psychologist messages */
.user-message {
text-align: right;
margin-bottom: 0.5rem;
color: #4caf50;
}

.psychologist-message {
display: flex;
align-items: center;
text-align: left;
margin-bottom: 0.5rem;
color: #2196f3;
}

/* Psychologist's image styling */
.psychologist-image img {
width: 40px;
height: 40px;
border-radius: 50%;
margin-right: 10px; /* Add space between image and message */
}

/* Input box and send button */
.input-box {
display: flex;
gap: 0.5rem;
width: 100%;
max-width: 600px;
}

.input-box input {
flex-grow: 1;
padding: 0.8rem;
border: 1px solid #ddd;
border-radius: 4px;
font-size: 1rem;
}

.input-box button {
background-color: #4caf50;
color: white;
padding: 0.8rem 1.5rem;
border: none;
border-radius: 4px;
font-size: 1rem;
cursor: pointer;
}

.input-box button:hover {
background-color: #45a049;
}

/* Back to Introduction button */
.back-button-container {
margin-top: 1rem;
}

.back-button {
background-color: #f44336;
color: white;
padding: 0.8rem 1.5rem;
border: none;
border-radius: 4px;
font-size: 1rem;
cursor: pointer;
}

.back-button:hover {
background-color: #d32f2f;
}
</style>