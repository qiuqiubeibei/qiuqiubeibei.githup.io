import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
p = {"wd": "千锋"}
url_temp = "https://www.baidu.com/s?wd={}".format('千锋')
r = requests.get(url_temp, headers=headers)
print(r.status_code)
print(r.request.url)

 