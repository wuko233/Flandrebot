import configparser
import sys
import ctrl

sys.path.append(sys.path[0] + "/plugins/")

config = configparser.ConfigParser()
config.read("config.ini")
main_group = int(config["User"]["main_group"])
bot_master = config["User"]["master"]
bot_id = int(config["User"]["bot_id"])
bot_name = config["User"]["bot_name"]

def menu(msg, gid):
    """菜单"""
    cd_msg = "菜单\n/hot\n/about\n原神签到菜单\n--------\n目前处于开发状态"
    ctrl.send("g", gid, cd_msg)

#QQ终端(测试)
def sudo(msg, uid, gid = 0):
    if uid == bot_master:
        if msg[1:5] == "发群消息":
            s = msg.split()
            sgid = (s[1])
            smsg = s[2]
            sudo_send_msg(sgid, smsg)
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

def weather_plugin(uid, msg, gid=0):
    try:
        import weather
        weather.handle(uid, msg, gid)
    except ModuleNotFoundError as error_log:
        print("未导入'weather'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'weather'\n\n错误信息:" + str(repr(error_log)))

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