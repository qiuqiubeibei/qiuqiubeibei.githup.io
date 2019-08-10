import requests

proxies = {'http': 'http://119.3.212.26:56264'}
headrs = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
}
re = requests.get("http://www.baidu.com", proxies=proxies, headers=headrs)
print(re.status_code)