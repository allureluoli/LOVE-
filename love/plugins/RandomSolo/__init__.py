import os
import random
from pathlib import Path

from nonebot.adapters.onebot.v11 import Event, MessageSegment
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_fullmatch
'''本文件主要实现随机单挑图'''

RandomSolo = on_fullmatch('随机单挑图', priority=50)

@RandomSolo.handle()
async def handle_func(bot: Bot, event: Event):
    rnd3 = random.Random()
    x = rnd3.randint(0, 8)
    listFiles = os.listdir(os.getcwd()+"/love/data/images/")
    #  Pycharm sb 重构

    path = Path(os.getcwd()+f"/love/data/images/{listFiles[x]}").parent / f"{listFiles[x]}"

    image = MessageSegment.image(path)

    message= listFiles[x].replace('.png','')

    await RandomSolo.send(f'你抽到的地图为：【{message}】'+image)
