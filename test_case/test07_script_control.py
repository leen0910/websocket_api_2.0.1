#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time




class websocket_request(unittest.TestCase):
    """ 脚本运行 &  修改运行速度 & 运行模式切换"""
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

    def test01_script_control(self):
        """脚本运行控制相关操作。 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_init=rm.get_data("设备初始化","init")
        print("step 2、初始化。")
        c.checkAction(url,data_init)
        time.sleep(8)


        data_script_start=rm.get_data("脚本运行控制","script_start")
        print("step 3、运行脚本：tutorial.lua.")
        t=c.checkAction(url,data_script_start)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_velocity=rm.get_data("调整全局速度","adjust_velocity")
        print("step 4、调节运行速度为40%")
        t=c.checkAction(url,data_velocity)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_script_pause=rm.get_data("脚本运行控制","script_pause")
        print("step 5、暂停脚本运行：")
        t=c.checkAction(url,data_script_pause)
        self.assertEqual(t["success"],True)
        time.sleep(2)

        data_script_continue=rm.get_data("脚本运行控制","script_continue")
        print("step 6、暂停后继续脚本运行：")
        t=c.checkAction(url,data_script_continue)
        self.assertEqual(t["success"],True)
        time.sleep(4)

        data_script_stop=rm.get_data("脚本运行控制","script_stop")
        print("step 7、停止脚本运行：")
        c.checkAction(url,data_script_stop)

        data_logout=rm.get_data("退出登录","logout")
        print("step 8、退出登录。")
        c.checkAction(url,data_logout)

    def test02_script_emergency_stop(self):
        """脚本运行时急停 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_init=rm.get_data("设备初始化","init")
        print("step 2、初始化。")
        c.checkAction(url,data_init)
        time.sleep(8)


        data_script_start=rm.get_data("脚本运行控制","script_start")
        print("step 3、运行脚本：tutorial.lua.")
        t=c.checkAction(url,data_script_start)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_velocity=rm.get_data("调整全局速度","adjust_velocity")
        print("step 4、调节运行速度为40%")
        t=c.checkAction(url,data_velocity)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_script_pause=rm.get_data("紧急停止","emergency_stop")
        print("step 5、运行过程中急停。")
        t=c.checkAction(url,data_script_pause)
        self.assertEqual(t["success"],True)
        time.sleep(2)

        data_script_start=rm.get_data("脚本运行控制","script_start")
        print("step 6、再次运行脚本：tutorial.lua.")
        t=c.checkAction(url,data_script_start)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_script_stop=rm.get_data("脚本运行控制","script_stop")
        print("step 7、停止脚本运行：")
        c.checkAction(url,data_script_stop)

        data_logout=rm.get_data("退出登录","logout")
        print("step 8、退出登录。")
        c.checkAction(url,data_logout)




    def tearDown(self):
        self.ws.close()

if __name__ == "__main__":
    unittest.main()