#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """8 io管理：8.2 设置localIo"""
    name=["Y0","Y1"]
    state=[0,1]

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
        """ 设置localIo"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_write_localIo=rm.get_data("设置localIo","write_localIo")
        data_read_localIo=rm.get_data("读取localIo","read_localIo")
        print("step 2、准备设置localIo：")
        names=self.name
        states=self.state
        for name in names:
            for state in states:
                data_dict=json.loads(data_write_localIo)
                data_dict1=json.loads(data_read_localIo)
                data_dict["data"]["name"]=name
                data_dict["data"]["state"]=state
                data_dict1["data"]["name"]=name
                data_write_localIo=json.dumps(data_dict)
                data_read_localIo=json.dumps(data_dict1)
                t=c.checkAction(url,data_write_localIo)
                time.sleep(0.3)
                t1=c.checkAction(url,data_read_localIo)
                self.assertEqual(t["success"],True)
                print("设置localIO:%s,状态值：%s"%(name,state))
                if t1["data"]["state"]==state:
                    print("设置localIO:%s，状态值正确。"%name)
                else:
                    print("设置localIO:%s，状态值错误。设置状态：%s，实际状态：%s"%(name,state,t1["data"]["state"]))
                time.sleep(0.2)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
