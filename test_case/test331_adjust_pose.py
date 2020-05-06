#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """设备标定：姿态参数矫正"""
    #同一点两个姿态的关节数组
    pose1=[0,0,0,0]
    pose2=[0,0,0,0]
    point=[pose1,pose2]
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

    def test01_adjust_pose(self):
        """ 只矫正姿态"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_adjust_pose=rm.get_data("参数矫正","calibration_correct_type0_pose")
        print("step 2、姿态矫正。")
        point=self.point
        data_dict=json.loads(data_adjust_pose)

        data_dict["data"]["point"]=point
        data_adjust_pose=json.dumps(data_dict)
        t=c.checkAction(url,data_adjust_pose)
        self.assertEqual(t["success"],True)
        print("姿态矫正成功。")
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
