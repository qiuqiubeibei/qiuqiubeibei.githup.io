# -*- coding: utf-8 -*-
import requests

class TiebaSpider:
    def __init__(self, tieba_name):
        self.name = tieba_name
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"=utf-8&pn="
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    def get_list(self): #1获取网页的翻页值及url
        # page_list = []
        #         # for x in range(1000):
        #         #     page_list.append(self.url_temp+str(x*50)) #按照贴吧翻页pn值进行计算
        #         # return page_list
        return [self.url_temp+str(i*50) for i in range(1000)]

    def parse_url(self, url): #2、发送请求，获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode("gbk")

    def save_data(self, data, page_index): #3对网页内容进行存储
        file_path = 'SaveData/{}吧-第{}页.html'.format(self.name, page_index)
        with open(file_path, 'w', encoding="utf-8") as p: #存储文件名为“李毅吧-第2页”
            p.write(data)
        return file_path

    def run(self): #实现主要的逻辑
        url_list = self.get_list()
        for url in url_list: #对pn值进行遍历，发送请求，获取响应
            html_str = self.parse_url(url)
            page_index = url_list.index(url)
            #对数据进行存储
            save_info = self.save_data(html_str, page_index)
            print(save_info)


if __name__ == '__main__':
    tieba_spider = TiebaSpider("lol")
    tieba_spider.run()
