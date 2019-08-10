# 使用requests获取页面信息，用XPath / re 做数据提取
# 获取每个帖子里的用户头像链接、用户姓名、段子内容、点赞次数和评论次数
# 保存到 json 文件内
import re
import requests
import json
from lxml import etree


class Spider:
    def __init__(self):
        # 请求头
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

        # 请求地址
        self.temp_url = "https://www.qiushibaike.com/8hr/page/1/"

    def run(self):
        # 发送请求，获取响应
        response = requests.get(self.temp_url, headers=self.headers)
        # 对数据进行提取
        new_data = self.fetch_data(response.content.decode())
        # 对数据进行存储

    def fetch_data(self, data):
        try:
            datas = etree.HTML(data)
            # 对数据进行分列表
            dataList = datas.xpath('//ul/li[contains(@id,"qiushi_tag")]')

            for index, datas in enumerate(dataList):
                # 用户头像链接
                userLink = datas.xpath('//li/div/a/@href')[index]

                # 段子内容
                pattern = re.compile(r'<a class="recmd-content".+>(.+)</a>')
                userData = pattern.findall(data)[index]

                # 段子用户姓名
                userPattern = re.compile(r'<span class="recmd-name">(.+)</span>')
                userName = userPattern.findall(data)[index]

                # 获取点赞次数和评论数
                recmdTimes = datas.xpath('//div[@class="recmd-num"]/span[4]/text()')[0]
                agreeTimes = datas.xpath('//div[@class="recmd-num"]/span[1]/text()')[0]
                # 把数据以字典的形式进行存储
                data_dict = {"url":userLink,
                             "contents":userData,
                             "name":userName,
                             "agree_nums":agreeTimes,
                             "recmd_times":recmdTimes
                             }
                save_data = json.dumps(data_dict, ensure_ascii=False)
                with open("../SaveData/qiushi.json", 'a',encoding="utf-8") as f:
                    f.write(save_data)
                    f.write("\n")
        except Exception as e:
            print(e)



    def replace_data(self, datas):
        return datas.group(0)


if __name__ == '__main__':
    spider = Spider()
    spider.run()
