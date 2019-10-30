#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """本地IO控制"""
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

    def test01_read_io(self):
        """1、读取本地IO """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.5)

        # data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        # print("step 2、读取Z0的io。")
        # t=c.checkAction(url,data_io_read)
        # self.assertEqual(t["success"],True)
        # time.sleep(0.5)

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

    def test02_read_io_param(self):
        """2、按配置读取IO:nick_name 可修改 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        print("step 2、按配置参数读取io：")
        io_list=["input_0","input_1","input_2","input_3","input_4","input_5","X0","X1","X2","X3","X4","X5"]

        data_dict=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("读取io的参数：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("读取io成功")
            else:
                print("读取io失败。")
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test03_write_io_off(self):
        """3、设置本地IO_off：nick_name 可修改"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_off")
        print("step 2、设置io:")
        io_list=["output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7","Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7"]
        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
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

            data_dict_read["data"]["name"]=name
            print("读取io：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True:
                print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("io：%s读取失败。"%name)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test04_write_io_on(self):
        """4、设置本地IO_on：nick_name 可修改 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.2)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置io:")
        io_list=["output_0","output_1","output_2","output_3","output_4","output_5","output_6","output_7","Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7"]

        data_dict=json.loads(data_io_set)

        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
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

            data_dict_read["data"]["name"]=name
            print("读取io：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True:
                print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("io：%s读取失败。"%name)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test05_read_io_default(self):
        """5、读取default IO:default 不可修改 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        print("step 2、读取default_io：")
        io_list=["stop_input","X6"]

        data_dict=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("读取io的参数：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("读取default_io成功")
            else:
                print("读取default_io失败。")
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test06_write_io_default_off(self):
        """6、设置本地IO_off：default 不可修改"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_off")
        print("step 2、设置io:")
        io_list=["red","Y8","green","Y9","yellow","Y10","stop_output","Y11"]
        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("修改default_io：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("状态置为0。")
            else:
                print("io状态修改失败。")
            time.sleep(0.1)

            data_dict_read["data"]["name"]=name
            print("读取io：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True:
                print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("io：%s读取失败。"%name)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test07_write_io_default_on(self):
        """7、设置本地IO_on：default 不可修改 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.2)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置io:")
        io_list=["red","Y8","green","Y9","yellow","Y10","stop_output","Y11"]

        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("修改default_io：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("状态置为1。")
            else:
                print("io状态修改失败。")
            time.sleep(0.1)

            data_dict_read["data"]["name"]=name
            print("读取io：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True:
                print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("io：%s读取失败。"%name)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    # def test04_write_io_pulse(self):
    #     """2、设置本地IO_pulse """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(0.1)
    #
    #     data_io_set=rm.get_data("设置本地IO","io_write_local_on")
    #     print("step 2、设置io:")
    #     io_list=["pulse_0","pulse_1","pulse_2","pulse_3","pulse_4","pulse_5"]
    #     numbers=[3,15,30,68,125,385,1420]
    #
    #     data_dict=json.loads(data_io_set)
    #     for name in io_list:
    #         data_dict["data"]["name"]=name
    #         for state in numbers:
    #             data_dict["data"]["state"]=state
    #             print("修改io：%s"%name )
    #             data_io_set=json.dumps(data_dict)
    #             t=c.checkAction(url,data_io_set)
    #             if t["success"]==True:
    #                 print("%s 的脉冲个数为：%s"%(name,state))
    #             else:
    #                 print("%s的脉冲个数设置失败。"%name)
    #             time.sleep(0.1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # for i in range(1,100000):
    #     suite = unittest.TestSuite()
    #     suite.addTest(websocket_request('setUp'))
    #     suite.addTest(websocket_request('test01_read_io'))
    #     suite.addTest(websocket_request('test02_read_io_param'))
    #     suite.addTest(websocket_request('test03_write_io_off'))
    #     suite.addTest(websocket_request('test04_write_io_on'))
    #     suite.addTest(websocket_request('test05_read_io_default'))
    #     suite.addTest(websocket_request('test06_write_io_default_off'))
    #     suite.addTest(websocket_request('test07_write_io_default_on'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)