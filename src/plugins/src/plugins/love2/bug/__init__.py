from ..function import FilePath
from pathlib import Path
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, MessageSegment
from nonebot.adapters.onebot.v11.bot import  Bot


tu3=on_fullmatch(['测试-加文字'],priority=50)
@tu3.handle()
async def handle_func(bot: Bot, event: Event):
    #把图片路径构造成一个列表
    j = 5
    while j > 0:
        j = j - 1
        list_2 = [r'\image\3.gif',r'\image\2.jpg', r'\image\3.jpg', '这是第二关文字', '这是个文字']
        list_3=['3.gif','2.jpg','3.jpg','null','null']
        if j > 2:
            await tu3.send(list_2[j])
        else:
            path = Path(FilePath(list_2[j])).parent / list_3[j]
            image = MessageSegment.image(path)
            await tu3.send(image)

        #构造图片消息段
