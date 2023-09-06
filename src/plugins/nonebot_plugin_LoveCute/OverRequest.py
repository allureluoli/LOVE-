import json
import nonebot
from nonebot import on_request
from nonebot.adapters.onebot.v11 import RequestEvent

config = nonebot.get_driver().config
superusers = config.superusers

Add_Group = on_request(priority=1, block=True)


@Add_Group.handle()
async def _():
    # data = json.loads(str(event))
    # # message = f"收到来自QQ:{data['request.group.invite']['user_id']}\n的邀请加群请求\n" \
    # #           f"群号:{data['request.group.invite']['group_id']}"

    for i in superusers:
        await nonebot.get_bot().send_private_msg(user_id=i, message='收到了新的加群邀请。')
        # 同意请求怎么写啊，好麻烦啊，摆烂了
