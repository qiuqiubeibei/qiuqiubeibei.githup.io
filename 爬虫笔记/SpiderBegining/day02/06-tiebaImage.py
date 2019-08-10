import requests
from lxml import etree


class Spider:
    def __init__(self):
        self.url_name = input("请输入要爬取的贴吧名:")
        self.start_page = int(input("请输入爬取的起始页:"))
        self.end_page = int(input("请输入爬取的终止页:"))
        self.tieba_url = "https://tieba.baidu.com/f?kw=" + self.url_name + "&pn="
        self.user_url = []
        self.image_url = "https://tieba.baidu.com/"  # 存储用户的url地址
        self.index = 0  # 图片数量
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
        }

    # 主要逻辑
    def run(self):
        # 1.获取爬取的url列表
        url_list = self.get_list()
        # 2.对指定贴吧发送请求，获取响应
        for url in url_list:
            # 2.1 将获取的评论url放入列表
            self.user_url.append(self.parse_tieba(url))
            # 2.2 获取贴吧里的图片url地址

        # 3.对指定图片url地址发送请求，获取响应

    # 获取贴吧的url地址
    def get_list(self):
        return [self.tieba_url + str((x - 1) * 50) for x in range(self.start_page, self.end_page)]

    # 对指定贴吧发送请求，获取响应。处理数据，提取图片url地址
    def parse_tieba(self, url):
        response = requests.get(url, headers=self.headers)
        return self.collect_userInfo(response.content.decode())

    # 收集贴吧用户url
    def collect_userInfo(self, data):
        #   清除html文件中的注释符,使能得到完整的信息
        new_data = data.replace("<!--", "")
        new_data = new_data.replace("-->", "")

        # 通过xpath方法，提取html文件中的关键信息
        new_data = etree.HTML(new_data)
        # 得到etreeElementString类型的 列表
        retList = new_data.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
        #   对得到的用户地址进行遍历，对用户发起请求，获取响应
        print("正在爬取中......")
        for ret in retList:
            self.parse_image(ret)

    #  对指定图片地址发送请求，获取响应,提取图片
    def parse_image(self, info):
        temp_url = self.image_url + str(info)
        response = requests.get(temp_url, headers=self.headers)
        self.collect_imageUrl(response.content.decode())

    def collect_imageUrl(self, data):

        # 通过xpath方法，提取html文件中的关键信息
        new_data = etree.HTML(data)
        # 得到etreeElementString类型的 列表
        retList = new_data.xpath('//img[@class="BDE_Image"]/@src')
        #   对得到的用户地址进行遍历，对用户发起请求，获取响应
        for ret in retList:
            print(ret)
            # self.save_image(ret)

    # 对获取的图片进行存储
    def save_image(self, image_url):
        new_image = str(image_url)
        formatIndex = new_image.rfind('.')

        imageNames = "images_" + str(self.index) + new_image[formatIndex:]
        response = requests.get(image_url, headers=self.headers)
        with open("../SpiderImages/" + imageNames, 'wb') as f:
            f.write(response.content)
        self.index += 1


if __name__ == '__main__':
    tiebaSpider = Spider()
    tiebaSpider.run()
