import os
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event


def GroupCheck(message):
    path = os.getcwd() + '/data/RustedWarfareData/GroupCheck/' + message + '.txt'
    with open(path, encoding='utf-8') as f:
        return f.read()


Check = on_fullmatch(('MOD群查询', '战队群查询', '模组群查询', '闲聊群查询', '地图群查询', '赛事群查询', '粉丝群查询'), priority=50)


@Check.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    match message:
        case '战队群查询':
            message = 'RW-TEAM'
        case 'MOD群查询':
            message = 'RW-MOD'
            await Check.send('我就知道有人会把模组打成MOD！')
        case '模组群查询':
            message = 'RW-MOD'
        case '闲聊群查询':
            message = 'RW-PLAYER'
        case '地图群查询':
            message = 'RW-TEAM'
        case '赛事群查询':
            message = 'RW-MATCH'
        case '粉丝群查询':
            message = 'RW-IDOL'
    await Check.send('声明:本功能部分数据引用于《铁锈战队群》by:深渊,《铁锈海军组织名册》by:铁锈海军组织\nps:现向全铁征集更多群聊数据，希望能收录更多的群。')
    await Check.finish(GroupCheck(message))
