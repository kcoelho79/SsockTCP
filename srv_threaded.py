# workd many thread to receive several connection

import zen_utils
from threading import Thread

def start_threads(listener, worker=4):
    t = (listener,)
    for i in range(worker):
        Thread(target=zen_utils.accept_connections_forever, args=t).start()

if __name__ == '__main__':
    address = zen_utils.parse_command_line('multi-threaded server')
    listener = zen_utils.create_srv_socket(address)
    start_threads(listener)