import requests

headers = {"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"
}

data = {
    "query": "人生苦短，我用Python",
    "from": "zh",
    "to": "en",
    # "token": "2e933a125b2287317147b42b7dfdef73",
    # "sign": "46544.284385",
}

post_url = "https://fanyi.baidu.com/basetrans"

r = requests.post(post_url, data=data, headers=headers)
print(r.content.decode())