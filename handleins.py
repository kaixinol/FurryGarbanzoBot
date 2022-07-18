#from configparser import  Plugins.
import miraicle
from plugins.onlinecompile import Compile 

def handle_ins(ins: str,argv: list, bot: miraicle, group: int):

 match ins:
        case "在线编译":
       #  bot.send_group_msg(group, msg=[miraicle.Plain(Compile(argv[1],argv[0]))])
         print(Compile(argv[1],argv[0]))
        case "云黑":
         pass
        case "每日一题":
         pass
        case _:
         bot.send_group_msg(group, msg=[miraicle.Plain("未知指令："+ins)])