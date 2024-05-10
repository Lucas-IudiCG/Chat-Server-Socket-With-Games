#Gabriel Ramires- 42080681
#Lucas Iudi Corregliano Gallinari - 32138628

import socket
import threading
import time

IP = "172.16.16.74"
PORTA = 42080
ADDR = (IP, PORTA)
TAM = 1024
FORMATO = "utf-8"
MSG_DESCONECTAR = "QUIT"
Clientes=[]
Names=[]


def JogoDaVelha(conn,J1):
    import pygame
    def Initialize():
        V=[]
        for i in range(3):
             linha = []
             for j in range(3):
                 linha.append("*")
             V.append(linha)
        return V

    def step(M,lin,col,gamer):
        Final=True
        if gamer==1:
            if M[lin][col]=="*":
                M[lin][col]="O"
                print("Comando Aceito")
                Final=True
                return Final
            elif M[lin][col]=="O":
                print("Comando Inválido")
                print("Você já escolheu esse espaço")
                Final=False
                return Final
            elif M[lin][col]=="X":
                print("Comando Inválido")
                print("O seu Oponente já escolheu esse espaço")
                Final=False
                return Final
        elif gamer==2:
            if M[lin][col]=="*":
                M[lin][col]="X"
                print("Comando Aceito")
                Final=True
                return Final
            elif M[lin][col]=="O":
                print("Comando Inválido")
                print("O seu Oponente já escolheu esse espaço")
                Final=False
                return Final
            elif M[lin][col]=="X":
                print("Comando Inválido")
                print("Você já escolheu esse espaço")
                Final=False
                return Final

    def status(M):
        if M[0][0]==M[1][1]==M[2][2]=="X":
            D=2
            return D
        elif M[0][2]==M[1][1]==M[2][0]=="X":
            D=2
            return D
        
        elif M[0][0]==M[0][1]==M[0][2]=="X":
            D=2
            return D
        elif M[1][0]==M[1][1]==M[1][2]=="X":
            D=2
            return D
        elif M[2][0]==M[1][1]==M[0][2]=="X":
            D=2
            return D
        
        elif M[0][0]==M[1][0]==M[2][0]=="X":
            D=2
            return D
        elif M[0][1]==M[1][1]==M[2][1]=="X":
            D=2
            return D
        elif M[0][2]==M[1][2]==M[2][2]=="X":
            D=2
            return D

        elif M[0][0]==M[1][1]==M[2][2]=="O":
            D=1
            return D
        elif M[0][2]==M[1][1]==M[2][0]=="O":
            D=1
            return D
        
        elif M[0][0]==M[0][1]==M[0][2]=="O":
            D=1
            return D
        elif M[1][0]==M[1][1]==M[1][2]=="O":
            D=1
            return D
        elif M[2][0]==M[2][1]==M[2][2]=="O":
            D=1
            return D

        elif M[0][0]==M[1][0]==M[2][0]=="O":
            D=1
            return D
        elif M[0][1]==M[1][1]==M[2][1]=="O":
            D=1
            return D
        elif M[0][2]==M[1][2]==M[2][2]=="O":
            D=1
            return D
        
        else:
            D=0
            for i in range(3):
                for j in range(3):
                    if M[i][j]=="*":
                        D+=1
            if D>0:
                D=3
                return D
            else:
                D=0
                return D


    def Imprime (M,veri,j1,j2):
        preto=(0,0,0)
        sombra=(18,27,32)
        branco=(255,255,255)
        vermelho=(255,0,0)
        verde=(0,255,0)
        azul=(0,0,255)
        amarelo=(255,255,0)
        ciano=(0,255,255)
        magenta=(255,0,255)
        roxo=(153,51,153)
        
        coordsX=[200,500,800]
        coordsY=[150,400,650]
        

        screen= pygame.display.set_mode((1100,900),5,0)
        pygame.display.set_caption("Jogo da Velha")
        screen.fill((255,255,255))
        font = pygame.font.SysFont('Consolas.ttf',200) 
        X = font.render('X' , True , azul)
        O = font.render('O' , True , vermelho)
        pygame.draw.polygon(screen,preto,([900,600],[900,600],[100,600],[100,600]),5)
        pygame.draw.polygon(screen,preto,([900,305],[500,305],[100,305],[100,305]),5)
        pygame.draw.polygon(screen,preto,([400,800],[400,800],[400,100],[400,100]),5)
        pygame.draw.polygon(screen,preto,([700,800],[700,800],[700,100],[700,100]),5)
        for i in range(3):
            for j in range(3):
                if M[i][j] =="O":
                   screen.blit(O , (coordsX[i],coordsY[j]))
                elif M[i][j]=="X":
                    screen.blit(X, (coordsX[i],coordsY[j]))
        pygame.display.flip()
        
        if veri==2:
            Vi2 = font.render('Vitória de' , True , azul)
            JV2= font.render(str(j2), True , azul)
            screen.blit(Vi2, (100,0))
            screen.blit(JV2, (400,700))
            pygame.display.flip()

        elif veri==1:
            Vi1 = font.render('Vitória d2' , True , vermelho)
            JV1= font.render(str(j1) , True , vermelho)
            screen.blit(Vi1, (100,0))
            screen.blit(JV1, (400,700))
            pygame.display.flip()


        elif veri==0:
            V = font.render('Empate' , True , roxo)
            screen.blit(V, (400,700))
            pygame.display.flip()
        
    def Velha(conn,J1):
        pygame.init()
        M= Initialize()
        Imprime(M,5,0,0)
        lin=0
        col=0
        Jogador=1
        K=0
        Cont=1
        veri=3
        num=[]
        print("Jogador 1:\n",J1)
        J2=str(input("Digite o nome do Jogador2 :"))
        end1="Comando Inválido\nTurno de"+str(J1)+"\nEscolha uma Coordenada:"
        while veri==3:
            F=False
            Cont=1
            if Jogador==1 and veri==3:
                lin=-1
                col=-1
                while F==False or lin<0 or lin>3 or col<0 or col>3:
                    num.clear()
                    if lin<0 or lin>3 or col<0 or col>3:
                        msg="Turno de"+str(J1)+"\nEscolha uma Coordenada: "
                        conn.send(msg.encode(FORMATO))
                        Mensagem=" "
                        time.sleep(5)
                        Mensagem+= conn.recv(TAM).decode(FORMATO)
                        if Mensagem=="Quit":
                                veri==2
                        num = [int(x) for x in Mensagem.split() if x.isdigit()]
                        if len(num)>=2:
                            lin=num[0]-1
                            col=num[1]-1
                        F=step(M,lin,col,Cont)

                veri=status(M)
                Imprime(M,veri, J1,J2)
                Cont+=1
                K+=1
                F=False
                Jogador=2
                if Jogador==2 and veri==3:
                    lin=-1
                    col=-1
                    while F==False or lin<0 or lin>3 or col<0 or col>3:
                        num.clear()
                        if lin<0 or lin>3 or col<0 or col>3:
                            print("Escolha uma Coordenada")
                            Mensagem=str(input(": "))
                            if Mensagem=="Quit":
                                veri==1
                            num = [int(x) for x in Mensagem.split() if x.isdigit()]
                            if len(num)>=2:
                                lin=num[0]-1
                                col=num[1]-1
                            F=step(M,lin,col,Cont)

                    veri=status(M)
                    Imprime(M,veri, J1,J2)
                    Cont+=1
                    K+=1
                    F=False
                    Jogador=1
            
        test=False
        if veri==1:
            msg="Parabens"+str(J1)+"você Venceu"
        if veri==2:
            msg="Que Pena"+str(J2)+"você Perdeu"
        if veri==0:
            msg="EMPATOU"
        
        conn.send(msg.encode(FORMATO))
        time.sleep(8)
        pygame.quit()
        
    Velha(conn,J1)

