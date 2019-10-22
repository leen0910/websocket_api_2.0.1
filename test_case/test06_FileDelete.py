#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import os


class websocket_request(unittest.TestCase):
    """4.控制器删除文件"""
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

    def test01_FileRemove_script(self):
        """4.控制器删除文件/删除script文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_delete=rm.get_data("控制器删除文件","file_remove_script")
        print("step 2、删除script文件：test.lua。")
        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    # def test02_FileRemove_config(self):
    #     """4.控制器删除文件/删除config文件 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_delete=rm.get_data("控制器删除文件","file_remove_config")
    #     print("step 2、删除config文件：test.json。")
    #     t=c.checkAction(url,data_file_delete)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)

    # def test03_FileRemove_log(self):
    #     """4.控制器删除文件/删除log文件 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_delete=rm.get_data("控制器删除文件","file_remove_log")
    #     print("step 2、删除log文件：test.log。")
    #     t=c.checkAction(url,data_file_delete)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)

    def test04_reduce_FileReceive(self):
        """再次执行一次 test01_FileReceive.py 文件，生成temp文件。"""
        os.system("python C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\test_case\\test01_FileReceive.py")
        print("已写入tempFile文件。")

    def test05_FileRemove_temp_script(self):
        """4.控制器删除文件/删除temp_script文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_delete=rm.get_data("控制器删除文件","file_remove_temp_script")
        print("step 2、删除temp_script文件：test.lua。")
        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    def test06_FileRemove_temp_temp_config(self):
        """4.控制器删除文件/删除temp_config文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_delete=rm.get_data("控制器删除文件","file_remove_temp_config")
        print("step 2、删除temp_config文件：test.json。")
        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    def test07_FileRemove_temp_temp_update(self):
        """4.控制器删除文件/删除temp_update文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_delete=rm.get_data("控制器删除文件","file_remove_temp_update")
        print("step 2、删除temp_update文件：test.reb。")
        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)

    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # f=websocket_request()
    # f.test031_reduce_test01()