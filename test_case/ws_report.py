#!/usr/bin/python

from websocket import create_connection

from common import read_info
import json
import signal
from common import read_message
from common import check_action as c
import time

def stop(signum, frame):

  global is_sigint_up
  is_sigint_up = True
  print("catched interrupt signal!")

signal.signal(signal.SIGINT, stop)
# signal.signal(signal.SIGHUP, stop)
signal.signal(signal.SIGTERM, stop)

def ws_connect():
    is_sigint_up = False
    rt=read_info.ReadInfo()
    web=rt.get_device_ip()
    port=rt.get_port()
    url=web+":"+port
    try:
        ws=create_connection(url,timeout=10)    #建立设备连接
        rm=read_message.ReadMessage()
        data_login=rm.get_data("登录设备","login_monitor")
        print("step 1、登录设备/监控者")
        t=c.checkAction(ws,data_login)

        # rm=read_message.ReadMessage()
        # data_query_position=rm.get_data("31","query_position")
        while(is_sigint_up==False):
            if ws.connected:
                # print("服务：%s连接成功!"%url)
                # t=ws.recv()
                t=json.loads(ws.recv())
                if t["action"]=="publish.status":
                    print("机器状态：%s"%t["data"]["state_machine"])
                    print("lua模块状态：%s"%t["data"]["lua_state"])
                    print("motion模块状态：%s"%t["data"]["motion_state"])
                    print("系统当前全局速度：%s"%t["data"]["global_vel"])
                if t["action"]=="publish.motionInfo":
                    print("末端世界坐标系的位置：%s"%t["data"]["cart_pose"])
                if t["action"]=="publish.error":
                    print("错误码：%s"%t["data"]["code"])
                if t["action"]=="publish.io.state":
                    print("本地IO输入：%s"%t["data"]["localIO"]["input"])
                    print("本地IO输出：%s"%t["data"]["localIO"]["output"])
                    print("CanIO输入：%s"%t["data"]["canIO"]["input"])
                    print("CanIO输出：%s"%t["data"]["canIO"]["output"])
                # else:
                #     print(t)
                time.sleep(5)
        ws.close()
    except Exception as e:
        print("websocket连接失败：%s"%e)
        pass


if __name__ == "__main__":
    ws_connect()
