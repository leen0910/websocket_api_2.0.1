#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import Base_64
from common import WR_file
import time
import json




class websocket_request(unittest.TestCase):
    """文件管理/5.2 控制器接收文件"""
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


    def test01_LogFile_send(self):
        """5.1 控制器发送文件/读取所有日志文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        # log_list=['qxlog.log','qxlog_detail.log','qxlog_detail.1.log','qxlog_detail.2.log','qxlog_detail.3.log','qxlog_detail.4.log','qxlog_detail.5.log']
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\LogFile_name.txt'
        # for log_name in log_list:
        for log_name in WR_file.ReadFile(fpath):
            data_file_send=rm.get_data("控制器发送文件","file_send_log")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%log_name
            print("step 2、从设备读取log文件。")
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s log文件读取成功。"%log_name)

            print("step 3、解码后保存到files目录。")
            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+log_name
            WR_file.WriteFile_b(path,file_content)
            print("%s LOG文件保存成功。"%log_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test02_ConfigFile_send(self):
        """5.1 控制器发送文件/读取配置文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取config目录下所有配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\ConfigFile_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置安装文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_config")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取config文件。")
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("config文件：%s读取成功。"%f_name)

            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s config文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test03_TemConfig_send(self):
        """5.1 控制器发送文件/上传的但未安装的配置文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中上传的但未安装的配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\TempConfig_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_temconfig")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取config文件。")
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("TempConfig文件：%s读取成功。"%f_name)

            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s config文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test04_TemUpdate_send(self):
        """5.1 控制器发送文件/上传的但未安装的升级包 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        print("step 1、debug登录。")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中上传的但未安装的配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\TempUpdate_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_temupdate")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取temp_update文件。")
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("temp_update文件：%s读取成功。"%f_name)

            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s config文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)



    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
