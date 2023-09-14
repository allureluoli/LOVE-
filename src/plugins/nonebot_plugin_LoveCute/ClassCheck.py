import json
import os

from nonebot import on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import Event


def CheckPIODEF(Text):
    path = os.getcwd() + '/data/LoveCuteData/ChatData/'
    List = ['日常词汇', '科普词汇', '问答词汇', '娱乐词汇词汇']

    # 准备更新以为了适配新地编号类教学
    for i in List:
        with open(path + 'new-data.json', encoding='utf-8') as f:
            data = json.load(f)
            try:
                for j in range(len(data[i])):
                    try:
                        t = data[i][f'编号{j}'][Text]
                        return f'{Text}:{t} 的类型为 {i} ,编号为{j}'
                    except KeyError:
                        pass
            except KeyError:
                pass
    with open(path + 'old-data.json', encoding='utf-8') as f:
        data = json.load(f)
        try:
            for j in range(len(data['old'])):
                try:
                    t = data['old'][f'编号{j}'][Text]
                    return f'{Text}:{t} 的类型为old,编号为{j}'
                except KeyError:
                    pass
        except KeyError:
            return '由于不存在你要查询的词汇，所以无法得出编号。'


def CheckWord(name: str):
    name = name.replace('查看', '')
    file = 'old-data.json'
    if name != 'old词汇':
        file = 'new-data.json'
    path = os.getcwd() + '/data/LoveCuteData/ChatData/'
    with open(path + file, encoding='utf-8') as f:
        data = json.load(f)

        return str(data[name])


Check = on_fullmatch(('查看娱乐词汇', '查看科普词汇', '查看问答词汇', '查看日常词汇'), priority=50)


@Check.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    match message:
        case '查看娱乐词汇':
            await Check.finish(CheckWord(message))
        case '查看科普词汇':
            await Check.finish(CheckWord(message))
        case '查看问答词汇':
            await Check.finish(CheckWord(message))
        case '查看日常词汇':
            await Check.finish(CheckWord(message))
        case '查看old':
            await Check.finish(CheckWord(message))


CheckPIO = on_command(cmd='查看词汇编号', priority=50)


@CheckPIO.handle()
async def han_func(event: Event):
    message = str(event.get_message())
    message = message.replace('查看词汇编号', '')

    await CheckPIO.finish(CheckPIODEF(message))
