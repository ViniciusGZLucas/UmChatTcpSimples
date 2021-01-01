import socket
import threading
import time

Host = "201.62.76.189"#Ip da rede onde esta rodando o servidor
Port = 11111#Porta configurada no servidor

Nick = input("Digite seu nick: \n>")

#Cria o socket -> Conecta no servidor -> Envia o nick escolhido que aparecera para quem mais estiver conectado.
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))
s.send(Nick.encode())

#Função responsavel por ficar verificando se alguem mandou mensagem e mostrar na tela.
def Receber():
    while True:
        Mensagem = s.recv(1024).decode()
        print(Mensagem)

#Função responsavel por enviar a mensagem desejada para o servidor que retornara para os outros usuario.
def Enviar():
    while True:
        Mensagem = input("")
        s.send(f"{Nick}:{Mensagem}".encode("utf-8"))

#Cria dois threads um sendo responsavel por verificar novas mensagem e outro para enviar a mensagem que voce quiser.
EnviarThread = threading.Thread(target=Enviar)
ReceberThread = threading.Thread(target=Receber)
ReceberThread.start()
time.sleep(2)
EnviarThread.start()
