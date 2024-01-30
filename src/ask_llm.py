import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import (SystemMessage, HumanMessage, AIMessage)

load_dotenv()
OPEN_API_KEY = os.getenv("OPENAI_API_KEY")
chat = ChatOpenAI(api_key = OPEN_API_KEY, model = 'gpt-3.5-turbo')

def llm_response(query):
    messages = [
    SystemMessage(content="You are a helpful assistent")
    ]
    prompt = HumanMessage(content=f"{query}")
    messages.append(prompt)
    res = chat(messages)
    return(res.content) 
