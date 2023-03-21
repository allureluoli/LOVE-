import threading
from datetime import datetime
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_command

from love.db import JsonDB, Clean, Number
from love.plugins.RWCheck.Reptile import CheckRW, home_list

"""md 今天真是失了智了 居然忘了 on_command_start 感谢Nonebot群友的提醒 才没让我彻底裂开"""
""" 单位查询和房间列表 """

query = on_command(cmd='查询单位-', aliases={"查询-"}, priority=20)


@query.handle()
async def handle_func(bot: Bot, event: Event):
    text = str(event.get_message()).split('-', 1)
    try:
        a = CheckRW(text[1])

        await query.send(a.wiki())

    except:
        print("不行喵")


introduce = on_command("获取房间列表")


@introduce.handle()
async def handle_func(bot: Bot, event: Event):
    game_list = ""

    await introduce.finish(home_list(game_list))


TeamGroup = on_command("添加战队群-")


@TeamGroup.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]

    master = JsonDB(QQ='', send='', Reply='')

    if int(QQ) != master.Config():

        await TeamGroup.send("你不是LOVE酱的主人哦~")
        # await TeamGroup.send(master.Load())
    else:
        message = str(event.get_message()).split('-')[1].split('=')  # 事件消息内容
        send = message

        Save = JsonDB(QQ=QQ, send=send, Reply='')
        Save.TeamGroup()

        await TeamGroup.send("添加成功！")


CheckTeamGroup = on_command("战队群查询")


@CheckTeamGroup.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='', Reply='')

    await CheckTeamGroup.send(message.TeamCheck())


MODGroup = on_command("添加模组群-")


@MODGroup.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    master = JsonDB(QQ='', send='', Reply='')

    if int(QQ) != master.Config():

        await MODGroup.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]  # 事件消息内容
        send = message
        Save = JsonDB(QQ=QQ, send=send, Reply='')
        Save.MODGroup()

        await MODGroup.send("添加成功！")


CheckMODCheck = on_command("模组群查询")


@CheckMODCheck.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='', Reply='')

    await CheckMODCheck.send(message.MODCheck())


TechnologyGroup = on_command("添加技术群-")


@TechnologyGroup.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    master = JsonDB(QQ='', send='', Reply='')

    if int(QQ) != master.Config():

        await TechnologyGroup.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]  # 事件消息内容
        send = message

        Save = JsonDB(QQ=QQ, send=send, Reply='')
        Save.TechnologyGrop()

        await TechnologyGroup.send("添加成功！")


TechnologyCheck = on_command("技术群查询")


@TechnologyCheck.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='', Reply='')

    await TechnologyCheck.send(message.TechnologyCheck())


ArderGruop = on_command("添加闲聊群-")


@ArderGruop.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    master = JsonDB(QQ='', send='', Reply='')

    if int(QQ) != master.Config():

        await ArderGruop.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]  # 事件消息内容
        send = message

        Save = JsonDB(QQ=QQ, send=send, Reply='')
        Save.ArderGruop()

        await ArderGruop.send("添加成功！")


ArderCheck = on_command("闲聊群查询")


@ArderCheck.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='', Reply='')

    await TechnologyCheck.send(message.ArderCheck())


MatchGrop = on_command("添加赛事群-")


@MatchGrop.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    master = JsonDB(QQ='', send='', Reply='')

    if int(QQ) != master.Config():

        await MatchGrop.send("你不是LOVE的主人哦~")

    else:
        message = str(event.get_message()).split('-')[1]  # 事件消息内容
        send = message

        Save = JsonDB(QQ=QQ, send=send, Reply='')
        Save.MatchGrop()

        await MatchGrop.send("添加成功！")


MatchCheck = on_command("赛事群查询")


@MatchCheck.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='', Reply='')

    await TechnologyCheck.send(message.MatchCheck())


MapCourse = on_command("地图导入教程")


@MapCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='Map', Reply='')

    await MapCourse.send(message.Course())


ReplayCourse = on_command("回放导入教程")


@ReplayCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='Replay', Reply='')

    await ReplayCourse.send(message.Course())


MODCourse = on_command("模组导入教程")


@MODCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='MOD', Reply='')

    await MODCourse.send(message.Course())


