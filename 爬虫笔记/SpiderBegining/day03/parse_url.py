# 爬虫封装模块
import requests
from retrying import retry

#简单的请求头
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"}

# retry装饰器对指定url发送请求，若失败，重复发送指定次数。
@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data, proxies):

    print("*" * 20)
    if method == "post":
        response = requests.post(url, data=data, headers=headers, proxies=proxies)
    else:
        response = requests.get(url, headers=headers, timeout=3, proxies=proxies)
    assert response.status_code == 200
    return response.content.decode()

# 封装url发送请求,获取请求模块，对其进行异常处理
def parse_url(url, method=None, data=None, proxies=None):
    try:
        # 对requests中的url地址，请求方法,请求指定数据,指定ip代理等
        html_str = _parse_url(url, method, data, proxies)
    except:
        html_str = None

    return html_str


if __name__ == '__main__':
    url = "http://www.baidu.com"
    print(parse_url(url))
