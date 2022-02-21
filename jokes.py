# 從 Dad jokes 網站爬取笑話，並可以讓使用者指定『關鍵字』，將相關資料收集下來，儲存到一個 txt 檔中。
# Packages
import requests
import json
import random
import time
def date_time():
    now = time.localtime()
    rightnow = time.strftime("%Y/%m/%d, %H:%M:%S", now)
    return rightnow

url = "https://icanhazdadjoke.com/search"
search = input("Please enter what you want to search: ")
response = requests.get(url, headers = {"Accept": "application/json"}, params = {"term": search})
result = json.loads(response.text)
joke_num = result['total_jokes']
with open("jokes.txt","a") as f:
    if joke_num>0:
        results = random.choice(result['results'])
        answer = results["joke"]
        f.write(f"[{date_time()}]\n")
        f.write(f"I found {joke_num} jokes about \"{search}\", here is one for you:\n")
        f.write(f"{answer}\n")
    else:
        f.write(f"[{date_time()}]\n")
        f.write(f"There is no joke about \"{search}\"\n")


