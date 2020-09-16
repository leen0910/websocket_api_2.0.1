#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """2. 控制器接收文件"""
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            self.ws=create_connection(url,timeout=10)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    # def test01_file_receive_script(self):
    #     """2. 控制器接收文件/发送文件类型：script"""
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_receive=rm.get_data("控制器接收文件","file_receive_script")
    #     print("step 2、向设备写入脚本文件test.lua。")
    #     t=c.checkAction(url,data_file_receive)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)

    def test02_file_receive_config(self):
        """2. 控制器接收文件/发送文件类型：config"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_receive=rm.get_data("控制器接收文件","file_receive_config")
        print("step 2、向设备写入配置文件permission.json。")
        t=c.checkAction(url,data_file_receive)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    def test03_file_receive_update(self):
        """2. 控制器接收文件/发送文件类型：update"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_receive=rm.get_data("控制器接收文件","file_receive_update")
        print("step 2、向设备写入升级文件test.reb。")
        t=c.checkAction(url,data_file_receive)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
