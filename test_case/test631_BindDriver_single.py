#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """6 授权管理：6.3 驱动器绑定"""
    bind_id=1  # 驱动器id
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

    def test01_BindDriver_single(self):
        """ 单驱动器绑定 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_bind_driver=rm.get_data("驱动器绑定","device_bind_driver_single")
        print("step 2、单驱动器绑定。")
        bind_id=self.bind_id
        data_dict=json.loads(data_bind_driver)
        data_dict["data"]["bind_id"]=bind_id
        data_bind_driver=json.dumps(data_dict)
        t=c.checkAction(url,data_bind_driver)
        self.assertEqual(t["success"],True)
        print("驱动器id:%s 绑定成功。"%bind_id)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
