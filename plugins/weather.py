import requests
import ctrl
import configparser

def config_summon():
    config["Weather"] = {"weather_api_key": "获取到的key"}
    with open("/config.ini", "a") as f:
        config.write(f)
    print("初始化完成。")

config = configparser.ConfigParser()
config.read("config.ini")
if "Weather" not in config:
    config_summon()
    print("已生成天气插件配置文件, 请填写'config.ini'文件中'Weather'。获取key方法：未完待续")
else:
    key = config["Weather"]["weather_api_key"]

def handle(uid, msg, gid=0):
        if msg == "天气":
            msg = "天气查询:\n天气 now [地区] [上级行政区(可选)]\n测试中。。"
            if gid == 0:
                ctrl.send("p", uid, msg)
            else:
                ctrl.send("g", gid, msg)
        elif msg.split()[1] == "now":
            try:
                location = msg.split()[2]
            except IndexError:
                err = "传入参数错误，请检查格式是否正确。"
            try:
                adm = msg.split()[3]
                data = look_up(location, adm)
            except IndexError:
                data = look_up(location)
            data_id = data["id"]
            if data_id == 404:
                error(uid, gid, 404)
            elif data_id == 200:
                info = now(data["location_id"])
                msg = msg.split()[2] +" "+ data["adm1"] +" "+ data["adm2"] + "\n" + info
                if gid == 0:
                    ctrl.send("p", uid, msg)
                else:
                    ctrl.send("g", gid, msg)
            else:
                error(uid, gid, 901)

def look_up(location, adm= None):
    """
    查询location_id
    传入地方名与上级行政区（默认无）
    返回location_id与code
    """
    url = "https://geoapi.qweather.com/v2/city/lookup?"
    if adm == None:
        value = {"key": key, "location": location}
    else:
        value = {"key": key, "location": location, "adm": adm}
    r = requests.get(url, params= value)
    res = r.json()
    code = res["code"]
    if code == "404":
        return {"id": code}
    elif code == "200":
        location_id = res["location"][0]["id"]
        adm1 = res["location"][0]["adm1"]
        adm2 = res["location"][0]["country"]
        data = {"id": 200, "location_id": location_id, "adm1":adm1, "adm2":adm2}
        return data



def now(location_id):
    """以整合文本形式返回当前时间该地区天气"""
    url = "https://devapi.qweather.com/v7/weather/now?"
    value = {"key": key, "location": location_id}
    r = requests.get(url, params= value)
    res = r.json()
    code = int(res["code"])
    if code == 404:
        return code
    elif code == 200:
        now = res["now"]
        updatetime = now["obsTime"]
        info_link = res["fxLink"]
        temp = now["temp"]
        feels_temp = now["feelsLike"]
        weather_text = now["text"]
        wind_scale = now["windScale"]
        wind_dir = now["windDir"]
        wind_speed = now["windSpeed"]
        humidity = now["humidity"]
        msg = weather_text + "\n当前气温 " + temp + "℃\n体感温度 " + feels_temp + "℃\n" + wind_scale + "级 " + wind_dir + "\n风速 " + wind_speed + "km/h\n湿度 " + humidity +"％" + "\n详情:" + info_link
        return msg

def weather_3d(location_id):
    """返回该地区3天内天气"""
    pass

def weather_7d(location_id):
    """返回该地区7天内天气"""
    pass

def error(uid, gid, id, info=None):
    pass