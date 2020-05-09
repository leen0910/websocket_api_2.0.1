#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """设备标定：硬限位标定"""
    # 驱动id
    driver_id=0
    # true 最小硬限位,false 最大硬限位
    miminum=bool(1)
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

    def test01_set_hardLimit(self):
        """ 手动硬限位标定"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_set_hardLimit=rm.get_data("硬限位标定","calibration_limit_hard")
        print("step 2、硬限位标定")
        driver_id=self.driver_id
        miminum=self.miminum
        data_dict=json.loads(data_set_hardLimit)

        data_dict["data"]["driver_id"]=driver_id
        data_dict["data"]["miminum"]=miminum
        data_set_hardLimit=json.dumps(data_dict)
        t=c.checkAction(url,data_set_hardLimit)
        self.assertEqual(t["success"],True)
        print("关节:%s 的最%s 硬限位设定成功。"%(driver_id,miminum))
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(1)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
