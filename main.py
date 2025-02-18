import os
from openai import OpenAI
from langchain_openai import OpenAI
from langchain.agents import load_tools
from langchain.agents import create_react_agent
from langchain.prompts import PromptTemplate

#初始化模型
llm = OpenAI(api_key="",base_url="https://api.siliconflow.cn/v1")

#设置工具

template =(
    '尽你所能回答以下问题。如果能力不够，你可以使用以下工具:\n\n'
    '{tools}\n\n'
    'Use the following format:\n\n'
    'Thought: you should always think about whaht to do \n'
    'Action: the action to take, should be one of [{tool_names}]\n'
    'Action Input: the input to the action\n'
    'Observation: the result of the action\n'
    '... (this Thought/Action/Action Input/Observation can repeat N times)\n'
    'Thought: I now know the final answer \n'
    'Final Answer: the final answer to the original input question\n\n'
    'Begin!\n\n'
    'Question: {input}\n'
    'Thought:{agent_scratchpad}'
)

#初始化提示词模版
prompt = PromptTemplate.from_template(template)



#初始化Agent_
agent = create_react_agent(llm,tools,prompt)





# client = OpenAI(api_key="sk-nsmdcbmcnwdttiwmrpptskpwispbxxmesqenbpbfuhglkfjt", base_url="https://api.siliconflow.cn/v1")
# response = client.chat.completions.create(
#     model='deepseek-ai/DeepSeek-R1',
#     messages=[
#         {'role': 'user',
#          'content': "中国大模型行业2025年将会迎来哪些机遇和挑战"}
#     ],
#     stream=True
# )
#
# for chunk in response:
#     print(chunk.choices[0].delta.content, end='')
