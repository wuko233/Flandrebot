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
            uid = msg["user_id"]
            mid = msg["message_id"]
            seq = msg["message_seq"]
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
                    all_msg(uid, new_msg, gid)
                    group_msg(uid, new_msg, gid)
        else:
            ctrl.send("g", return_group, "无法判断的消息类型：\n" + msg)
    except KeyError:
        print("有错误信息，已记录至“log.txt”")
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
        ml(other_msg, uid, gid)

def private_msg(uid, msg):
    """处理私聊消息"""
    ml(msg, uid)

"""QQ终端（测试）"""
def sudo_send_msg(type, msg, id):
    """主动发送消息"""
    pass

"""调用第三方接口"""
def ml(msg, uid, gid = 0):
    """调用茉莉机器人聊天接口"""
    url = "http://i.itpk.cn/api.php?api_key=" + ml_api_key + "&api_secret=" + ml_api_secret + "&question=" + msg
    r = requests.get(url)
    new_msg = r.text
    remsg = new_msg.replace("[user_name]", "你")
    if gid == 0:
        ctrl.send("p", uid, remsg)
    else:
        ctrl.send("g", gid, remsg)

