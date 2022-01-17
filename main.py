import requests

import plugins
import ctrl

return_group = 857326510 #主控群
bot_master = 2338196179
bot_id = 2604208757
ml_api_key = "e87328122b090688177aec4a875af31a"
ml_api_secret = "n70r5gbnfxsb"

def handle(msg):
    """处理消息"""
    try:
        if msg["post_type"] == "meta_event":
            pass
        elif msg["post_type"] == "notice":
            if "sub_type" in msg and msg["sub_type"] == "poke" and msg["target_id"] == bot_id: #对机器人发起的拍一拍
                if msg["sender_id"] == bot_id:
                    pass
                uid = msg["sender_id"]
                if "group_id" not in msg:
                    ctrl.send("p", uid, ctrl.poke(uid))
                else:
                    ctrl.send("g", msg["group_id"], ctrl.poke(uid))
                pass
            elif msg["notice_type"] == "client_status": #登录状态
                if msg["online"] == True:
                    online = "上线"
                else:
                    online = "下线"
                ctrl.send("p", bot_master, "您的机器人账户状态发生变化:\n类型：" + online + "\n详细信息:" + str(msg["client"]))
            else:
                ctrl.send("p", bot_master, "这是一个非文本消息：\n" + str(msg))
        elif msg["post_type"] == "message":
                if msg["message_type"] == "private":  #私聊消息
                    new_msg = msg["message"]
                    uid = msg["user_id"]
                    mid = msg["message_id"]
                    if msg["sub_type"] == "friend":
                        relation = 1
                    else:
                        relation = 0
                    if all_msg(uid, new_msg) == False:
                        private_msg(uid, new_msg)
                elif msg["message_type"] == "group":  #群消息
                    new_msg = msg["message"]
                    gid = msg["group_id"]
                    uid = msg["user_id"]
                    mid = msg["message_id"]
                    role = msg["sender"]["role"]
                    nickname = msg["sender"]["nickname"]
                    sex = msg["sender"]["sex"]
                    if all_msg(uid, new_msg, gid) == False:
                        group_msg(uid, new_msg, gid, nickname, sex)
        else:
            ctrl.send("p", bot_master, "无法判断的消息类型：\n" + msg)
    except Exception as error_log:
        print("有错误信息，已发送至机器管理员”")
        ctrl.send("p", bot_master, "错误：\n" + str(msg) + "\n\n错误信息:" + str(repr(error_log)))

def read_write(route, content):
    """读写文件"""
    pass


"""处理消息"""
def all_msg(uid, msg, gid = 0):
    """所有类型消息处理方法"""
    if "机器人" in msg:
        if gid == 0:
            ctrl.send("p", uid, "你是机器人吗？")
        else:
            ctrl.send("g", gid, "哪有机器人？")
    elif msg == "？" or msg == "?":
         if gid == 0:
            ctrl.send("p", uid, "咋了？")
         else:
            ctrl.send("g", gid, "？")
    elif msg == "/hot":
        plugins.bd_hot(uid, gid)
    else:
        return False

def group_msg(uid, msg, gid, nickname = None , sex = None):
    """处理群消息"""
    if msg[0] == "#":
        other_msg = msg[:0:-1]
        plugins.ml(other_msg, uid, gid, nickname)

def private_msg(uid, msg):
    """处理私聊消息"""
    if msg[:3] == "发消息":
        plugins.sudo_send_msg(uid, msg)
    else:
        plugins.ml(msg, uid)
