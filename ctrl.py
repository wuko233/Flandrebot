import requests
import json

with open("./config.json")as config:
    config_data = json.load(config)
    post_host = config_data["post_address"]["host"] + ":" + config_data["post_address"]["port"]



"""go-cqhttp自带接口"""
def send(type, id, msg, auto_escape=False):
    """
    发送消息
    type为g(group群聊)或p(private私聊) id msg
    auto_escape为是否使用CQ码
    """
    umsg = str(msg)
    uid = int(id)
    if type == "p":
        k_v = {"user_id" : uid, "message" : umsg}
        r = requests.get("http://" + post_host + "/send_private_msg", params = k_v)
        print(r.url)
        print(r)
    elif type == "g":
        k_v = {"group_id" : uid, "message" : umsg}
        r = requests.get("http://" + post_host + "/send_group_msg", params = k_v)
        print(r.url)
        print(r)

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

