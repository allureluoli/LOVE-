import os
import random
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_command, on_keyword
from nonebot.rule import to_me
from love.db import JsonDB
from datetime import datetime

"""本模块主要实现LOVE酱的学习功能"""

"""同时实现了飙脏话功能和持续性聊天功能"""

study = on_command(cmd='教学-', rule=to_me(), priority=20)


@study.handle()
async def handle_func(bot: Bot, event: Event):

    try:
        QQ = event.get_session_id().split('_')[2]  # 获取QQ号
        message = str(event.get_message()).split('-')[1].split('=')  # 事件消息内容
        send = message[0]
        Reply = message[1]

        Save = JsonDB(QQ=QQ, send=send, Reply=Reply)
        Save.Save()

        await study.send('教学成功！(请等待主人审核哦~)')

    except:
        await study.finish("教学失败，请注意教学格式哦！")


study2 = on_command(cmd='我说', rule=to_me(), priority=20)


@study2.handle()
async def handle_func(bot: Bot, event: Event):
    try:
        QQ = event.get_session_id().split('_')[2]  # 获取QQ号
        message = str(event.get_message()).split('我说')[1].split('你就说')  # 事件消息内容
        send = message[0]
        Reply = message[1]

        Save = JsonDB(QQ=QQ, send=send, Reply=Reply)
        Save.Save()

        await study2.send('教学成功！(请等待主人审核哦~)')
    except:
        await study2.finish("教学失败，请注意教学格式哦！")

Chat = on_command(cmd='和我聊天', rule=to_me(), priority=20)

@Chat.handle()
async def handle_func(bot: Bot,event: Event):
    QQ = event.get_session_id().split('_')[2]
    # 生成一个QQ名文件

    ChatMe = JsonDB(QQ=QQ,send='',Reply='start')
    ChatMe.ChatOS()


    #套娃）））
    await Chat.send("聊天开始~！")
    #如此，便生成一个事件响应器


ChatWW = on_command(cmd='', priority=60)


@ChatWW.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    FindQQ = JsonDB(QQ=QQ, Reply='find', send='')

    if QQ == FindQQ.ChatOS():

        message = event.get_message()

        Load = JsonDB(QQ=QQ, Reply='', send=message)

        if str(message) == '不聊了':
            ChatEnd = JsonDB(QQ=QQ, Reply='end', send='')
            ChatEnd.ChatOS()

            await ChatWW.finish("聊天结束，欢迎下次也来找LOVE玩哦~")


        if len(str(event.get_message())) >= 1:

            try:
                nowtime = datetime.now()
                cdtime = Load.idioctoniaTime()

                duration = nowtime - cdtime
                # 现在时间-cd时间

                interval = duration.seconds

                # 记仇功能

                if str(event.get_message()) == '紫砂' and Load.idioctoniaTime() == 0:
                    # 如果是紫砂就这么来一套
                    await ChatWW.send(Load.idioctonia())
                    # 但是也要检测一下时间
                elif interval >= 600:
                    # 这里开始判断时间
                    # 获取紫砂时间与现在时间的差值
                    if '紫砂' in str(event.get_message()):
                        # 如果是紫砂就这么来一套
                        await ChatWW.send(Load.idioctonia())
                    else:
                        await ChatWW.send(Load.Load())

                else:
                    # 装死
                    await ChatWW.send('')
            except:
                if '紫砂' in str(event.get_message()):
                    # 如果是紫砂就这么来一套
                    await ChatWW.send(Load.idioctonia())
                else:
                    await ChatWW.send(Load.Load())

        else:
            message = ["你好，这里是LOVE酱，发送 帮助 可以查看我的功能哦！",
                       "你好呀，我是LOVE酱，一个专为铁锈战争服务的虚拟少女！",
                       "你好~有什么需要帮助的吗？"]
            rnd = random.Random()
            Num = rnd.randint(0, 2)

            await ChatWW.send(message[Num])

    else:
        await ChatWW.finish('')





attack = on_keyword({'泥马','傻逼','操你妈','你妈','脑瘫','煞笔', '纱布', '草泥马', '傻必', '傻碧', '傻臂', '傻弊', '沙比', '傻笔', '傻鸟'}, to_me())

