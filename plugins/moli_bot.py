import requests
import ctrl

ml_api_key = ""
ml_api_secret = ""


def moli(msg, uid, gid = 0, nickname = None):    
    url = "http://i.itpk.cn/api.php?api_key=" + ml_api_key + "&api_secret=" + ml_api_secret + "&question=" + msg
    r = requests.get(url)
    new_msg = r.text
    if gid == 0:
        remsg = new_msg.replace("[user_name]", "你")
        ctrl.send("p", uid, remsg)
    else:
        remsg = ctrl.at(uid, nickname) + new_msg.replace("[user_name]", "你")
        ctrl.send("g", gid, remsg)
    return 200