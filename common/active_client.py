import socket
import json
import time
import base64

if __name__ == "__main__":
    HOST = "192.168.1.110"
    POST = 4321

    registration_code = "JqFdsBHctbT6LGfRIZr6MK7vcX45s4NmVm/QPe8Xb8fV6H6Ud9bMYvEX6vVXRTXmh2qg19wdr6NEccPBNIRGx+M8jjpovPB5Sxq9+d1MlcD9O39eIy2MP3qM20avyYxRFRDvuqEiUXi+R+7h0rt3elhsebpGh5EmU0tOxzhIazI="
    expiration_time = "2050-05-21.12:00:00"
    #
    dic_active = {"registration_code": registration_code,
                  "expiration_time": expiration_time}
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect((HOST, POST))
    # time.sleep(1)
    c.send(json.dumps(dic_active).encode())
    data = bytes()
    try:
        while True:
            rdata = c.recv(1024)
            if not rdata or len(rdata) < 1024:
                data += rdata
                break
            data += rdata
    except KeyboardInterrupt:
        print("ready to exit ...")
    str_active = data.decode()
    print("激活码:")
    print(str_active)
    c.close()
    print("Bye~")
