# workd many thread to receive several connection

import s_utils
from threading import Thread

def start_threads(listener, worker=4):
    t = (listener,)
    for i in range(worker):
        Thread(target=s_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = s_utils.parse_command_line('multi-threaded server')
    listener = s_utils.create_srv_socket(address)
    start_threads(listener)