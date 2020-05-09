#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """8 io管理：8.1 读取localIo"""
    name=["X0","X1"]
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

    def test01_read_localIO(self):
        """ 读取localIo"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_read_localIo=rm.get_data("读取localIo","read_localIo")
        print("step 2、准备读取localIo：")
        names=self.name
        for name in names:
            data_dict=json.loads(data_read_localIo)
            data_dict["data"]["name"]=name
            data_read_localIo=json.dumps(data_dict)
            t=c.checkAction(url,data_read_localIo)
            self.assertEqual(t["success"],True)
            print("读取localIO:%s,状态值：%s"%(name,t["data"]["state"]))
            time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
