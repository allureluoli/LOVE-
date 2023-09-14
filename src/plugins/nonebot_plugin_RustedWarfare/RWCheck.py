import asyncio
import os
from pathlib import Path

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, MessageSegment


def RWCheck(name):
    path = os.getcwd() + '/data/RustedWarfareData/Units/ORIGINAL/' + name + '.txt'
    with open(path, encoding='utf-8') as f:
        return f.read()


Check = on_command('查询-', priority=50)


@Check.handle()
async def handle_func(event: Event):
    try:
        Text = str(event.get_message()).split('查询-')[1]
        message = RWCheck(Text)
        path = os.getcwd() + '/data/RustedWarfareData/Units/'
        try:
            with open(path + 'UnitsImage/' + Text + '.jpg', mode='rb') as f:
                f.read()

            image = MessageSegment.image(cache=True, file=Path(path + 'UnitsImage/' + Text + '.jpg'))

            await Check.send(message+'\n 数据源自铁锈战争wiki: https://rustedwarfare.org/' )
            await asyncio.sleep(2)
            await Check.send(image)
        except FileNotFoundError:
            await Check.send(message + '\n 数据源自铁锈战争wiki: https://rustedwarfare.org/')
    except FileNotFoundError:
        await Check.send('你输入的单位名无法识别。')

nameList = on_command('查看', priority=60)


@nameList.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    match message:
        case '查看虫族单位':
            message = '虫族'
        case '查看海军单位':
            message = '海军'
        case '查看建筑单位':
            message = '建筑'
        case '查看旧版单位':
            message = '旧版单位'
        case '查看空军单位':
            message = '空军'
        case '查看陆军单位':
            message = '陆军'
        case '查看特殊单位':
            message = '特殊'

    await nameList.send(RWCheck(message))
