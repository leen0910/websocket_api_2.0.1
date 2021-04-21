#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json
import os


class websocket_request(unittest.TestCase):
    filename="test.zip"    #要移除的文件名
    type="script"   #要移除的文件类型[script/config/temp_script/temp_config/temp_update/expansion/global/sub_script]
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

    def test01_FileRemove_script(self):
        """4.控制器删除文件 """
        type=self.type
        filename=self.filename

        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)
        """重新设置删除文件名，文件类型"""

        data_file_delete=rm.get_data("控制器删除文件","file_remove_script")

        data_dict=json.loads(data_file_delete)
        data_dict["data"]["type"]="%s"%type
        data_dict["data"]["file_name"]="%s"%filename
        data_file_delete=json.dumps(data_dict)

        print("step 2、删除 %s类型的 %s文件。"%(type,filename))

        t=c.checkAction(url,data_file_delete)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、释放设备：")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # f=websocket_request()
    # f.test031_reduce_test01()