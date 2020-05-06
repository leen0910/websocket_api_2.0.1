#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """硬件测试：本地IO测试"""
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

    def test01_testIO(self):
        """本地IO测试 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_test_io=rm.get_data("本地IO测试","hardware_test_io_start")
        print("step 2、开始本地IO硬件测试")
        t=c.checkAction(url,data_test_io)
        self.assertEqual(t["success"],True)
        print("开始硬件测试：本地IO。")
        time.sleep(100)

        data_test_io_stop=rm.get_data("本地IO测试","hardware_test_io_stop")
        print("step 3、停止本地IO硬件测试")
        t_q=c.checkAction(url,data_test_io_stop)
        self.assertEqual(t_q["success"],True)
        print("本地IO测试停止。")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # for i in range(1,500):
    #     suite = unittest.TestSuite()
    #     # suite.addTest(websocket_request('setUp'))
    #     suite.addTest(websocket_request('test01_modbus_connect'))
    #     suite.addTest(websocket_request('test02_read_modbus_coil'))
    #     suite.addTest(websocket_request('test03_write_modbus_coil_Robot'))
    #     suite.addTest(websocket_request('test04_read_modbus_register'))
    #     suite.addTest(websocket_request('test05_write_modbus_register'))
    #     suite.addTest(websocket_request('test06_modbus_disconnect'))
    #     # suite.addTest(websocket_request('tearDown'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)