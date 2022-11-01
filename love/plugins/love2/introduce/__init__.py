import json #带师傅
import os
from pathlib import Path #带师傅
from typing import Union #带师傅
from nonebot import on_fullmatch, on_message
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, message, event
from nonebot.adapters.onebot.v11.bot import Bot, send

introduce=on_fullmatch(['自我介绍','LOVE酱介绍'],priority=50)
@introduce.handle()
async def handle_func(bot: Bot,event :Event):
    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说：【love酱功能】吧！')

function1=on_fullmatch(['love酱功能','LOVE酱功能'],priority=50)
@function1.handle()
async def handle_func(bot: Bot,event :Event):
    await function1.finish('群聊代宣请加群\nLOVE酱的家：827472569\n查询命令：群聊查询、教程查询、单位查询（制作中）、地图查询（制作中）、模组查询（制作中）\n教程命令：LOVE酱铁锈教程\n联系作者：3345483363')

start=on_fullmatch(['开启聊天系统'],priority=50)
@start.handle()
async def handle_func(bot: Bot,event :Event):
    start_1 = 1
#挖坑，制作专属回复
LOVE=on_fullmatch(['LOVE','love','爱','LOVE酱','love酱','小宝贝'],priority=50)
@LOVE.handle()
async def handle_func(bot: Bot,event :Event):
    await LOVE.finish('呐呐呐？是在叫我嘛~')

six=on_fullmatch(['6'],priority=50)
@six.handle()
async def handle_func(bot: Bot,event :Event):
    h=3
    while h>0:
        h=h-1
        list=['乖','不要一直Q6喔','你谈吐良好的样子更好哦']
        await six.send(list[h])


pao=on_fullmatch(['。'],priority=50)
@pao.handle()
async def handle_func(bot: Bot,event :Event):
  await pao.send("一个泡泡")

sb=on_fullmatch(['?','？'],priority=50)
@sb.handle()
async def handle_func(bot: Bot,event :Event):
  await sb.send("你想表达什么？")

wife=on_fullmatch(['碳酸'],priority=50)
@wife.handle()
async def handle_func(bot: Bot,event :Event):
  await wife.send("可爱爱♥")

wife2=on_fullmatch(['碳酸是'],priority=50)
@wife2.handle()
async def handle_func(bot: Bot,event :Event):
  await wife2.send("二月的")

wife3=on_fullmatch(['二月是'],priority=50)
@wife3.handle()
async def handle_func(bot: Bot,event :Event):
  await wife3.send("碳酸的")


class Dialogue:
    x=''
    m=''
    #dialogue_1=''
    def __init__(self,x,m):
        self.x = x
        self.m = m
        #self.dialogue_1 =dialogue_1
    def speak(self):
        dialogue_1 = on_fullmatch([self.x], priority=50)
        @dialogue_1.handle() #出错
        async def handle_func(bot: Bot, event: Event):
            await dialogue_1.send(self.m)




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

i = 0
FG_2 = []
Fi_1 = open(FilePath(r'\introduce\cat.ini'))
Fi_2 = Fi_1.readlines()
for i in range(len(Fi_2)):
    FG_1 = Fi_2[i].split("=")
    FG_2.append(FG_1[0])
    FG_2.append(FG_1[1])
    i = i + 1

zd_1 = {}
i = 0
while i<=175:
    i = i + 2
    zd_1[FG_2[i]]=FG_2[i+1]


dialogue_1 = on_message(priority=20)
@dialogue_1.handle() #出错
async def handle_func(bot: Bot, event: GroupMessageEvent):
    jsq = zd_1.get(str(event.get_message()))
    try:
        await dialogue_1.send(jsq)
    except:
        print("不行喵")






#这种情况的话，是从字典第一个开始的吗？
#解决方法应该是字典留空吧
#先试试先






class Simplify:#简易
    e_1=''  #接收词--等于机器人收到的纯文本消息
    q=''   #发出词
    def __init__(self,e_1):#规定形式参数
        self.e_1 = e_1
        dict_2={}
        self.q = dict_2.get(self.e_1)
        print(e_1)
        #返回字典指定的键
    def speak(self):
        #他是怎么遍历确认相关的呢
        #答案是get
        #收到的消息拿去确认是否有字典！
        #q确认有则事件响应机器触发，返回字典的键
        str_1=self.e_1

        #如何实现不通过事件响应器直接回消息呢
        send(self.q)



#async def user_checker(event: Event) -> bool:
#    return type(event.get_user_id()) == int




#wcnmd= on_message(priority=5)
#@wcnmd.handle()




