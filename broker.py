"""
 broker.py
 intercambio de mensagens
"""
import requests, json
# recebe mensagem + endereco origem
#  appenda o endereço na mensage,
# enviar msg para o controler

def get_address(message):
    address = message[-6:]
    #host = BitHandler.fmtByte_to_Str(address[0:4],'.')
    host = str(address[0]) +'.'+ str(address[1]) +'.'+ str(address[2]) +'.'+ str(address[3])
    port = int.from_bytes(address[4:], 'big')
    return ((host,port))


def append_host_to(message,address):
    ip = bytes([int(x) for x in address[0].split('.')])
    port = address[1].to_bytes(2,byteorder='big')
    print("broker --> ",port,ip)
    message += ip + port
    print('--- Broker ---- Message : ', message)
    print('--- Broker ---- addreess : ', get_address(message))
    return message

def post_to_controler(message,address,sock):

    #URL = "http://127.0.0.1:8000/portaria/evento"
    print('mensagem para post: ',message)
    URL = "http://d6cb4801c648.ngrok.io/portaria/evento"

    headers = {'content-type': 'application/json'}
    # receber endereço e acrescentar no frame, converter

    r = requests.post(URL, data=message, headers=headers)
    # receber a resposta do request, formato frame
    # enviar frame de volta conexao.
    print(r.text)

def send_to_controler(message,address):
    # import classe/ funct  - events.py
    pass
