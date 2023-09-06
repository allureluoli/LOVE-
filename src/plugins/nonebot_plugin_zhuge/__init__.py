import random

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event

LOVE = on_command('鉴定', priority=50)


def ss(s, add='', name=''):
    a = random.Random()
    num = a.random()
    # if add == '力量' and name == '摄影师':
    #     if num > 0.4:
    #         return s + f'鉴定成功:{int(num * 100)}'
    #     return s + f'鉴定失败{int(num * 100)}'
    # if add == '敏捷' and name == '摄影师':
    #     if num > 0.4:
    #         return s + f'鉴定成功:{int(num * 100)}'
    #     return s + f'鉴定失败{int(num * 100)}'
    # if add == '交际学' and name == '摄影师':
    #     if num > 0.4:
    #         return s + f'鉴定成功:{int(num * 100)}'
    #     return s + f'鉴定失败{int(num * 100)}'
    # if add == '教育' and name == '摄影师':
    #     if num > 0.4:
    # #         return s + f'鉴定成功:{int(num * 100)}'
    #     return s + f'鉴定失败{int(num * 100)}'

    if num > 0.5:
        return s + f'鉴定成功:{int(num * 100)}'

    return s + f'鉴定失败{int(num * 100)}'


@LOVE.handle()
async def handle_func(event: Event):
    txt = str(event.get_user_id())
    if txt == 2455380297:
        txt = '兽医'
    elif txt == 3282903035:
        txt = '摄影师'
    s = str(event.get_message())
    s = s.replace('鉴定', '')
    match s:
        case '灵感':
            await LOVE.finish(ss(s, name=txt))
        case '力量':
            await LOVE.finish(ss(s, name=txt))
        case '智力':
            await LOVE.finish(ss(s, name=txt))
        case '敏捷':
            await LOVE.finish(ss(s, name=txt))
        case '幸运':
            await LOVE.finish(ss(s, name=txt))
        case '交际学':
            await LOVE.finish(ss(s, name=txt))
        case '理智':
            await LOVE.finish(ss(s, name=txt))
        case '意志':
            await LOVE.finish(ss(s, name=txt))
        case '鉴尸':
            await LOVE.finish(ss(s, name=txt))
        case '聆听':
            await LOVE.finish(ss(s, name=txt))

