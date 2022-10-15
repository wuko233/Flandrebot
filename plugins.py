import sys
import json
import ctrl

sys.path.append(sys.path[0] + "/plugins/")

import bot_schedule

with open("./config.json")as config:
    config_data = json.load(config)
    main_group = config_data["user_data"]["control_groupid"]
    bot_master = config_data["user_data"]["bot_masterid"]
    bot_id = config_data["user_data"]["bot_id"]

def menu(msg, gid):
    """菜单"""
    cd_msg = "菜单\n/hot\n/about\n原神签到菜单\n--------\n目前处于开发状态"
    ctrl.send("g", gid, cd_msg)

"""QQ终端（测试）"""
def sudo(msg, uid, gid = 0):
    if uid == bot_master:
        if msg[1:5] == "发群消息":
            s = msg.split()
            sgid = (s[1])
            smsg = s[2]
            sudo_send_gmsg(sgid, smsg)
    else:
        pass


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

def genshin_sign(uid, msg):
    try:
        import genshin_sign
        genshin_sign.main(uid, msg)
    except ModuleNotFoundError as error_log:
        print("未导入'genshin_sign'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'genshin_sign'\n\n错误信息:" + str(repr(error_log)))


def ml(msg, uid, gid = 0, nickname = None):
    """调用茉莉机器人聊天接口"""
    try:
        import moli_bot
        moli_bot.moli(msg, uid, gid = 0, nickname = None)
    except ModuleNotFoundError as error_log:
        print("未导入'moli_bot'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'moli_bot'\n\n错误信息:" + str(repr(error_log)))

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
   
        