#!/usr/bin/env python3
# Simple client that connect server, asks three questions then disconnects.
# receive paramms either line command or python shell

import argparse, random, socket, s_utils, time, sys


def transmit(sock,message):
    sock.sendall(message)
    sys.stdout.flush()
    print('mensagem recebida : ',zen_utils.recv_until(sock))

def main():
    sock = s_utils.create_cli_connection(address)
    msg = (b"teste")
    transmit(sock,msg)
    zen_utils.close_connection(sock)

if __name__ == '__main__':

    #todo get parse_coomand_line from zen_utils, intead it
    parser = argparse.ArgumentParser(description='client connect server')
    parser.add_argument('host', help='IP or hostname')
    parser.add_argument('-e', action='store_true', help='cause an error')
    parser.add_argument('-p', metavar='port', type=int, default=1060,
                        help='TCP port (default 1060)')
    args = parser.parse_args()
    address = (args.host, args.p)
    main()
