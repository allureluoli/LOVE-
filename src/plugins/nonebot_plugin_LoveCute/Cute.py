import os
import random
from pathlib import Path
from nonebot import on_fullmatch

# ImageSaid = on_keyword({'悲', '比心', '别急', '吃饭', '哈哈'}, priority=50)
# 无法得到Keyword 因此使用 on_full match 并且考虑到响应过多的问题

from nonebot.adapters.onebot.v11 import Event, MessageSegment

ImageSaid = on_fullmatch(
    ('H', 'vd', 'V我', '不玩了', '不理', '不要', '信息量过大', '动脑', '变态', '吃掉', '吃饭', '吓', '呆', '哈哈哈',
     '哈哈哈哈', '喜欢', '喝茶', '嘿', '大吉', '威胁', '害怕', '尊嘟假嘟', '很酷', '怕', '思考', '恼', '惊了',
     '投降',
     '挥手', '摆烂', '敬礼', '晕', '暴力', '杀', '汗', '爽', '看报', '看看', '睡觉', '祝福', '笔记', '耶',
     '苦笑', '茶',
     '萌', '谢谢', '赞', '鄙视', '阿弥陀佛', '雪糕', '震撼', '鼓掌', '为什么', '偷听', '别急', '吃饭', '哈吉米', '哈哈',
     '学习', '寄', '开车', '怕', '悲', '摇起来', '比心', '水枪', '秀', '笑', '色色', '酷', '乐', '傻', '睿智', '笑',
     '寄', '?', '？', '看', '懵', '跳舞', '吃瓜', '看书'),
    priority=50)


def SaidImage(Text):
    path = Text
    image = MessageSegment.image(Path(path))

    return image


@ImageSaid.handle()
async def handle_func(event: Event):
    path = os.getcwd() + '/data/LoveCuteData/CuteImage/'
    Text = str(event.get_message())
    match Text:
        case '乐':
            Text = random.choice(['乐-1', '乐-2', '乐-3'])
        case '傻':
            Text = random.choice(['傻-1', '傻-2', '傻-3', '傻-4', '傻-6'])
        case '睿智':
            Text = random.choice(['睿智-1', '睿智-2'])
        case '笑':
            Text = random.choice(['笑-2', '笑'])
        case '寄':
            Text = random.choice(['寄', '寄了-2', '寄了'])
        case '？':
            Text = random.choice(['问号-1', '问号-2'])
        case '?':
            Text = random.choice(['问号-1', '问号-2'])
        case '看':
            Text = random.choice(['看-2', '看-3', '看-4', '看-5', '看-6', '看-7', '看'])
        case '懵逼':
            Text = random.choice(['懵-1', '懵-2'])
        case '跳舞':
            Text = random.choice(['跳舞-1', '跳舞-2', '跳舞-3'])
        case '吃瓜':
            Text = random.choice(['吃瓜-1', '吃瓜-2', '面包-3'])
    try:
        with open(path + Text + '.jpg', mode='rb') as f:
            f.read()

        image = SaidImage(path + Text + '.jpg')
        await ImageSaid.send(image)
    except FileNotFoundError:
        await ImageSaid.send(path + Text + '.jpg')
        image = SaidImage(path + Text + '.gif')
        await ImageSaid.send(image)
