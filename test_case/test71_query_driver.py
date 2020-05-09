#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """7 信息查询：7.1 查询关节信息"""
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

    def test01_QueryDriver(self):
        """ 查询关节信息 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_query_joint=rm.get_data("查询关节信息","query_joint_all")
        print("step 2、查询所有关节信息。")
        t=c.checkAction(url,data_query_joint)
        self.assertEqual(t["success"],True)
        lenth=len(t["data"])
        for i in range(0,lenth):
            print("关节名称：%s，关节id：%s，的驱动信息："%(t["data"][i]["name"],t["data"]["id"]))
            print("驱动id：%s。"%(t["data"][i]["driver"]["id"]))
            print("驱动类型：%s。"%(t["data"][i]["driver"]["type"]))
            print("驱动节点号：%s。"%(t["data"][i]["driver"]["node_id"]))
            print("最大硬限位：%s。"%(t["data"][i]["driver"]["limit_maxinum"]))
            print("最小硬限位：%s。"%(t["data"][i]["driver"]["limit_minimum"]))
            print("序列号：%s。"%(t["data"][i]["driver"]["serial_num"]))
            print("软件版本：%s。"%(t["data"][i]["driver"]["soft_version"]))
            print("硬件版本：%s。"%(t["data"][i]["driver"]["hardware_version"]))
            print("-"*30)

        time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
