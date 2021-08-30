import requests
import ctrl

return_group = 12345 #主控群号
bot_master = [123456789, 987654321] #机器人主人
ml_api_key = "" #茉莉机器人apikey
ml_api_secret = "" #茉莉机器人apisecret

def handle(msg):
    """处理消息"""
    try:
        if msg["post_type"] == "meta_event":
            pass
        elif msg["post_type"] == "notice":
            ctrl.send("g", return_group, "这是一个非文本消息：\n" + str(msg))
            if msg["sub_type"] == "poke" and msg["target_id"] == msg["self_id"]:
                uid = msg["sender_id"]
                if msg["group_id"] == None:
                    ctrl.send("p", uid, ctrl.poke(uid) + "hi")
                else:
                    ctrl.send("g", msg["group_id"], ctrl.poke(uid))
        elif msg["post_type"] == "message":
                if msg["message_type"] == "private":  #私聊消息
                    new_msg = msg["message"]
                    uid = msg["user_id"]
                    mid = msg["message_id"]
                    if msg["sub_type"] == "friend":
                        relation = 1
                    else:
                        relation = 0
                    all_msg(uid, new_msg)
                    private_msg(uid, new_msg)
                elif msg["message_type"] == "group":  #群消息
                    new_msg = msg["message"]
                    gid = msg["group_id"]
                    uid = msg["user_id"]
                    mid = msg["message_id"]
                    role = msg["sender"]["role"]
                    nickname = msg["sender"]["nickname"]
                    sex = msg["sender"]["sex"]
                    all_msg(uid, new_msg, gid)
                    group_msg(uid, new_msg, gid, nickname, sex)
        else:
            ctrl.send("g", return_group, "无法判断的消息类型：\n" + msg)
    except KeyError:
        print("有错误信息，已发送至调试群聊”")
        ctrl.send("g", return_group, "错误：\n" + str(msg))

def read_write(route, content):
    """读写文件"""
    pass


"""处理消息"""
def all_msg(uid, msg, gid = 0):
    """所有类型消息处理方法"""
    if msg[:3] == "发消息":
        pass
    elif "机器人" in msg:
        if gid == 0:
            ctrl.send("p", uid, "你是机器人吗？")
        else:
            ctrl.send("g", gid, "哪有机器人？")
    elif msg == "？" or msg == "?":
         if gid == 0:
            ctrl.send("p", uid, "咋了？")
         else:
            ctrl.send("g", gid, "？")

def group_msg(uid, msg, gid):
    """处理群消息"""
    if msg[0] == "#":
        other_msg = msg[:0:-1]
        api.ml(other_msg, uid, gid)

def private_msg(uid, msg):
    """处理私聊消息"""
    api.ml(msg, uid， nickname)

