from duckduckgo_search import DDGS

with DDGS() as ddgs:
    # 使用正确的 text() 方法
    for result in ddgs.text("搜索关键词", max_results=5):
        print(result)
