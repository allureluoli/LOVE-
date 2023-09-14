import json
import os
from nonebot.adapters.onebot.v11 import Event
from nonebot.rule import to_me
from nonebot import on_command
import random


def Said(Text):
    path = os.getcwd() + '/data/LoveCuteData/ChatData/'
    List = ['日常词汇', '科普词汇', '问答词汇', '娱乐词汇']

    # 准备更新以为了适配新地编号类教学
    for i in List:
        with open(path + 'new-data.json', encoding='utf-8') as f:
            data = json.load(f)
            for j in range(len(data[i]) + 1):
                try:
                    return data[i][f'编号{j}'][Text]
                except KeyError:
                    pass

    with open(path + 'old-data.json', encoding='utf-8') as f:
        data = json.load(f)

        for j in range(len(data['old'])):
            try:
                return data['old'][f'编号{j}'][Text]
            except KeyError:
                pass

    return '呐？这个词汇没有被教学哦\n发送  词汇教学  进行教学'


at = on_command(cmd='', rule=to_me(), priority=60)
""" 被艾特时回复 """


@at.handle()
async def handle_func(event: Event):
    Text = str(event.get_message())
    if len(Text) == 0:
        message = ["你好，这里是LOVE酱，发送 帮助 可以查看我的功能哦！",
                   "你好呀，我是LOVE酱，一个专为铁锈战争服务的虚拟少女！",
                   "你好~有什么需要帮助的吗？",
                   "LOVE酱的开源代码仓：https://github.com/allureluoli/LOVE- ,如果你喜欢LOVE，就请给一个STAR吧！"]

        message = random.choice(message)
        await at.finish(message)

    await at.finish(Said(Text))
