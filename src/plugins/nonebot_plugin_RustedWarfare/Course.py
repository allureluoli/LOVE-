import os
from nonebot import on_fullmatch
from nonebot.adapters.onebot.v11 import Event

Course = on_fullmatch(('房间指令教程', '地图导入教程', '模组导入教程', 'MOD导入教程', '回放导入教程'), priority=50)


@Course.handle()
async def handle_func(event: Event):
    message = str(event.get_message())
    path = os.getcwd() + '/data/RustedWarfareData/Course/' + message

    def W(T):
        with open(path + T, encoding='utf-8') as M:
            return M.read()

    match message:
        case '房间指令教程':
            await Course.finish(W('server_instruct.txt'))
        case '地图导入教程':
            await Course.finish(W('map_course.txt'))
        case '模组导入教程':
            await Course.finish(W('mod_course.txt'))
        case 'MOD导入教程':
            await Course.finish(W('mod_course.txt'))
        case '回放导入教程':
            await Course.finish(W('replay_course.txt'))
