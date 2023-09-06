import json
import os
import nonebot
from nonebot import on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import Event
config = nonebot.get_driver().config
superusers = config.superusers


def OverReview(path, name):
    with open(path + 'new-data.json', encoding='utf-8') as f:
        data = json.load(f)

    with open(path + 'Temp/' + name, encoding='utf-8') as f:
        D = json.load(f)

        data[D['class']][D['content']['put']] = D['content']['return']

    with open(path + 'new-data.json', encoding='utf-8', mode='w') as f:
        json.dump(data, f)


Check = on_fullmatch('待审核词汇', priority=50)


@Check.handle()
async def handle_func(event: Event):
    if event.get_user_id() not in superusers:
        await Check.finish('你没有权限使用该命令。')
    path = os.getcwd() + '/data/LoveCuteData/ChatData/Temp/'
    message = os.listdir(path)
    SUM = 0
    STR = ''
    for i in message:
        SUM += 1
        with open(path + i) as f:
            message = json.load(f)
            message = f"【编号{SUM}】\n类型:{message['class']}\n内容:{message['content']}\n教学者QQ:{message['QQ']}"
            STR += message + '\n'

    await Check.finish(STR)


Check = on_command('过审编号', aliases={'拒绝过审编号'}, priority=50)


@Check.handle()
async def handle_func(event: Event):
    Text = str(event.get_message())
    if event.get_user_id() not in superusers:
        await Check.finish('你没有权限使用该命令。')

    try:
        SUM = int(Text.replace('过审编号', '')) - 1
        path = os.getcwd() + '/data/LoveCuteData/ChatData/'
        message = os.listdir(path + 'Temp/')
        if '拒绝过审编号' in Text:
            os.remove(path + 'Temp/' + message[SUM])
            await Check.finish(f'已拒绝过审编号【{SUM+1}】')
        OverReview(path=path, name=message[SUM])
        os.remove(path + 'Temp/' + message[SUM])
        await Check.finish('你成功过审了【' + message[SUM].replace('.json', '') + '】')
    except IndexError:
        await Check.finish('编号数字不正确。')
    except ValueError:
        await Check.finish('编号请使用阿拉伯数字。')
