import random

from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Event
from nonebot.adapters.onebot.v11.bot import Bot

from ..function import FilePath

##本模块转用于对铁锈群进行聊天内容转发

#确认文件内群号


pvp = on_command(cmd='最高权限-开始群发--阿巴阿巴', priority=50)

@pvp.handle()



async def handle_func(bot: Bot, event: GroupMessageEvent):

    #读取有多少行
    tyt_1 = open(str(FilePath(r'/rustedwarfare/rw/group_id.txt')), encoding='UTF-8')
    tyt_2 = tyt_1.readlines()

    hang = 0
    for x in range(len(tyt_2)):
        hang = hang + 1

    #内置循环
    while hang > 0:#循环32次
        hang = hang - 1


        tyt_1 = open(str(FilePath(r'/rustedwarfare/rw/group_id.txt')), encoding='UTF-8')
        tyt_2 = tyt_1.readlines()
        tyt_1.close()
        s = hang - 1
        group_id = tyt_2[s]

        wot2 = open(str(FilePath(r'/rustedwarfare/help/xuanchaun.txt')), encoding='UTF-8')
        text = wot2.read()
        wot2.close()

        await pvp.send(group_id=int(group_id), message=text, auto_escape=False)



#开始写骰子(
'''

指令格式为，LOVE丢XXX
LOVE回复：你丢出了XXX点

'''
touzi = on_command(cmd='LOVE丢', priority=50)
@touzi.handle()


async def handle_func(bot: Bot, event: Event):
    text = str(event.get_message()).split('丢', 1)

    rnd3 = random.Random()
    x = rnd3.randint(0, int(text[1]))

    try:
        await touzi.send(f'呐呐呐~你丢出了{x}点呢！')
    except:
        await touzi.send("请输入一个正确的点数哦~")