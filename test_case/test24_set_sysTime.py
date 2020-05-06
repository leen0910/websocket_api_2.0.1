#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """出厂配置：配置系统时间"""
    s_date="2020/04/22"
    s_time="16:31:22"
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

    def test01_set_sysTime(self):
        """ 配置系统时间"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_set_sysTime=rm.get_data("配置系统时间","factory_config_system_time")
        print("step 2、配置系统时间")
        s_date=self.s_date
        s_time=self.s_time
        data_dict=json.loads(data_set_sysTime)

        data_dict["data"]["date"]=s_date
        data_dict["data"]["time"]=s_time
        data_set_sysTime=json.dumps(data_dict)
        t=c.checkAction(url,data_set_sysTime)
        self.assertEqual(t["success"],True)
        print("配置系统时间:%s,%s成功。"%(s_date,s_time))
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
