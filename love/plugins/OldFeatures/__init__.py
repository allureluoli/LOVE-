import os
import random
from datetime import date
from pathlib import Path

from nonebot.adapters.onebot.v11 import Event, MessageSegment, GroupMessageEvent
from nonebot.adapters.onebot.v11.bot import Bot
from nonebot.plugin.on import on_fullmatch, on_command

tu=on_fullmatch('英灵召唤',priority=50)
@tu.handle()
async def handle_func(bot: Bot, event: Event):
    rnd = random.Random()
    lucknum = rnd.randint(1, 367)

    if lucknum >= 100:
        wtm="http://fgo-cdn.vgtime.com/media/fgo/servant/card/" + str(lucknum) + "A.png"
    elif lucknum >= 10:
        wtm="http://fgo-cdn.vgtime.com/media/fgo/servant/card/0" + str(lucknum) + "A.png"
    else:
        wtm="http://fgo-cdn.vgtime.com/media/fgo/servant/card/00" + str(lucknum) + "A.png"
    image = MessageSegment.image(wtm)
    await tu.finish(image)


tu_3=on_fullmatch('FGO付费十连',priority=50)
@tu_3.handle()
async def handle_func(bot: Bot, event: Event):
    cxk=0
    imageend = ""
    while cxk <10:
        one_star = [341, 294, 259, 257, 254, 174, 53, 50, 45, 39, 36, 16, 107]
        two_star = [260, 258, 256, 255, 57, 54, 44, 43, 40, 34, 33, 25, 24, 21, 19]
        three_star = [7, 9, 13, 15, 17, 20, 22, 23, 26, 27, 28, 31, 32, 35, 38, 42, 49, 55, 56, 63, 64, 71, 72, 79, 80,
                      81, 95, 104, 105, 110, 117, 124, 125, 126, 148, 172, 186, 203, 204, 210, 231, 246, 249, 251, 273,
                      348, 352]

        cxk +=1
        rnd3 = random.Random()
        lucknum3 = rnd3.randint(1, 100)
        if lucknum3 <=25:
            rnd3 = random.Random()
            x = rnd3.randint(1, 12)
            lucknum=one_star[x]
        elif lucknum3 <=35:
            rnd3 = random.Random()
            x = rnd3.randint(1, 14)
            lucknum = two_star[x]
        elif lucknum3 <= 45:
            rnd3 = random.Random()
            x = rnd3.randint(1, 46)
            lucknum = three_star[x]
        else:
            rnd2 = random.Random()
            lucknum = rnd2.randint(1, 367)

        #一星爆率50 二星爆率30 三星爆率25 剩下百分之五去好池子里面抽

        if lucknum >= 100:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/" + str(lucknum) + ".jpg"
        elif lucknum >= 10:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/0" + str(lucknum) + ".jpg"
        else:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/00" + str(lucknum) + ".jpg"

        image = MessageSegment.image(wtm)
        imageend += image

    await tu_3.send(imageend)

tu_2=on_fullmatch('FGO十连',priority=50)
@tu_2.handle()
async def handle_func(bot: Bot, event: Event):
    cxk=0
    imageend = ""
    while cxk <10:
        one_star = [341, 294, 259, 257, 254, 174, 53, 50, 45, 39, 36, 16, 107]
        two_star = [260, 258, 256, 255, 57, 54, 44, 43, 40, 34, 33, 25, 24, 21, 19]
        three_star = [7, 9, 13, 15, 17, 20, 22, 23, 26, 27, 28, 31, 32, 35, 38, 42, 49, 55, 56, 63, 64, 71, 72, 79, 80,
                      81, 95, 104, 105, 110, 117, 124, 125, 126, 148, 172, 186, 203, 204, 210, 231, 246, 249, 251, 273,
                      348, 352]

        cxk +=1
        rnd3 = random.Random()
        lucknum3 = rnd3.randint(1, 100)
        if lucknum3 <=45:
            rnd3 = random.Random()
            x = rnd3.randint(1, 12)
            lucknum=one_star[x]
        elif lucknum3 <=75:
            rnd3 = random.Random()
            x = rnd3.randint(1, 14)
            lucknum = two_star[x]
        elif lucknum3 <= 95:
            rnd3 = random.Random()
            x = rnd3.randint(1, 46)
            lucknum = three_star[x]
        else:
            rnd2 = random.Random()
            lucknum = rnd2.randint(1, 367)

        #一星爆率50 二星爆率30 三星爆率25 剩下百分之五去好池子里面抽

        if lucknum >= 100:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/" + str(lucknum) + ".jpg"
        elif lucknum >= 10:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/0" + str(lucknum) + ".jpg"
        else:
            wtm = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/00" + str(lucknum) + ".jpg"

        image = MessageSegment.image(wtm)
        imageend += image

    await tu_2.send(imageend)

