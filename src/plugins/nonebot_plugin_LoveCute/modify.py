import json
import os
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.internal.matcher import Matcher
from nonebot.params import CommandArg

courtesy = on_command(cmd='修改科普类型编号', aliases={
    '修改娱乐类型编号', '修改问答类型编号', '修改日常类型编号'}, priority=50)


@courtesy.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    await courtesy.finish('你太傻逼了你为什么要写这样的功能？')
    await courtesy.send(plain_text)
    if plain_text:
        matcher.set_arg("word", args)

        # 设置一个got消息


@courtesy.got('word', prompt='请发送修改后的响应词')
async def handle_func(event: Event):
    message = str(event.get_message())
    Class = message


@courtesy.got('word', prompt='请发送修改后的回复词')
async def handle_func(event: Event):
    SerialNumber = str(event.get_message())

    path = os.getcwd() + '/data/LoveCuteData/ChatData/'
    name = 'new-data.json'

    with open(path + name, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    with open(path + name, mode='w', encoding='utf-8') as f:
        json.dump(data, f)
