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
        print("step 1、monitor登录。")
        c.checkAction(ws,data_login)

        while(is_sigint_up==False):
            if ws.connected:
                print("服务：%s连接中..."%url)
                # t=ws.recv()

                t=json.loads(ws.recv())
                if t["action"]=="publish.status":
                    print("状态机状态为：%s"%t["data"]["state_machine"])
                    print("motion模块状态：%s"%t["data"]["motion_state"])
                    print("系统当前全局速度：%s"%t["data"]["global_vel"])
                    print("系统当前示教速度：%s"%t["data"]["teach_vel"])
                    print("lua模块状态：%s"%t["data"]["lua_state"])
                    print("脚本运行模式：%s"%t["data"]["lua_run_mode"])
                    print("脚本当前运行的行数：%s"%t["data"]["lua_current_line"])
                if t["action"]=="publish.motion.info":
                    print("末端世界坐标系的位置：%s"%t["data"]["chain_info"][0]["pose"])
                    lenth=len(t["data"]["joint_info"])
                    i=0
                    arm_joint=[]
                    while i < lenth:
                        arm_joint.append(t["data"]["joint_info"][i]["posit"])
                        id=t["data"]["joint_info"][i]["id"]
                        v=t["data"]["joint_info"][i]["velocity"]
                        torque=t["data"]["joint_info"][i]["torque"]
                        vol=t["data"]["joint_info"][i]["voltage"]
                        tem=t["data"]["joint_info"][i]["temperature"]
                        print("关节id：%s，速度：%s，扭矩：%s，电压：%s，温度：%s。"%(id,v,torque,vol,tem))
                        i=i+1
                    print("关节位置：%s"%arm_joint)

                if t["action"]=="publish.error":
                    print("错误码：%s"%t["data"]["code"])
                if t["action"]=="publish.io.state":
                    print("本地IO输入：%s"%t["data"]["local_io"]["input"])
                    print("本地IO输出：%s"%t["data"]["local_io"]["output"])
                    print("扩展IO输入：%s"%t["data"]["extend_io"]["input"])
                    print("扩展IO输出：%s"%t["data"]["extend_io"]["output"])

                if t["action"]=="publish.custom.info":
                    print("识别码：%s"%t["data"]["identity"])
                    print("info值：%s"%t["data"]["value"])

                time.sleep(5)
            else:
                print("服务：%s连接断开"%url)



        # ws.close()
    except Exception as e:
        print("websocket连接失败：%s"%e)
        pass


if __name__ == "__main__":
    ws_connect()

