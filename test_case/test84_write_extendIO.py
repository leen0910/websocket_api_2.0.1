#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """extendIO:设置extendIO"""
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
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_set=rm.get_data("设置extendIo","write_extendIo")
        print("step 2、设置io:")
        io_list=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11","Y12","Y13","Y14","Y15","output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7","output_8","output_9","output_10","output_11","output_12","output_13","output_14","output_15"]
        values=[0,1]
        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取extendIo","read_extendIo")
        data_dict_read=json.loads(data_io_read)
        for value in values:
            for name in io_list:
                data_dict["data"]["name"]=name
                data_dict["data"]["state"]=value
                data_io_set=json.dumps(data_dict)
                t1=c.checkAction(url,data_io_set)
                if t1["success"]==True:
                    print("设置extendIO：%s的值：%s"%(name,value))
                else:
                    print("设置extendIO失败。")
                time.sleep(0.1)

                data_dict_read["data"]["name"]=name
                print("读取extendIO：%s"%name )
                data_io_read=json.dumps(data_dict_read)
                t2=c.checkAction(url,data_io_read)
                if t2["success"]==True:
                    print("extendIO: %s 的state值为：%s。"%(name,t2["data"]["state"]))
                else:
                    print("extendIO：%s读取失败。"%name)
                time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()