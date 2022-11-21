import requests
import configparser
import ctrl

config = configparser.ConfigParser()

def config_summon():
    config["Moli_bot"] = {}
    config["Moli_bot"] = {"key": "你申请到的key", "secret": "你申请到的secret"}
    with open("config.ini", "w") as f:
        config.write(f)
    print("配置初始化完成。")


def start():
    config.read("config.ini")
    if "Moli_bot" not in config:
        config_summon()
        print("[moli_bot]已生成配置文件, 请填写'config.ini'文件。")
        exit()
        return 100
    else:
        return 200

def moli(msg, uid, gid = 0, nickname = None):
    code = start()
    if code == 200:
        ml_api_key = config["Moli_bot"]["key"]
        ml_api_secret = config["Moli_bot"]["secret"]
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