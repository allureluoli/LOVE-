import json
with open('new-data.json',encoding='utf-8') as f:
    a = json.load(f)

    a['娱乐词汇']['测试'] = '测试呢'

with open('new-data.json',encoding='utf-8',mode='w') as f:
    json.dump(a,f)