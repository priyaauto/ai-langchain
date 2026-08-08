from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate


llm = ChatOllama(model ="llama3.2", temperature=0)

info =""" Devops is a team. They work on both operations and support"""

prompt_template = """ 

Give the information for below team

{info}

1. A short summary
3. Main 2 works

"""

prompt = PromptTemplate(
    input = ["info"],
    template= prompt_template,
)

langchain = prompt | llm

reponse= langchain.invoke(
    {"info":info}
)
print(reponse.text)

