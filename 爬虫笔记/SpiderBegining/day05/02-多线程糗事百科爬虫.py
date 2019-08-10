# 多线程爬取糗事百科

from spiderparse.parse_url import parse_url
from threading import Thread, Lock
from queue import Queue
from lxml import etree
import json
import time
import re

# 初始化数据队列
data_queue = Queue()
# 设置互斥锁
lock = Lock()
# 统计数据队列处理次数
totals = 0
# 数据提取标志位，通知程序是否停止
parse_flag = False


# 1.定义一个爬取页面类,向指定页面发送请求,获取响应
class Spiders(Thread):
    def __init__(self, threadId, queues):
        Thread.__init__(self)
        # 请求头
        self.url = "https://www.qiushibaike.com/8hr/page/"
        self.threadId = threadId
        self.queues = queues

    # 实现主要逻辑
    def run(self):
        print("Starting--->", self.threadId)
        # 对指定网页发送请求，获取响应
        self.fetch_data()
        print("Ending--->", self.threadId)

    def fetch_data(self):
        global data_queue
        # 进入循环，通过判断队列里的值为0作为出口
        while True:
            if self.queues.empty():
                break
            else:
                # 获取page的页码
                pages = self.queues.get()
                # 构造url地址
                urls = self.url + str(pages)
                # 发送请求，获取响应
                htmlStr = parse_url(urls)
                # 如果数据正确返回  将数据保存到队列中
                if htmlStr:
                    data_queue.put(htmlStr)


# 2.定义一个数据处理类，进行数据的提取和存储
class FetchData(Thread):
    def __init__(self, threadIds, queues, locks):
        Thread.__init__(self)
        self.threadIds = threadIds
        self.queues = queues
        self.locks = locks

    # 对数据进行处理主逻辑
    def run(self):
        print("Starting--->", self.threadIds)
        # 对指定网页发送请求，获取响应
        while not parse_flag:
            try:
                items = self.queues.get(False)
                if not items:
                    pass
                self.fetch_data(items)
                '''
                q.task_done()，每次从queue中get一个数据之后，当处理好相关问题，最后调用该方法，以提示q.join()
                是否停止阻塞，让线程向前执行或者退出；
                '''
                # self.queues.task_done()
                # time.sleep(1)
            except:
                pass
        print("Ending--->", self.threadIds)

    def fetch_data(self, data):
        '''
                解析网页函数
        '''
        global totals

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
                data_dict = {"url": "https://www.qiushibaike.com" + userLink,
                             "contents": userData,
                             "name": userName,
                             "agree_nums": agreeTimes,
                             "recmd_times": recmdTimes
                             }
                save_data = json.dumps(data_dict, ensure_ascii=False)
                with open("../SaveData/qiushi.json", 'a', encoding="utf-8") as f:
                    with self.locks:
                        f.write(save_data)
                        f.write("\n")
        except Exception as e:
            print(e)
        with self.locks:
            totals += 1

    def replace_data(self, datas):
        return datas.group(0)


def main():
    global parse_flag
    global data_queue
    # 1.获取指定页面内容
    # 1.1初始化存储页面数据的队列
    page_queue = Queue(50)
    # 1.2爬取指定的1-10个页面
    for pages in range(1, 11):
        page_queue.put(pages)

        # 1.3初始化数据采集线程
    crawl_thread = []
    crawl_list = ['crawl_1', 'crawl_2', 'crawl_3', 'crawl_4']
    for crawl in crawl_list:
        thread = Spiders(crawl, page_queue)
        thread.start()
        crawl_thread.append(thread)

        # 1.4初始化数据提取线程
    parse_thread = []
    parse_list = ['parse_1', 'parse_2', 'parse_3', 'parse_4']
    for parses in parse_list:
        threads = FetchData(parses, data_queue, lock)
        threads.start()
        parse_thread.append(threads)

    # 等待页码队列清空
    while not page_queue.empty():
        pass
    # 等待页码队列子线程结束
    for threads in crawl_thread:
        threads.join()
    print("采集线程已经结束")

    # 等待数据清洗队列清空
    while not data_queue.empty():
        pass
    print("数据队列已经清空")
    # 通知线程可以结束,标志位为true
    parse_flag = True

    # 等待队列子线程结束
    for t in parse_thread:
        t.join()
    print("totals----->", totals)


if __name__ == '__main__':
    main()
    # time.sleep(10)
    # print(data_queue.qsize())
    # print(data_queue.get())
    # 分别会产生许多负面的情绪和想法，但是慢慢的我又回到了初始。
    # 爱情是双方的，当我选择了这份爱情，我便相信爱情,除却一切杂质。
    # 无论与否，只要你相信爱情，它就会带给你幸福。
    # 结局得取决于你自己的对事物的接受能力
