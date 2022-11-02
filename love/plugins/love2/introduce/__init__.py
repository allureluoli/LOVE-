import json #带师傅
import os
from pathlib import Path #带师傅
from typing import Union #带师傅

import goto
from goto import with_goto
from nonebot import on_fullmatch, on_message, on_command
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, message, event
from nonebot.adapters.onebot.v11.bot import Bot, send

introduce=on_fullmatch(['自我介绍','LOVE酱介绍','@LOVE酱',],priority=50)
@introduce.handle()
async def handle_func(bot: Bot,event :Event):
    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说：【love酱功能】吧！')

function1=on_fullmatch(['love酱功能','LOVE酱功能'],priority=50)
@function1.handle()
async def handle_func(bot: Bot,event :Event):
    await function1.finish('群聊代宣请加群\nLOVE酱的家：827472569\n查询命令：群聊查询、教程查询、单位查询（制作中）、地图查询（制作中）、模组查询（制作中）\n教程命令：LOVE酱铁锈教程\n联系作者：3345483363')


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
        list=['你谈吐良好的样子更好哦','不要一直Q6喔','乖']
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



#废弃的类。效率太低
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


class wcnm:
    i = 0
    FG_2 = []
    Fi_1 = open(FilePath(r'\introduce\cat.ini'),encoding='UTF-8')
    Fi_2 = Fi_1.readlines()

    for i in range(len(Fi_2)):
        try:
            FG_1 = Fi_2[i].split("=")
            FG_2.append(FG_1[0])
            FG_2.append(FG_1[1])
            i = i + 1

        except:
            print("又BUG了喵")
    Fi_1.close()
    zd_1 = {}
    i = 0
    while i<=400:
        try:
            i = i + 2
            zd_1[FG_2[i]]=FG_2[i+1]
        except:
            print("失败了喵~~~")
'''
失败的方法
    def zdcd(self):
        i = 0
        FG_2 = []
        Fi_1 = open(FilePath(r'\introduce\cat.ini'), encoding='UTF-8')
        Fi_2 = Fi_1.readlines()
        Fi_1.close()
        for i in range(len(Fi_2)):
            FG_1 = Fi_2[i].split("=")
            FG_2.append(FG_1[0])
            FG_2.append(FG_1[1])
            i = i + 1
        zd_1 = {}
        i = 0
        while i <= 400:
            try:
                i = i + 2
                zd_1[FG_2[i]] = FG_2[i + 1]
            except:
                print("失败了喵~~~")
'''

dialogue_1 = on_message(priority=100)
@dialogue_1.handle() #出错
async def handle_func(bot: Bot, event: GroupMessageEvent, ):
    wcnm()
    zd_1=wcnm.zd_1
    jsq = zd_1.get(str(event.get_message()))
    try:
        await dialogue_1.send(jsq)
    except:
        print("不行喵")

#格式 LOVE教学-XX=XX
#设置权限
start=on_command(cmd='LOVE教学-',priority=50)
@start.handle()
async def handle_func(bot: Bot,event :Event):
    try:
        teaching=open(FilePath(r'\introduce\cat.ini'),'a+',encoding='UTF-8')
        #分割消息
        text = str(event.get_message()).split('-', 1)

        teaching.write(str('\n'+text[1]))
        teaching.close()
        #import os
        #os.system('exit',r'cd C:\Users\33454\Desktop\LOVE','nb run')
        await start.send('呐呐呐！教学成功~\n(被添加的新回复将在次日审核通过后才可使用哦~)')
    except:
        teaching.close()
        await start.send('教学失败，请检查命令格式')


gy=['玉可碎 却不可改其白,竹可焚 而不可毁其节.身虽死 名可垂于竹帛也 又何惧哉.']
#这种情况的话，是从字典第一个开始的吗？
#解决方法应该是字典留空吧
#先试试先










#async def user_checker(event: Event) -> bool:
#    return type(event.get_user_id()) == int




#wcnmd= on_message(priority=5)
#@wcnmd.handle()




