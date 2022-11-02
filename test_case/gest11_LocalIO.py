#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """本地IO控制：V2.3版本中local_option_io.json文件无效"""
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



    def test01_read_io_input(self):
        """1、读取本地input_IO: [0-31] """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.3)

        data_io_read=rm.get_data("读取本地IO","io_read_local")
        print("step 2、读取io_input：")
        io_list=["X0","X1","X2","X3","X4","X5","X6","X7","X8","X9","X10","X11","X12","X13","X14","X15","X16","X17","X18","X19","X20","X21","X22","X23","X24","X25","X26","X27","X28","X29","X30","X31"]

        data_dict=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("读取input_IO：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("读取input_IO成功")
                print("input_IO: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("读取input_IO: %s 失败。"%name)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test02_write_io_output_off(self):
        """2、设置本地IO_output：[0-31]"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.3)

        data_io_set=rm.get_data("设置本地IO","io_write_local_off")
        print("step 2、设置io_output:")
        io_list=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11","Y12","Y13","Y14","Y15","Y16","Y17","Y18","Y19","Y20","Y21","Y22","Y23","Y24","Y25","Y26","Y27","Y28","Y29","Y30","Y31"]
        data_dict=json.loads(data_io_set)
        data_io_read=rm.get_data("读取本地IO","io_read_local")
        data_dict_read=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("output_IO：%s 置为off。"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("output_IO: %s状态设置为0。"%name)
            else:
                print("output_IO: %s状态修改失败。"%name)
            time.sleep(0.01)

            data_dict_read["data"]["name"]=name
            print("读取output_io：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True and t["data"]["state"]==0:
                print("output_io: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("output_io：%s读取失败。"%name)
            # time.sleep(0.05)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test03_write_io_on(self):
        """3、设置本地output_IO on:[0-31] """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.3)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置output_IO为on:")
        io_list=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11","Y12","Y13","Y14","Y15","Y16","Y17","Y18","Y19","Y20","Y21","Y22","Y23","Y24","Y25","Y26","Y27","Y28","Y29","Y30","Y31"]

        data_dict=json.loads(data_io_set)

        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
        for name in io_list:
            data_dict["data"]["name"]=name
            print("修改output_IO：%s"%name )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                print("output_IO: %s状态设置为1。"%name)
            else:
                print("output_IO: %s状态修改失败。"%name)
            time.sleep(0.1)

            data_dict_read["data"]["name"]=name
            print("读取output_IO：%s"%name )
            data_io_read=json.dumps(data_dict_read)
            t=c.checkAction(url,data_io_read)
            if t["success"]==True and t["data"]["state"]==1:
                print("output_IO: %s 的state值为：%s。"%(name,t["data"]["state"]))
            else:
                print("output_IO：%s读取失败。"%name)
            # time.sleep(0.05)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test04_write_io_off_on(self):
        """3、设置本地output_IO on:[0-31] """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_on")
        print("step 2、设置output_IO为on:")
        io_list=["Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11","Y12","Y13","Y14","Y15","Y16","Y17","Y18","Y19","Y20","Y21","Y22","Y23","Y24","Y25","Y26","Y27","Y28","Y29","Y30","Y31"]
        state_list=[0,1]
        data_dict=json.loads(data_io_set)

        data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        data_dict_read=json.loads(data_io_read)
        for name in io_list:
            for state in state_list:
                data_dict["data"]["name"]=name
                data_dict["data"]["state"]=state
                print("修改output_IO：%s"%name )
                data_io_set=json.dumps(data_dict)
                t=c.checkAction(url,data_io_set)
                if t["success"]==True:
                    print("output_IO: %s状态设置: %s。"%(name,state))
                else:
                    print("output_IO: %s状态修改失败。"%name)
                time.sleep(0.01)

                # data_dict_read["data"]["name"]=name
                # print("读取output_IO：%s"%name )
                # data_io_read=json.dumps(data_dict_read)
                # t=c.checkAction(url,data_io_read)
                # if t["success"]==True and t["data"]["state"]==1:
                #     print("output_IO: %s 的state值为：%s。"%(name,t["data"]["state"]))
                # else:
                #     print("output_IO：%s读取失败。"%name)
                # time.sleep(0.05)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test05_write_io_all(self):
        """3、设置本地output_IO all:[0-31] """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(0.1)

        data_io_set=rm.get_data("设置本地IO","io_write_local_all")
        print("step 2、设置output_IO全部状态")

        value_list=[0,4294967295,3804175089,2058836592,45613040,4294844403          ,0,4294967295]
        data_dict=json.loads(data_io_set)

        # data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
        # data_dict_read=json.loads(data_io_read)

        for value in value_list:
            data_dict["data"]["value"]=value
            print("打开全部output。" )
            data_io_set=json.dumps(data_dict)
            t=c.checkAction(url,data_io_set)
            if t["success"]==True:
                if value==0:
                    print("output_IO全部关闭")
                else:
                    print("output_IO全部打开")
            else:
                print("output_IO全部状态修改失败。")
            time.sleep(0.5)



        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    # def test04_read_io_default(self):
    #     """4、读取default IO:default 不可修改 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
    #     print("step 2、读取default_io：")
    #     io_list=["X0","X1","X2","X3","X4","X5","X6","Y0","Y1","Y2","Y3","Y4","Y5","Y6","Y7","Y8","Y9","Y10","Y11"]
    #
    #     data_dict=json.loads(data_io_read)
    #     for name in io_list:
    #         data_dict["data"]["name"]=name
    #         print("读取io的参数：%s"%name )
    #         data_io_set=json.dumps(data_dict)
    #         t=c.checkAction(url,data_io_set)
    #         if t["success"]==True:
    #             print("读取default_io:%s成功"%name)
    #         else:
    #             print("读取default_io: %s失败。"%name)
    #         time.sleep(0.1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

    # def test05_write_io_default_off(self):
    #     """5、设置本地IO_off：default 不可修改"""
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_io_set=rm.get_data("设置本地IO","io_write_local_off")
    #     print("step 2、设置io:")
    #     io_list=["Y0","output0","Y1","output1","Y2","output2","Y3","output3","Y4","output4","Y5","output5","Y6","output6","Y7","output7","Y8","em_stop_out","Y9","sys_red","Y10","sys_green","Y11","sys_yellow"]
    #     data_dict=json.loads(data_io_set)
    #     data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
    #     data_dict_read=json.loads(data_io_read)
    #     for name in io_list:
    #         data_dict["data"]["name"]=name
    #         print("修改default_io：%s"%name )
    #         data_io_set=json.dumps(data_dict)
    #         t=c.checkAction(url,data_io_set)
    #         if t["success"]==True:
    #             print("io: %s 状态设置为0。"%name)
    #         else:
    #             print("io: %s状态修改失败。"%name)
    #         time.sleep(0.1)
    #
    #         data_dict_read["data"]["name"]=name
    #         print("读取io：%s"%name )
    #         data_io_read=json.dumps(data_dict_read)
    #         t=c.checkAction(url,data_io_read)
    #         if t["success"]==True:
    #             print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
    #         else:
    #             print("io：%s读取失败。"%name)
    #         time.sleep(0.1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

    # def test06_write_io_default_on(self):
    #     """6、设置本地IO_on：default 不可修改 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(0.2)
    #
    #     data_io_set=rm.get_data("设置本地IO","io_write_local_on")
    #     print("step 2、设置io:")
    #     io_list=["Y0","output0","Y1","output1","Y2","output2","Y3","output3","Y4","output4","Y5","output5","Y6","output6","Y7","output7","Y8","em_stop_out","Y9","sys_red","Y10","sys_green","Y11","sys_yellow"]
    #
    #     data_dict=json.loads(data_io_set)
    #     data_io_read=rm.get_data("读取本地IO","io_read_local_Z0")
    #     data_dict_read=json.loads(data_io_read)
    #     for name in io_list:
    #         data_dict["data"]["name"]=name
    #         print("修改default_io：%s"%name )
    #         data_io_set=json.dumps(data_dict)
    #         t=c.checkAction(url,data_io_set)
    #         if t["success"]==True:
    #             print("io: %s 状态设置为1。"%name)
    #         else:
    #             print("io: %s 状态修改失败。"%name)
    #         time.sleep(0.1)
    #
    #         data_dict_read["data"]["name"]=name
    #         print("读取io：%s"%name )
    #         data_io_read=json.dumps(data_dict_read)
    #         t=c.checkAction(url,data_io_read)
    #         if t["success"]==True:
    #             print("io: %s 的state值为：%s。"%(name,t["data"]["state"]))
    #         else:
    #             print("io：%s读取失败。"%name)
    #         time.sleep(0.1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

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
    # unittest.main()


    for i in range(1,10000):
        suite = unittest.TestSuite()
        suite.addTest(websocket_request('setUp'))
        # suite.addTest(websocket_request('test01_read_io_input'))
        suite.addTest(websocket_request('test02_write_io_output_off'))
        suite.addTest(websocket_request('test03_write_io_on'))
        suite.addTest(websocket_request('test02_write_io_output_off'))
        suite.addTest(websocket_request('test03_write_io_on'))
        suite.addTest(websocket_request('test04_write_io_off_on'))
        suite.addTest(websocket_request('test05_write_io_all'))
        suite.addTest(websocket_request('tearDown'))
        unittest.TextTestRunner(verbosity=2).run(suite)