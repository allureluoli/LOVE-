from function import FilePath

wot2 = open(str(FilePath(r'/rustedwarfare/help/mod_course.txt')), encoding='UTF-8')
text = wot2.read()

print(text)