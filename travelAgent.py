from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub

llm = ChatOpenAI(model="gpt-3.5-turbo")

query = """
Vou viajar para Londres em agosto de 2024.
Quero que faça um roteiro de viagem para mim com eventos que irão ocorrer na data da viagem e com o preço de passagem de São Paulo para Londres.
"""

def researchAgent(query, llm):
  tools = load_tools(["ddg-search", "wikipedia"], llm=llm)
  prompt = hub.pull("hwchase17/react")
  agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)
  agent_executor = AgentExecutor(agent=agent, llm=llm, tools=tools, prompt=prompt, verbose=True)
  webContext = agent_executor.invoke({ "input": query })
  return webContext["output"]

print(researchAgent(query,llm))