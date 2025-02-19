# from duckduckgo_search import DDGS
#
# with DDGS() as ddgs:
#     # 使用正确的 text() 方法
#     for result in ddgs.text("搜索关键词", max_results=5):
#         print(result)

import easyocr
import time

t = time.time()
reader = easyocr.Reader(['ch_sim','en'], gpu=False) # this needs to run only once to load the model into memory

n = 100
sum = 0
counter = 1
while counter <= n :
    sum = sum + counter
    counter +=1
    result = reader.readtext('example.png')
    print(result)
print(f'coast:{time.time()- t:.4f}s')