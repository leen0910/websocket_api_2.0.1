# python3 udpGetIp.py 9999
from socket import *
import sys
from time import ctime
import datetime

if __name__ == "__main__":
    PORT = 9001
    if len(sys.argv) > 3:
        print("error param num,expect [3~4]")
        exit(0)

    if len(sys.argv) == 3:
        PORT = sys.argv[2]

    HOST = '0.0.0.0'
    BUFSIZE = 10240
    ADDR = (HOST, PORT)
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    udpSerSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udpSerSock.bind(ADDR)
    print('wating for message...')
    try:
        while True:
            data, addr = udpSerSock.recvfrom(BUFSIZE)
            print(
                datetime.datetime.now(),
                '...received ->%s  %s' % (addr, data.decode(encoding='utf-8')))

    except KeyboardInterrupt:
        print("ready to exit ...")
    udpSerSock.close()
    print("done.")