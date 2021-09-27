
# python3 udpGetIp.py 9999
from socket import *
import sys
from time import ctime

if __name__ == "__main__":
    PORT = 9001

    if len(sys.argv) > 3:
        print("error param num,expect [3~4]")
        exit(0)

    if len(sys.argv) == 3:
        PORT = sys.argv[2]

    HOST = '0.0.0.0'
    BUFSIZE = 1024
    ADDR = (HOST, PORT)
    udpSerSock = socket(AF_INET, SOCK_DGRAM)
    udpSerSock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    udpSerSock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    udpSerSock.bind(ADDR)

    count = 0
    print('wating for message...')
    try:
        while True:
            data, addr = udpSerSock.recvfrom(BUFSIZE)
            data = data.decode(encoding='utf-8').upper()
            count = count + 1

            print(count, '...received ->%s  %s' % (addr, data))
    except KeyboardInterrupt:
        print("ready to exit ...")
    udpSerSock.close()
    print("done.")