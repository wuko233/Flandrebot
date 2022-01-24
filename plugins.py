import sys
import json

import ctrl

sys.path.append(sys.path[0] + "/plugins/")
with open("./config.json")as config:
    config_data = json.load(config)
    main_group = config_data["user_data"]["control_groupid"]
    bot_master = config_data["user_data"]["bot_masterid"]
    bot_id = config_data["user_data"]["bot_id"]

def keyword(msg, uid, gid = 0):
    if msg == "菜单":
        cd(msg, gid)
    elif msg[0] == "#":
        other_msg = msg[1:]
        ml(other_msg, uid, gid)
    

def cd(msg, gid):
    """菜单"""
    cd_msg = "菜单\n/hot\n/about"
    if gid == 0:
        pass
    else:
        ctrl.send("g", gid, cd_msg)

"""调用第三方接口"""

def ml(msg, uid, gid = 0, nickname = None):
    """调用茉莉机器人聊天接口"""
    try:
        import moli_bot
        moli_bot.moli(msg, uid, gid = 0, nickname = None)
    except ModuleNotFoundError as error_log:
        print("未导入'bd_hot_list'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'bd_hot_list'\n\n错误信息:" + str(repr(error_log)))

def bd_hot(uid, gid = 0):
    try:
        import bd_hot_list
        if gid == 0:
            ctrl.send("p", uid, bd_hot_list.show())
        else:
            ctrl.send("g", gid, bd_hot_list.show())
    except ModuleNotFoundError as error_log:
        print("未导入'bd_hot_list'")
        print(sys.path)
        ctrl.send("p", bot_master, "错误：\n未导入'bd_hot_list'\n\n错误信息:" + str(repr(error_log)))
   
        