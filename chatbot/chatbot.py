import os
from dotenv import load_dotenv
from openai_config import generation_config
from langchain_openai import ChatOpenAI, OpenAI



def chat_openai(model_name: str) -> ChatOpenAI:
    
    """
    Creates and returns an LLM object with appropriate error handling.

    Args: model_name (str): Name of the LLM model to create.
    Returns: ChatOpenAI: The created LLM object.
    """
    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("Missing API key")
    
    try:
        chat_model = ChatOpenAI(
            model=model_name,
            openai_api_key=OPENAI_API_KEY,
        )
        return chat_model
    
    except Exception as error:
        if "Invalid API key" in str(error):
            raise ValueError("Invalid API key provided.") from error
        else:
            raise RuntimeError("Unexpected error:", error) from error



def openai(model_name: str) -> OpenAI:
    
    """
    Creates and returns an LLM object with appropriate error handling.

    Args: model_name (str): Name of the LLM model to create.
    Returns: OpenAI: The created LLM object.
    """
    load_dotenv()
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    if not OPENAI_API_KEY:
        raise ValueError("Missing API key")
    
    try:
        chat_model = OpenAI(
            model=model_name,
            generation_config=generation_config,
            openai_api_key=OPENAI_API_KEY,
        )
        return chat_model
    
    except Exception as error:
        if "Invalid API key" in str(error):
            raise ValueError("Invalid API key provided.") from error
        else:
            raise RuntimeError("Unexpected error:", error) from error


