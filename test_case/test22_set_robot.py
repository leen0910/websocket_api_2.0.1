#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """出厂配置：配置机器型号"""
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

    def test01_set_robot(self):
        """ 配置机器型号: 目前五种机型 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_set_robot_01=rm.get_data("配置机器型号","factory_config_robot_01")
        print("step 2、配置机器型号：琦星外置4轴sacra机械臂,最大负载3kg,最大臂展600mm,z轴行程200mm,标配,花键黑色")
        t_01=c.checkAction(url,data_set_robot_01)
        self.assertEqual(t_01["success"],True)
        print("配置机器型号：01 成功。")
        time.sleep(1)

        data_set_robot_02=rm.get_data("配置机器型号","factory_config_robot_02")
        print("step 3、配置机器型号：琦星外置4轴sacra机械臂,最大负载3kg,最大臂展600mm,z轴行程200mm,标配,花键绿色")
        t_02=c.checkAction(url,data_set_robot_02)
        self.assertEqual(t_02["success"],True)
        print("配置机器型号：02 成功。")
        time.sleep(1)

        data_set_robot_09=rm.get_data("配置机器型号","factory_config_robot_09")
        print("step 4、配置机器型号：琦星外置4轴sacra机械臂,最大负载3kg,最大臂展400mm,z轴行程150mm,标配,一体")
        t_09=c.checkAction(url,data_set_robot_09)
        self.assertEqual(t_09["success"],True)
        print("配置机器型号：09 成功。")
        time.sleep(1)

        data_set_robot_10=rm.get_data("配置机器型号","factory_config_robot_10")
        print("step 5、配置机器型号：琦星外置4轴sacra机械臂,最大负载3kg,最大臂展400mm,z轴行程150mm,标配,分体")
        t_10=c.checkAction(url,data_set_robot_10)
        self.assertEqual(t_10["success"],True)
        print("配置机器型号：10 成功。")
        time.sleep(1)

        data_set_robot_21=rm.get_data("配置机器型号","factory_config_robot_21")
        print("step 6、配置机器型号：琦星外置3轴sacra机械臂,最大负载5kg,最大臂展600mm,z轴行程100mm,标配,一体")
        t_21=c.checkAction(url,data_set_robot_21)
        self.assertEqual(t_21["success"],True)
        print("配置机器型号：21 成功。")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 7、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
