from urllib import request, error,parse
from bs4 import BeautifulSoup

def home_list(game_list):
    url = "http://fgo-cdn.vgtime.com/media/fgo/servant/head/"
    headers = {
        "Accept": r"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection": "keep-alive",
        "Host": "www.corrodinggames.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0",
        "accept-encoding":"identity"
    }

    dict = {
        "name": "Germey"
    }
    data = bytes(parse.urlencode(dict), encoding="utf8")

    try:
        req = request.Request(url=url, data=data, headers=headers, method="POST")
        response = request.urlopen(req)
        zfc1=response.read()
        soup = BeautifulSoup(zfc1,"html.parser")
    except:pass

