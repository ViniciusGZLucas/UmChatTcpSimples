import socket
import threading
import time

Host = "192.168.86.3"
Port = 11111

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((Host,Port))
s.listen()

Conexoes = []
Nomes = []

def Mandar(Mensagem):
    for Conexao in Conexoes:
        try:
            Conexao.send(Mensagem)
        except:
            pass

def Start():
    while True:
        Conn,Address = s.accept()
        Conexoes.append(Conn)
        Nome = Conn.recv(1024).decode("utf-8")
        Nomes.append(Nome)
        print(f"Uma pessoa se conectou com o ip({Address}) e o Nick({Nome})")
        Conn.send(f"Bem Vindo {Nome}!\n".encode("utf-8"))
        Mandar(f"O usuario {Nome} Entrou no chat!".encode("utf-8"))
        Thread = threading.Thread(target=Receber,args=(Conn,))
        Thread.start()

def Receber(Conn):
    while True:
        try:
            Recebido = Conn.recv(1024)
            Data = time.asctime(time.localtime())
            print(f"{Data} > "+Recebido.decode("utf-8"))
            Mandar(Recebido)
        except Exception:
            Cliente = Conexoes.index(Conn)
            Mandar(f"O Usuario {Nomes[Cliente]} saiu do Chat!".encode("utf-8"))
            Nomes.remove(Nomes[Cliente])
            Conexoes.remove(Conn)
            Conn.close()
            break

print("Servidor Ativo!")
Start()