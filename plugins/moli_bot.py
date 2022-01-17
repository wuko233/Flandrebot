
def moli():    
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