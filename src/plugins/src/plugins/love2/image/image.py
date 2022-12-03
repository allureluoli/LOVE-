import os

def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find('love2') + len('love2')]
    return rootPath

FilePath_1=str(getRootPath())

print(FilePath_1)
def FilePath(FilePath_2):#拼接捏
    FilePath_2=FilePath_1+FilePath_2
    return FilePath_2