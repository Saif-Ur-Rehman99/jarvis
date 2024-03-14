import os
import sys
sys.path.append('/home/saif/Documents/jarvis/chatbot')
from chatbot import chat_openai
from langchain.agents import Tool, initialize_agent
from langchain_community.utilities.serpapi import SerpAPIWrapper
from dotenv import load_dotenv

load_dotenv()

llm = chat_openai('gpt-3.5-turbo')

# Google Search
search = SerpAPIWrapper(
    params = {
        "engine": 'google',
        "gl" : "us",
        "hl" : "en",
    },
    serpapi_api_key=os.getenv('SERPAPI_API_KEY')
)

search_tool = Tool(
    name = "Web Search",
    func=search.run,
    description="A useful tool for searching the Internet to find information on world events, issues, etc. Worth using for general topics. Use precise questions."
)


agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=[search_tool],
    llm=llm,
    verbose=True,
    max_iterations=3
)

response = agent('who is the current president of Pakistan')
print(response)