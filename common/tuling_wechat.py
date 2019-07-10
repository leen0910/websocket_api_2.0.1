import itchat
import requests
def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key': '440c26f6ed9f4ad8ac55dd529a35ef19',  # Tuling Key,替换为你自己的
        'info': msg,  # 这是我们发出去的消息
        'userid': 'test1234',  # 这里你想改什么都可以
    }
    # 我们通过如下命令发送一个 post 请求
    r = requests.post(apiUrl, data=data).json()
    return r.get('text')
@itchat.msg_register(itchat.content.TEXT)
def print_content(msg):
    return get_response(msg['Text'])
# @itchat.msg_register([itchat.content.TEXT], isGroupChat=True)
# def print_content(msg):
#     return get_response(msg['Text'])
itchat.auto_login(True)
itchat.run()


# # -*- coding:utf-8 -*-
#
# from wxpy import *
#
# # 实例化，并登录微信
# bot = Bot(cache_path=True)
# # 图灵机器人的apikey
# api_key='440c26f6ed9f4ad8ac55dd529a35ef19' #
#
# '''
# 1. 好友统计信息
# '''
# # 获取好友信息
# bot.chats()
#
# # 获取好友的统计信息
# Friends = bot.friends()
# print(Friends.stats_text())
#
# '''
# 2. 使用图灵机器人自动与指定好友聊天
# '''
# # my_friend = ensure_one(bot.search(u'最是一年春好色'))  # 想和机器人聊天的好友的备注
# # tuling = Tuling(api_key)
# #
# # @bot.register(my_friend)  # 使用图灵机器人自动与指定好友聊天
# # def reply_my_friend(msg):
# #     tuling.do_reply(msg)
# # embed()
#
# '''
# 3. 使用图灵机器人自动在指定群聊天 要保存在通讯录里的才行
# '''
# # my_group = bot.groups().search(u'群组名')[0]  # 记得把名字改成想用机器人的群
# # tuling = Tuling(api_key)
# # print(my_group)
# # @bot.register(my_group, except_self=False)  # 使用图灵机器人自动在指定群聊天
# # def reply_my_group(msg):
# #     print(tuling.do_reply(msg))
# # embed()
#
# '''
# 4. 使用图灵机器人 回复所有微信群或好友的信息 慎用
# '''
# tuling = Tuling(api_key)
#
# @bot.register()
# def auto_reply(msg):
#     tuling.do_reply(msg)
#
# embed()
