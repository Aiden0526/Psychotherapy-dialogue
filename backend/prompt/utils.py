import openai
import os

class OpenAIChat:
    """Class to handle interactions with the OpenAI api"""
    
    def __init__(self) -> None:
        self.model = "gpt-3.5-turbo"
        self.historical_messages = []
        
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        
    def load_file(self) -> None:
        """Load prompt template
        
        Returns:
            str: Full prompt
        """
        file_path = "./prompt/prompt.txt"
        with open(file_path) as f:
            prompt_template = f.read()
        return prompt_template
    
    def construct_prompt(self, psychologist_name: str, user_question: str, historical_message_list: list) -> str:
        """Construct prompt to role-play psychologist

        Args:
            psychologist_name (str): The name of the psychologist to role-play.
            user_question (str): The question posed by the user.
            historical_message_list (list): List of historical messages from the conversation.
        
        Returns:
            str: A formatted prompt with the psychologist's name, the user's question, 
                 and the last historical message.
        
        Raises:
            IndexError: If historical_message_list is empty when trying to access the last message.
        """
        full_prompt = self.load_file()
        full_prompt = full_prompt.replace("{psychologist_name}", psychologist_name)
        full_prompt = full_prompt.replace("{user_question}", user_question)
        full_prompt = full_prompt.replace("{historical_messages}", historical_message_list[-1]) # Only use the last message to avoid hitting the token limit
        return full_prompt
    
    def get_response(self, prompt: str) -> str:
        """Get response from OpenAI
        
        Args:
            prompt (str): The constructed prompt for OpenAI API to process.
        
        Returns:
            str: The response text from OpenAI.
        
        Raises:
            openai.error.OpenAIError: If the OpenAI API request fails.
        """
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            temperature=0.7,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text