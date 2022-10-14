#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """extendIO:module_name: io_extend.json"""
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

    def test01_read_extendIO(self):
        """1、读取extendIO """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_read=rm.get_data("读取extendIO","io_read_extend")
        print("step 2、按配置参数读取总线io：")
        io_list=["X0","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10","X11","X12","Y16","Y17"]

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


    def test02_write_extendIO(self):
        """2、设置extendIO"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_set=rm.get_data("设置extendIO","io_write_extend")
        print("step 2、设置io:")
        io_list=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11","Y12","Y13","Y14","Y15","Y16","Y17"]
        values=[1,0]
        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取extendIO","io_read_extend")
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
    # for i in range(1,1000):
    #     suite = unittest.TestSuite()
    #     suite.addTest(websocket_request('setUp'))
    #     suite.addTest(websocket_request('test01_read_extendIO'))
    #     suite.addTest(websocket_request('test02_write_extendIO'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)