from nonebot import on_notice
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, MessageSegment, Message


notice_handle = on_notice(priority=40, block=True)  # 通知事件


@notice_handle.handle()
async def GroupNewMember(bot: Bot, event: GroupIncreaseNoticeEvent):

    if event.user_id == event.self_id:
        await bot.send_group_msg(group_id=event.group_id, message=Message(
            MessageSegment.text('大家好！ 这里是LOVE酱哦，希望能和大家愉快相处。\n LOVE酱会好多东西呢！发送help查看吧~~')))
    elif event.get_message != event.self_id:
        await bot.send_group_msg(group_id=event.group_id, message=Message(
            MessageSegment.at(event.user_id) + MessageSegment.text("欢迎新群友哦~\n")))
