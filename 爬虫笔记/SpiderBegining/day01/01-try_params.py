import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
p = {"wd": "千锋"}
url_temp = "https://www.baidu.com/s?"

#特别注意的是，在get里参数必须得以键值的方式来传，不然参数会混乱导致程序异常，因为在get方法当中参数是有具体的位置的
r = requests.get(url_temp, headers=headers, params=p)
print(r.status_code)
print(r.request.url)
print(r.url)
