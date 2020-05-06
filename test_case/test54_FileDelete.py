#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json


class websocket_request(unittest.TestCase):
    """5.4 控制器删除文件"""
    # 要移除的文件类型:
    type="temp_config"  # 要移除的文件类型[temp_config/temp_update/log]
    # 要移除的文件名:
    file_name="123"

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

    def test01_FileRemove(self):
        """5.4 控制器删除文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_delete=rm.get_data("控制器删除文件","file_remove")
        print("step 2、删除文件。")
        type=self.type
        file_name=self.file_name
        data_dict=json.loads(data_file_delete)
        data_dict["data"]["type"]="%s"%type
        data_dict["data"]["file_name"]="%s"%file_name
        data_file_delete=json.dumps(data_dict)
        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        print("删除type: %s，文件：%s 成功。"%(type,file_name))
        time.sleep(1)


        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
