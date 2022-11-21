import configparser
from flask import Flask, request
import main


def config_summon():
    config["Sys_setting"] = {"get_host": "替换为http服务器的地址",
                         "get_port": "替换为http服务器的端口",
                         "post_host": "替换为go-cqhttp地址",
                         "post_port": "替换为go-cqhttp端口",
                         "debug": "False"}
    config["User"] = {"bot_id": "机器人的QQ号",
                   "bot_name": "机器人昵称",
                   "master": "主人QQ",
                   "main_group": "主群号码"}
    with open("config.ini", "a") as f:
        config.write(f)
    print("初始化完成。")

config = configparser.ConfigParser()
config.read("config.ini")
if "Sys_setting" not in config:
    config_summon()
    print("已生成配置文件, 请填写'config.ini'文件。")
    exit()
else:
    get_host = config["Sys_setting"]["get_host"]
    get_port = int(config["Sys_setting"]["get_port"])
    debug_mode = config["Sys_setting"]["debug"]

app = Flask(__name__)
@app.route('/', methods = ['post'])
def post():
    t = request.get_json()
    main.process_msg(t)
    return 'OK'

app.run(host = get_host, port = get_port, debug = debug_mode)