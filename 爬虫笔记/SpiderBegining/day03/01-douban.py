import requests
import json
from pprint import pprint

class Spider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36",
            "Referer": "https://m.douban.com/tv/american"
        }
        self.url = "https://m.douban.com/rexxar/api/v2/subject_collection/tv_american/items?os=android&for_mobile=1&start=0&count=18&loc_id=108288&_=1564540942448"

    def run(self):
        response = requests.get(self.url, headers=self.headers)
        self.deal_data(response)

    def deal_data(self, data):
        ret = json.loads(data.content.decode())
        ret2 = ret["subject_collection_items"][0]["card_subtitle"]
        print(ret2)
        print(type(ret2))

        # pprint(ret)  # 美化输出
        # print(type(ret))
        # with open("../SaveData/json1.json", 'w', encoding="utf-8") as f:
        #     f.write(json.dumps(ret, ensure_ascii=False, indent=4))
        #
        # with open("../SaveData/json1.json", 'r', encoding="utf-8") as r:
        #     ret2 = r.read()
        #     ret3 = json.loads(ret2)
        #     pprint(ret3)
        #     print(type(ret3))



    def get_list(self):
        pass


if __name__ == '__main__':
    spider = Spider()
    spider.run()
