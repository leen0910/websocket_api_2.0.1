#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """出厂配置：配置扩展IO"""
    type="user_custom"  #user_custom 用户自定义
    is_add=bool(0)     #扩展IO是否能够扩展和控制器型号相关。true 在原有的扩展上添加扩展IO配置。false 将现有的扩展IO重置为设定的配置。
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

        data_set_extIO=rm.get_data("配置扩展IO","factory_config_extended_io")
        print("step 2、配置扩展IO")
        type=self.type
        is_add=self.is_add
        data_dict=json.loads(data_set_extIO)
        data_dict["data"]["type"]="%s"%type
        data_dict["data"]["is_add"]=is_add
        data_set_extIO=json.dumps(data_dict)
        t=c.checkAction(url,data_set_extIO)
        self.assertEqual(t["success"],True)
        print("配置扩展IO:%s,%s成功。"%(type,is_add))
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
