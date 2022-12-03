import os
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot

class Dialogue:
    x=''
    m=''
    #dialogue_1=''
    def __init__(self,x,m):
        #使用面向对线，创建类，对类中的对象赋值
        self.x = x
        self.m = m
        #self.dialogue_1 =dialogue_1
    def speak(self):
        dialogue_1 = on_fullmatch([self.x], priority=50)
        @dialogue_1.handle() #出错
        async def handle_func(bot: Bot, event: Event):
            await dialogue_1.send(self.m)

miss_1 = Dialogue('测试','测试成功')
miss_1.speak()

miss_2 =Dialogue('测试2','测试2成功')
miss_2.speak()


def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find('love2') + len('love2')]
    return rootPath
FilePath_1 = str(getRootPath())
print(FilePath_1)
def FilePath(FilePath_2):  # 拼接捏
    FilePath_2 = FilePath_1 + FilePath_2
    return FilePath_2
