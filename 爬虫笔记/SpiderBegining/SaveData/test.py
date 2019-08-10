from lxml import etree

# 读取外部文件 hello.html
with open("tieba.html", "r",encoding="utf-8") as f:
    text = f.read()
print(type(text))
new_text = etree.HTML(text)
print(type(new_text))
result = new_text.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')
print(result)

