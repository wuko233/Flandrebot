# Flandre bot

** 因腾讯风控，环境不可用，停止更新。 **

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/9be0bc5b84414df382bad502adaa8087)](https://www.codacy.com/gh/wuko233/Flandrebot/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=wuko233/Flandrebot&amp;utm_campaign=Badge_Grade)

## 关于

对接go-cqhttp，使用python编写。

本人第一次编写项目，有很多不足之处，还请海涵。

跪求提issue，一个人想不到太多。

仅用作个人学习

功能列表:

1. 基本Event处理 （未完全）

2. ~~ 使用茉莉bot的聊天功能 ~~ (换接口了，正在重写)

3. Genshin Impact签到功能

4. 百度热搜功能

5. 定时任务(实验中)

6. 天气查询(未完成)

## 如何使用

### 0，环境配置

`Python3以及所需第三方包`

### 1，克隆本项目至您的设备

`git clone 本项目地址`

### 2，编辑配置文件`config.ini`

先运行 start.py

之后编辑配置文件

`vim config.ini`

### 3，运行`start.py`

`python start.py`

## 第三方库

requests

schedule

beautifulsoups

configparser

待续

## 第三方服务列表

待续

## Q&A

**Q:如何停用不想要的功能？**

A:删除或修改目录`plugins`下相关功能文件

**Q:报错:`ModuleNotFoundError: No module named 'XXX'`**

A:使用`pip install 相关模块`即可（请先确保您已安装pip）

...

