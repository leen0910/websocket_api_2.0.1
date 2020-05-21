import websocket
from common import read_info
import json
import sys

import time

rt=read_info.ReadInfo()
web=rt.get_device_ip()
port=rt.get_port()
url=web+":"+port

def on_message(ws, message):  # 服务器有数据更新时，主动推送过来的数据

    message=json.loads(message)

    t=time.strftime('%Y/%m/%d %H:%M:%S',time.localtime(time.time()))
    # f = open("out.txt", "a")
    with open('out.txt','a',encoding='utf-8') as f:
        if message["action"]=="publish.status":      #"publish.custom.info"
            # if message["action"]["identity"]=="打表值":

            print("{} -------打表值： {}".format(t,message["data"]["state_machine"]),file=f)



def on_error(ws, error):  # 程序报错时，就会触发on_error事件
    print("####### on_error #######")
    print(error)


def on_close(ws):
    print("####### on_close #######")
    print("Connection closed ……")


def on_open(ws):  # 连接到服务器之后就会触发on_open事件，这里用于帐号登录
    data='''{
    "action":"permission.login",
    "data":{
        "username":"Monitor",
        "identity":"monitor",
        "password":"MTIzNDU2"
    }
    }'''
    print(data)
    ws.send(data)



    # req = '{"event":"subscribe", "channel":"btc_usdt.deep"}'
    # print(req)
    # ws.send(req)


def connect(a):
    time.sleep(a % 1)
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("{}".format(url),
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.run_forever(ping_timeout=10)
    return ws

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("{}".format(url),
                                # on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    ws.on_message=on_message

    ws.run_forever(ping_timeout=10)
