import glob
import os
import random
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_command
from nonebot.rule import to_me

from love.db import JsonDB

"""本模块主要实现LOVE酱的学习功能"""


study = on_command(cmd='教学-',rule=to_me(),priority=20)


@study.handle()
async def handle_func(bot: Bot, event: Event ):
    QQ=event.get_session_id().split('_')[2]     #获取QQ号
    message=str(event.get_message()).split('-')[1].split('=')   #事件消息内容
    send = message[0]
    Reply = message[1]

    Save=JsonDB(QQ=QQ,send=send,Reply=Reply)
    Save.Save()

    await study.send('教学成功！(请等待主人审核哦~)')

"""实现被艾特时回话功能"""
Reply = on_command(cmd='',rule=to_me(),priority=60)


@Reply.handle()
async def handle_func(bot: Bot, event: Event ):



    if len(str(event.get_message())) > 1:

        Load = JsonDB(QQ='', Reply='', send=event.get_message())

        await Reply.send(Load.Load())

    else:
        message = ["你好，这里是LOVE酱，发送 帮助 可以查看我的功能哦！",
                   "你好呀，我是LOVE酱，一个专为铁锈战争服务的虚拟少女！",
                   "你好~有什么需要帮助的吗？"]
        rnd = random.Random()
        Num = rnd.randint(0, 2)

        await  Reply.send(message[Num])

"""审核功能"""

Examine  = on_command(cmd='查看待审核词汇',priority=20)

@Examine.handle()
async def handle_func(bot: Bot, event: Event ):
    QQ=event.get_session_id().split('_')[2]

    if int(QQ) !=3345483363:

        await Examine.send("你不是LOVE的主人哦~")

    else:

        curPath = os.path.abspath(os.path.pardir) + "/LOVE/love/data/Examine/"
        listFiles = os.listdir(curPath)  # 获取文件目录
        message=''
        QQ=''

        for i in  range(0,len(listFiles)):
            Load=JsonDB(QQ=QQ,Reply='',send=listFiles[i])
            Text=listFiles[i].split('.')[0]+':'+Load.ExamineLoad()
            message += Text+'|'

        await Examine.send(f"待审核的词汇如下：{message}")


OverExamination = on_command(cmd='过审-',priority=20)

@OverExamination.handle()
async def handle_func(bot: Bot, event: Event ):
    QQ=event.get_session_id().split('_')[2]

    if int(QQ) !=3345483363:

        await OverExamination.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]#获取需要过审的词汇
        MOVE=JsonDB(QQ='',send=message+'.json',Reply='')
        MOVE.MOVE()
        await OverExamination.send('过审成功')

RefuseExamination = on_command(cmd='拒绝过审-',priority=20)

@RefuseExamination.handle()
async def handle_func(bot: Bot, event: Event ):
    QQ=event.get_session_id().split('_')[2]

    if int(QQ) !=3345483363:

        await RefuseExamination.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]
        Refus = JsonDB(QQ='', send=message + '.json', Reply='')
        Refus.refuse()

        await RefuseExamination.send("已成功删除内容")
