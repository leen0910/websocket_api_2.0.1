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
    IO_type=["D"]
    address1=[0,1,2,3,4,5,6,7]  # uint16
    address2=[8,9,10,11,12,13,14,15,16,17,18,19,20,22,23]  #double
    address3=[21,24]  #int
    value1=[4,0,12,35,15749,22233]
    value2=[0,1.2,35.25555,3.141592678521,55,96956]
    value3=[0,-15,-135565]
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
                        print("%s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 寄存器索引地址设置失败。"%(index,address))
                    time.sleep(0.5)
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
                        print("%s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 寄存器索引地址设置失败。"%(index,address))
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
                        print("%s号机器的%s 寄存器索引地址，值设置：%s成功。"%(index,address,value))
                        data_modbus_read=json.dumps(data_dict1)
                        t1=c.checkAction(url,data_modbus_read)
                        print("%s号机器的 %s 寄存器索引地址的值读取为：%s。"%(index,address,t1["data"]["value"]))
                    else:
                        print("%s号机器的%s 寄存器索引地址设置失败。"%(index,address))
                    time.sleep(0.5)
        data_logout=rm.get_data("退出登录","logout")
        print("step 3、退出登录。")
        c.checkAction(url,data_logout)






    # def test05_read_modbus_register(self):
    #     """读取MODBUS/本机&其它设备 /读寄存器"""
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、管理员登录。")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_modbus_read=rm.get_data("读取MODBUS","io_read_modbus")
    #     print("step 2、读取寄存器。")
    #
    #     server_index=self.server_index
    #     name_list=["follow_ref_X","follow_ref_Y","follow_ref_Z","follow_ref_A","follow_ref_B","follow_ref_C","follow_dir_X","follow_dir_Y","follow_dir_Z","follow_dir_A","follow_dir_B","follow_dir_C","follow_vel","error_time","start_length","end_length","type_id"]
    #
    #     data_dict=json.loads(data_modbus_read)
    #     for index in server_index:
    #         data_dict["data"]["server_index"]=index
    #         print("modbus机器号：%s"%index )
    #         for nick_name in name_list:
    #             data_dict["data"]["nick_name"]=nick_name
    #             print("读取的寄存器地址别名：%s"%nick_name)
    #
    #             data_modbus_read=json.dumps(data_dict)
    #             t=c.checkAction(url,data_modbus_read)
    #             if t["success"]==True:
    #                 print("%s号机器的 %s 寄存器地址值读取为：%s。"%(index,nick_name,t["data"]["value"]))
    #             else:
    #                 print("%s号机器的%s 寄存器地址设置失败。"%(index,nick_name))
    #             time.sleep(0.5)
    #
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 3、退出登录。")
    #     c.checkAction(url,data_logout)

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
    for i in range(1,2):
        suite = unittest.TestSuite()
        # suite.addTest(websocket_request('setUp'))
        suite.addTest(websocket_request('test01_write_modbus_register_uint16'))
        suite.addTest(websocket_request('test02_write_modbus_register_double'))
        suite.addTest(websocket_request('test03_write_modbus_register_int'))

        # suite.addTest(websocket_request('tearDown'))
        unittest.TextTestRunner(verbosity=2).run(suite)