#from configparser import  Plugins.
import miraicle
import random
import os
from plugins.onlinecompile import Compile 

def handle_ins(ins: str,argv: list, bot: miraicle, msg: miraicle.GroupMessage,config: dict):

 match ins:
        case "在线编译":
         try:
          raw_info=Compile(argv[1],argv[0],config)
          info=""
          for index in range(len(raw_info)):
           info+=raw_info[index]
          info=info[:256]
          if info.count('\n')>8:
           info="请勿滥用本bot恶意刷屏"
         except Exception as e:
          info=str(e)
         finally:
          bot.send_group_msg(msg.group, msg=[miraicle.Plain(info)])
         #print(Compile(argv[1],argv[0]))
        case "云黑":
         pass
        case "每日一题":
         url="https://www.luogu.com.cn/problem/P"+str(random.randint(1000,8308))
         bot.send_group_msg(msg.group, msg=[miraicle.Plain(url)])
        case "停用bot":
         if bot.is_administrator(msg.sender,msg.group)==True or config["plugin"]["Master"]==3607922630:
          bot.send_group_msg(msg.group, msg=[miraicle.Plain("bot已经停止运作！")])
          os._exit(233)
        case _:
         bot.send_group_msg(msg.group, msg=[miraicle.Plain("未知指令："+ins)])