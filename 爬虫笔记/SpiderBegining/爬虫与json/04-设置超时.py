import urllib.request

#如果网页长时间超时未响应，判断系统超时，无法爬取

for i in range(1, 100):
    try:
        response = urllib.request.urlopen("http://www.baidu.com", timeout=0.5)
        print(len(response.read().decode("utf-8")))
    except:
        print("请求超时，继续下一个爬取")