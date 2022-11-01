import os
from pathlib import Path
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import MessageSegment, Event
from nonebot.adapters.onebot.v11.bot import Bot

def getRootPath():
    # 获取文件目录
    curPath = os.path.abspath(os.path.dirname(__file__))
    # 获取项目根路径，内容为当前项目的名字
    rootPath = curPath[:curPath.find('love2') + len('love2')]
    return rootPath

FilePath_1=str(getRootPath())

print(FilePath_1)
def FilePath(FilePath_2):#拼接捏
    FilePath_2=FilePath_1+FilePath_2
    return FilePath_2

tu2=on_keyword(['MIKU','血月是个什么'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\rustedwarfare\PVP\MIKU.jpg")).parent / "MIKU.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)

tu2=on_keyword(['摆烂'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\摆烂.jpg")).parent / "摆烂.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)


tu233 = on_keyword(['2333'], priority=50)

@tu233.handle()
async def handle_func(bot: Bot, event: Event):
    # 构造图片消息段
    image = MessageSegment.face(id_=18)
    await tu233.send(image)


tu=on_keyword(['发图'],priority=50)
@tu.handle()
async def handle_func(bot: Bot, event: Event):

    image = MessageSegment.image("https://i2.hdslb.com/bfs/face/be662100c1a783026930891c43d64e36b3ddab16.jpg")

    await tu.finish(image)


