from langchain_core.tools import tool
from langchain_ollama import ChatOllama

@tool
def get_weather():
    """Get the current weather in CBE."""
    message = "CBE weather is 40 degree Celsius"
    return message


llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

# Give the tool to the LLM
llm_with_tools = llm.bind_tools([get_weather])


# Ask the LLM
response = llm_with_tools.invoke(
    "What is the weather in CBE?"
)

print("LLM response:")
print(response)


# Check whether LLM requested a tool
if response.tool_calls:

    tool_call = response.tool_calls[0]

    print("Tool requested:")
    print(tool_call["name"])

    # Actually execute the tool
    result = get_weather.invoke(
        tool_call["args"]
    )

    print("Tool result:")
    print(result)