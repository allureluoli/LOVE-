import os

b = os.listdir('.')

print(b)

for i in b:
    if '.txt' in i:
        with open(i, encoding='utf-8') as f:
            a = f.read()
            a = a.replace('视野：\n', '视野：')
        with open(i, encoding='utf-8', mode='w') as f:
            f.write(a)
            print('重写了' + i)
