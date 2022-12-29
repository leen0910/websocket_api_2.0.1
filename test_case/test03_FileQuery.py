#!/usr/bin/python

from websocket import create_connection
import unittest
from common import read_info
from common import read_message
from common import check_action as c
from common import WR_file
import os
import time




class websocket_request(unittest.TestCase):
    """文件管理/5. 控制器查询文件列表"""
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

    def test01_FileQuery_script(self):
        """5. 控制器查询文件列表/查询script目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_script")
        print("step 2、查询script目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出script目录脚本名称：")
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\ScriptFile_name.txt'
        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件

        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、script脚本文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test02_FileQuery_config(self):
        """5. 控制器查询文件列表/查询config目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_config")
        print("step 2、查询config目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出config目录文件名称：")
        # files=t["data"]["file_list"]
        # file_list=list(files)
        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\ConfigFile_name.txt'
        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件


        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、config文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test03_FileQuery_log(self):
        """5. 控制器查询文件列表/查询log目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_log")
        print("step 2、查询log目录。")
        t=c.checkAction(url,data_file_query)
        print(t)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出log目录文件名称：")
        # files=t["data"]["file_list"]
        # file_list=list(files)
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\LogFile_name.txt'

        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件

        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、log文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test04_FileQuery_temp_script(self):
        """5. 控制器查询文件列表/查询temp_script目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_temp_script")
        print("step 2、查询temp_script目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出temp_script目录文件名称：")
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\TempScript_name.txt'
        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件
        # files=t["data"]["file_list"]
        # file_list=list(files)


        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、temp_script文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test05_FileQuery_temp_config(self):
        """5. 控制器查询文件列表/查询temp_config目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_temp_config")
        print("step 2、查询temp_config目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出temp_config目录文件名称：")
        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\TempConfig_name.txt'
        if os.path.exists(path):
            os.remove(path)   # 先删除之前写过的文件
        # files=t["data"]["file_list"]
        # file_list=list(files)


        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、temp_config文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test06_FileQuery_temp_update(self):
        """5. 控制器查询文件列表/查询temp_update目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_temp_update")
        print("step 2、查询temp_update目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出temp_update目录文件名称：")

        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\TempUpdate_name.txt'

        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件


        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、temp_update文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)


    def test07_FileQuery_expansion(self):
        """5. 控制器查询文件列表/查询expansion目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_expansion")
        print("step 2、查询Expansion目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出Expansion目录文件名称：")

        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\Expansion.txt'

        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件


        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入脚本文件名
        print("step 4、expansion文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def test08_FileQuery_global_script(self):
        """5. 控制器查询文件列表/查询global目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_global_script")
        print("step 2、查询global_script目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出global目录文件名称：")

        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\global_script.txt'

        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件


        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id<num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入文件名
        print("step 4、global文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)


    def test09_FileQuery_sub_script(self):
        """5. 控制器查询文件列表/查询sub_script目录 """
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        print("step 1、控制设备：")
        c.checkAction(url,data_login)
        time.sleep(1)

        data_file_query=rm.get_data("控制器查询文件列表","file_query_sub_script")
        print("step 2、查询sub_script目录。")
        t=c.checkAction(url,data_file_query)
        self.assertEqual(t["success"],True)
        time.sleep(1)

        print("step 3、列出sub_script目录文件名称：")

        path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\files\\sub_script.txt'

        if os.path.exists(path):
            os.remove(path)   #先删除之前写过的文件

        num=len(t['data']["file_list"])
        id=0
        file_list=[]
        while id < num:
            file_list.append(t['data']["file_list"][id]["file_name"])
            id=id+1

        for file in file_list:
            print(file)
            WR_file.WriteFile_add(path,file)    #追加写入文件名
        print("step 4、sub_script文件名保存到文件: %s。"%path)

        data_logout=rm.get_data("退出登录","logout")
        print("step 5、释放设备：")
        c.checkAction(url,data_logout)

    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()


