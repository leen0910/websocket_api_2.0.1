#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import Base_64
import time
import json




class websocket_request(unittest.TestCase):
    """权限管理:设置密码 """
    # 输入设置的密码：
    password="123456"

    password=Base_64.encode(password)

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

    def test01_reset_passwrod(self):
        """设置debug密码"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录设备")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_reset=rm.get_data("设置密码","password_reset_debug")
        url=self.ws
        print("step 2、设置debug密码。")

        password=self.password
        data_dict=json.loads(data_reset)

        data_dict["data"]["password"]="\"%s\""%password
        data_reset=json.dumps(data_dict)

        t=c.checkAction(url,data_reset)
        self.assertEqual(t["success"],True)
        print("成功设置debug密码：%s。")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()



