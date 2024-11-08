from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import OpenAIChat
import logging
from flask_socketio import SocketIO

# Set up logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

openai_chat = OpenAIChat()

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint to receive a message from the frontend and get a response from OpenAI API.
    
    Input:
        JSON payload with the following fields:
            psychologist_name (str): The name of the psychologist to role-play.
            user_question (str): The question posed by the user.

    Returns:
        JSON response containing:
            response (str): The generated response from the OpenAI API based on the constructed prompt.
        
    Raises:
        400 Bad Request: If either `psychologist_name` or `user_question` is missing from the payload.
        500 Internal Server Error: If there is an issue communicating with the OpenAI API.
    """
    data = request.get_json()
    logging.debug(f"Request JSON payload: {data}")
    psychologist_name = data.get('psychologist_name')
    user_question = data.get('user_question')
    
    # Validate input
    if not user_question or not psychologist_name:
        return jsonify({"error": "Missing required fields: message or psychologist_name"}), 400
    
    # Load prompt template
    prompt = openai_chat.construct_prompt(psychologist_name, user_question, openai_chat.historical_messages)
    logging.debug(f"Constructed prompt: {prompt}")
    
    # Get response from OpenAI
    try:
        response = openai_chat.get_response(prompt).strip()
        logging.debug(f"Response from utils: {response}")
    except Exception as e:
        return jsonify({"Fail to get response from OpenAI": str(e)}), 500
    
    # Update historical messages
    messages = f"User: {user_question}\nPsychologist: {response}"
    openai_chat.historical_messages.append(messages)
    
    # Send response to frontend
    return jsonify({"response": response})


@app.route('/chat/streaming', methods=['POST'])
def chat_streaming():
    """Endpoint to handle and initiate streaming response to the client.
    
    Input:
        JSON payload with the following fields:
            - `psychologist_name` (str): The name of the psychologist to role-play.
            - `user_question` (str): The question posed by the user.

    Output:
        - Emits each chunk of the OpenAI streaming response to the client using Socket.IO.
        - Final JSON response to indicate completion of streaming (not part of streaming itself).
    
    Raises:
        - 400 Bad Request: If either `psychologist_name` or `user_question` is missing from the request payload.
        - 500 Internal Server Error: If there is an issue while communicating with OpenAI API.
    """
    data = request.get_json()
    logging.debug(f"Request JSON payload: {data}")
    psychologist_name = data.get('psychologist_name')
    user_question = data.get('user_question')
    
    # Validate input
    if not user_question or not psychologist_name:
        return jsonify({"error": "Missing required fields: message or psychologist_name"}), 400
    
    # Load prompt template
    prompt = openai_chat.construct_prompt(psychologist_name, user_question, openai_chat.historical_messages)
    logging.debug(f"Constructed prompt: {prompt}")
    
    # Get response from OpenAI
    try:
        # Stream the OpenAI response to the client
        for chunk in openai_chat.get_response_streaming(prompt):
            if chunk:
                logging.debug(f"Response from utils: {chunk}")
                socketio.emit('response_streaming', {'data': chunk})
            else:
                logging.debug("Received empty chunk, skipping.")

    except Exception as e:
        logging.error(f"Failed to get response from utils: {e}")
        return jsonify({"Fail to get response from utils": str(e)}), 500
    
    return jsonify({"error": "Streaming complete"})

if __name__ == '__main__':
    socketio.run(app, debug=True)
