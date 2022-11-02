import os
from pathlib import Path
from nonebot import on_keyword, on_fullmatch
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

tu2=on_fullmatch(['MIKU','血月是个什么','北音'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\rustedwarfare\PVP\MIKU.jpg")).parent / "MIKU.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)

tu2=on_fullmatch(['摆烂'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\摆烂.jpg")).parent / "摆烂.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)


tu233 = on_fullmatch(['2333'], priority=50)

@tu233.handle()
async def handle_func(bot: Bot, event: Event):
    # 构造图片消息段
    image = MessageSegment.face(id_=18)
    await tu233.send(image)


tu=on_fullmatch(['测试。。。。发图'],priority=50)
@tu.handle()
async def handle_func(bot: Bot, event: Event):

    image = MessageSegment.image("https://i2.hdslb.com/bfs/face/be662100c1a783026930891c43d64e36b3ddab16.jpg")

    await tu.finish(image)

tu3=on_fullmatch(['早','早安','安','中午好','晚上好','午安','晚安','半夜好','凌晨好','睡了'],priority=50)
@tu3.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\好.jpg")).parent / "好.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu3.finish(image)

tu5=on_fullmatch(['666','牛逼'],priority=50)
@tu5.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\6.jpg")).parent / "6.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu5.finish(image)

tu6=on_fullmatch(['???','？？？','什么情况'],priority=50)
@tu6.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\2.jpg")).parent / "2.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu6.finish(image)

tu7=on_fullmatch(['摸摸'],priority=50)
@tu7.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"\image\1.jpg")).parent / "1.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu7.finish(image)