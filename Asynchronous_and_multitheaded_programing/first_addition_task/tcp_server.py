import socket
import time
import sys
import threading

TCP_IP = input("Host IP: ")
TCP_PORT = int(input("Host Port: "))
BUFFER_SIZE = 1024


def create_new_thread(function):
    threading.Thread(target=function).start()


def listening():
    try:
        while True:
            s.listen(1)

            conn, addr = s.accept()
            threading.Thread(target=listening).start()
            print("User joined with IP %s" % (addr[0]))
            while 1:
                data = conn.recv(BUFFER_SIZE)
                result_list = []

                for item in data.split(b','):
                    item = int(item)
                    result_list.append(item)
                integer_result = sum(result_list)
                print(f"{result_list[0]} + {result_list[1]} = {integer_result}")
                conn.send(f"{result_list[0]} + {result_list[1]} = {integer_result}".encode('ascii'))
                if not data:
                    break
                conn.send(addr[0].encode("utf-8") + b': ' + data)
            conn.close()
    except ConnectionResetError as e:
        print("Connection was closed: ", e)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((TCP_IP, TCP_PORT))
    print("-----Server started-----")
    listening()
except socket.error as e:
    print("Socket error occured. More info: ", e)
