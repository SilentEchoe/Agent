import os
from langchain_openai import OpenAI
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain_community.agent_toolkits.load_tools import load_tools

# 配置密钥（示例值，请替换为实际密钥）

# 正确配置第三方API（关键修改点）
llm = OpenAI(
    openai_api_base="https://api.siliconflow.cn/v1",  # 统一使用官方参数名
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model="deepseek-ai/DeepSeek-V3",  # 确认模型名称正确
    temperature=0.7,
    max_tokens=500,
    # 已移除 headers 参数
)

# 加载工具（添加超时配置）
tools = load_tools(
    ["serpapi", "llm-math"],
    llm=llm,
    serpapi_params={"timeout": 30}
)

# 优化提示模板（强调数值处理）
template = """请按以下步骤执行：

工具列表：{tools}

回答格式：
Question: 问题内容
Thought: 分析思路
Action: 使用工具 [{tool_names}]
Action Input: 工具输入（需明确数值单位）
Observation: 工具返回结果
...（最多重复3次）
Thought: 最终结论
Final Answer: 答案（必须包含具体数值和单位）

当前问题：{input}
已执行步骤：{agent_scratchpad}
"""

prompt = PromptTemplate.from_template(template)

# 创建执行器（增强容错）
agent_executor = AgentExecutor(
    agent=create_react_agent(llm, tools, prompt),
    tools=tools,
    verbose=True,
    max_execution_time=120,  # 总执行时间限制
    handle_parsing_errors=lambda _: "请求解析失败，请重试",  # 简化错误处理
    return_intermediate_steps=True  # 用于调试
)

# 执行调用（添加重试机制）
try:
    result = agent_executor.invoke({
        "input": "请执行：1.查询玫瑰花当前批发价（每支） 2.计算加价5%后的售价"
    })
    print("最终结果：", result["output"])
except Exception as e:
    print(f"执行异常：{str(e)}")
    if hasattr(agent_executor, 'intermediate_steps'):
        print("中间步骤：", agent_executor.intermediate_steps)
