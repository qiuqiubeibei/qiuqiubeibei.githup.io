import requests

images_url = 'https://www.baidu.com/img/bd_logo1.png'

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
}

re = requests.get(images_url, headers=headers)

with open("SaveData/baidu.png", 'wb') as f:
    f.write(re.content)
print(re.status_code)