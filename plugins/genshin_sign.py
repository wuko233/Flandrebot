import requests
import time
import json
import os
import ctrl


def sign_daily():
    sign_list = os.listdir("./plugins/d/genshin_sign")
    for uid in sign_list:
        sign = genshin_sign(uid)
        ctrl.send("p",uid, "定时签到任务成功，任务结果:\n" + sign)
        time.sleep(10)

def bind(uid, cookie_token, account_id):
    with open("./plugins/d/genshin_sign/" + str(uid), mode = "w") as f:
        data = {}
        data["cookie_token"] = cookie_token
        data["account_id"] = account_id
        json.dump(data, f)
    ctrl.send("p", uid, "绑定成功！\n" + cookie_token + "\n" + str(account_id))

def unbind(uid):
    try:
        os.remove("./plugins/d/genshin_sign/" + str(uid))
        print("解绑成功")
        ctrl.send("p", uid, "解绑成功")
    except FileNotFoundError:
        ctrl.send("p", uid, "解绑失败，请先发送'原神签到'进行绑定！")
    except Exception as error_log:
       print(str(error_log))
       ctrl.send("p", uid, "解绑失败，请联系开发者\n" + str(error_log))

def genshin_sign(uid):
    if os.path.isfile("./plugins/d/genshin_sign/" + str(uid)) is False:
        return 404
    else:
        with open("./plugins/d/genshin_sign/" + str(uid), "r") as f:
            data = json.load(f)
            cookie_token = data["cookie_token"]
            account_id = data["account_id"]
        cookies = {"account_id": account_id, "cookie_token": cookie_token}
        try:
            r1 =requests.post("https://hk4e-api-os.mihoyo.com/event/sol/sign?lang=zh-cn&act_id=e202102251931481", cookies = cookies).json()
            r = requests.get("https://hk4e-api-os.mihoyo.com/event/sol/info?lang=zh-cn&act_id=e202102251931481", cookies = cookies).json()
        except Exception as error_log:
            ctrl.send("p", uid, "签到失败，请联系开发者:\n" + str(error_log))
        if r["retcode"] == -100:
            msg = "登录状态异常，请检查信息是否正确！"
            return msg
        elif r1["retcode"] == 0:
            total_sign_day = r["data"]["total_sign_day"]
            today = r["data"]["today"]
            msg = str(today) + "\n旅行者，本日签到成功！\n本月累积签到:" + str(total_sign_day) + "天。"
            return msg
        elif r1["retcode"] == -5003:
            total_sign_day = r["data"]["total_sign_day"]
            today = r["data"]["today"]
            msg = today + "\n" + r1["message"] + "\n本月累积签到:" + str(total_sign_day) + "天。"
            return msg
        else:
            pass

def main(uid, msg):
    if os.path.isdir('./plugins/d/genshin_sign') is False:
        os.mkdir("./plugins/d/genshin_sign")
        print("创建目录成功")
    try:
        if msg == "原神签到":
            data = genshin_sign(uid)
            if data == 404:
                info = """您未绑定您的cookies与HOYOVERSE通行证号码！请发送
                        原神签到 绑定 [你的cookie_token] [你的MIHOYO通行id]
                        绑定即代表您同意我们使用您的cookies进行签到，我们承诺您的账号信息安全！
                        获取cookie_token方法：未完待续"""
                ctrl.send("p", uid, info)
            else:
                ctrl.send("p", uid, data)
        elif msg.split()[1] == "绑定":
            bind(uid, msg.split()[2], msg.split()[3])
        elif msg.split()[1] == "解绑":
            unbind(uid)
        elif msg.split()[1] == "测试":
            sign_daily()
        else:
            ctrl.send("p", uid, "GS_SIGN:\n\n所有命令:\n原神签到\n原神签到 绑定 [cookies] [HYV通行证]\n原神签到 解绑")
    except IndexError:
        ctrl.send("p", uid, "入参错误！请检查您发送的命令是否多或少参数!")