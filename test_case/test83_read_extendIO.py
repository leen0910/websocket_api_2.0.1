#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """extendIO:读取extendIo"""
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

    def test01_write_extendIO(self):
        """2、设置extendIO"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_read=rm.get_data("读取extendIo","read_extendIo")
        print("step 2、按配置参数读取总线io：")
        io_list=["X0","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10","X11","X12","X13","X14","input0","input1","input2","input3","input4","input5","input6","input7","input8","input9","input10","input11","input12","pulseF","pulseC"]

        data_dict=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("读取io的参数：%s"%name )
            data_io_read=json.dumps(data_dict)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True:
                print("读取extendIO: %s 的state值：%s"%(t["data"]["name"],t["data"]["state"]))
            else:
                print("读取extendIO失败。")
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()