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
                print("服务：%s连接成功!"%url)
                # t=ws.recv()
                t=json.loads(ws.recv())
                if t["action"]=="publish.status":
                    print("状态机状态为：%s"%t["data"]["state_machine"])
                if t["action"]=="publish.motion.info":
                    print("末端世界坐标系的位置：%s"%t["data"]["cart_pose"])
                    lenth=len(t["data"]["joint_info"]["arm_joint"])
                    i=0
                    arm_joint=[]
                    while i < lenth:
                        arm_joint.append(t["data"]["joint_info"]["arm_joint"][i]["posit"])
                        id=t["data"]["joint_info"]["arm_joint"][i]["driver_id"]
                        v=t["data"]["joint_info"]["arm_joint"][i]["velocity"]
                        torque=t["data"]["joint_info"]["arm_joint"][i]["torque"]
                        hard_limit=t["data"]["joint_info"]["arm_joint"][i]["hard_limit"]
                        vol=t["data"]["joint_info"]["arm_joint"][i]["voltage"]
                        tem=t["data"]["joint_info"]["arm_joint"][i]["temperature"]
                        print("关节id：%s，速度：%s，扭矩：%s，电压：%s，温度：%s，硬限位：%s"%(id,v,torque,vol,tem,hard_limit))
                        i=i+1
                    print("关节位置：%s"%arm_joint)
                    print("扩展轴坐标：%s"%t["data"]["joint_info"]["ext_joint"])
                if t["action"]=="publish.error":
                    print("错误码：%s"%t["data"]["code"])
                if t["action"]=="publish.io.state":
                    print("本地IO输入：%s"%t["data"]["localIO"]["input"])
                    print("本地IO输出：%s"%t["data"]["localIO"]["output"])
                    print("CanIO输入：%s"%t["data"]["canIO"]["input"])
                    print("CanIO输出：%s"%t["data"]["canIO"]["output"])
                if t["action"]=="publish.config.info":
                    print("设备id：%s"%t["data"]["identity"])
                    print("机器型号是否已配置：%s"%t["data"]["robot_is_config"])
                    print("机器型号：%s"%t["data"]["robot_type"])
                    print(" 驱动是否已设置：%s"%t["data"]["driver_is_config"])
                    print(" 驱动型号：%s"%t["data"]["driver_type"])
                    print(" 控制器型号是否已设置：%s"%t["data"]["board_is_config"])
                    print(" 控制器型号：%s"%t["data"]["board_type"])
                    print(" 扩展io是否已设置：%s"%t["data"]["extend_io_is_config"])
                    print(" 扩展io型号：%s"%t["data"]["extend_io_type"])
                if t["action"]=="publish.authorization.info":
                    print("是否已激活：%s"%t["data"]["identity"])
                time.sleep(5)


        ws.close()
    except Exception as e:
        print("websocket连接失败：%s"%e)
        pass


if __name__ == "__main__":
    ws_connect()
