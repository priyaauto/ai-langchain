from langchain_tavily import TavilySearch
from dotenv import load_dotenv

load_dotenv()
search = TavilySearch(max_results=5)

results = search.invoke({
    "query": "latest devops news"
})

print(results)