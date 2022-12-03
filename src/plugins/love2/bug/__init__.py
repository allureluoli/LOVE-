from ..function import FilePath
from pathlib import Path
from nonebot import on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import Event, MessageSegment, GroupMessageEvent
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

#小型转发模块测试
pvp = on_command(cmd='最高权限-开始群发--测试', priority=50)

@pvp.handle()

async def handle_func(bot: Bot, event: GroupMessageEvent):

    tyt_1 = open(str(FilePath(r'/function/group_id.txt')), encoding='UTF-8')
    tyt_2 = tyt_1.readlines()

    hang = 0
    for x in range(len(tyt_2)):
        hang = hang + 1

    #内置循环
    while hang > 0:#循环32次
            hang = hang - 1


    tyt_1 = open(str(FilePath(r'/function/group_id.txt')), encoding='UTF-8')
    tyt_2 = tyt_1.readlines()
    tyt_1.close()
    s = hang - 1
    group_id = tyt_2[s]

    wot2 = open(str(FilePath(r'/function/xuanchuan.txt')), encoding='UTF-8')
    text = wot2.read()
    wot2.close()

    await pvp.send(group_id=int(group_id), message=text, auto_escape=False)