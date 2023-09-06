import os
import random
from pathlib import Path
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event, MessageSegment

RandomMap = on_fullmatch(('随机单挑图', '随机2p图', '随机2P图',
                          '随机3P图', '随机3p图', '随机4P图', '随机4p图',
                          '随机6p图', '随机6P图', '随机8p图', '随机8P图',
                          '随机10p图', '随机10P图', 'psc抽图', 'PSC抽图'), priority=50)


@RandomMap.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    if message in ['随机单挑图', '随机2p图', '随机2P图']:
        message = 'p2'
    elif message in ['随机3P图', '随机3p图']:
        message = 'p3'
    elif message in ['随机4P图', '随机4p图']:
        message = 'p4'
    elif message in ['随机6P图', '随机6p图']:
        message = 'p6'
    elif message in ['随机8P图', '随机8p图']:
        message = 'p8'
    elif message in ['随机10P图', '随机10p图']:
        message = 'p10'
    elif message in ['PSC抽图', 'psc抽图']:
        message = 'PSC'
    path = os.getcwd()+'/data/RustedWarfareData/Map/'+message
    MapList = os.listdir(path)
    message = random.choice(MapList)
    image = MessageSegment.image(Path(path+'/'+message))
    await RandomMap.send(f'你抽到的地图为：【{message}】'.replace('.png', '')+image)
