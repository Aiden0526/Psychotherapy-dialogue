import openai
import os

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
    
    def construct_prompt(self, psychologist_name: str, user_question: str, historical_message_list: list) -> str:
        """Construct prompt to role-play psychologist"""
        full_prompt = self.load_file()
        full_prompt = full_prompt.replace("{psychologist_name}", psychologist_name)
        full_prompt = full_prompt.replace("{user_question}", user_question)
        full_prompt = full_prompt.replace("{historical_messages}", historical_message_list[-1]) # Only use the last message to avoid hitting the token limit
        return full_prompt
    
    def get_response(self, prompt: str) -> str:
        """Get response from OpenAI"""
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text