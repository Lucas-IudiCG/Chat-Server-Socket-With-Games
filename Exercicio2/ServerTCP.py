#Gabriel Ramires- 42080681
#Lucas Iudi Corregliano Gallinari - 32138628

import socket
from threading import Thread
import time

IP_servidor = "192.168.15.28" #endereço onde o Server será executado
PORTA_servidor = 31238 #porta aberta pelo Server para conexão
data=""
MENSAGEM=""
# Criação de socket UDP
# Argumentos, AF_INET que declara a família do protocolo; se fosse um envio via Bluetooth usariamos AF_BLUETOOTH
# SOCK_DGRAM, indica que será UDP.

def enviar(sock,MENSAGEM):
    while(MENSAGEM!="QUIT"):
        MENSAGEM=str(input("Mensagem para o Cliente:"))
        sock.sendto(MENSAGEM.encode('UTF-8'), ("192.168.15.28", 31238))
        time.sleep(1)
        
def receber(sock,data):
   while (data!="QUIT"):
        data= sock.recv(1024)
        print (data)
        time.sleep(1)
       


def main():
    MENSAGEM=""
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    # IP e porta que o servidor deve aguardar a conexão
    sock.bind(('192.168.15.28', 31238))
    sock.listen(1)
    conn,addr = sock.accept()
    receive = Thread(target=receber,args=[conn,""])
    send = Thread(target=enviar,args=[conn,""])
    receive.start()
    send.start()


main()
