#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
import time
import json

class websocket_request(unittest.TestCase):
    server_index=[0]
    IO_type="D"
    IO_type_X="X"
    IO_type_Y="Y"
    address1=[0,1,2,3,4,5,6,7] # uint16
    address2=[100,104,108,112,116,120,124,128,132,136,140,144,148,154,158,452,456,460,464,468,472,482,486,490,494,498,502,512,516,520,524,528,532,542,546,550,554,558,562,602,606,610,614,618,636,640,644,648,662,666,670,674,678,692,696,700,704,708]  #double
    address3=[152,162,400,402,404,406,408,410,412,414,450,480,510,540,600,630,660,690]  #int
    address_X=[0,1,2,3,4,5,6,100,101,102,103,104,105,106,107,108,109,110,111,112]
    address_Y=[0,1,2,3,4,5,6,7,8,9,10,11,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117]
    value1=[4,0,12,35,15749,22233]
    value2=[0,1.2,35.25555,3.141592678521,55,96956]
    value3=[0,-15,-135565,20]
    value_y=[0,1]
    """modbus通讯:robot设备，需要配置文件"""
    def setUp(self):
        rt=read_info.ReadInfo()
        web=rt.get_device_ip()
        port=rt.get_port()
        url=web+":"+port
        try:
            self.ws=create_connection(url,timeout=10)    #建立设备连接
            if self.ws.connected:
                print("服务：%s连接成功！"%url)
        except Exception as e:
            print("websocket连接失败：%s"%e)
            pass

    # def test01_modbus_connect(self):
    #     """激活modbus连接 """
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

    # def test02_write_modbus_coil_Robot(self):
    #     """设置MODBUS/本设备&其它设备/写线圈 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
    #     data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
    #     print("step 2、写入线圈。")
    #
    #     """
    #     "server_index":1,
    #     "nick_name":"output_coil_0",
    #     "value": 10
    #     """
    #     server_index=self.server_index
    #     name_list=["motor_on","motor_off","lua_start","lua_stop","lua_pause","lua_resume","brake","motion_flag","motor_speed"]
    #     values=[0,1]
    #     data_dict=json.loads(data_modbus_set)
    #     data_dict1=json.loads(data_modbus_read)
    #     for index in server_index:
    #         data_dict["data"]["server_index"]=index
    #         data_dict1["data"]["server_index"]=index
    #         print("modbus机器号：%s"%index )
    #         for nick_name in name_list:
    #             data_dict["data"]["nick_name"]=nick_name
    #             data_dict1["data"]["nick_name"]=nick_name
    #             print("写入的线圈地址别名：%s"%nick_name)
    #             for value in values:
    #                 data_dict["data"]["value"]=value
    #                 data_modbus_set=json.dumps(data_dict)
    #                 t=c.checkAction(url,data_modbus_set)
    #                 if t["success"]==True:
    #                     print("%s号机器的%s 线圈地址别名，值设置：%s成功。"%(index,nick_name,value))
    #                     data_modbus_read=json.dumps(data_dict1)
    #                     t1=c.checkAction(url,data_modbus_read)
    #                     print("%s号机器的%s 线圈地址值读取为：%s。"%(index,nick_name,t1["data"]["value"]))
    #
    #                 else:
    #                     print("%s号机器的%s 线圈地址设置失败。"%(index,nick_name))
    #                 time.sleep(0.5)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)
    #
    # def test03_read_modbus_coil(self):
    #     """读取MODBUS/本机&其它设备 /读线圈"""
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
    #     print("step 2、读取线圈。")
    #
    #     server_index=self.server_index
    #     name_list=["motor_on","motor_off","lua_start","lua_stop","lua_pause","lua_resume","brake","motion_flag","motor_speed"]
    #
    #     data_dict=json.loads(data_modbus_read)
    #     for index in server_index:
    #         data_dict["data"]["server_index"]=index
    #         print("modbus机器号：%s"%index )
    #         for nick_name in name_list:
    #             data_dict["data"]["nick_name"]=nick_name
    #             print("读取的线圈地址别名：%s"%nick_name)
    #
    #             data_modbus_read=json.dumps(data_dict)
    #             t=c.checkAction(url,data_modbus_read)
    #             if t["success"]==True:
    #                 print("%s号机器的%s 线圈地址值读取为：%s。"%(index,nick_name,t["data"]["value"]))
    #             else:
    #                 print("%s号机器的%s 线圈地址设置失败。"%(index,nick_name))
    #             time.sleep(0.5)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

    def test01_write_modbus_register_uint16(self):
        """设置MODBUS/本机&其它设备/写寄存器 /需要配置文件"""
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
        add=self.address1
        values=self.value1
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入的寄存器索引地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("Index: %s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("Index: %s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                         print("Index: %s号机器的%s 寄存器索引地址设置失败。"%(index,address))
                    time.sleep(0.2)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test02_write_modbus_register_double(self):
        """设置MODBUS/本机&其它设备/写寄存器 /需要配置文件"""
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
        add=self.address2
        values=self.value2
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入的寄存器索引地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("Index: %s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("Index: %s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("Index: %s号机器的%s 寄存器索引地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test03_write_modbus_register_int(self):
        """设置MODBUS/本机&其它设备/写寄存器 /需要配置文件"""
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
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入的寄存器索引地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("Index: %s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("Index: %s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("Index: %s号机器的%s 寄存器索引地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)


    def test04_read_modbus_input_coil(self):
        """读取MODBUS/本机&其它设备 /读input_coil"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取input_coil。")


        server_index=self.server_index
        add=self.address_X
        type=self.IO_type_X


        data_dict=json.loads(data_modbus_read)

        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict["data"]["IO_type"]="%s"%type
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                print("读取input_coil索引地址：%s"%address)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("Index: %s号机器的 %s input_coil地址值读取为：%s。"%(index,address,t["data"]["value"]))
                else:
                    print("Index: %s号机器的%s input_coil地址值读取失败。"%(index,address))
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test05_read_modbus_output_coil(self):
        """读取MODBUS/本机&其它设备 /读output_coil"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、读取output_coil。")

        server_index=self.server_index
        add=self.address_Y
        type=self.IO_type_Y

        data_dict=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict["data"]["IO_type"]="%s"%type
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                print("读取output_coil索引地址：%s"%address)

                data_modbus_read=json.dumps(data_dict)
                t=c.checkAction(url,data_modbus_read)
                if t["success"]==True:
                    print("Index: %s号机器的 %s output_coil地址值读取为：%s。"%(index,address,t["data"]["value"]))
                else:
                    print("Index: %s号机器的%s output_coil地址值读取失败。"%(index,address))
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)

    def test06_write_modbus_output_coil(self):
        """设置MODBUS/本机&其它设备/写线圈 /需要配置文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、管理员登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_modbus_set=rm.get_data("设置MODBUS","io_write_modbus")
        data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
        print("step 2、写入输出线圈。")

        """
        "server_index":1,
        "IO_type":"D",
        "address":10,
        "value":1
        """
        server_index=self.server_index
        add=self.address_Y
        values=self.value_y
        IO_type=self.IO_type_Y
        data_dict=json.loads(data_modbus_set)
        data_dict1=json.loads(data_modbus_read)
        for index in server_index:
            data_dict["data"]["server_index"]=index
            data_dict1["data"]["server_index"]=index
            data_dict["data"]["IO_type"]=IO_type
            data_dict1["data"]["IO_type"]=IO_type
            print("modbus机器号：%s"%index )
            for address in add:
                data_dict["data"]["address"]=address
                data_dict1["data"]["address"]=address
                print("写入输出线圈的地址：%s"%address)
                for value in values:
                    data_dict["data"]["value"]=value
                    data_modbus_set=json.dumps(data_dict)
                    t=c.checkAction(url,data_modbus_set)
                    if t["success"]==True:
                        print("Index: %s号机器的%s 输出线圈地址值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("Index: %s号机器的 %s 输出线圈地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("Index: %s号机器的%s 输出线圈地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)





    # def test06_modbus_disconnect(self):
    #     """断开index_server的modbus连接 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
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
    #         print("step 2、断开index_server:{}的modbus连接。".format(server_index))
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
    # unittest.main()
    for i in range(1,20):
        suite = unittest.TestSuite()
        suite.addTest(websocket_request('setUp'))
        suite.addTest(websocket_request('test01_write_modbus_register_uint16'))
        suite.addTest(websocket_request('test02_write_modbus_register_double'))
        suite.addTest(websocket_request('test03_write_modbus_register_int'))
        suite.addTest(websocket_request('test04_read_modbus_input_coil'))
        suite.addTest(websocket_request('test05_read_modbus_output_coil'))
        suite.addTest(websocket_request('test06_write_modbus_output_coil'))
        suite.addTest(websocket_request('tearDown'))
        unittest.TextTestRunner(verbosity=2).run(suite)