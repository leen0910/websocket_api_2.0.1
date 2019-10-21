#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time

class websocket_request(unittest.TestCase):
    """默认脚本"""
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

    def test01_set_default(self):
        """3. 设置默认脚本 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_def_script=rm.get_data("设置默认脚本","script_set_default")
        print("step 2、设置tutorial.lua为默认程序。")
        t=c.checkAction(url,data_def_script)
        self.assertEqual(t["success"],True)
        time.sleep(1)


        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出设备：")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test02_query_script(self):
        """4. 查询脚本信息 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_def_script=rm.get_data("查询脚本信息","script_query_script_name")
        print("step 2、查询tutorial.lua脚本信息。")
        t=c.checkAction(url,data_def_script)
        self.assertEqual(t["success"],True)
        time.sleep(1)
        if t["data"]["default"]==True:
            print("default脚本设置成功！")
        else:
            print("default脚本设置失败！")

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出设备：")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test03_query_default(self):
        """4. 查询脚本信息/查询默认脚本 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_def_script=rm.get_data("查询脚本信息","script_query_script_default")
        print("step 3、查询默认脚本信息。")
        t=c.checkAction(url,data_def_script)
        self.assertEqual(t["success"],True)
        time.sleep(1)
        if t["data"]["default"]==True and t["data"]["name"]=='tutorial.lua':
            print("default脚本查询正确！")
        else:
            print("default脚本查询错误！")

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出设备：")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)



    def test04_clear_default(self):
        """清除默认脚本 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_def_script=rm.get_data("设置默认脚本","script_set_default_clear")
        print("step 2、清除默认程序设置。")
        t=c.checkAction(url,data_def_script)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_def_script=rm.get_data("查询脚本信息","script_query_script_name")
        print("step 3、查询tutorial.lua脚本信息。")
        t1=c.checkAction(url,data_def_script)
        self.assertEqual(t["success"],True)
        time.sleep(1)
        if t1["data"]["default"]==False:
            print("default脚本清除成功！")
        else:
            print("default脚本清除失败！")

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、退出设备：")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)




    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()