def Poesia(conn):
    import pygame
    from pygame import mixer
    import os

    preto=(0,0,0)
    sombra=(18,27,32)
    branco=(255,255,255)
    vermelho=(255,0,0)
    verde=(0,255,0)
    azul=(0,0,255)
    amarelo=(255,255,0)
    ciano=(0,255,255)
    magenta=(255,0,255)


    pygame.init()
    mixer.init()
    os.chdir("D:/Hino de Redes")
    song=os.listdir()
    playlist=[]
    for s in song:
        playlist.append(s)
    mixer.music.load(playlist[0])
    mixer.music.play()
    msg=f"Bem vindo a Melhor Poesia contemporânea"
    conn.send(msg.encode(FORMATO))
    conectado = True
    while conectado:
        msg = conn.recv(TAM).decode(FORMATO)
        if msg == "Poesia_QUIT":
            conectado = False
        for c in range (len(Clientes)):
            Clientes[c].send(msg.encode(FORMATO))
        screen= pygame.display.set_mode((900,900),5,0)
        pygame.display.set_caption("Hino de Redes")
        screen.fill((225,198,153))
        font = pygame.font.SysFont('impact.ttf',30)
        font2 = pygame.font.SysFont('Consolas.ttf',30) 
        linha1= font.render("Na rede dos dados a circular," , True , preto)
        linha2= font.render("O modelo TCP/IP é o padrão a se usar," , True , preto)
        linha3= font.render("Dividido em camadas, quatro a contar," , True , preto)
        linha4= font.render("Cada uma com funções a desempenhar." , True , preto)
        screen.blit(linha1,(0,0))
        screen.blit(linha2,(0,20))
        screen.blit(linha3,(0,40))
        screen.blit(linha4,(0,60))

        linha1= font.render("A camada de aplicação no topo está," , True , preto)
        linha2= font.render("com protocolos que o usário usa para navegar," , True , preto)
        linha3= font.render("HTTP,FTP,DNS,e-mail, e mais," , True , preto)
        linha4= font.render("Todos os dados que o usuário precisa acessar." , True , preto)
        screen.blit(linha1,(0,100))
        screen.blit(linha2,(0,120))
        screen.blit(linha3,(0,140))
        screen.blit(linha4,(0,160))

        linha1= font.render("A camada de transporte é a segunda a descer," , True , preto)
        linha2= font.render("Garante que os dados sejam entregues sem perder," , True , preto)
        linha3= font.render("TCP confiável ou UDP mais rápido," , True , preto)
        linha4= font.render("Escolha um para seu aplicativo ficar satisfatório." , True , preto)
        screen.blit(linha1,(0,200))
        screen.blit(linha2,(0,220))
        screen.blit(linha3,(0,240))
        screen.blit(linha4,(0,260))

        linha1= font.render("A camada de rede é a terceira a passar," , True , preto)
        linha2= font.render("Onde os pacotes são roteados para o destino chegar," , True , preto)
        linha3= font.render("IP é o protocolo chave nessa camada," , True , preto)
        linha4= font.render("que conecta as redes e envia as informações desejadas." , True , preto)
        screen.blit(linha1,(0,300))
        screen.blit(linha2,(0,320))
        screen.blit(linha3,(0,340))
        screen.blit(linha4,(0,360))
        
        linha1= font.render("A camada de enlace é a última a estar," , True , preto)
        linha2= font.render("Com protocolos para transferência física de ar," , True , preto)
        linha3= font.render("Ehernet,Wi-fi e outros que se usar," , True , preto)
        linha4= font.render("Cada um com seus Prórpios meios para trafegar." , True , preto)
        screen.blit(linha1,(0,400))
        screen.blit(linha2,(0,420))
        screen.blit(linha3,(0,440))
        screen.blit(linha4,(0,460))

        linha1= font.render("Assim, o modelo TCP/IP é essencial," , True , preto)
        linha2= font.render("Para as comunicações de redes serem funcionais," , True , preto)
        linha3= font.render("Dividido em camadas e protoclos a confiar," , True , preto)
        linha4= font.render("Essa arquitetura garante que tudo irá operar." , True , preto)
        screen.blit(linha1,(0,500))
        screen.blit(linha2,(0,520))
        screen.blit(linha3,(0,540))
        screen.blit(linha4,(0,560))

        imp = pygame.image.load("D:\\ChatGPT.png").convert()
        linha4= font2.render("GPT,Chat.Poesia redes,21/3/2023." , True , preto)
        screen.blit(imp, (650, 600))
        screen.blit(linha4,(550,850))
        pygame.display.flip()
    pygame.quit()
    mixer.quit()


