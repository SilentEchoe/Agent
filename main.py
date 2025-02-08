from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_community.llms import Cohere, HuggingFaceHub
from langchain.model_laboratory import ModelLaboratory

#初始化环境变量
load_dotenv()

OpenAI = OpenAI(temperature=0.1)
cohere =Cohere(model="command",temperature=0.1)
huggingface = HuggingFaceHub(repo_id="tiiuae/falcon-7b",model_kwargs={'temperature':0.1})
#创建一个模型实验室的实例，整合OpenAI,cohere,huggingface
model_lab = ModelLaboratory.from_llms([OpenAI,cohere,huggingface])
#使用模型实验室比较不同模型对同一个问题的答案
model_lab.compare("樱花源于哪个国家")