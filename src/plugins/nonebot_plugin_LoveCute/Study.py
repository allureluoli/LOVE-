import json
import os
import nonebot
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.internal.matcher import Matcher
from nonebot.params import CommandArg

config = nonebot.get_driver().config
superusers = config.superusers

Study = on_fullmatch('词汇教学', priority=50)


@Study.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("word", args)
        # 设置一个got消息


message_one = ''


@Study.got("word")
async def handle_func(event: Event):
    global message_one
    message_one = str(event.get_message())

    if message_one not in ['日常词汇', '科普词汇', '问答词汇', '娱乐词汇']:
        await Study.reject(
            '词汇共分为日常词汇、科普词汇、问答词汇、娱乐词汇，四个分区，请选择你要教学的词汇应在的分区哦~\n例教学科普词汇，发送:科普词汇')
    await Study.send('选择成功！')


message_two = ''


@Study.got("IN", prompt=f"请发送响应词（也就是场景下对bot说的词）。")
async def handle_func(event: Event):
    global message_two
    message_two = str(event.get_message())

    await Study.send('发送成功！')


@Study.got("PUT", prompt=f"请发送回复词（也就是场景下bot的回复）。")
async def handle_func(event: Event):
    message_three = str(event.get_message())

    # 发现python贴心的地方，即使字典里用的是单引号，写入的时候也是双引号，json。
    DICT = {
        "class": message_one,
        "content": {
            'put': message_two,
            'return': message_three
        },
        "QQ": event.get_user_id()
    }
    with open(os.getcwd() + f'/data/LoveCuteData/ChatData/Temp/{message_two}.json', encoding='utf-8', mode='w') as f:
        json.dump(DICT, f)
    await Study.send('教学完成！(请等待审核)')
    for i in superusers:
        await nonebot.get_bot().send_private_msg(user_id=i, message='收到了新的教学内容,请及时审核.')
