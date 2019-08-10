import urllib.request
import random

url = "http://www.baidu.com"
'''
反反爬虫方式一模拟浏览器

#模拟请求头
headers= {

    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) \
     AppleWebKit/537.36(KHTML, like Gecko) chrome/59.0.3071.115 Safari/537.36"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)

#发起请求

response = urllib.request.urlopen(req)
data = response.read().decode("utf-8")
print(data)

'''
#通过对Users-Agent进行更换，达到反反爬虫的目的
agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0"
]
agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加了User-Agent
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))