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
import time
import json




class install(unittest.TestCase):
    """安装升级文件"""
    filename="QRSP4-034015-00-09-T-2019-09-26.tar.gz"
    path='../update/QRSP4-034015-00-09-T-2019-09-26.tar.gz'
    i=8
    size=300*1024
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

    def test_install(self):
        """控制器接收文件"""
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_admin")
        url=self.ws
        path=self.path
        filename=self.filename
        print("step 1、管理员登录设备。")
        c.checkAction(url,data_login)
        time.sleep(1)

        print("step 2、向设备写入升级文件：")

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
                    "type":"update",
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
            print(script_base64)


        data_install_update=rm.get_data("控制器安装文件","file_install_update")

        """重新设置安装文件名"""
        data_dict=json.loads(data_install_update)
        data_dict["data"]["index"]=self.i
        data_dict["data"]["file_name"]="%s"%filename
        print("安装升级文件："+data_dict["data"]["file_name"])
        data_install_script=json.dumps(data_dict)
        print(data_install_script)

        print("step 3、安装：%s文件"%filename)
        c.checkAction(url,data_install_script)
        time.sleep(2)


    def tearDown(self):
        time.sleep(3)
        self.ws.close()

if __name__ == "__main__":
    unittest.main()
    # t=install()
    # t.setUp()
    # t.install_lua_script()