import os
import random
from pathlib import Path
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, Message, MessageSegment
from nonebot.internal.matcher import Matcher
from nonebot.params import CommandArg
import asyncio

MatchMap = on_fullmatch('比赛抽图模式启动', priority=50)


@MatchMap.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()
    if plain_text:
        matcher.set_arg("Map", args)
        # 设置一个got消息


# 这里Ban图
MatchMapList = os.listdir(os.getcwd()+'/data/RustedWarfareData/Map/match')


@MatchMap.got("Map",
              prompt=f"当前地图池为{str(MatchMapList).replace('.png', '')}\nBan图指【BanXXX】\nBan图结束请发送【开始抽图】")
async def handle_func(event: Event):
    MapName = str(event.get_message()).replace('Ban', '')

    if MapName != '开始抽图':

        MatchMapList.remove(MapName + '.png')

        await MatchMap.reject("Ban图成功，地图池中还有：" + str(MatchMapList).replace('.png', ''))

    else:
        await MatchMap.send("Ban图结束，最终地图池中还有：" + str(MatchMapList).replace('.png', '') + "这些地图")


@MatchMap.got("Number", prompt=f"请发送需要抽取地图的数量，如果抽1张图请发送 1 。")
async def handle_func(event: Event):
    Number = eval(str(event.get_message()))
    output_list = []
    # 判断数字大于列表索引就重来
    # try:
    while len(output_list) < Number:

        MapN = random.choice(MatchMapList)  # 返回列表中的随机项

        if MapN not in output_list:
            message = MapN

            path = Path(os.getcwd()+'/data/RustedWarfareData/Map/match/'+MapN)

            image = MessageSegment.image(path)

            output_list.append(MapN)

            await MatchMap.send("呐呐~你抽到的地图为：" + message.replace('.png', '') + image)
            await asyncio.sleep(1)

    await MatchMap.finish("抽图结束，祝您比赛愉快")
