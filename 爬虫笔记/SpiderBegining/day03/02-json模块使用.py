import json
import chardet
from pprint import pprint

with open("../SaveData/json1.json", 'r', encoding="utf-8") as r:
    ret2 = r.read()
    ret3 = json.loads(ret2)
    pprint(ret3)
    print(type(ret3))
    print(chardet.detect(json.dumps(ret3,ensure_ascii=False)))

# with open("../SaveData/json1.json", 'w', encoding="utf-8") as f:
#     f.write(json.dumps(ret2, ensure_ascii=False, indent=4))
