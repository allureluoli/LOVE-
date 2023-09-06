from nonebot import on_fullmatch, on_command
from nonebot.adapters.onebot.v11 import Event

import requests
import json


def get_access_token():
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    APIKEY = 'PCT1PDOGGGVIw4Ra4vYKnmoI'

    SecretKey = 'oRUddrw9ahqVrQMchGLDpjT6dNemhbFe'

    url = f'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={APIKEY}&client_secret={SecretKey}' # noqa

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")  # 得到token


def YiYan(Text):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/completions?access_token=" + get_access_token() # noqa

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": f"{Text}"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    try:

        response_json = response.json()

        if 'result' in response_json:

            return response_json['result']

        else:

            # 处理请求成功但返回结果不是预期的情况
            print('Unexpected response:', response_json)

            return None

    except json.JSONDecodeError:

        # 处理请求失败或返回结果不是JSON格式的情况

        print('Failed to decode response:', response.text)

        return None


wenxin = on_command('YY-', priority=50)


@wenxin.handle()
async def handle_func(event: Event):
    Text = str(event.get_message()).split('YY-')[1]

    message = YiYan(Text)

    await wenxin.send(message)