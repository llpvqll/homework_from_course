import socket
import sys
import time

TCP_IP = input("Connect to Local IP: ")
TCP_PORT = int(input("Connect to Local Port: "))
BUFFER_SIZE = 1024
running = True
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


while True:
    try:

        print("Connecting...")
        s.connect((TCP_IP, TCP_PORT))
        print("Connected!")
        while True:
            MESSAGE = input("Enter two numbers split by coma(without space): ")
            if MESSAGE == "close":
                s.close()
                raise SystemExit
            s.send(MESSAGE.encode('ascii'))
            data = s.recv(BUFFER_SIZE)
            print(data.decode('ascii'))

            running = False
            time.sleep(3)
    except SystemExit:
        print(sys.exc_info()[0])
        time.sleep(1)
        s.close()