MODCourse = on_command("房间指令教程")


@MODCourse.handle()
async def handle_func(bot: Bot, event: Event):
    message = JsonDB(QQ='', send='Server', Reply='MOD')

    await MODCourse.send(message.Course())


Advertisement = on_command(("查看告示栏"), aliases={('有人吗', '有人吗？'), '有房吗', ('有房吗？', '有人吗?', "有房吗?")})


@Advertisement.handle()
async def handle_func(bot: Bot, event: Event):
    masssage = JsonDB(QQ='', send='', Reply='')

    await Advertisement.send(masssage.CheckAdvertisement())


Advertisement = on_command("查看告示栏2")


@Advertisement.handle()
async def handle_func(bot: Bot, event: Event):
    masssage = JsonDB(QQ='', send='Two', Reply='')

    await Advertisement.send(masssage.CheckAdvertisement())


UpdateAdvertisement = on_command("提交告示-")


@UpdateAdvertisement.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]
    message = str(event.get_message()).split('-')[1]  # 事件消息内容

    if len(message) > 30:
        await UpdateAdvertisement.finish('请不要提交过长的消息哦！')

    if QQ == "黑名单用户":

        await UpdateAdvertisement.finish("你已被拉黑。")
    else:

        send = message
        TMD = JsonDB(QQ=QQ, send=send, Reply='')

        nowtime = datetime.now()

        if TMD.AdvertisementTime() != 0:
            cdtime = TMD.AdvertisementTime()
            duration = nowtime - cdtime
            # 现在时间-过去时间=过去了多少秒
            interval = duration.seconds
        else:
            interval = 180
            # 若过去了180s则允许
        if interval >= 180:
            wfole = Clean(i=Number)
            # 创建新线程
            thread = threading.Thread(target=wfole.Clean)
            # 设置为后台运行，程序不会阻塞
            thread.daemon = True
            # 启动线程
            thread.start()

            await UpdateAdvertisement.send(TMD.Advertisement())
        else:

            await UpdateAdvertisement.send(f"你在{180 - interval}s后才可再次提交哦~")


delete = on_command("清空告示栏")


@delete.handle()
async def handle_func(bot: Bot, event: Event):
    QQ = event.get_session_id().split('_')[2]

    if int(QQ) == 3345483363 or int(QQ) == 2060598058:

        a = Clean(i='')

        a.Cleanall()

        await delete.send("成功！")

    else:

        await delete.send(f"QQ为：{QQ}的用户没有权限！")


'''暂未解决程序堵塞问题'''
'''暂时不使用告示栏2'''
# UpdateAdvertisementTWO = on_command("提交告示2-")
#
#
# @UpdateAdvertisementTWO.handle()
# async def handle_func(bot: Bot, event: Event):
#     QQ = event.get_session_id().split('_')[2]
#     if QQ == "黑名单用户":
#
#         await UpdateAdvertisementTWO.send("你已被拉黑。")
#     else:
#         message = str(event.get_message()).split('-')[1]  # 事件消息内容
#         send = message
#         TMD = JsonDB(QQ=QQ, send=send, Reply='')
#
#         nowtime = datetime.now()
#
#         if TMD.AdvertisementTime() != 0:
#             cdtime = TMD.AdvertisementTime()
#             duration = nowtime - cdtime
#             # 现在时间-过去时间=过去了多少秒
#             interval = duration.seconds
#         else:
#             interval = 180
#             # 若过去了180s则允许
#         if interval >= 180:
#
#             await UpdateAdvertisementTWO.send(TMD.AdvertisementTWO())
#         else:
#
#             await UpdateAdvertisementTWO.send(f"你在{180 - interval}s后才可再次提交哦~")
#
#
# @UpdateAdvertisementTWO.handle()
# async def handle_func(bot: Bot, event: Event):
#     message = str(event.get_message()).split('-')[1]  # 事件消息内容
#     send = message
#     TMD = Clean(i='')
#     # 创建新线程
#     # 设置为后台运行，程序不会阻塞
#     thread = threading.Thread(target=TMD.CleanTWO(),daemon=True)
#
#     # 启动线程
#     thread.start()
#
#     await UpdateAdvertisementTWO.send('')
