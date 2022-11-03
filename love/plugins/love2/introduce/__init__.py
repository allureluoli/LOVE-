from importlib import reload

from nonebot.rule import to_me

import function
from function import FilePath
from nonebot import on_fullmatch, on_message, on_command
from nonebot.adapters.onebot.v11 import Event, GroupMessageEvent, event
from nonebot.adapters.onebot.v11.bot import Bot

reload(function)#重新载入模块

introduce_2 = on_fullmatch([''], rule=to_me(),priority=50)
@introduce_2.handle()
async def handle_func(bot: Bot, event: Event):


    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说： love酱功能 吧！')

introduce = on_fullmatch(['自我介绍', 'LOVE酱介绍', '@LOVE酱','maa'], priority=50)

@introduce.handle()
async def handle_func(bot: Bot, event: Event):


    await introduce.finish('呐呐~我是love酱哒，一个为铁锈战争群聊提供服务的虚拟少女~试试对我说： love酱功能 吧！')

function1 = on_fullmatch(['love酱功能', 'LOVE酱功能'], priority=50)

@function1.handle()
async def handle_func(bot: Bot, event: Event):
    await function1.finish(
        '群聊代宣请加群\nLOVE酱的家：827472569\n查询命令：群聊查询、教程查询、单位查询（制作中）、地图查询（制作中）、模组查询（制作中）\n教程命令：LOVE酱铁锈教程\n联系作者：3345483363')


# 挖坑，制作专属回复
LOVE = on_fullmatch(['LOVE', 'love', '爱', 'LOVE酱', 'love酱', '小宝贝'], priority=50)


@LOVE.handle()
async def handle_func(bot: Bot, event: Event):
    await LOVE.finish('呐呐呐？是在叫我嘛~')


six = on_fullmatch(['6'], priority=50)


@six.handle()
async def handle_func(bot: Bot, event: Event):
    h = 3
    while h > 0:
        h = h - 1
        list = ['你谈吐良好的样子更好哦', '不要一直Q6喔', '乖']
        await six.send(list[h])

pao = on_fullmatch(['。'], priority=50)

@pao.handle()
async def handle_func(bot: Bot, event: Event):
    await pao.send("一个泡泡")


sb = on_fullmatch(['?', '？'], priority=50)


@sb.handle()
async def handle_func(bot: Bot, event: Event):
    await sb.send("你想表达什么？")


wife = on_fullmatch(['碳酸'], priority=50)


@wife.handle()
async def handle_func(bot: Bot, event: Event):
    await wife.send("可爱爱♥")


wife2 = on_fullmatch(['碳酸是'], priority=50)


@wife2.handle()
async def handle_func(bot: Bot, event: Event):
    await wife2.send("二月的")


wife3 = on_fullmatch(['二月是'], priority=50)


@wife3.handle()
async def handle_func(bot: Bot, event: Event):
    await wife3.send("碳酸的")

class wcnm:
    i = 0
    FG_2 = []
    Fi_1 = open(FilePath(r'\introduce\cat.ini'), encoding='UTF-8')
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
    while i <= 400:
        try:
            i = i + 2
            zd_1[FG_2[i]] = FG_2[i + 1]
        except:
            print("失败了喵~~~")


start = on_command(cmd='LOVE教学-', priority=20)


@start.handle()
async def handle_func(bot: Bot, event: Event):
    try:
        teaching = open(FilePath(r'\introduce\cat.ini'), 'a+', encoding='UTF-8')
        # 分割消息
        text = str(event.get_message()).split('-', 1)
        teaching.write(str('\n' + text[1]))
        teaching.close()
        # import os
        # os.system('exit',r'cd C:\Users\33454\Desktop\LOVE','nb run')
        await start.send('呐呐呐！教学成功~\n(被添加的新回复将在次日审核通过后才可使用哦~)')
    except:
        teaching.close()
        await start.send('教学失败，请检查命令格式')


dialogue_1 = on_message(priority=100)


@dialogue_1.handle()
async def handle_func(bot: Bot, event: GroupMessageEvent, ):
    wcnm()
    zd_1 = wcnm.zd_1
    jsq = zd_1.get(str(event.get_message()))
    try:
        await dialogue_1.send(jsq)

    except:
        print("不行喵")
