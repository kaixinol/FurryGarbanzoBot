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
          from plugins.banwords import BanWord
          raw_info=Compile(argv[1],argv[0],config["plugin"]["OnlineCompile"])
          info=""
          for index in range(len(raw_info)):
           info+=raw_info[index]
          info=info[:256]
          if info.count('\n')>8:
           info="请勿滥用本bot恶意刷屏"
         except Exception as e:
          info=str(e)
         finally:
          bot.send_group_msg(msg.group, msg=[miraicle.MiraiCode(BanWord(info))])
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
        case "LIST":
         output=""
         buffer=bot.group_list()
         for i in range(0,len(buffer["data"])):
          output+=buffer["data"][i]["name"]+"("+str(buffer["data"][i]["id"])+")"
          output+='\t'
          output+=buffer["data"][i]["permission"]
          output+='\n'
         bot.send_group_msg(msg.group, msg=[miraicle.Plain(output)])
        case "来只兽":
         from plugins.randomfurryimg import GetRandomFurryImg
         if len(argv)==0:
          dataSet=GetRandomFurryImg(config["plugin"]["E621"],"changed_(video_game)")
          bot.send_group_msg(msg.group, msg=[miraicle.Image(
                                                            url=dataSet["url"]),
                                                            miraicle.Plain("sources:"+json.dumps(dataSet["sources"])+"\nid:"+str(dataSet["id"])
                                                            )])
         else:
          dataSet=GetRandomFurryImg(config["plugin"]["E621"],'+'.join(argv))
          bot.send_group_msg(msg.group, msg=[miraicle.Image(
                                                            url=dataSet["url"]),
                                                            miraicle.Plain("sources:"+json.dumps(dataSet["sources"])+"\nid:"+str(dataSet["id"]
                                                            ))])
        case "来个meme":
          from plugins.randomvideo import GetRanDomVideo
          if len(argv)==0:
           buffer=GetRanDomVideo(config["plugin"]["randomvideo"])
          else:
           buffer=GetRanDomVideo({"fav_id": argv[0]})
          bot.send_group_msg(msg.group, msg=[miraicle.Plain(buffer)])
        case "设定上传":
         pass
        case "设定":
          #from plugins.fursonahandle import RetSomebodyFursonaProfile
          #print(RetSomebodyFursonaProfile(argv[0])["img"])
          #bot.send_group_msg(msg.group, msg=[miraicle.Image(url=RetSomebodyFursonaProfile(argv[0])["img"])])
          pass
        case "我的全部崽子":
          #from plugins.fursonahandle import RetMyAllFursonaProfile
          #bot.send_group_msg(msg.group, msg=[miraicle.Plain(RetMyAllFursonaProfile(msg.sender))])
          pass
        case _:
         bot.send_group_msg(msg.group, msg=[miraicle.Plain("未知指令："+ins)])
 else:
  bot.send_group_msg(msg.group, msg=[miraicle.Plain("主人已设置不响应")],quote=msg.id)