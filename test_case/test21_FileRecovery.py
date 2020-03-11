#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """控制器配置文件恢复"""
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

    def test01_file_recovery(self):
        """控制器配置文件恢复 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_recovery=rm.get_data("控制器配置文件恢复","file_recovery")
        print("step 2、控制配置文件恢复：")
        files=["motion_param_config.json","modbus_own_qxrobot.json","modbus_other_qxrobot.json","modbus_qxVision.json","modbus_Delta_plc.json","permission.json","local_option_io.json","IO_bind.json","bus_connect.json","modbus_4_way_relay.json","bus_extio_can_v2.json","bus_extio_can_v1.json","modbus_DAQM_4302.json","modbus_8_way_relay.json"]


        data_dict=json.loads(data_file_recovery)
        for file in files:
            data_dict["data"]["file_name"]=file
            print("恢复的控制配置文件：%s"%file )
            data_file_recovery=json.dumps(data_dict)
            t=c.checkAction(url,data_file_recovery)
            if t["success"]==True:
                print("控制配置文件：%s 恢复成功"%file)
            else:
                print("控制配置文件：%s 恢复失败"%file)
            time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()