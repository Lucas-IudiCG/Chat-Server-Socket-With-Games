#Gabriel Ramires- 42080681
#Lucas Iudi Corregliano Gallinari - 32138628

import socket

IP = "172.16.16.74"
PORTA = 42080
ADDR = (IP, PORTA)
TAM = 1024
FORMATO = "utf-8"
MSG_DESCONECTAR = "QUIT"


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect(ADDR)
    print(f"[CONECTADO] Cliente conectado ao servidor em: {IP}:{PORTA}")
    Music=False
    conectado = True
    while conectado:
        msg = input(">")

        cliente.send(msg.encode(FORMATO))
        
        if msg == MSG_DESCONECTAR and Music==False:
            conectado=False
        if msg=="Username()":
            data = cliente.recv(TAM).decode(FORMATO)
            print(f"{data}")
            msg = input("> ")
            cliente.send(msg.encode(FORMATO))
        if msg=="Hash()":
            data = cliente.recv(TAM).decode(FORMATO)
            print(f"{data}")
            msg = input("> ")
            cliente.send(msg.encode(FORMATO))
        if msg=="Music_Player()":
            Music=True
        if msg=="Music_QUIT":
            Music=False
        data = cliente.recv(TAM).decode(FORMATO)
        print(f"{data}")




if __name__ == "__main__":
    main()
