from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app)

class OpenAIChat:
    """Class to handle interactions with the OpenAI api"""
    
    def __init__(self) -> None:
        self.model = "gpt-3.5-turbo"
        self.historical_messages = []
        
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        
    def load_file(self) -> None:
        """Load prompt template"""
        file_path = "./prompt/prompt.txt"
        with open(file_path) as f:
            prompt_template = f.read()
        return prompt_template
            
        




if __name__ == '__main__':
    app.run(debug=True)