def Music_Player(conn):
    from pygame import mixer
    import os
    mixer.init()

    def playsong(playlist,i):
        currentsong=str(playlist[i])
        print(currentsong)
        mixer.music.load(currentsong)
        mixer.music.play()
            
    def stopsong():
        mixer.music.stop()
    def pausesong():
        mixer.music.pause()
    def resumesong():
        mixer.music.unpause()
        

    def Music(conn):
        os.chdir("D:/Musicas")
        song=os.listdir()
        playlist=[]
        num=[]
        songs=""
        x=1
        for s in song:
            playlist.append(s)
            songs=str(songs+"["+str(x)+"]"+str(playlist[x-1] +"\n"))
            x+=1
        x=0
        comando=1
        msg=""
        menu = f"[1]= Escolher Música Para Tocar\n[2]=Pausar Música Atual\n[3]=Parar Música Atual\n[4]=Despausar Música Atual\n"
        while msg!="Music_QUIT":
            conn.send(menu.encode(FORMATO))
            msg = conn.recv(TAM).decode(FORMATO)
            num.clear()
            num = [int(x) for x in msg.split() if x.isdigit()]
            if num:
                comando= num[0]
                if comando==1:
                    conn.send(songs.encode(FORMATO))
                    num.clear()
                    msg = conn.recv(TAM).decode(FORMATO)
                    num = [int(x) for x in msg.split() if x.isdigit()] 
                    y= num[0]-1
                    playsong(playlist,y)
                if comando==2:
                    pausesong()
                if comando==3:
                    stopsong()
                if comando==4:
                    resumesong()
        
        stopsong()
        msg=f"Music Player Finalizado"
        conn.send(msg.encode(FORMATO))    
    Music(conn)


    

