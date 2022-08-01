from urllib.request import Request, urlopen
import urllib
import json
import random


def GetVideoJson(id: str, link: str):
    url = link + id
    print(url)
    headers = {"User-Agent": "ZanksiBot/1.0 FurryGarbanzoBot"}
    request = Request(url, headers=headers)
    html = urlopen(request).read()
    return json.loads(html.decode("utf-8"))


def GetRanDomVideo(config: dict):
    buffer = GetVideoJson(
        config["fav_id"], "https://api.bilibili.com/x/v3/fav/resource/ids?media_id="
    )["data"]
    buffer2 = GetVideoJson(
        buffer[random.randint(0, len(buffer) - 1)]["bvid"],
        "https://api.bilibili.com/x/web-interface/view?bvid=",
    )["data"]
    return (
        "UP主："
        + buffer2["owner"]["name"]
        + "\n"
        + "Title:"
        + buffer2["title"]
        + "\n"
        + "https://www.bilibili.com/video/"
        + buffer2["bvid"]
    )
