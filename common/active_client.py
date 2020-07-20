import socket
import json
import time
import base64

if __name__ == "__main__":
    HOST = "192.168.1.110"
    POST = 4321

    registration_code = "b5opFGrVi1CLFPTBKOzEbShXSmIm/jR2omo61bF7YpqLQeOicVlySSKvEcL2qvC2fFmmelbDIZveLhIrW6F3XZzXvMuDTUhqseDsWn4qMM3XUJIlf2JSnx13lGiBIHneLyPpyfJQMSFodmgMdJnPaX4Kn2OTUw10UtIZ+nh11hA="
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
