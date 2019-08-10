from bs4 import BeautifulSoup
import requests
from pprint import pprint


class Spider:
    def __init__(self):
        self.headers = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
        }
        self.temp_url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?&postId=1123176879843446784&language=zh-cn"

    def run(self):
        # 1.发送请求，获取响应

        response = requests.get(self.temp_url, headers=self.headers)
        # 2.存储数据
        # with open("tencent.html",'w',encoding="utf-8") as f:
        #     f.write(response.content.decode())
        # 3.清洗数据，保存数据
        self.fetch_data(response.content.decode())

    def fetch_data(self,data):
        print(data)
        soup = BeautifulSoup(data, "lxml")
        dataList = soup.select("div")
        print(dataList)



if __name__ == '__main__':
    tencent = Spider()
    tencent.run()
