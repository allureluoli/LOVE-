import asyncio
import os
import random
from datetime import date
from pathlib import Path
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import MessageSegment, Event

JRRP = on_fullmatch(('今日抽签', 'jrrp', '今日运势', '运势'), priority=50) # noqa


@JRRP.handle()
async def handle_func(event: Event):
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(event.get_user_id()))
    path = os.getcwd() + '/data/LoveCuteData/RandomImage/'
    ImageList = os.listdir(path)
    image = rnd.choice(ImageList)
    image = MessageSegment.image(Path(path + image))

    await JRRP.finish(image)

Rabbit = on_fullmatch('铁锈抓兔机', priority=50)


@Rabbit.handle()
async def handle_func():

    path = os.getcwd() + '/data/RustedWarfareData/Units/'
    with open(path + 'ORIGINAL/总单位.txt', encoding='utf-8') as f:
        STR = f.read().split('\n')
    rabbit = random.choice(STR)
    try:

        with open(path + 'UnitsImage/' + rabbit + '.jpg', mode='rb') as f:
            f.read()

        image = MessageSegment.image(Path(path + 'UnitsImage/' + rabbit + '.jpg'))

        await Rabbit.send(f'恭喜你抓到了【{rabbit}】捏,将它抱回家吧！')
        await asyncio.sleep(2)
        await Rabbit.send(image)
    except FileNotFoundError:
        await Rabbit.send(f'恭喜你抓到了【{rabbit}】捏,将它抱回家吧！')
