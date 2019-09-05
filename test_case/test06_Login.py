#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """权限管理 """
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

    def test01_login_monitor(self):
        """1. 登录设备/监控者"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_monitor")
        url=self.ws
        print("step 1、登录设备/监控者")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 2、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test02_login_operator(self):
        """1. 登录设备/操作者"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_operator")
        url=self.ws
        print("step 1、登录设备/操作者")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 2、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test03_login_admin(self):
        """1. 登录设备/管理员"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、登录设备/管理员")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 2、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test04_password_reset_monitor(self):
        """3. 修改密码/监控者无权修改密码"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_monitor")
        url=self.ws
        print("step 1、登录设备/监控者")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_reset=rm.get_data("修改密码","password_reset_monitor")
        url=self.ws
        print("step 2、修改监控者密码")
        t=c.checkAction(url,data_reset)
        self.assertEqual(t["success"],False)
        print("监控者无权修改密码")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test05_password_reset_operator(self):
        """3. 修改密码/操作者无权修改密码"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_operator")
        url=self.ws
        print("step 1、登录设备/操作者")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_reset=rm.get_data("修改密码","password_reset_operator")
        url=self.ws
        print("step 2、修改操作者密码")
        t=c.checkAction(url,data_reset)
        self.assertEqual(t["success"],False)
        print("操作者无权修改密码")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def test06_password_reset_admin(self):
        """3. 修改密码/管理员可以修改密码"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、登录设备/管理员")
        t=c.checkAction(url,data_login)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_reset_monitor=rm.get_data("修改密码","password_reset_monitor")
        url=self.ws
        print("step 2、修改监控者密码")
        t=c.checkAction(url,data_reset_monitor)
        self.assertEqual(t["success"],True)
        print("成功修改临控者密码")
        time.sleep(1)

        data_reset_operator=rm.get_data("修改密码","password_reset_operator")
        url=self.ws
        print("step 3、修改操作者密码")
        t=c.checkAction(url,data_reset_operator)
        self.assertEqual(t["success"],True)
        print("成功修改操作者密码")
        time.sleep(1)


        data_reset_admin=rm.get_data("修改密码","password_reset_admin")
        url=self.ws
        print("step 4、修改管理员密码")
        t=c.checkAction(url,data_reset_admin)
        self.assertEqual(t["success"],True)
        print("成功修改管理员密码")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、退出登录。")
        t=c.checkAction(url,data_logout)
        self.assertEqual(t["success"],True)

    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # for i in range(1,1000):
    #     suite = unittest.TestSuite()
    #     suite.addTest(websocket_request('setUp'))
    #     suite.addTest(websocket_request('test01_login_monitor'))
    #     suite.addTest(websocket_request('tearDown'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)


