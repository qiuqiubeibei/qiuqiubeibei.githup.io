import requests

# 准备请求头
headers = { "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
            "Cookie": "JSESSIONID=DD6AAA57753F6EC899B5BC4517E287DD",
            "Referer": "http://ks.1000phone.net/examController/examineeExamList?userId=134836"
            }

# 准备data
post_data = {
    "Account": "510922199709033255",
    "PassWord": "a1124081670"
}

# 准备url地址
post_url = "http://ks.1000phone.net/examController/viewExamResult?id=74686"

response = requests.get(post_url, headers=headers)

print(response.content.decode())
# print(response.status_code)