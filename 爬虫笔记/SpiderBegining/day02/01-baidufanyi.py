import requests
import json
import sys


class BaiduTranslate:
    def __init__(self, trans_str):
        # 获取语言类型内容
        self.trans_str = trans_str
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.headers = {"Mozilla/5.0 (Linux; Android 7.1.1; Nexus 6 Build/N6F26U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Mobile Safari/537.36"}

    def parse_url(self, url, data):
        response = requests.post(url, data=data, headers=self.headers)
        return json.load(response.content.decode())

    def get_ret(self, dic_response): # 提取翻译的结果
        ret = dic_response['trans'][0]['dist']
        print("result is :",ret)

    def run(self): # 实现主要的逻辑
        # 1.获取语言类型
            #1.1 先准备post的url地址，post_data
        lang_detect_data = {"query": "你好"}
            #1.2 发送Post请求，获取响应
        # 1.3 提取语言类型
        lang = self.parse_url(self.lang_detect_url, lang_detect_data)["lan"]

        # 2.准备Post数据
        trans_data = {"query": self.trans_str, "from": "zh", "to": "en"} if lang == "zh" else {"query": self.trans_str, "from": "en", "to": "zh"}
        # 3.发送post请求，获取响应
        dict_response = self.parse_url(self.trans_url, trans_data)
        # 4.提取翻译的结果
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_str = sys.argv[1]
    baidu_fanyi = BaiduTranslate(trans_str)
    baidu_fanyi.run()

