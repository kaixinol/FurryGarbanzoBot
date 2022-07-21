import miraicle
import random
import os
import json
def handle_ins(ins: str,argv: list, bot: miraicle, msg: miraicle.GroupMessage,config: dict,load_dict: dict):
 if load_dict.get(str(msg.group))==None or load_dict[str(msg.group)]==1:
  match ins:
        case "在线编译":
         try:
          from plugins.onlinecompile import Compile
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
          bot.send_group_msg(msg.group, msg=[miraicle.MiraiCode(info)])
        case "查云黑":
         from plugins.blacklist import IsBlacklisted
         bot.send_group_msg(msg.group, msg=[miraicle.Plain(IsBlacklisted(argv[0]))])
        case "每日一题":
         url="https://www.luogu.com.cn/problem/P"+str(random.randint(1000,8308))
         bot.send_group_msg(msg.group, msg=[miraicle.Plain(url)])
        case "警告":
         from plugins.warn import WarnMember
         if (bot.is_administrator(msg.sender,msg.group)==True or  config["Master"]==msg.sender) and len(msg.chain)==3:
          WarnMember(str(msg.group),str(msg.chain[1].qq),str(msg.sender),msg.chain[2].text)
         else:
          bot.send_group_msg(msg.group, msg=[miraicle.Plain("你没有权限或语法错误。")])
        case "查警告":
         from plugins.warn import NumberOfWarnings
         bot.send_group_msg(msg.group, msg=[miraicle.MiraiCode(NumberOfWarnings(str(msg.group),str(msg.chain[1].qq)))])
        case "冷更新":
         if config["Master"]==msg.sender:
          bot.send_group_msg(msg.group, msg=[miraicle.Plain("bot已经停止运作！")])
          os._exit(0)
        case _:
         bot.send_group_msg(msg.group, msg=[miraicle.Plain("未知指令："+ins)])
 else:
  bot.send_group_msg(msg.group, msg=[miraicle.Plain("主人已设置不响应")],quote=msg.id)