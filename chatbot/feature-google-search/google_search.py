import sys
sys.path.append('/home/saif/Documents/jarvis/chatbot')
from chatbot import chat_openai
from langchain.agents import Tool, load_tools, create_openai_functions_agent
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, AIMessage, HumanMessage
from langchain_community.utilities.serpapi import SerpAPIWrapper
from langchain_community.utilities.you import YouSearchAPIWrapper
from dotenv import load_dotenv
import os

load_dotenv()

llm = chat_openai('gpt-3.5-turbo')


# Create the ChatPromptTemplate
prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content='you are a helper'
        ),
        MessagesPlaceholder(variable_name="agent_scratchpad"),
    ]
)


# Google Search
search = SerpAPIWrapper(
    params = {
        "engine": 'google',
        "gl" : "us",
        "hl" : "en",
    },
    serpapi_api_key=os.getenv('SERPAPI_API_KEY')
)

print(type(search))

tools = load_tools({"serpapi": search})

agent = create_openai_functions_agent(
    llm,
    tools,
    prompt,
)

agent.invoke('who is the current president of Pakistan')




# repl_tool = Tool(
#     name="python_repl",
#     description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",
#     func=search.run('?'),
# )

# print(type(repl_tool))