import ctrl
import requests

from bs4 import BeautifulSoup
import sys

sys.path.append(sys.path[0] + "/plugins/")
return_group = 857326510 #主控群
bot_master = 2338196179
bot_id = 2604208757

def keyword(msg, uid, gid = 0):
    if msg[:4] == "发群消息" and uid == bot_master:
        s = msg.split()
        sgid = (s[1])
        smsg = s[2]
        sudo_send_gmsg(sgid, smsg)
    elif msg == "菜单":
        cd(msg, gid)
    elif msg[0] == "#":
        other_msg = msg[1:]
        ml(other_msg, uid, gid)
    

def cd(msg, gid):
    """菜单"""
    cd_msg = "菜单\n/hot\n/about"
    if gid == 0:
        pass
    else:
        ctrl.send("g", gid, cd_msg)

"""QQ终端（测试）"""
def sudo_send_msg(uid, msg):
    """主动发送消息"""
    if uid in bot_master:
        new_msg = str(msg[4:]).split(" ")
        send_type = new_msg[0]
        if send_type == "g" or send_type == "G" or send_type == "群" or send_type == "群聊":
            msg_type = "g"
        elif send_type == "p" or send_type == "P" or send_type == "私" or send_type == "私聊":
            msg_type = "p"
        else:
            print("err:消息类型错误")
            ctrl.send("p", uid, "消息类型错误")
            return
        ctrl.send(msg_type, new_msg[1], new_msg[2])
        ctrl.send("p", uid, "发送消息成功")
    else:
        print("err:权限不足")
        ctrl.send("p", uid, "权限不足")

"""调用第三方接口"""

def ml(msg, uid, gid = 0, nickname = None):
    """调用茉莉机器人聊天接口"""
    ml_api_key = "e87328122b090688177aec4a875af31a"
    ml_api_secret = "n70r5gbnfxsb"
    url = "http://i.itpk.cn/api.php?api_key=" + ml_api_key + "&api_secret=" + ml_api_secret + "&question=" + msg
    r = requests.get(url)
    new_msg = r.text
    if gid == 0:
        remsg = new_msg.replace("[user_name]", "你")
        ctrl.send("p", uid, remsg)
    else:
        remsg = ctrl.at(uid, nickname) + new_msg.replace("[user_name]", "你")
        ctrl.send("g", gid, remsg)

def bd_hot(uid, gid = 0):
    try:
        import bd_hot_list
        if gid == 0:
            ctrl.send("p", uid, bd_hot_list.show())
        else:
            ctrl.send("g", gid, bd_hot_list.show())
    except ModuleNotFoundError as error_log:
        print("未导入'bd_hot_list'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'bd_hot_list'\n\n错误信息:" + str(repr(error_log)))
   
        