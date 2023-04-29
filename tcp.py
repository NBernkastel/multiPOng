import socket
import time

class TcpConnect:
    client_sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    is_server = False

    @classmethod
    def bind(cls, ip: str, port: int):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.bind((ip, port))
        cls.sock.listen(1)
        cls.client_sock, cls.adr = cls.sock.accept()
        cls.is_server = True

    @classmethod
    def connect(cls, ip: str, port: int):
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.connect((ip, port))
        cls.is_server = False

    @classmethod
    def getdata(cls) -> bytes:
        data = cls.client_sock.recv(24) if cls.is_server else cls.sock.recv(24)
        return data

    @classmethod
    def senddata(cls, data: any):
        if cls.is_server:
            cls.client_sock.send(data)
        else:
            cls.sock.send(data)

    @classmethod
    def close(cls):
        if cls.is_server:
            cls.client_sock.close()
        cls.sock.close()