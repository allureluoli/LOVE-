import json
import os
import nonebot
from nonebot import on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import Event

config = nonebot.get_driver().config
superusers = config.superusers


def OverReview(path, name):
    """ 实现将教学词汇的文件存入总数据json"""
    with open(path + 'new-data.json', encoding='utf-8') as f:
        data = json.load(f)

    with open(path + 'Temp/' + name, encoding='utf-8') as f:
        D = json.load(f)
        # 获取编号
        No_ = len(data[D['class']]) + 1
        NewData = {
            f"编号{No_}": {
                D['content']['put']: D['content']['return']
            }
        }

    data[D['class']].update(NewData)
    with open(path + 'new-data.json', encoding='utf-8', mode='w') as f:
        json.dump(data, f)
    return f"已被存入{D['class']}类型编号{No_}"


def CheckFILE():
    SUM = 0
    STR = ''
    path = os.getcwd() + '/data/LoveCuteData/ChatData/Temp/'
    message = os.listdir(path)
    if len(message) < 1:
        return '所有的词汇都审核完成了呢，幸苦你啦主人~~~'
    for i in message:
        SUM += 1
        try:
            with open(path + i) as f:
                message = json.load(f)
                message = f"【编号{SUM}】\n类型:{message['class']}\n内容:{message['content']}\n教学者QQ:{message['QQ']}"
                STR += message + '\n'
        except json.decoder.JSONDecodeError:
            pass
        # 跳过这个文件

    return STR


Check = on_fullmatch('待审核词汇', priority=50)


@Check.handle()
async def handle_func(event: Event):
    if event.get_user_id() not in superusers:
        await Check.finish('你没有权限使用该命令。')

    await Check.finish(CheckFILE())


Check = on_command('过审编号', aliases={'拒绝过审编号'}, priority=50)


@Check.handle()
async def handle_func(event: Event):
    Text = str(event.get_message())
    if event.get_user_id() not in superusers:
        await Check.finish('你没有权限使用该命令。')

    try:
        path = os.getcwd() + '/data/LoveCuteData/ChatData/'
        message = os.listdir(path + 'Temp/')
        if '拒绝过审编号' in Text:
            SUM = int(Text.replace('拒绝过审编号', '')) - 1
            os.remove(path + 'Temp/' + message[SUM])
            await Check.send(f'已拒绝过审编号【{SUM + 1}】')
            await Check.finish(CheckFILE())
        SUM = int(Text.replace('过审编号', '')) - 1
        await Check.send('你成功过审了【' + message[SUM].replace('.json', '') + '】')
        await Check.send(OverReview(path=path, name=message[SUM]))
        os.remove(path + 'Temp/' + message[SUM])
        await Check.finish(CheckFILE())
    except IndexError:
        await Check.finish('编号数字不正确。')
    except ValueError:
        await Check.finish('编号请使用阿拉伯数字。')
