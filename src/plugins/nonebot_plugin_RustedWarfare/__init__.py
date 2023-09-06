from nonebot.adapters.onebot.v11 import Event
from nonebot import on_fullmatch
from src.plugins.nonebot_plugin_RustedWarfare.HomeList import HomeList
from . import MatchMap, GroupCheck, RWCheck, RandomMap, Course
LOVE = on_fullmatch(('爱!', '爱酱', 'love', 'LOVE酱', 'love酱', '小宝贝', 'Love'), priority=50)


@LOVE.handle()
async def handle_func():
    await LOVE.finish('呐呐呐？是在叫我嘛~')


Help = on_fullmatch(('help', '帮助', '功能', 'LOVE酱功能'), priority=50)


@Help.handle()
async def handle_func():
    message = """【LOVE酱♥基本功能列表】\n【@LOVE 进行教学和聊天捏！】\n【词汇教学】:【约战大厅】\n【单位查询】:【今日抽签】\n【随机地图】:【群聊查询】\n【铁锈教程】:【抓兔机】\n【为我发电】:【更多功能】"""  # noqa

    await Help.finish(message)


MoreHelp = on_fullmatch(('随机地图', '铁锈教程', '为我发电', '更多功能', '主人功能',
                         '单位查询', '群聊查询', '导入教程', '约战大厅', '抓兔机',
                         '获取房间列表', '联机教程', '开发教程'), priority=50)


@MoreHelp.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    match message:
        case '随机地图':
            message = """---随机地图的指令---\n\t随机单挑图\n\t随机3P图\n\t随机4P图\n\t随机6P图\n\t随机8P图\n\t随机10P图\n\tpsc抽图"""
        case '铁锈教程':
            message = """ ---【目前仅支持的教程命令】---\n\t【导入教程】\t【房间指令教程】\n\t【联机教程】\n\t【开发教程】"""
        case '为我发电':
            message = """ ---【你的每一份支持都会成为LOVE酱开发的动力!】---\n【爱发电网址】:"https://afdian.net/a/allureluoli" """
        case '更多功能':   # 没写完的功能 ---模拟骰子功能哦！---\n\t【丢个骰子】\n
            message = """---看看房间列表---\n\t【获取房间列表】\n---抓兔机!---\n【铁锈抓兔机】\n---比赛专用---\t【比赛抽图模式启动】 """  # noqa
        case '抓兔机':
            message = '请发送: 铁锈抓兔机'
        case '单位查询':
            message = "请以【查询-单位名】这样的格式输入哦！\n 目前已经支持新功能 查看单位目录 可依据目录查看可查询的列表 \n 查看单位一览表请发送【查看XX单位】命令，共有【陆军、海军、空军、建筑、虫族、特殊、旧版单位，六种类型。】\n（数据源自铁锈wiki！）\n (https://rustedwarfare.org/)"  # noqa
        case '群聊查询':
            message = "群聊查询有五种模式：\n【战队群查询】\n【模组群查询】\n【闲聊群查询】\n【地图群查询】\n【赛事群查询】\n【粉丝群查询】"
        case '导入教程':
            message = "导入教程有三个：\n【模组导入教程】\n【地图导入教程】\n【回放导入教程】"
        case '约战大厅':
            message = '此功能暂时弃用'
            # message = "作者写代码写累了该功能还未维护\n\n【欢迎来到约战大厅，在这里你可以看到寻求对局的玩家的房间号，上限10条，每十分钟清理一次。】\n发送【提交告示-房间类型 房间地址】提交告示（符号皆为英文版不要输错哦~）\n发送【查看告示栏】即可查看公告！"  # noqa
        case '联机教程':
            message = '联机教程: https://allureluoli.gitee.io/2023/09/05/%E8%81%94%E6%9C%BA/'
        case '开发教程':
            message = '模组/地图 开发教程：https://rustedwarfareapicode.top/'
        case '获取房间列表':
            await MoreHelp.send('获取中,请等待~~')
            message = HomeList()

    await MoreHelp.finish(message)
