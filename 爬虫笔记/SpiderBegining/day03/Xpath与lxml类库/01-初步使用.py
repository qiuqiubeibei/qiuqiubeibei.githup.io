# coding:utf-8
# 使用lxml里的etree库
from lxml import etree

text = '''
<div>
    <ul>
         <li class="item-0"><a href="link1.html">first item</a></li>
         <li class="item-1"><a href="link2.html">second item</a></li>
         <li class="item-inactive"><a href="link3.html">third item</a></li>
         <li class="item-1"><a href="link4.html">fourth 你好</a></li>
         <li class="item-0"><a href="link5.html">fifth item</a> 
     </ul>
 </div>
'''
# 利用etree.HTML 将字符串转化为html文档
text_html = etree.HTML(text)

# 按字符串序列化html文档,如果中文乱码的话，我们可以使用encoding进行编码设置为utf-8
result = etree.tostring(text_html, encoding="utf-8")

#因为这里result得到的类型是bytes，我们需要用utf-8进行解码
print(result.decode("utf-8"))