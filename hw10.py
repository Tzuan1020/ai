# 參考111010529顏瑋成同學所完成
import os
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_groq import ChatGroq

# set up API key
os.environ["TAVILY_API_KEY"] = "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"

tools = [TavilySearchResults(max_results=1)]

# Get the prompt to use - you can modify this!
prompt = hub.pull("hwchase17/react")

# Choose the LLM to use
llm = ChatGroq(api_key="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")

# Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt)

# Create an agent executor by passing in the agent and tools
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

question = input ("請輸入問題: ")

agent_executor.invoke({"input": "question"})
