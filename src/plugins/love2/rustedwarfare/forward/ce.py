from function import FilePath


tyt_1 = open(str(FilePath(r'/rustedwarfare/rw/group_id.txt')), encoding='UTF-8')
tyt_2 = tyt_1.readlines()

hang = 0
for x in range(len(tyt_2)):
    hang = hang + 1

while hang > 0:  # 循环32次
    hang = hang - 1

    tyt_1 = open(str(FilePath(r'/rustedwarfare/rw/group_id.txt')), encoding='UTF-8')
    tyt_2 = tyt_1.readlines()
    tyt_1.close()
    s = hang - 1
    group_id = tyt_2[s]
    print(group_id)