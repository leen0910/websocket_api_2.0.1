import websocket
import time


def on_message(ws, message):
    print(ws)
    print(message)


def on_error(ws, error):
    print(ws)
    print(error)


def on_close(ws):
    print(ws)
    print("### closed ###")

def on_start(ws_url):
  time.sleep(5)
  websocket.enableTrace(True)
  ws = websocket.WebSocketApp(ws_url,
                on_message=on_message,
                on_error=on_error,
                on_close=on_close)
  # ws.on_open = on_open
  ws.run_forever()



