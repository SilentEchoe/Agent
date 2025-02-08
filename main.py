#导入LangChain Hub
from langchain import hub
# 从LangChain Hub中获取ReAct的提示
prompt = hub.pull("hwchase17/react")
print(prompt)
#导入OpenAI
from langchain_openai import OpenAI
llm = OpenAI()
from langchain_community.utilities import SerpAPIWrapper
from langchain.agents.tools import Tool
#实例化SerpAPIWrapper
search = SerpAPIWrapper()
tools = [
    Tool(
        name="Search",
        func = search.run,
        description="当大模型没有相关知识时，用于搜索知识"
    )
]
from langchain.agents import create_react_agent
#构建ReAct Agent
agent = create_react_agent(llm,tools,prompt)
#导入AgentExecutor
from langchain.agents import AgentExecutor
agent_executor = AgentExecutor(agent=agent,tools=tools,verbose = True)
#调用AgentExecutor
agent_executor.invoke({"input:":"当前Agent最新研究进展是什么？"})

