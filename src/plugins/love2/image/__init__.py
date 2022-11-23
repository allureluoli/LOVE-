import random
from datetime import date
from pathlib import Path
from nonebot import  on_fullmatch,on_command
from nonebot.adapters.onebot.v11 import MessageSegment, Event, event, GroupMessageEvent
from nonebot.adapters.onebot.v11.bot import Bot
from ..function import FilePath


tu2=on_fullmatch(['MIKU','血月是个什么','北音'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/rustedwarfare/PVP/MIKU.jpg")).parent / "MIKU.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)

tu2=on_fullmatch(['摆烂'],priority=50)
@tu2.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/image/摆烂.jpg")).parent / "摆烂.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu2.finish(image)


tu233 = on_fullmatch(['2333'], priority=50)

@tu233.handle()
async def handle_func(bot: Bot, event: Event):
    # 构造图片消息段
    image = MessageSegment.face(id_=18)
    await tu233.send(image)


tu=on_fullmatch(['英灵召唤'],priority=50)
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


tu_3=on_fullmatch(['FGO付费十连'],priority=50)
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

tu_2=on_fullmatch(['FGO十连'],priority=50)
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

txztj = on_fullmatch(['铁锈抓兔机'], priority=50)

@txztj.handle()
async def handle_func(bot: Bot, event: Event):
    File_1=open(FilePath(r"/data/铁锈单位.txt"),encoding="UTF-8")
    list_1=File_1.read().replace("\n","").split("→")
    rnd3 = random.Random()
    x = rnd3.randint(0, 200)
    try:
        await txztj.send(f"恭喜你抓到了【{list_1[x]}】捏!将它抱回家吧！")
    except:
        await txztj.send("没有抓到捏~~嘿嘿！")

txztj2 = on_fullmatch(['战队抓兔机'], priority=50)

@txztj2.handle()
async def handle_func(bot: Bot, event: Event):
    File_1=open(FilePath(r"/data/铁锈单位2.txt"),encoding="UTF-8")
    list_1=File_1.read().replace("\n","").split("→")
    rnd3 = random.Random()
    x = rnd3.randint(0, 250)
    try:
        await txztj2.send(f"恭喜你抓到了【{list_1[x]}】捏!将它抱回家吧！")
    except:
        await txztj2.send("没有抓到捏~~嘿嘿！")




tu3=on_fullmatch(['早','早安','安','中午好','晚上好','午安','晚安','半夜好','凌晨好','睡了'],priority=50)
@tu3.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/image/好.jpg")).parent / "好.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu3.finish(image)

tu5=on_fullmatch(['666','牛逼'],priority=50)
@tu5.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/image/6.jpg")).parent / "6.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu5.finish(image)

tu6=on_fullmatch(['???','？？？','什么情况'],priority=50)
@tu6.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/image/2.jpg")).parent / "2.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu6.finish(image)

tu7=on_fullmatch(['摸摸'],priority=50)
@tu7.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath(r"/image/1.jpg")).parent / "1.jpg"
    # 构造图片消息段
    image = MessageSegment.image(path)
    await tu7.finish(image)

read_book=on_fullmatch(['看书','读书'],priority=50)
@read_book.handle()
async def handle_func(bot: Bot, event: Event):
    path = Path(FilePath("/data/read_book.jpg")).parent / "read_book.jpg"
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
    zfcc = str(lucknum)+".jpg"
    path = Path(FilePath("//data//"+str(lucknum)+".jpg"))
    print(path)
    # 构造图片消息段
    image = MessageSegment.image(path)
    await jrrp.finish(image)

