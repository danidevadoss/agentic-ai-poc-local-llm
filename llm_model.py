from langchain_ollama import ChatOllama
from langchain_openai.chat_models import AzureChatOpenAI
import httpx

llm_instance = ChatOllama(
    model="llama3.1:8b",
    base_url="http://localhost:4892",
    temperature=0
)