def Username(conn,addr):
    msg=f"Username: "
    conn.send(msg.encode(FORMATO))
    msg=conn.recv(TAM).decode(FORMATO)
    for n in range (len(Names)):
        if Names[n]==addr:
            Names[n]=msg
    return msg

            
def cliente(conn, addr):
    print(f"[NOVA CONEXÃO] {addr} conectado.")
    conectado = True
    while conectado:
        msg=""
        msg = conn.recv(TAM).decode(FORMATO)
        if msg=="Username()":
            addr=Username(conn,addr)
        if msg=="Poesia()":
            Poesia(conn)
            msg = conn.recv(TAM).decode(FORMATO)
        if msg=="Hash()":
            JogoDaVelha(conn,addr)
            msg = conn.recv(TAM).decode(FORMATO)
        if msg=="Music_Player()":
            Music_Player(conn)
            msg = conn.recv(TAM).decode(FORMATO)
        if msg == MSG_DESCONECTAR:
            conectado = False
            break
        print(f"[{addr}] {msg}")
        msg=f"[{addr}]: {msg}\n"
        existe=False
        msg1=""
        time.sleep(1)
        for c in range (len(Clientes)):
            Clientes[c].send(msg.encode(FORMATO))

    conn.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=cliente, args=(conn, addr))
        Clientes.append(conn)
        Names.append(addr)
        thread.start()
        print(f"[Conexoes Ativas] {threading.active_count() - 1}")


if __name__ == "__main__":
    main()
