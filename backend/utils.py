import openai
from openai.error import OpenAIError
import os
import time
import logging

logger = logging.getLogger(__name__)

class OpenAIChat:
    """Class to handle interactions with the OpenAI api"""
    
    def __init__(self) -> None:
        self.model = "gpt-3.5-turbo"
        self.historical_messages = []
        
        openai.api_key = os.environ.get("OPENAI_API_KEY")
        
    def load_prompt(self) -> None:
        """Load the conversation prompt template
        
        Returns:
            str: Full prompt
        """
        file_path = "./prompt/prompt.txt"
        with open(file_path) as f:
            prompt_template = f.read()
        return prompt_template
    
    def load_summary_prompt(self) -> None:
        """Load the conversation summary prompt template
        
        Returns:
            str: Full prompt
        """
        file_path = "./prompt/summary_prompt.txt"
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
        full_prompt = self.load_prompt()
        full_prompt = full_prompt.replace("{psychologist_name}", psychologist_name)
        full_prompt = full_prompt.replace("{user_question}", user_question)
        
        # Only use the last message to avoid hitting the token limit
        last_message = historical_message_list[-1] if historical_message_list else "No historical messages"
        full_prompt = full_prompt.replace("{historical_messages}", last_message) 
        return full_prompt
    
    def construct_summary_prompt(self, historical_message_list: list) -> str:
        """Construct prompt to generate summary of conversation
        
        Args:
            historical_message_list (list): List of historical messages from the conversation.
        
        Returns:
            str: A formatted prompt with the historical messages.
        """
        if not historical_message_list:
            return 'No historical messages to summarize.'
        else:
            historical_messages_text = "\n".join(historical_message_list)
        
        full_prompt = self.load_summary_prompt()
        full_prompt = full_prompt.replace("{historical_messages}", historical_messages_text)
        return full_prompt
    
    def get_response(self, prompt: str, retries: int = 3, delay: float = 1.0) -> str:
        """Get response from OpenAI
        
        Args:
            prompt (str): The constructed prompt for OpenAI API to process.
        
        Returns:
            str: The response text from OpenAI.
        
        Raises:
            openai.error.OpenAIError: If the OpenAI API request fails after all retry attempts.
        """
        attempt = 0
        while attempt <= retries:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                )
                logging.debug(f"Response from OpenAI: {response}")
                return response.choices[0].message['content']
            
            except OpenAIError as e:
                if attempt == retries:
                    raise  # Re-raise the exception after the last attempt
                else:
                    print(f"Attempt {attempt + 1} failed: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
                    attempt += 1
                    
                    
    def get_response_streaming(self, prompt: str, retries: int = 3, delay: float = 1.0) -> str:
        """Get response from OpenAI in Streaming
        
        Args:
            prompt (str): The constructed prompt for OpenAI API to process.
        
        Returns:
            str: The response text from OpenAI.
        
        Raises:
            openai.error.OpenAIError: If the OpenAI API request fails after all retry attempts.
        """
        attempt = 0
        while attempt <= retries:
            try:
                response = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    stream=True
                )
                logger.info("Successfully connected to OpenAI. Streaming response started.")
                
                # Yield each part of the streaming response
                for chunk in response:
                    text_part = chunk['choices'][0]['delta'].get('content', '')
                    logging.debug(f"Text part from OpenAI: {text_part}")
                    yield text_part
                break
            
            except OpenAIError as e:
                logging.error(f"OpenAIError during streaming: {e}")
                if attempt == retries:
                    yield "Error: Unable to process request."
            except Exception as e:
                logging.error(f"Error during streaming: {e}")
                yield "Error: Unable to process request."
