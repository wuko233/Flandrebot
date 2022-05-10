#请使用[nonebot](https://github.com/nonebot/nonebot2)

(22.5.10:今天才发现自己在发明轮子…本来打算直接归档这个仓库，不过发现过去的这几个月通过编写这个项目学到了不少东西，所以就决定继续完善啦，当做一次学习的机会)

# Toby bot

## 关于

对接go-cqhttp，使用python编写。

本人第一次编写项目，有很多不足之处，还请包容，欢迎提issue；如果您觉得还可以的话，可以给我一个star，您的支持是我前进的最大动力；如果您想要完善本项目，欢迎提交您的代码，谢谢！

功能列表:

1. 基本Event处理 （未完全）

2. 使用茉莉bot的聊天功能

3. Genshin Impact签到功能

4. 百度热搜功能

## 如何使用

### 0，环境配置

`Python3以及所需第三方包`

### 1，克隆本项目至您的设备

`git clone 本项目地址`

### 2，编辑配置文件`config.json`

`vim config.json`

### 3，运行`start.py`

`python start.py`

## config文件说明

`post_address`:向go-cqhttp发送数据的地址（go-cqhttp接受post的地址）

`get_address`:go-cqhttp发送数据到的地址（接受go-cqhttp的Event的地址）

`user_data`:用户数据

`control_groupid`:用来测试bot的群聊群号

`bot_masterid`:机器人主人QQ（用于接受bot错误信息）

`bot_id`:机器人QQ

## 第三方库

待续

## 第三方服务列表

待续

## Q&A

**Q:如何停用不想要的功能？**

A:删除或修改目录`plugins`下相关功能文件

**Q:报错:`ModuleNotFoundError: No module named 'XXX'`**

A:使用`pip install 相关模块`即可（请先确保您已安装pip）

...

