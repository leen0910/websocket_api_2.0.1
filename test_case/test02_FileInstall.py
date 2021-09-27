#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json




class websocket_request(unittest.TestCase):
    """3.控制器安装文件"""
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

    # def test01_install_script(self):
    #     """3.控制器安装文件/安装script """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_install_file=rm.get_data("控制器安装文件","file_install_script")
    #
    #     # """重新设置安装文件名"""
    #     # data_dict=json.loads(data_install_file)
    #     # data_dict["data"]["index"]=1
    #     # data_dict["data"]["file_name"]="test.lua"
    #     # print("安装脚本："+data_dict["data"]["file_name"])
    #     # data_install_file=json.dumps(data_dict)
    #     # print(data_install_file)
    #
    #     print("step 2、安装script文件: test.lua。")
    #     t=c.checkAction(url,data_install_file)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)

    # def test02_install_config(self):
    #     """3.控制器安装文件/安装config """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_install_file=rm.get_data("控制器安装文件","file_install_config")
    #
    #     print("step 2、安装config文件: permission.json 。")
    #     t=c.checkAction(url,data_install_file)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)

    # def test03_install_update(self):
    #     """3.控制器安装文件/安装update """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_install_file=rm.get_data("控制器安装文件","file_install_update")
    #
    #     print("step 2、安装update文件: test.reb。")
    #     t=c.checkAction(url,data_install_file)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、释放设备：")
    #     c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()