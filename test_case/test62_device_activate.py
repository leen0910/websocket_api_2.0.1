#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """6 授权管理：6.2 设备授权"""
    activation_code=""  # 设备激活码
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

    def test01_set_extIO(self):
        """ 配置扩展IO """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_device_activate=rm.get_data("设备授权","device_activate")
        print("step 2、设备授权。")
        activation_code=self.activation_code
        data_dict=json.loads(data_device_activate)
        data_dict["data"]["activation_code"]="%s"%activation_code
        data_device_activate=json.dumps(data_dict)
        t=c.checkAction(url,data_device_activate)
        self.assertEqual(t["success"],True)
        print("设备授权成功。")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
