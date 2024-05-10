#Gabriel Ramires- 42080681
#Lucas Iudi Corregliano Gallinari - 32138628

import socket #importa modulo socket
from threading import Thread
import time

IP_destino = "192.168.15.28" #Endereço IP do servidor
PORTA_destino = 31238 #Numero de porta do servidor
data=""
MENSAGEM=""

def enviar(sock,MENSAGEM):
    while(MENSAGEM!="QUIT"):
        MENSAGEM=str(input("Mensagem para o Server:"))
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
    sock.connect(("192.168.15.28",31238))

    receive = Thread(target=receber,args=[sock,""])
    send= Thread(target=enviar,args=[sock,""])
    receive.start()
    send.start()

main()
