#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import Base_64
from common import WR_file
import time
import json




class websocket_request(unittest.TestCase):
    """文件管理/1. 控制器发送文件"""
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            self.ws=create_connection(url,timeout=5)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    def test01_ScriptFile_send(self):
        """1. 控制器发送文件/脚本文件/读取一个脚本文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_send=rm.get_data("控制器发送文件","file_send_script")
        print("step 2、从设备读取脚本文件tutorial.lua：")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)

        print("step 3、解码后保存到files目录。")
        str=t["data"]["value"]
        file_content=Base_64.decode(str)
        path='../files/tutorial.lua'
        WR_file.WriteFile(path,file_content)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test02_ConfigFile_send(self):
        """1. 控制器发送文件/配置文件/读取一个配置文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_send=rm.get_data("控制器发送文件","file_send_config")
        print("step 2、从设备读取配置文件：lua.json ")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)

        print("step 3、解码后保存到files目录。")
        str=t["data"]["value"]
        file_content=Base_64.decode(str)
        path='../files/lua.json'
        WR_file.WriteFile(path,file_content)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    # def test03_LogFile_send(self):
    #     """1. 控制器发送文件/日志文件/读取一个日志文件 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_send=rm.get_data("控制器发送文件","file_send_log")
    #     print("step 2、从设备读取配置文件：test.log ")
    #     t=c.checkAction(url,data_file_send)
    #     time.sleep(1)
    #     self.assertEqual(t["success"],True)
    #
    #     print("step 3、解码后保存到files目录。")
    #     str=t["data"]["value"]
    #     file_content=Base_64.decode(str)
    #     path='../files/test.log'
    #     WR_file.WriteFile(path,file_content)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 4、释放设备：")
    #     c.checkAction(url,data_logout)

    def test04_ConfigFile_send_all(self):
        """1. 控制器发送文件/配置文件/读取所有配置文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取config目录下所有配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='../files/ConfigFile_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置安装文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_config")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取config文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s config文件读取成功。"%f_name)

            str=t["data"]["value"]
            file_content=Base_64.decode(str)
            path='../files/'+f_name
            WR_file.WriteFile(path,file_content)
            print("%s config文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)



    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
