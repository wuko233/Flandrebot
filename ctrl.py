import requests
import configparser

config = configparser.ConfigParser()
config.read("config.ini")
post_host = config["Sys_setting"]["post_host"]
post_host = post_host + ":" + (config["Sys_setting"]["post_port"])

#go-cqhttp自带接口
def send(msg_type, id, msg, auto_escape=False):
    """
    发送消息
    msg_type为g(group群聊)或p(private私聊) id msg
    auto_escape为是否使用CQ码
    """
    umsg = str(msg)
    uid = int(id)
    if msg_type == "p":
        k_v = {"user_id" : uid, "message" : umsg}
        r = requests.get("http://" + post_host + "/send_private_msg", params = k_v)
        print(r.url)
        print(r)
    elif msg_type == "g":
        k_v = {"group_id" : uid, "message" : umsg}
        r = requests.get("http://" + post_host + "/send_group_msg", params = k_v)
        print(r.url)
        print(r)

def send_image(file):
    pass

def at(qq, nickname = None):
    """
    at接口
    返回CQ码
    """
    at = "[CQ:at,qq=" + str(qq) + ",name=" + str(nickname) + "]"
    return at

def poke(qq):
    """
    戳一戳接口
    返回CQ码
    """
    poke = "[CQ:poke,qq=" + str(qq) + "]"
    return poke

def reply(text, uid, time, sqe):
    """
    回复接口
    seq即message_seq
    time Unix时间
    返回CQ码
    """
    reply = "[CQ:reply,text=" + text + ",qq=" + uid + ",time=" + time + ",sqe=" + sqe + "]"
    return reply

