import os
import random
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_fullmatch

CatcherOne = on_fullmatch('铁锈抓兔机', priority=50)

@CatcherOne.handle()
async def handle_func(bot: Bot, event: Event):
    File_1=open(os.getcwd()+"/love/data/CatcherData/铁锈单位.txt",encoding="UTF-8")
    list_1=File_1.read().replace("\n","").split("→")
    rnd3 = random.Random()
    x = rnd3.randint(0, 200)
    try:
        await CatcherOne.send(f"恭喜你抓到了【{list_1[x]}】捏!将它抱回家吧！")
    except:
        await CatcherOne.send("没有抓到捏~~嘿嘿！")

CatCherTwo = on_fullmatch('战队抓兔机', priority=50)

@CatCherTwo.handle()
async def handle_func(bot: Bot, event: Event):
    File_1=open(os.getcwd()+"/love/data/CatcherData/铁锈单位2.txt",encoding="UTF-8")
    list_1=File_1.read().replace("\n","").split("→")
    rnd3 = random.Random()
    x = rnd3.randint(0, 250)
    try:
        await CatCherTwo.send(f"恭喜你抓到了【{list_1[x]}】捏!将它抱回家吧！")
    except:
        await CatCherTwo.send("没有抓到捏~~嘿嘿！")