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
        files=["motion_param_config.json","lua.json","device_custom.json","modbus_info.json"]


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

    def test02_file_recovery_all(self):
        """控制器配置文件恢复:is_all=true 恢复OPTIONAL下所有文件,当前仅支持[device_custom.json/modbus_info.json/motion_param_config.json/lua.json],不包含SUPPORT下的子文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_recovery=rm.get_data("控制器配置文件恢复","file_recovery")
        print("step 2、控制配置文件恢复：")

        data_dict=json.loads(data_file_recovery)

        data_dict["data"]["is_all"]=bool(1)
        print("恢复所有文件。" )
        data_file_recovery=json.dumps(data_dict)
        t=c.checkAction(url,data_file_recovery)
        if t["success"]==True:
            print("恢复所有文件成功")
        else:
            print("恢复所有文件失败")
        time.sleep(0.1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()

