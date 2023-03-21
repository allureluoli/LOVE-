import os
import random
from pathlib import Path
from nonebot.adapters.onebot.v11 import Event, MessageSegment
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_fullmatch, on_command

'''本文件主要实现随机单挑图'''

RandomSolo = on_fullmatch(('随机单挑图', '随机2p图', '随机2P图'), priority=50)


@RandomSolo.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 8)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await RandomSolo.send(f'你抽到的地图为：【{message}】' + image)


'''顺便把随机团战图也实现了'''

Random3P = on_fullmatch(('随机3P图', '随机3p图'), priority=50)


@Random3P.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 1)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/p3/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/p3/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await Random3P.send(f'你抽到的地图为：【{message}】' + image)


Random4P = on_fullmatch(('随机4P图', '随机4p图'), priority=50)


@Random4P.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 9)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/p4/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/p4/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await Random4P.send(f'你抽到的地图为：【{message}】' + image)


Random6P = on_fullmatch(('随机6P图', '随机6p图'), priority=50)


@Random6P.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 2)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/p6/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/p6/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await Random6P.send(f'你抽到的地图为：【{message}】' + image)


Random8P = on_fullmatch(('随机8P图', '随机8p图'), priority=50)


@Random8P.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 14)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/p8/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/p8/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await Random8P.send(f'你抽到的地图为：【{message}】' + image)


Random10P = on_fullmatch(('随机10P图', '随机10p图'), priority=50)


@Random10P.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 8)
    listFiles = os.listdir(os.getcwd() + "/love/data/images/p10/")
    #  Pycharm sb 重构

    path = Path(os.getcwd() + f"/love/data/images/p10/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message = listFiles[x].replace('.png', '')

    await Random10P.send(f'你抽到的地图为：【{message}】' + image)


# BanMap = on_command('比赛抽图模式启动', aliases={'Ban-', 'ban-', 'Ban图结束', 'ban图结束'}, priority=50)
#
#
# @BanMap.handle()
# async def handle_func(event: Event):
#
#         listFiles = os.listdir(os.getcwd() + "/love/data/images/p8/")
#         MapN = len(listFiles)
#
#         if str(event.get_message()) == 'Ban图结束' or str(event.get_message()) == 'ban图结束':
#             rnd3 = random.Random()
#             x = rnd3.randint(0, MapN)
#
#             path = Path(os.getcwd() + f"/love/data/images/p10/{listFiles[x]}").parent / f"{listFiles[x]}"
#
#             image = MessageSegment.image(path)
#
#             message = listFiles[x].replace('.png', '')
#
#             await BanMap.finish(f'比赛抽图结束:\t你抽到的地图为：【{message}】' + image)
#
#         # 获取文件夹内地图为一个列表
#         try:
#             message = str(event.get_message()).split('-')[1]
#
#             if message not in listFiles:
#
#                 await BanMap.send(f"地图池中没有名为{message}的地图哦~")
#             else:
#
#                 MapN -= 1
#                 listFiles.remove(message)
#
#                 await BanMap.send(f"呐呐,目前地图池为：{listFiles}\n需要Ban图请发送【ban-地图名称】哦~")
#         except:
#             await BanMap.send(f"呐呐,目前地图池为：{listFiles}\n需要Ban图请发送【ban-地图名称】哦~")
