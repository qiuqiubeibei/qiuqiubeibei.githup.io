import requests
import re


class NeihanSpider:

    def __init__(self, get_url):
        self.get_url = get_url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    # 获取相关的url列表
    def geturl_list(self):
        return [self.get_url + str(x) + ".html" for x in range(1, 5)]

    # 发送请求，获取响应
    def parse_url(self, url):
        response = requests.get(url, headers=self.headers)
        return response.content.decode('gbk')

    # 对获取的数据进行处理和清洗
    def deal_data(self, data, index):
        temp_data = data
        pattern_all = re.compile(r'<div.*?class="f18 mb20">(.*?)</div>', re.S)
        ret = pattern_all.findall(temp_data)

        pattern_list = re.compile(r'[a-zA-Z&/<>; ]*')
        for x in ret:
            new_info = pattern_list.sub('', x)
            self.save_data(new_info, index)
            # print(new_info)
        filePath = '../SaveData/neihan' + str(index) + '.txt'
        return filePath

    # 存储处理后的信息
    def save_data(self, data, index):
        filePath = '../SaveData/neihan' + str(index) + '.txt'
        with open(filePath, 'a', encoding='utf-8') as f:
            f.write(data)

    # 实现主要步骤
    def run(self):
        # 1.1准备url地址
        url_list = self.geturl_list()

        for url in url_list:
            # 1.2发送请求，获取响应
            # 1.3 获取数据
            # 1.4处理数据
            # 1.5存储数据
            url_index = url_list.index(url)
            dealInfo = self.deal_data(self.parse_url(url), url_index+1)
            # saveData = self.save_data(self.parse_url(url), url_index)
            print(dealInfo)



if __name__ == '__main__':
    get_url = "https://www.neihan8.com/article/list_5_"
    neihanspider = NeihanSpider(get_url)
    neihanspider.run()
