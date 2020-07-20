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
    """向设备端写入文件"""
    filename="plug.lua"    #写入文件的名字
    path='C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\scripts\\A到B插件.lua'  #需要写入设备端的文件

    #C:\Users\test\AppData\Local\Programs\Python\Python36\autotest\websocket_api_2.0\scripts\400_arc.lua

    i=0  #当type为script时需要指定安装的序号，取值范围[0-20)；当type为config时指定index值，index为1代表modbus子文件，为0代表其他配置文件
    size=300*1024    #分包大小
    type="expansion"       #发送文件类型  script/config/update/expansion   类型为expansion时需要debug权限操作安装和删除
    source_dir="C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\test"  #需要打包生成zip的文件目录
    output_filename="C:\\Users\\test\\AppData\\Local\\Programs\\Python\\Python36\\autotest\\websocket_api_2.0\\test.zip"     #zip文件的输出目录
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

    def test_ReceiveFiles(self):
        """控制器接收文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_debug")
        url=self.ws
        path=self.path
        filename=self.filename
        type=self.type
        source_dir=self.source_dir
        output_filename=self.output_filename
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        # print("step 2、生成zip文件。")
        # to_zip.make_zip(source_dir, output_filename)
        # time.sleep(3)

        print("step 3、向设备发送zip脚本文件：")

        # """一个总包直接传输文件"""
        # f=open(path,'r',encoding='utf-8')
        # str=f.read()
        # script_base64=Base_64.encode(str)
        # f.close()
        # data_file={
        #     "action":"device.file.receive",
        #     "data":{
        #         "type":"script",
        #         "file_name":filename,
        #         "md5":"",
        #         "total":1,
        #         "index":1,
        #         "content":script_base64
        #         }
        #     }
        # data_file=json.dumps(data_file)
        # c.checkAction(url,data_file)


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
            print(""+data_file)
            c.checkAction(url,data_file)
            index=index+1
            # print(script_base64)


        data_install_script=rm.get_data("控制器安装文件","file_install_script")

        """重新设置安装文件名"""
        data_dict=json.loads(data_install_script)
        data_dict["data"]["index"]=self.i
        data_dict["data"]["type"]="%s"%type
        data_dict["data"]["file_name"]="%s"%filename
        # print("安装文件："+data_dict["data"]["file_name"])
        data_install_script=json.dumps(data_dict)
        print(data_install_script)

        print("step 4、安装：%s文件"%filename)
        c.checkAction(url,data_install_script)
        time.sleep(2)

        data_logout=rm.get_data("退出登录","logout")
        print("step5、释放设备：")
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
    # t.tearDown()
    # for i in range(1,5):
    #     suite = unittest.TestSuite()
    #     suite.addTest(websocket_request('test01_read_io'))
    #     suite.addTest(websocket_request('test02_write_io_off'))
    #     suite.addTest(websocket_request('test03_write_io_on'))
    #     suite.addTest(websocket_request('test04_read_io_default'))
    #     suite.addTest(websocket_request('test05_write_io_default_off'))
    #     suite.addTest(websocket_request('test06_write_io_default_on'))
    #     unittest.TextTestRunner(verbosity=2).run(suite)