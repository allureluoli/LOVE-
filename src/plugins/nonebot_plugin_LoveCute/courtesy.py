from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event

courtesy = on_fullmatch(('早', '早安', '晚安', '晚上好', '中午好', '午安', '睡了', '再见', '拜拜', '886',
                         'bye', '溜了', '润了', '走了', '晚', '吃了么', '你好', '挥挥', '挥挥~', '吃了', '回见'), priority=50)


@courtesy.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    match message:
        case '早':
            message = "早上好~~见到你很开心呐~"
        case '早安':
            message = "早安~~"
        case '晚安':
            message = "晚安~~好梦哦~~"
        case '晚上好':
            message = "晚上好~~我好想你~~"
        case '中午好':
            message = '中午好哦~~吃午饭了么~'
        case '吃了':
            message = "咱也吃了哦~~"
        case '睡了':
            message = "晚安，好梦哦~~"
        case '再见':
            message = "拜拜，下次也来找咱玩哦~~"
        case '886':
            message = '886~~挥挥~'
        case 'bye':
            message = 'bye~~baby~'
        case '溜了':
            message = '慢走哦，随时都可以找咱玩哦~~'
        case '润了':
            message = "拜拜哦~回见哦~"
        case '走了':
            message = "我会想你的喔~~"
        case '晚':
            message = "晚上好~~见到你好开心~~"
        case '吃了么':
            message = "吃了哦~~"
        case '你好':
            message = "你好！"
        case '挥挥~':
            message = "拜拜~~~"
        case '回见':
            message = "下次一定要再见哦~~"
        case '挥挥':
            message = "拜拜哦~"
        case '吃了':
            message = "www~LOVE好羡慕你们的饮食哦~"
    await courtesy.finish(message)
