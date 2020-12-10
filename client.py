#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/client.py
# Simple Zen-of-Python client that asks three questions then disconnects.

import argparse, random, socket, zen_utils, time


def connect(address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    return sock

def get_msg(msg):
    "do somthings"
    return msg

def transmit(sock,msg):
    sock.sendall(msg)
    print('mensagem recebida : ',zen_utils.recv_until(sock))
    #close(sock)

def client(address, cause_error=False):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)

def close(sock):
    sock.close()

import os
def main():
    """

    """
    sock = connect(address)
    zen_utils.set_keepalive_osx(sock)
    has_msg=True
    path = os.getcwd() + '/' + 'placeholder'
    while has_msg:
        for filename in os.listdir(path):
            file = path + '/' + filename
            with open (file , 'r') as r:
                transmit(sock,r.read().encode('utf-8'))
            os.remove(file)

    #msg = get_msg(b'primeiro teste')
    #transmit(sock,msg)



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Example client')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    main()



