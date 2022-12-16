from urllib import request, error,parse
from bs4 import BeautifulSoup
import json

def Setu(setu):
    url = "https://api.lolicon.app/setu/v2"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Host": "api.lolicon.app",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0"
    }

    dict = {
        "name": "Germey"
    }
    data = bytes(parse.urlencode(dict), encoding="utf8")

    try:
        req = request.Request(url=url, data=data, headers=headers, method="POST")
        response = request.urlopen(req)
        zfc1=response.read()
        soup = BeautifulSoup(zfc1, "html.parser")


        data1 = json.loads(str(soup))

        setu_1 = data1['data']

        setu=str(setu_1).split("'original': '")[1].replace("'}}]",'')



        print(soup)

    except error.HTTPError as e:
        print(e.code, '\n', e.reason, '\n', e.headers)

    return setu



