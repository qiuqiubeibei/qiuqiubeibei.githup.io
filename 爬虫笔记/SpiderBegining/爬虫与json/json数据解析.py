'''

概念：一种保存数据的格式
作用：可以保存本地的json文件，页可以将json串进行传输，
通常将json称为轻量级的传输方式

xml
json文件组成
{} 代表对象（字典）
[] 代表列表
: 代表键值对
， 代表分割两个部分

'''
import json
jsonStr = '{"name":"qihao", "age":18, "hobby":["money","power","english"], \
        "parames":{"a":1,"b":2} }'
#将json格式的字符串转为pyhton数据类型的对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["name"])

#将python数据类型的对象转换为json格式的字符串
jsonData2 = {"name": "qihao", "age": 18, "hobby": ["money", "power", "english"], \
             "parames": {"a": 1, "b": 2}
             }
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)
print(type(jsonStr2))

#读取本地的Json文件
path = r"本地json文件路径"

f = open(path, "rb")
data = json.load(f)
print(data)
#字典类型
print(type(data))
f.close()

#写本地的json文件
path2 = r"本地json文件路径"
jsonData3 = {"name": "qihao", "age": 18, "hobby": ["money", "power", "english"], \
             "parames": {"a": 1, "b": 2}
             }
fw = open(path2,"w")

json.dump(jsonData3,fw)

fw.close()