tu1=on_fullmatch('vd',priority=50)
@tu1.handle()
async def handle_func(bot: Bot, event: Event):


    path = Path(os.getcwd()+f"/love/data/Emoticon/vd.jpg").parent / "vd.jpg"

    image = MessageSegment.image(path)

    await tu1.send(image)

tu2=on_fullmatch('可爱',priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):


    path = Path(os.getcwd()+f"/love/data/Emoticon/cat.jpg").parent / "cat.jpg"

    image = MessageSegment.image(path)

    await tu2.send(image)

tu3=on_fullmatch(('早','早安','安','中午好','晚上好','午安','晚安','半夜好','凌晨好','睡了'),priority=50)
@tu3.handle()
async def handle_func(bot: Bot, event: Event):


    path = Path(os.getcwd()+f"/love/data/Emoticon/好.jpg").parent / "好.jpg"

    image = MessageSegment.image(path)

    await tu3.send(image)


tu4=on_fullmatch('摆烂',priority=50)
@tu4.handle()
async def handle_func(bot: Bot, event: Event):


    path = Path(os.getcwd()+f"/love/data/Emoticon/摆烂.jpg").parent / "摆烂.jpg"

    image = MessageSegment.image(path)

    await tu4.send(image)

tu6=on_fullmatch(('???','？？？','什么情况'),priority=50)
@tu6.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(os.getcwd() + f"/love/data/Emoticon/ask.jpg").parent / "ask.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu6.finish(image)

read_book=on_fullmatch(('看书','读书'),priority=50)

@read_book.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(os.getcwd() + f"/love/data/Emoticon/read_book.jpg").parent / "read_book.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await read_book.finish(image)

jrrp=on_command('今日抽签',priority=50)
@jrrp.handle()
async def handle_func(bot: Bot, event: GroupMessageEvent):
    txet_5 = str(event.get_session_id()).split('_', 2)
    txet_7 = txet_5[2]
    rnd = random.Random()
    rnd.seed(int(date.today().strftime("%y%m%d")) + int(txet_7))
    lucknum = rnd.randint(1, 7)

    path= Path(os.getcwd() + f"/love/data/Emoticon/"+str(lucknum)+".jpg")


    # 构造图片消息段
    image = MessageSegment.image(path)
    await jrrp.finish(image)


LOVEROMD =  on_command('LOVE丢-',priority=50)

@LOVEROMD.handle()
async def handle_func(bot: Bot, event: GroupMessageEvent):
    X = str(event.get_message()).split('-')[1]
    rnd = random.Random()
    x = rnd.randint(1, int(X))

    await LOVEROMD.send(f"呐呐呐~你丢了{x}点呢！")



pao = on_fullmatch('。', priority=50)

@pao.handle()
async def handle_func(bot: Bot, event: Event):
    await pao.send("一个泡泡")


sb = on_fullmatch(('?', '？'), priority=50)


@sb.handle()
async def handle_func(bot: Bot, event: Event):
    await sb.send("单独发一个问号很让重视你的人费解哦~")


wife = on_fullmatch('碳酸', priority=50)


@wife.handle()
async def handle_func(bot: Bot, event: Event):
    await wife.send("可爱爱♥")


wife2 = on_fullmatch('碳酸是', priority=50)


@wife2.handle()
async def handle_func(bot: Bot, event: Event):
    await wife2.send("二月的")


wife3 = on_fullmatch('二月是', priority=50)


@wife3.handle()
async def handle_func(bot: Bot, event: Event):
    await wife3.send("碳酸的")