@attack.handle()
async def handle_func(bot: Bot, event: Event):


    TextList = ['超你麻麻', '你麻麻似了', '我超你麻麻', '你是不是吃屎了阿嘴怎么这么臭',
                '你是刚从花粉迟里出来嘛怎么这么恶心', '你怎么跟依托市一样恶心', '别恶心我好嘛', '滚滚滚', '超你嘛',
                '你个钩砸中快滚', '煞笔', '好煞笔快滚', '你怎么不说话了是在给你麻麻哭坟吗', '哪来的dinner',
                '别在这里发电快滚', '好弱治', '你麻麻霹雳有两条四幅麻将']

    rnd3 = random.Random()
    x = rnd3.randint(0, len(TextList) - 1)

    QQ = event.get_session_id().split('_')[2]
    message = event.get_message()

    Load = JsonDB(QQ=QQ, Reply='', send=message)


    try:
        nowtime = datetime.now()
        cdtime = Load.idioctoniaTime()

        duration = nowtime - cdtime
        # 现在时间-cd时间

        interval = duration.seconds
        Load.idioctonia()
        if interval >= 600:

            await attack.send(TextList[x] + '\n（检测到侮辱性词汇，将对你关闭十分钟聊天系统）')
        else:

            await attack.send('')
    except:
        Load.idioctonia()
        await attack.send(TextList[x] + '\n（检测到侮辱性词汇，将对你关闭十分钟聊天系统）')


"""实现被艾特时回话功能"""
Reply = on_command(cmd='', rule=to_me(), priority=60)


@Reply.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    message = event.get_message()

    Load = JsonDB(QQ=QQ, Reply='', send=message)

    if len(str(event.get_message())) >= 1:

        try:
            nowtime = datetime.now()
            cdtime = Load.idioctoniaTime()

            duration = nowtime - cdtime
            # 现在时间-cd时间

            interval = duration.seconds

            # 记仇功能

            if str(event.get_message()) == '紫砂' and Load.idioctoniaTime() == 0:
                # 如果是紫砂就这么来一套
                await Reply.send(Load.idioctonia())
                # 但是也要检测一下时间
            elif interval >= 600:
                # 这里开始判断时间
                # 获取紫砂时间与现在时间的差值
                if '紫砂' in str(event.get_message()):
                    # 如果是紫砂就这么来一套
                    await Reply.send(Load.idioctonia())
                else:
                    await Reply.send(Load.Load())

            else:
                # 装死
                await Reply.send('')
        except:
            if '紫砂' in str(event.get_message()):
                # 如果是紫砂就这么来一套
                await Reply.send(Load.idioctonia())
            else:
                await Reply.send(Load.Load())


    else:
        message = ["你好，这里是LOVE酱，发送 帮助 可以查看我的功能哦！",
                   "你好呀，我是LOVE酱，一个专为铁锈战争服务的虚拟少女！",
                   "你好~有什么需要帮助的吗？",
                   "LOVE酱的开源代码仓：https://github.com/allureluoli/LOVE- ,如果你喜欢LOVE，就请给一个STAR吧！"]
        rnd = random.Random()
        Num = rnd.randint(0, 3)

        await Reply.send(message[Num])


# 让人可以撤回自己还没有过审的词汇
recall = on_command(cmd='撤回-', rule=to_me(), priority=20)


@recall.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]  # 获取QQ号
    message = str(event.get_message()).split('-')[1]  # 事件消息内容
    send = message

    REC = JsonDB(QQ=QQ, send=send, Reply='')

    await recall.send(REC.recall())


"""审核功能"""

Examine = on_command(cmd='查看待审核词汇', priority=20)


@Examine.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]

    if int(QQ) != 3345483363:

        await Examine.send("你不是LOVE的主人哦~")

    else:

        curPath = os.path.abspath(os.path.pardir) + "/LOVE/love/data/Examine/"
        listFiles = os.listdir(curPath)  # 获取文件目录
        message = ''
        QQ = ''

        for i in range(0, len(listFiles)):
            Load = JsonDB(QQ=QQ, Reply='', send=listFiles[i])
            Text = listFiles[i].split('.')[0] + ':' + Load.ExamineLoad()
            message += Text + '|'

        await Examine.send(f"待审核的词汇如下：{message}")


OverExamination = on_command(cmd='过审-', priority=20)


@OverExamination.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]

    if int(QQ) != 3345483363:

        await OverExamination.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]  # 获取需要过审的词汇
        MOVE = JsonDB(QQ='', send=message + '.json', Reply='')
        MOVE.MOVE()
        await OverExamination.send('过审成功')


RefuseExamination = on_command(cmd='拒绝过审-', priority=20)


@RefuseExamination.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]

    if int(QQ) != 3345483363:

        await RefuseExamination.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]
        Refus = JsonDB(QQ='', send=message + '.json', Reply='')
        Refus.refuse()

        await RefuseExamination.send("已成功删除内容")
