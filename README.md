# Psychotherapy-dialogue

A web-based psychotherapy dialogue system that allows users to have therapeutic conversations with simulated renowned psychologists. This application includes a real-time chat interface, personalized responses from psychologists, and a summary generation feature.


## Set up

### Prerequisites:
- Node.js and npm
- Python 3.9

### Clone the Repository:
```
git clone https://github.com/yourusername/psychotherapy-dialogue
cd psychotherapy-dialogue
```

### Backend Setup

1. **Navigate to the backend directory**:
```bash
cd backend
```
2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Set up environment variables**:
Replace [your-api-key] with your openai api key.
```
export OPENAI_API_KEY=[your-api-key]
```

### Frontend Setup

1. **Navigate to the frontend directory**:
```bash
cd ../frontend
```

2. **Install frontend dependencies**:
```bash
npm install
```

## Running the Application

### Starting the Backend Server

```bash
# Navigate to backend directory
cd backend
# Start the Flask server
python app.py
```

The backend server will run on `http://localhost:5000`.

### Starting the Frontend Development Server

In a new terminal window:

```bash
# Navigate to frontend directory
cd frontend
# Start the Vue development server
npm run serve
```

The frontend server will run on `http://localhost:8080`.


## Usage

1. **Homepage**: Select a psychologist to start a session.
2. **Introduction Page**: View the psychologist's bio and begin the chat.
3. **Chat Page**: Engage in a conversation. Type messages, and view the psychologist's responses streamed in real-time.
4. **View Summary**: Click the “View Summary” button to see a synthesized summary of key therapeutic points.