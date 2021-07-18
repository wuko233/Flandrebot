import requests

server_address = "http://192.168.0.100:5700/" #临时，未来放入配置文件
"""go-cqhttp自带接口"""
def send(type, id, msg, auto_escape=False):
    """
    发送消息
    type g(group群聊)或p(private私聊) id msg
    auto_escape为是否使用CQ码
    """
    umsg = str(msg)
    uid = int(id)
    if type == "p":
        k_v = {
        "user_id" : uid,
        "message" : umsg
        }
        r = requests.get(server_address + "send_private_msg", params = k_v)
        print(r.url)
        print(r)
    elif type == "g":
        k_v = {
        "group_id" : uid,
        "message" : umsg
        }
        r = requests.get(server_address + "send_group_msg", params = k_v)
        print(r.url)
        print(r)

def at(qq, name = None):
    """
    at接口
    返回CQ码
    """
    at = "[CQ:at,qq=" + str(qq) + ",name=" + name + "]"
    return at

def reply(text, uid, time, sqe):
    """
    回复接口
    seq即message_seq
    time Unix时间
    返回CQ码
    """
    reply = "[CQ:reply,text=" + text + ",qq=" + uid + ",time=" + time + ",sqe=" + sqe + "]"

