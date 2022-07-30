import miraicle
import random
import os
import json
import emoji
import base64
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
          from plugins.fursonahandle import AddFursona
          from plugins.fursonahandle import SaveImg
          from plugins.fursonahandle import RetSomebodyFursonaProfile
          if RetSomebodyFursonaProfile(argv[0])==None or RetSomebodyFursonaProfile(argv[0])["Owner"]==msg.sender:
           if len(msg.chain)==3 and AddFursona(argv[0],
                                                     msg.sender,argv[1],
                                                     SaveImg(msg.chain[1].url,argv[0],msg.chain[1].image_id))!=True:
             bot.send_group_msg(msg.group, msg=[miraicle.Plain("发生错误")])
           if len(msg.chain)==1 and AddFursona(argv[0],msg.sender,argv[1],None)!=True:
             bot.send_group_msg(msg.group, msg=[miraicle.Plain("发生错误")])
           if len(msg.chain)==2 and AddFursona(argv[0],msg.sender,None,SaveImg(msg.chain[1].url,argv[0],msg.chain[1].image_id))!=True:
            bot.send_group_msg(msg.group, msg=[miraicle.Plain("发生错误")])
          else:
           bot.send_group_msg(msg.group, msg=[miraicle.Plain("你没有权限。")])
        case "设定":
          from plugins.fursonahandle import RetSomebodyFursonaProfile
          if len(argv)==0:
           root = r"./plugins/database/"
           files_list = os.listdir(root)
           filter_files_list = [fn for fn in files_list if fn.endswith("json")]
           files_list = [os.path.join(root,fn) for fn in files_list]
           argv.append(base64.b64decode(os.path.basename(files_list[random.randint(0,len(files_list)-1)]).split('.')[0]).decode())
           print(argv[0])
          data=RetSomebodyFursonaProfile(argv[0])
          if data==None:
            bot.send_group_msg(msg.group, msg=[miraicle.Plain("没有叫%s的兽兽！"%argv[0])])
            return
          master=miraicle.Plain(emoji.emojize("\n[主人::paw_prints:%s:paw_prints:]"%data["Owner"]))
          cub=miraicle.Plain(emoji.emojize(":star:%s:star:\n"%argv[0]))
          if data["Img"]==None:
           output=[cub,miraicle.Plain(data["Desc"]),master]
          elif data["Desc"]==None:
           output=[cub,miraicle.Image.from_url(r"file:///%s/plugins/database/%s"%(os.getcwd(),data["Img"])),master]
          else:
           output=[cub,miraicle.Plain(data["Desc"]),miraicle.Image.from_url(r"file:///%s/plugins/database/%s"%(os.getcwd(),data["Img"])),master]
          bot.send_group_msg(msg.group, msg=output)
        case _:
         bot.send_group_msg(msg.group, msg=[miraicle.Plain("未知指令："+ins)])
 else:
  bot.send_group_msg(msg.group, msg=[miraicle.Plain("主人已设置不响应")],quote=msg.id)
