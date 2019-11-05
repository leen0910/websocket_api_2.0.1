#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
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
        """激活modbus连接 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        rm=read_message.ReadMessage()
        data_modbus_connect=rm.get_data("Modbus连接","io_modbus_connect")
        print("step 2、激活配置文件的modbus连接。")

        index_list=[0,1,2]

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
        """读取MODBUS/本机&其它设备 /读线圈"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取线圈。")

        server_index=[0,2]
        name_list=["input_coil_0","X0","input_coil_1","X1"]

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
        """设置MODBUS/本设备&其它设备/写线圈 """
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
        server_index=[0,2]
        name_list=["output_coil_0","Y0","output_coil_1","Y1"]
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


    def test04_read_modbus_register(self):
        """读取MODBUS/本机&其它设备 /读寄存器"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取寄存器。")

        server_index=[0,2]
        name_list=["input_reg_0","C0","input_reg_1","C1"]

        data_dict=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for nick_name in name_list:
                data_dict["data"]["nick_name"]=nick_name
                print("读取的寄存器地址别名：%s"%nick_name)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("%s号机器的 %s 寄存器地址值读取为：%s。"%(index,nick_name,t["data"]["value"]))
                else:
                    print("%s号机器的%s 寄存器地址设置失败。"%(index,nick_name))
                time.sleep(0.5)


        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test05_write_modbus_register(self):
        """设置MODBUS/本机&其它设备/写寄存器 """
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
        "nick_name":"output_coil_0",
        "value": 10
        """
        server_index=[0,2]
        name_list=["output_reg_0","D0","output_reg_1","D1"]
        values=[3541,15.234]
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for nick_name in name_list:
                data_dict["data"]["nick_name"]=nick_name
                data_dict1["data"]["nick_name"]=nick_name
                print("写入的寄存器地址别名：%s"%nick_name)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("%s号机器的%s 寄存器地址别名，值设置：%s成功。"%(index,nick_name,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 寄存器地址值读取为：%s。"%(index,nick_name,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 寄存器地址设置失败。"%(index,nick_name))
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