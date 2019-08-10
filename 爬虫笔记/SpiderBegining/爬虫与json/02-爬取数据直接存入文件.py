import urllib.request

url = "https://wenku.baidu.com/view/a74ae76c02d8ce2f0066f5335a8102d277a26160.html"
urllib.request.urlretrieve(url, filename=r"D:\Python_Work\tools\file1.html")

#urlretrieve在执行爬虫过程中，会产生一些缓存

#清除一些缓存
urllib.request.urlcleanup()

