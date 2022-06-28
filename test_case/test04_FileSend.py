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
    """文件管理/1. 控制器发送文件"""
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

    # def test01_ScriptFile_send(self):
    #     """1. 控制器发送文件/脚本文件/读取一个脚本文件"""
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_send=rm.get_data("控制器发送文件","file_send_script")
    #     print("step 2、从设备读取脚本文件test.zip：")
    #     t=c.checkAction(url,data_file_send)
    #     time.sleep(1)
    #     self.assertEqual(t["success"],True)
    #
    #     print("step 3、解码后保存到files目录。")
    #     str=t["data"]["value"]
    #     file_content=Base_64.decode_b(str)
    #     # print("内容：%s"%file_content)
    #     path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\test.zip'
    #     WR_file.WriteFile_b(path,file_content)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 4、释放设备：")
    #     c.checkAction(url,data_logout)

    # def test02_ConfigFile_send(self):
    #     """1. 控制器发送文件/配置文件/读取一个配置文件 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     data_file_send=rm.get_data("控制器发送文件","file_send_config")
    #     print("step 2、从设备读取配置文件：lua.json ")
    #     t=c.checkAction(url,data_file_send)
    #     time.sleep(1)
    #     self.assertEqual(t["success"],True)
    #
    #     print("step 3、解码后保存到files目录。")
    #     str=t["data"]["value"]
    #     file_content=Base_64.decode_b(str)
    #     path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\lua.json'
    #     WR_file.WriteFile_b(path,file_content)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 4、释放设备：")
    #     c.checkAction(url,data_logout)

    # def test03_LogFile_send(self):
    #     """1. 控制器发送文件/日志文件/读取日志文件 """
    #     rm=read_message.ReadMessage()
    #     data_login=rm.get_data("登录设备","login_admin")
    #     url=self.ws
    #     print("step 1、控制设备：")
    #     c.checkAction(url,data_login)
    #     time.sleep(1)
    #
    #     log_list=['qxlog.log','qxlog_detail.log','qxlog_detail.1.log','qxlog_detail.2.log','qxlog_detail.3.log','qxlog_detail.4.log','qxlog_detail.5.log']
    #     for log_name in log_list:
    #         data_file_send=rm.get_data("控制器发送文件","file_send_log")
    #         data_dict=json.loads(data_file_send)
    #         data_dict["data"]["file_name"]="%s"%log_name
    #         print("step 2、从设备读取配置文件："+data_dict["data"]["file_name"])
    #         t=c.checkAction(url,data_file_send)
    #         time.sleep(1)
    #         self.assertEqual(t["success"],True)
    #         print("%s log文件读取成功。"%log_name)
    #
    #         print("step 3、解码后保存到files目录。")
    #         str=t["data"]["value"]
    #         file_content=Base_64.decode_b(str)
    #         path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+log_name
    #         WR_file.WriteFile_b(path,file_content)
    #         print("%s LOG文件保存成功。"%log_name)
    #
    #     data_logout=rm.get_data("退出登录","logout")
    #     print("step 4、释放设备：")
    #     c.checkAction(url,data_logout)


    def test03_LogFile_send_all(self):
        """1. 控制器发送文件/日志文件/读取日志文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取log目录下所有配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\LogFile_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置日志文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_log")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取log文件：%s 。"%f_name)
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s log文件读取成功。"%f_name)
            time.sleep(0.2)
            print("获取: %s log文件总包个数。"%f_name)
            num=t["data"]["total"]
            print("%s : log文件包数：%s。"%(f_name,num))
            log_index=1
            str=""
            for i in range(num):
                data_dict["data"]["index"]=log_index
                data_file_send=json.dumps(data_dict)
                t=c.checkAction(url,data_file_send)
                str=str+t["data"]["value"]
                log_index=log_index+1
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s log文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)




    def test04_ConfigFile_send_all(self):
        """1. 控制器发送文件/配置文件/读取所有配置文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取config目录下所有配置文件。 ")
        print("step 3、解码后保存到files目录。")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\ConfigFile_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置配置文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_config")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取config文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s config文件读取成功。"%f_name)

            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s config文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test05_Script_send_all(self):
        """1. 控制器发送文件/脚本文件/读取所有脚本文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取PROGRAME目录下所有脚本文件。 ")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\ScriptFile_name.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置脚本文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_script")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取脚本文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s 脚本文件读取成功。"%f_name)

            print("step 3、解码后保存到files目录。")
            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s 脚本文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test06_Expansion_send_all(self):
        """1. 控制器发送文件/脚本文件/读取所有expansion文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取PROGRAME/EXPANSION目录下所有脚本文件。 ")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\Expansion.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置expansion文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_expansion")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取expansion文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s expansion文件读取成功。"%f_name)

            print("step 3、解码后保存到files目录。")
            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s 脚本文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test07_ConfigFile_send_zip(self):
        """当缺失file_name时，返回Config类型的所有文件的zip包: config.zip"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取config目录下所有文件:config.zip. ")
        print("step 3、解码后保存到files目录。")

        """保存文件"""
        data_file_send=rm.get_data("控制器发送文件","file_send_config_zip")
        print("开始读取config.zip文件")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)
        print("config.zip文件读取成功。")

        str=t["data"]["value"]
        file_content=Base_64.decode_b(str)
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+"config.zip"
        WR_file.WriteFile_b(path,file_content)
        print("config.zip文件保存成功。")

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test08_Expansion_send_zip(self):
        """当缺失file_name时，返回Expansion类型的所有文件的zip包: expansion.zip"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取config目录下所有文件:expansion.zip. ")
        print("step 3、解码后保存到files目录。")

        """保存文件"""
        data_file_send=rm.get_data("控制器发送文件","file_send_expansion_zip")
        print("开始读取expansion.zip文件")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)
        print("config.zip文件读取成功。")

        str=t["data"]["value"]
        file_content=Base_64.decode_b(str)
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+"expansion.zip"
        WR_file.WriteFile_b(path,file_content)
        print("expansion.zip文件保存成功。")

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)



    def test09_global_script_send_all(self):
        """1. 控制器发送文件/脚本文件/读取所有global文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取PROGRAME/global目录下所有脚本文件。 ")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\global_script.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置global文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_global_script")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取global文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s global文件读取成功。"%f_name)

            print("step 3、解码后保存到files目录。")
            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s global文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test10_global_script_send_zip(self):
        """当缺失file_name时，返回global类型的所有文件的zip包: global.zip"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取global目录下所有文件:global.zip. ")
        print("step 3、解码后保存到files目录。")

        """保存文件"""
        data_file_send=rm.get_data("控制器发送文件","file_send_global_script_zip")
        print("开始读取global.zip文件")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)
        print("global.zip文件读取成功。")

        str=t["data"]["value"]
        file_content=Base_64.decode_b(str)
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+"global.zip"
        WR_file.WriteFile_b(path,file_content)
        print("global.zip文件保存成功。")

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test11_sub_script_send_all(self):
        """1. 控制器发送文件/脚本文件/读取所有sub_script文件 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取PROGRAME/sub_script目录下所有脚本文件。 ")
        fpath='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\sub_script.txt'
        for f_name in WR_file.ReadFile(fpath):
            """重新设置sub_script文件名"""
            data_file_send=rm.get_data("控制器发送文件","file_send_sub_script")
            data_dict=json.loads(data_file_send)
            data_dict["data"]["file_name"]="%s"%f_name
            print("开始读取sub_script文件："+data_dict["data"]["file_name"])
            data_file_send=json.dumps(data_dict)
            t=c.checkAction(url,data_file_send)
            time.sleep(1)
            self.assertEqual(t["success"],True)
            print("%s sub_script文件读取成功。"%f_name)

            print("step 3、解码后保存到files目录。")
            str=t["data"]["value"]
            file_content=Base_64.decode_b(str)
            path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+f_name
            WR_file.WriteFile_b(path,file_content)
            print("%s sub_script文件保存成功。"%f_name)

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)

    def test12_sub_script_send_zip(self):
        """当缺失file_name时，返回sub_script类型的所有文件的zip包: sub_script.zip"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、从设备中读取sub_script目录下所有文件:sub_script.zip. ")
        print("step 3、解码后保存到files目录。")

        """保存文件"""
        data_file_send=rm.get_data("控制器发送文件","file_send_sub_script_zip")
        print("开始读取sub_script.zip文件")
        t=c.checkAction(url,data_file_send)
        time.sleep(1)
        self.assertEqual(t["success"],True)
        print("sub_script.zip文件读取成功。")

        str=t["data"]["value"]
        file_content=Base_64.decode_b(str)
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\'+"sub_script.zip"
        WR_file.WriteFile_b(path,file_content)
        print("sub_script.zip文件保存成功。")

        data_logout=rm.get_data("退出登录","logout")
        print("step 4、释放设备：")
        c.checkAction(url,data_logout)




    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
