from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11.bot import Bot
from .weiqi import Application

#__init__文件主要对整个游戏起到初始化和流程控制的作用


#主要流程设置为

# 开始游戏 - 或者改变模式 -然后再开始游戏）嗯，不改变原作者设置的流程了吧

#后期改良，加入棋局系统

#慢慢完善呗
Application()
#试试我一晚上能写到什么地步

introduce = on_fullmatch(['LOVE围棋开始'], priority=50)

@introduce.handle()
async def handle_func(bot: Bot, event: Event):



    await introduce.finish('默认开始游戏的人为先手哦，请开始下棋吧。')
