#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """IO控制"""
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            self.ws=create_connection(url,timeout=5)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    def test01_read_io(self):
        """1、读取本地IO """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_relayflag")
        print("step 2、读取Z0的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X0")
        print("step 3、读取X0的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X1")
        print("step 4、读取X1的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X2")
        print("step 5、读取X2的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X3")
        print("step 6、读取X3的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X4")
        print("step 7、读取X4的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_io_read=rm.get_data("读取本地IO","io_read_local_X5")
        print("step 8、读取X5的io。")
        t=c.checkAction(url,data_io_read)
        self.assertEqual(t["success"],True)
        time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test02_write_io_off(self):
        """2、设置本地IO_off """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_off")
        print("step 2、设置io:")
        io_list=["relayflag","output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7"]

        data_dict=json.loads(data_io_set)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("修改io：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("状态置为0。")
            else:
                print("io状态修改失败。")
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test03_write_io_on(self):
        """2、设置本地IO_on """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.2)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置io:")
        io_list=["relayflag","output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7"]

        data_dict=json.loads(data_io_set)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("修改io：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("状态置为1。")
            else:
                print("io状态修改失败。")
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test04_write_io_pulse(self):
        """2、设置本地IO_pulse """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置io:")
        io_list=["pulse_0","pulse_1","pulse_2","pulse_3","pulse_4","pulse_5"]
        numbers=[3,15,30,68,125,385,1420]

        data_dict=json.loads(data_io_set)
        for name in io_list:
            data_dict["data"]["name"]=name
            for state in numbers:
                data_dict["data"]["state"]=state
                print("修改io：%s"%name )
                data_io_set=json.dumps(data_dict)
                t=c.checkAction(url,data_io_set)
                if t["success"]==True:
                    print("%s 的脉冲个数为：%s"%(name,state))
                else:
                    print("%s的脉冲个数设置失败。"%name)
                time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()