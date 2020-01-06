#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    server_index=[1]


    """modbus通讯"""
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

    def test01_modbus_connect(self):
        """激活modbus：台达PLC连接 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data_modbus_connect=rm.get_data("Modbus连接","io_modbus_connect")
        print("step 2、激活配置文件的modbus连接。")

        index_list=self.server_index

        data_dict=json.loads(data_modbus_connect)
        for server_index in index_list:
            data_dict["data"]["server_index"]=server_index
            data_modbus_connect=json.dumps(data_dict)
            t=c.checkAction(url,data_modbus_connect)
            self.assertEqual(t["success"],True)
            print("成功激活modbus连接：%s"%server_index)
            time.sleep(1)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test02_read_modbus_coil(self):
        """读取MODBUS/台达PLC /读线圈"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取线圈。")

        server_index=self.server_index
        name_list=["input_coil_0","X0","input_coil_1","X1","input_coil_2","X2","input_coil_3","X3","input_coil_4","X4","input_coil_5","X5","input_coil_6","X6","input_coil_7","X7","input_coil_8","X8","input_coil_9","X9","input_coil_10","X10","input_coil_11","X11","input_coil_12","X12","input_coil_13","X13","input_coil_14","X14","input_coil_15","X15","input_coil_16","X16","input_coil_17","X17","input_coil_18","X18","input_coil_19","X19","input_coil_20","X20","input_coil_21","X21","input_coil_22","X22","input_coil_23","X23","input_coil_24","X24","input_coil_25","X25","input_coil_26","X26","input_coil_27","X27"]

        data_dict=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for nick_name in name_list:
                data_dict["data"]["nick_name"]=nick_name
                print("读取的线圈地址别名：%s"%nick_name)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("%s号机器的%s 线圈地址值读取为：%s。"%(index,nick_name,t["data"]["value"]))
                else:
                    print("%s号机器的%s 线圈地址设置失败。"%(index,nick_name))
                time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test03_write_modbus_coil_Robot(self):
        """设置MODBUS/台达PLC/写线圈 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        print("step 2、写入线圈。")

        """
        "server_index":1,
        "nick_name":"output_coil_0",
        "value": 10
        """
        server_index=self.server_index
        name_list=["output_coil_0","Y0","output_coil_1","Y1","output_coil_2","Y2","output_coil_3","Y3","output_coil_4","Y4","output_coil_5","Y5","output_coil_6","Y6","output_coil_7","Y7","output_coil_8","Y8","output_coil_9","Y9","output_coil_10","Y10","output_coil_11","Y11","output_coil_12","Y12","output_coil_13","Y13","output_coil_14","Y14","output_coil_15","Y15","output_coil_16","Y16"]
        values=[0,1]
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for nick_name in name_list:
                data_dict["data"]["nick_name"]=nick_name
                data_dict1["data"]["nick_name"]=nick_name
                print("写入的线圈地址别名：%s"%nick_name)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s 线圈地址别名，值设置：%s成功。"%(index,nick_name,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的%s 线圈地址值读取为：%s。"%(index,nick_name,t1["data"]["value"]))

                    else:
                        print("%s号机器的%s 线圈地址设置失败。"%(index,nick_name))
                    time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)



    def test04_modbus_disconnect(self):
        """断开index_server的modbus连接 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data_modbus_connect=rm.get_data("Modbus断开连接","io_modbus_disconnect")
        url=self.ws

        index_list=self.server_index
        data_dict=json.loads(data_modbus_connect)
        for server_index in index_list:
            data_dict["data"]["server_index"]=server_index
            data_modbus_connect=json.dumps(data_dict)
            print("step 2、断开index_server:%s的modbus连接。"%server_index)
            t=c.checkAction(url,data_modbus_connect)
            self.assertEqual(t["success"],True)
            time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()