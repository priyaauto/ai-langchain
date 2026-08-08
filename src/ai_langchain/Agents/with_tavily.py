from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from langchain_tavily import TavilySearch

from dotenv import load_dotenv

load_dotenv()


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

search = TavilySearch(max_results=5)

agent = create_agent(model=llm, tools= [search])


response = agent.invoke({
    
    "messages":[
        {
            "role": "user",
            "content": "What is the weather in coimbatore?"       
        }
    ]

})
print("LLM response:")
print(response["messages"][-1].content)

