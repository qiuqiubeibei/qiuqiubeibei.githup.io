import urllib.request#向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）

def main():

    response = urllib.request.urlopen("http://www.baidu.com")

    #读取文件的全部内容，方法1
    # data = response.read()
    # print(data)

    #读取文件的全部内容，方法2
    # data = response.readline()

    #方式3，每行按列表返回
    # data = response.readlines()
    # print(data)
    #response属性
    #返回当前有关的环境信息
    print(response.info())

    #返回状态码
    print(response.getcode())
    if response.getcode() == 200 or response.getcode() ==304:
        #处理网页信息
        print('处理网页信息')
    #将爬取下来的数据存储到文件中
    # f = open(r"D:\Python_Work\tools\file1.html", "wb")
    #
    # f.write(data)
    #
    # f.close()


if __name__ == "__main__":
    main()