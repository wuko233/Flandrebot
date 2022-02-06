import requests
import json
import os
import ctrl

def __init__():
    if os.path.isdir('d') == False:
        os.mkdir("d")

def bind(uid, cookie_token, account_id):
    with open("./plugins/d/" + str(uid) + "_genshin_sign", mode = "w") as f:
        data = {}
        data["cookie_token"] = cookie_token
        data["account_id"] = account_id
        json.dump(data, f)
    ctrl.send("p", uid, "绑定成功！\n" + cookie_token + "\n" + str(account_id))

def genshin_sign(uid):
    """str格式"""
    if os.path.isfile("./plugins/d/" + str(uid) + "_genshin_sign") == False:
        return 404
    else:
        with open("./plugins/d/" + str(uid) + "_genshin_sign", "r") as f:
            data = json.load(f)
            cookie_token = data["cookie_token"]
            account_id = data["account_id"]
        cookies = {"account_id": account_id, "cookie_token": cookie_token}
        r1 =requests.post("https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=zh-cn&act_id=e202102251931481", cookies = cookies).json()
        r = requests.get("https://hk4e-api-os.mihoyo.com/event/sol/info?lang=zh-cn&act_id=e202102251931481", cookies = cookies).json()
        if r["retcode"] == -100:
            msg = "登录状态异常，请检查信息是否正确！"
            return msg
        elif r1["retcode"] == 0:
            total_sign_day = r["data"]["total_sign_day"]
            today = r["data"]["today"]
            msg = str(today) + "\n旅行者，本日签到成功！\n本月累积签到:" + str(total_sign_day) + "天。"
            return msg
        elif r1["retcode"] == -100:
            msg = "登录状态异常，请检查信息是否正确！"
            return msg
        elif r1["retcode"] == -5003:
            total_sign_day = r["data"]["total_sign_day"]
            today = r["data"]["today"]
            msg = today + "\n" + r1["message"] + "\n本月累积签到:" + str(total_sign_day) + "天。"
            return msg

def main(uid, msg):
    if msg == "原神签到":
        d = genshin_sign(uid)
        if d == 404:
            ctrl.send("p", uid, "您未绑定您的cookies与MIHOYO通行证号码！请发送\n原神签到 绑定 [你的cookie_token] [你的MIHOYO通行id]\n绑定即代表您同意我们使用您的cookies进行签到，我们承诺您的账号信息安全！\n获取cookie_token方法：未完待续")
        else:
            ctrl.send("p", uid, d)
    elif msg.split()[1] == "绑定":  
        bind(uid, msg.split()[2], msg.split()[3])
    else:
        ctrl.send("p", uid, "无法识别的命令:" + msg)