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
    IO_type=["X","Y","C","D"]
    address1=[1024,1025,1026,1027,1028,1029,1030,1031]  #输入线圈地址

    address2=[1280,1281,1282,1283,1284,1285,1286,1287,2048,45056]  #输出线圈地址
    value2=[1,0]

    address3=[4096,36864]  #输出寄存器地址
    value3=[5,333,18356]
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

    # def test01_modbus_connect(self):
    #     """激活modbus：台达PLC连接 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     rm=read_message.ReadMessage()
    #     data_modbus_connect=rm.get_data("Modbus连接","io_modbus_connect")
    #     print("step 2、激活配置文件的modbus连接。")
    #
    #     index_list=self.server_index
    #
    #     data_dict=json.loads(data_modbus_connect)
    #     for server_index in index_list:
    #         data_dict["data"]["server_index"]=server_index
    #         data_modbus_connect=json.dumps(data_dict)
    #         t=c.checkAction(url,data_modbus_connect)
    #         self.assertEqual(t["success"],True)
    #         print("成功激活modbus连接：%s"%server_index)
    #         time.sleep(1)
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

    def test01_read_modbus_coil(self):
        """读取MODBUS/台达PLC /读线圈"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读线圈。")

        """
        "server_index":1,
        "IO_type":"D",
        "address":10
        """
        server_index=self.server_index
        add=self.address1
        data_dict1=json.loads(data_modbus_read)
        data_dict1["data"]["IO_type"]="X"
        for index in server_index:
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict1["data"]["address"]=address
                print("读取线圈地址：%s"%address)
                data_modbus_read=json.dumps(data_dict1)
                t1=c.checkAction(url,data_modbus_read)
                if t1["success"]==True:
                    print("%s号机器的 %s 线圈地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                else:
                    print("%s号机器的%s 线圈地址读取失败。"%(index,address))
            time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test02_write_modbus_coil(self):
        """设置MODBUS/台达PLC/写线圈 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、写入线圈。")

        """
        "server_index":1,
        "IO_type":"D",
        "address":10,
        "value":1
        """
        server_index=self.server_index
        add=self.address2
        values=self.value2
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        data_dict["data"]["IO_type"]="Y"
        data_dict1["data"]["IO_type"]="Y"
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入的线圈地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s 线圈地址，值设置：%s 成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 线圈地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 线圈地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test03_write_modbus_register(self):
        """设置MODBUS/台达PLC/写寄存器 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、写入寄存器。")

        """
        "server_index":1,
        "IO_type":"D",
        "address":10,
        "value":1
        """
        server_index=self.server_index
        add=self.address3
        values=self.value3
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        data_dict["data"]["IO_type"]="D"
        data_dict1["data"]["IO_type"]="D"
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入的寄存器地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s 寄存器地址，值设置：%s 成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 寄存器地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 寄存器地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    # def test04_modbus_disconnect(self):
    #     """断开index_server的modbus连接 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     rm=read_message.ReadMessage()
    #     data_modbus_connect=rm.get_data("Modbus断开连接","io_modbus_disconnect")
    #     url=self.ws
    #
    #     index_list=self.server_index
    #     data_dict=json.loads(data_modbus_connect)
    #     for server_index in index_list:
    #         data_dict["data"]["server_index"]=server_index
    #         data_modbus_connect=json.dumps(data_dict)
    #         print("step 2、断开index_server:%s的modbus连接。"%server_index)
    #         t=c.checkAction(url,data_modbus_connect)
    #         self.assertEqual(t["success"],True)
    #         time.sleep(1)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()