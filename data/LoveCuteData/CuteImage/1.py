import os

print(os.getcwd())

a = os.listdir()
s = ''
for i in a:
    if 'gif' not in i:
        s += "'"+i.replace('.jpg', '') + "'" +','
        print(s)
