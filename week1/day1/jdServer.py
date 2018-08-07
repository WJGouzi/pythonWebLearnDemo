#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@author: wj
@license: (C) Copyright 2013-2018.
@contact: 1693841903@qq.com
@file: jdServer.py
@version: 1.0
@time: 2018/8/7 10:24
@desc: 模拟jd的服务端
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
             ┏┓     ┏┓
            ┏┛┻━━━━━┛┻┓
            ┃    ☃    ┃
            ┃  ┳┛  ┗┳  ┃
            ┃    ┻     ┃
            ┗━┓     ┏━━┛
              ┃     ┗━━━━┓
              ┃  神兽保佑  ┣┓
              ┃　永无BUG！  ┏┛
              ┗┓┓┏━━━━━┳┓┏┛
               ┃┫┫     ┃┫┫
               ┗┻┛     ┗┻┛
"""

import socket


def main():

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 8089))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        print(buf.decode('utf8'))
        connection.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n", "utf8"))
        # connection.sendall(bytes("<h1>hello world</h1>", "utf8"))
        with open('hello.html', 'rb') as f:
            data = f.read()
        connection.sendall(data)
        connection.close()


if __name__ == '__main__':
    try:
        main()
    except:
        print("出现其他的错误")
