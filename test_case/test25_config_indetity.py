#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """出厂配置：配置设备id"""
    identity=""
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

    def test01_config_identity(self):
        """ 配置设备id"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_identity=rm.get_data("配置设备id","factory_config_identity")
        print("step 2、配置设备id")
        identity=self.identity
        data_dict=json.loads(data_identity)

        data_dict["data"]["identity"]="%s"%identity

        data_identity=json.dumps(data_dict)
        t=c.checkAction(url,data_identity)
        self.assertEqual(t["success"],True)
        print("配置设备id:%s成功。"%identity)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
