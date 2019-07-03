#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """6. 捕获设备信息 """
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

    def test01_info(self):
        """1、无需登录直接捕获。 """
        rm=read_message.ReadMessage()
        data=rm.get_data("捕获设备信息","info")   # 获取device.info.read命令发送数据包。
        ws=self.ws
        print("发送“查询设备信息”数据。")
        t=c.checkAction(ws,data)
        self.assertEqual(t["success"],True)
        print("设备网关：%s"%t["data"]["device_gateWay"])
        print("设备ip：%s"%t["data"]["device_ip"])
        print("设备子网：%s"%t["data"]["device_mask"])
        print("设备名称：%s"%t["data"]["device_name"])

    def test02_info_monitor(self):
        """2、监控者登录后，设备信息捕获。 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_monitor")
        url=self.ws
        print("step 1、登录设备/监控者")
        t=c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data=rm.get_data("捕获设备信息","info")   # 获取device.info.read命令发送数据包。
        ws=self.ws
        print("step 2、发送“查询设备信息”数据。")
        t=c.checkAction(ws,data)
        self.assertEqual(t["success"],True)
        print("设备名称：%s"%t["data"]["device_name"])
        print("分组：%s"%t["data"]["device_group"])
        print("设备ip：%s"%t["data"]["device_ip"])
        print("设备网关：%s"%t["data"]["device_gateWay"])
        print("设备子网：%s"%t["data"]["device_mask"])
        print("是否被占用：%s"%t["data"]["is_occupied"])
        print("占用者ip：%s"%t["data"]["occupier_ip"])
        print("占用者名字：%s"%t["data"]["occupier_name"])

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test03_info_operator(self):
        """3、操作者登录后，设备信息捕获。 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_operator")
        url=self.ws
        print("step 1、登录设备/操作者")
        t=c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data=rm.get_data("捕获设备信息","info")   # 获取device.info.read命令发送数据包。
        ws=self.ws
        print("step 2、发送“查询设备信息”数据。")
        t=c.checkAction(ws,data)
        self.assertEqual(t["success"],True)
        print("设备名称：%s"%t["data"]["device_name"])
        print("分组：%s"%t["data"]["device_group"])
        print("设备ip：%s"%t["data"]["device_ip"])
        print("设备网关：%s"%t["data"]["device_gateWay"])
        print("设备子网：%s"%t["data"]["device_mask"])
        print("是否被占用：%s"%t["data"]["is_occupied"])
        print("占用者ip：%s"%t["data"]["occupier_ip"])
        print("占用者名字：%s"%t["data"]["occupier_name"])

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test04_info_admin(self):
        """4、管理员登录后，设备信息捕获。 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、登录设备/管理员")
        t=c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data=rm.get_data("捕获设备信息","info")   # 获取device.info.read命令发送数据包。
        ws=self.ws
        print("step 2、发送“查询设备信息”数据。")
        t=c.checkAction(ws,data)
        self.assertEqual(t["success"],True)
        print("设备名称：%s"%t["data"]["device_name"])
        print("分组：%s"%t["data"]["device_group"])
        print("设备ip：%s"%t["data"]["device_ip"])
        print("设备网关：%s"%t["data"]["device_gateWay"])
        print("设备子网：%s"%t["data"]["device_mask"])
        print("是否被占用：%s"%t["data"]["is_occupied"])
        print("占用者ip：%s"%t["data"]["occupier_ip"])
        print("占用者名字：%s"%t["data"]["occupier_name"])

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # r=websocket_request()
    # r.setUp()
    # r.test01_info()
    # r.tearDown()
