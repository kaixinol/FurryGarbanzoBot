from urllib.request import Request, urlopen
import urllib
import html2text
import base64
import json
import random
def GetFurryJson(Tag: str,config: dict):
 base64string = base64.b64encode(bytes('%s:%s' % (config["username"], config["secret"]),'ascii'))
 url="https://e621.net/posts.json?tags=rating:s+"+Tag+"&limit="+str(config["limit"])
 print(url)
 headers = {'User-Agent': 'ZanksiBot/1.0 krawini'}
 request = Request(url, headers=headers)
 request.add_header("Authorization", "Basic %s" % base64string.decode('utf-8'))
 html = urlopen(request).read()
 return json.loads(html.decode("utf-8"))

def GetRandomFurryImg(config: dict,Tag: str):
 #try:
  buffer=GetFurryJson(Tag,config)["posts"]
  aBuffer=buffer[random.randint(0,len(buffer)-1)]
  return {'url':aBuffer["sample"]["url"],'sources':aBuffer["sources"],'id': aBuffer["id"]}
 #except:
  #return {'url':r"https://s1.ax1x.com/2022/07/23/jXR9D1.png",'sources':"None",'id': 114514}
