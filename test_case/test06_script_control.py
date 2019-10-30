#!/usr/bin/python

from websocket import create_connection
from common import webs
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
            # self.ws=webs.on_start(url)
            self.ws=create_connection(url,timeout=20)  #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功!"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    def test01_script_control_run(self):
        """脚本运行控制相关操作。step 2-step 5 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        # data_clear_error=rm.get_data("清除设备错误","clear_error")
        # url=self.ws
        # print("无论是否有错误，先清除错误。")
        # c.checkAction(url,data_clear_error)
        # time.sleep(3)


        data_servo_enable=rm.get_data("伺服使能","servo_enable")
        print("step 2、伺服使能。")
        c.checkAction(url,data_servo_enable)
        time.sleep(2)


        data_script_start=rm.get_data("脚本运行控制","script_start")
        print("step 3、运行脚本：tutorial.zip.")
        t1=c.checkAction(url,data_script_start)
        self.assertEqual(t1["success"],True)
        time.sleep(5)

        data_velocity=rm.get_data("调整全局速度","adjust_velocity")
        print("step 4、调节运行速度为40%")
        t2=c.checkAction(url,data_velocity)
        self.assertEqual(t2["success"],True)
        time.sleep(5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 11、退出登录。")
        c.checkAction(url,data_logout)
        time.sleep(3)

    def test02_script_control_pause(self):
        """脚本运行控制相关操作。step 2-step 5 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_script_pause=rm.get_data("脚本运行控制","script_pause")
        print("step 5、暂停脚本运行：")
        t3=c.checkAction(url,data_script_pause)
        self.assertEqual(t3["success"],True)
        time.sleep(5)


        data_logout=rm.get_data("退出登录","logout")
        print("step 11、退出登录。")
        c.checkAction(url,data_logout)
        time.sleep(3)

    def test03_script_control(self):
        """脚本运行控制相关操作。step 6-step 10 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)


        data_script_continue=rm.get_data("脚本运行控制","script_continue")
        print("step 6、暂停后继续脚本运行：")
        t4=c.checkAction(url,data_script_continue)
        self.assertEqual(t4["success"],True)
        time.sleep(5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 、退出登录。")
        c.checkAction(url,data_logout)
        time.sleep(2)

    def test04_script_control(self):
        """脚本运行控制相关操作。step 6-step 10 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_script_emergency=rm.get_data("紧急停止","emergency_stop")
        print("step 7、运行过程中急停。")
        t=c.checkAction(url,data_script_emergency)
        self.assertEqual(t["success"],True)
        time.sleep(5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 、退出登录。")
        c.checkAction(url,data_logout)
        time.sleep(2)

    def test05_script_control(self):
        """脚本运行控制相关操作。step 6-step 10 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_script_start=rm.get_data("脚本运行控制","script_start")
        print("step 8、运行脚本：tutorial.zip.")
        t6=c.checkAction(url,data_script_start)
        self.assertEqual(t6["success"],True)
        time.sleep(5)

        data_script_stop=rm.get_data("脚本运行控制","script_stop")
        print("step 9、停止脚本运行：")
        t5=c.checkAction(url,data_script_stop)
        self.assertEqual(t5["success"],True)
        time.sleep(2)

        data_servo_disable=rm.get_data("伺服失能","servo_disable")
        print("step 10、伺服失能.")
        t7=c.checkAction(url,data_servo_disable)
        self.assertEqual(t7["success"],True)
        time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step 11、退出登录。")
        c.checkAction(url,data_logout)
        time.sleep(2)




    # def test02_script_emergency_stop(self):
    #     """脚本运行时急停 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录设备。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_clear_error=rm.get_data("清除设备错误","clear_error")
    #     url=self.ws
    #     print("无论是否有错误，先清除错误。")
    #     c.checkAction(url,data_clear_error)
    #     time.sleep(3)
    #
    #     data_servo_enable=rm.get_data("伺服使能","servo_enable")
    #     print("step 2、伺服使能。")
    #     c.checkAction(url,data_servo_enable)
    #     time.sleep(4)
    #
    #
    #     data_script_start=rm.get_data("脚本运行控制","script_start")
    #     print("step 3、运行脚本：tutorial.lua.")
    #     t=c.checkAction(url,data_script_start)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(8)
    #
    #     data_velocity=rm.get_data("调整全局速度","adjust_velocity")
    #     print("step 4、调节运行速度为40%")
    #     t=c.checkAction(url,data_velocity)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(6)
    #
    #     data_script_emergency=rm.get_data("紧急停止","emergency_stop")
    #     print("step 5、运行过程中急停。")
    #     t=c.checkAction(url,data_script_emergency)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(8)
    #
    #     data_script_start=rm.get_data("脚本运行控制","script_start")
    #     print("step 6、再次运行脚本：tutorial.lua.")
    #     t=c.checkAction(url,data_script_start)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(8)
    #
    #     data_script_stop=rm.get_data("脚本运行控制","script_stop")
    #     print("step 7、停止脚本运行：")
    #     t=c.checkAction(url,data_script_stop)
    #     self.assertEqual(t["success"],True)
    #     time.sleep(5)
    #
    #     data_servo_disable=rm.get_data("伺服失能","servo_disable")
    #     print("step 8、伺服失能.")
    #     c.checkAction(url,data_servo_disable)
    #     time.sleep(3)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 9、退出登录。")
    #     c.checkAction(url,data_logout)
    #     time.sleep(3)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()