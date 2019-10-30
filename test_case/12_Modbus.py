#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    """与index=3设备之间的modbus通讯"""
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
        """激活index_server:3的modbus连接 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)


        rm=read_message.ReadMessage()
        data_modbus_connect=rm.get_data("Modbus连接","io_modbus_connect")
        url=self.ws
        print("step 2、激活index_server:3的modbus连接。")
        t=c.checkAction(url,data_modbus_connect)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test02_write_modbus_coil(self):
        """设置MODBUS/设备之间/写线圈 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        print("step 2、写入线圈。")
        # "agreement":"T",
        # "server_index":3,
        # "type":0,
        # "address":20,
        # "value":10
        agreement=["T","R","A"]
        server_index=[0,3]
        type=1
        address=[2,20,120,300]
        value=[0,1]
        data_dict=json.loads(data_modbus_set)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address1 in address:
                data_dict["data"]["address"]=address1
                print("写入的线圈地址：%s"%address1)
                for values in value:
                    data_dict["data"]["value"]=values
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s地址值设置：%s成功。"%(index,address1,values))
                    else:
                        print("%s号机器的%s地址设置失败。"%(index,address1))
                    time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test03_read_modbus_coil(self):
        """读取MODBUS/设备之间 /读线圈"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取线圈。")
        # "agreement":"T",
        # "server_index":3,
        # "type":0,
        # "address":20
        server_index=[0,3]
        type=0
        address=[2,20,120,300]

        data_dict=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address1 in address:
                data_dict["data"]["address"]=address1
                print("读取的线圈地址：%s"%address1)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("%s号机器的%s地址值读取为：%s。"%(index,address1,t["data"]["value"]))
                else:
                    print("%s号机器的%s地址设置失败。"%(index,address1))
                time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test04_write_modbus_register(self):
        """设置MODBUS/设备之间/写寄存器 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        print("step 2、写入寄存器。")
        # "agreement":"T",
        # "server_index":3,
        # "type":0,
        # "address":20,
        # "value":10
        agreement=["T","R","A"]
        server_index=[0,3]
        type=3
        address=[2,20,120,300]
        value=[3,49,100,2684]
        data_dict=json.loads(data_modbus_set)
        data_dict["data"]["type"]=type
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address1 in address:
                data_dict["data"]["address"]=address1
                print("写入的寄存器地址：%s"%address1)
                for values in value:
                    data_dict["data"]["value"]=values
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s地址值设置：%s成功。"%(index,address1,values))
                    else:
                        print("%s号机器的%s地址设置失败。"%(index,address1))
                    time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test05_read_modbus_register(self):
        """读取MODBUS/设备之间 /读寄存器"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取寄存器。")
        # "agreement":"T",
        # "server_index":3,
        # "type":0,
        # "address":20
        server_index=[0,3]
        type=2
        address=[2,20,120,300]

        data_dict=json.loads(data_modbus_read)
        data_dict["data"]["type"]=type
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address1 in address:
                data_dict["data"]["address"]=address1
                print("读取的寄存器地址：%s"%address1)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("%s号机器的%s地址值读取为：%s。"%(index,address1,t["data"]["value"]))
                else:
                    print("%s号机器的%s地址设置失败。"%(index,address1))
                time.sleep(0.5)

        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test06_modbus_disconnect(self):
        """断开index_server:3的modbus连接 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)


        rm=read_message.ReadMessage()
        data_modbus_connect=rm.get_data("Modbus断开连接","io_modbus_disconnect")
        url=self.ws
        print("step 2、断开index_server:3的modbus连接。")
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