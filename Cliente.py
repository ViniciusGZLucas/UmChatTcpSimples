import socket
import threading
import time

Host = "201.62.76.189"
Port = 11111

Nick = input("Digite seu nick: \n>")

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((Host,Port))
s.send(Nick.encode("utf-8"))

def Receber():
    while True:
        Mensagem = s.recv(1024).decode("utf-8")
        print(Mensagem)

def Enviar():
    while True:
        Mensagem = input("")
        s.send(f"{Nick}:{Mensagem}".encode("utf-8"))

EnviarThread = threading.Thread(target=Enviar)
ReceberThread = threading.Thread(target=Receber)
ReceberThread.start()
time.sleep(2)
EnviarThread.start()