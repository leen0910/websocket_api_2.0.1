#!/usr/bin/python
'''
./    当前目录（当前文件）
../  上级目录（上级文件）
'''
from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import Base_64
from common import split_read as s
from common import to_md5
from common import to_zip
import time
import json




class ReceiveFiles(unittest.TestCase):
    """当type为config时指定index值，index为1代表modbus子文件，为0代表其他配置文件"""
    filename0=["modbus_info.json","motion_param_config.json","lua.json","device_custom.json"]
    # filenameX=["io_extend.json","io_local.json","io_bind.json","motion_base_config.json","device_info.json","driver_config.json"]
    filename1=["modbus_1_reg_config.json","modbus_2_reg_config.json", "modbus_3_reg_config.json", "modbus_4_reg_config.json", "modbus_5_reg_config.json", "modbus_6_reg_config.json"]
    filename_base=["device_info.json","driver_config.json","io_extend.json","io_local.json","motion_base_config.json"]
    path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'  #需要写入设备端的文件的目录

    size=300*1024    #分包大小
    type="config"       #发送文件类型

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

    def test01_ConfigFiles_0(self):
        """写入安装控制器配置文件index=0的文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        filename0=self.filename0
        type=self.type

        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        for filename in filename0:
            path=self.path+filename

            print("step 2、向设备发送config文件：%s"%filename)

            """分包写入文件"""
            Block_Size=self.size
            total=s.total_count_b(path,Block_Size)
            str_md5=s.read_a_file_b(path)
            md5=to_md5.md5_b(str_md5)
            print("总包数为：%s"%total)
            index=1
            for content in s.read_file_b(path,Block_Size):
                str=content
                script_base64=Base_64.encode_b(str)
                data_file={
                    "action":"file.receive",
                    "data":{
                        "type":type,
                        "file_name":filename,
                        "total":total,
                        "index":index,
                        "md5":"%s"%md5,
                        "value":script_base64
                        }
                    }
                data_file=json.dumps(data_file)
                c.checkAction(url,data_file)
                index=index+1
                # print(script_base64)


            data_install_script=rm.get_data("控制器安装文件","file_install_script")

            """重新设置安装文件名"""
            data_dict=json.loads(data_install_script)
            data_dict["data"]["index"]=0
            data_dict["data"]["type"]="%s"%type
            data_dict["data"]["file_name"]="%s"%filename
            # print("安装文件："+data_dict["data"]["file_name"])
            data_install_script=json.dumps(data_dict)
            # print(data_install_script)

            print("step 3、安装index=0：%s文件"%filename)
            c.checkAction(url,data_install_script)
            time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step、释放设备：")
        c.checkAction(url,data_logout)

    def test02_ConfigFiles_1(self):
        """写入安装控制器配置文件index=1的文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        filename1=self.filename1
        type=self.type

        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        for filename in filename1:
            path=self.path+filename

            print("step 2、向设备发送config文件：%s"%filename)

            """分包写入文件"""
            Block_Size=self.size
            total=s.total_count_b(path,Block_Size)
            str_md5=s.read_a_file_b(path)
            md5=to_md5.md5_b(str_md5)
            print("总包数为：%s"%total)
            index=1
            for content in s.read_file_b(path,Block_Size):
                str=content
                script_base64=Base_64.encode_b(str)
                data_file={
                    "action":"file.receive",
                    "data":{
                        "type":type,
                        "file_name":filename,
                        "total":total,
                        "index":index,
                        "md5":"%s"%md5,
                        "value":script_base64
                        }
                    }
                data_file=json.dumps(data_file)
                c.checkAction(url,data_file)
                index=index+1
                # print(script_base64)


            data_install_script=rm.get_data("控制器安装文件","file_install_script")

            """重新设置安装文件名"""
            data_dict=json.loads(data_install_script)
            data_dict["data"]["index"]=1
            data_dict["data"]["type"]="%s"%type
            data_dict["data"]["file_name"]="%s"%filename
            # print("安装文件："+data_dict["data"]["file_name"])
            data_install_script=json.dumps(data_dict)
            # print(data_install_script)

            print("step 3、安装index=1：%s文件"%filename)
            c.checkAction(url,data_install_script)
            time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step、释放设备：")
        c.checkAction(url,data_logout)

    def test03_ConfigFiles_base(self):
        """debug帐号，写入base目录"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        filename_base=self.filename_base
        type=self.type

        print("step 1、debug权限登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        for filename in filename_base:
            path=self.path+filename

            print("step 2、向设备发送config文件：%s"%filename)

            """分包写入文件"""
            Block_Size=self.size
            total=s.total_count_b(path,Block_Size)
            str_md5=s.read_a_file_b(path)
            md5=to_md5.md5_b(str_md5)
            print("总包数为：%s"%total)
            index=1
            for content in s.read_file_b(path,Block_Size):
                str=content
                script_base64=Base_64.encode_b(str)
                data_file={
                    "action":"file.receive",
                    "data":{
                        "type":type,
                        "file_name":filename,
                        "total":total,
                        "index":index,
                        "md5":"%s"%md5,
                        "value":script_base64
                        }
                    }
                data_file=json.dumps(data_file)
                c.checkAction(url,data_file)
                index=index+1
                # print(script_base64)


            data_install_script=rm.get_data("控制器安装文件","file_install_script")

            """重新设置安装文件名"""
            data_dict=json.loads(data_install_script)
            data_dict["data"]["index"]=0
            data_dict["data"]["type"]="%s"%type
            data_dict["data"]["file_name"]="%s"%filename
            # print("安装文件："+data_dict["data"]["file_name"])
            data_install_script=json.dumps(data_dict)
            # print(data_install_script)

            print("step 3、安装index=0：%s文件"%filename)
            c.checkAction(url,data_install_script)
            time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step、释放设备：")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # t=ReceiveFiles()
    # t.setUp()
    # for i in range(1,100):
    #     t.test_ReceiveFiles()
    # for i in range(1,5):
    #     suite = unittest.TestSuite()
    #     suite.addTest(websocket_request('test01_read_io'))
    #     suite.addTest(websocket_request('test02_write_io_off'))
    #     suite.addTest(websocket_request('test03_write_io_on'))
    #     suite.addTest(websocket_request('test04_read_io_default'))
    #     suite.addTest(websocket_request('test05_write_io_default_off'))
    #     suite.addTest(websocket_request('test06_write_io_default_on'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)