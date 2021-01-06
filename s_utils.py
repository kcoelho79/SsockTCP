#!/usr/bin/env python3
# Foundations of Python Network Programming, Third Edition
# https://github.com/brandon-rhodes/fopnp/blob/m/py3/chapter07/zen_utils.py
# Constants and routines for supporting a certain network conversation.

#TODO transform to Class, __init__  create socket

import argparse, socket, sys
import broker


def parse_command_line(description):
    """Parse command line and return a socket address."""
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    return address

def create_socket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return sock

def create_cli_connection(address):
    """ create socket and connect server at address """
    sock = create_socket()
    sock.connect(address)
    print('connected at {}'.format(sock.getpeername()))
    return sock

def create_srv_socket(address):
    """Build and return a listening server socket."""
    listener = create_socket()
    listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    listener.bind(address)
    listener.listen(64)
    print('Listening at {}'.format(address))
    return listener

def accept_connections_forever(listener):
    """Forever answer incoming connections on a listening socket."""
    while True:
        sock, address = listener.accept()
        print('Accepted connection from {}'.format(address))
        handle_conversation(sock, address)

def handle_conversation(sock, address):
    """Converse with a client over `sock` until they are done talking."""
    try:
        while True:
            handle_request(sock, address)
    except EOFError:
        print('Client socket to {} has closed'.format(address))
    except Exception as e:
        print('Client {} error: {}'.format(address, e))
    finally:
        sock.close()

def handle_request(sock, address):
    """Receive a single client request on `sock` and send the answer."""
    #todo: @decorator receber como argumento a funcao, que vai tratar o retorno,
    message = recv_until(sock)
    print("handle_request > msg recebida: ",message)
    push_domain(message,address,sock)
    sock.sendall(message) #retorna o retorno hahaha
    #sock.sendall(b'MENSAGEM ENVIADA - SUCESSO' )
    #sock.sendall(b'\x00\x07\x07')

def recv_until(sock):
    """Receive bytes over socket `sock` until we receive the `suffix`."""
    message = sock.recv(4096)
    if not message:
        raise EOFError('socket closed')

#TODO: how to do to keep connetio until get warning for close,
#TODO: tips, use flag variable to keet conection

    # while not message.endswith(b'\n'):
    #     data = sock.recv(4096)
    #     if not data:
    #         raise IOError('received {!r} then socket closed'.format(message))
    #     message += data
    return message

def push_domain(message,address,sock):
    broker.post_to_controler(message,address,sock)

def close_connection(sock):
    sock.close()
