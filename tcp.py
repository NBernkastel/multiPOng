import socket
import time

class TcpConnect:
    client_sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    is_server = False
    @classmethod
    def bind(cls, ip: str, port: int) -> None:
        """Work like a server, listen and get client socket"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        cls.sock.bind((ip, port))
        cls.sock.listen(1)
        try:
            cls.client_sock, cls.adr = cls.sock.accept()
        except:
            pass
        cls.is_server = True

    @classmethod
    def connect(cls, ip: str, port: int) -> None:
        """Work like a client, will connect you to host"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        try:
            cls.sock.connect((ip, port))
        except:
            pass
        cls.is_server = False

    @classmethod
    def getdata(cls) -> bytes:
        try:
            data = cls.client_sock.recv(32) if cls.is_server else cls.sock.recv(32)
        except:
            pass
        print(data)
        return data

    @classmethod
    def senddata(cls, data: any) -> None:
        try:
            if cls.is_server:
                cls.client_sock.send(data)
            else:
                cls.sock.send(data)
        except:
            pass

    @classmethod
    def close(cls) -> None:
        if cls.is_server:
            cls.client_sock.close()
        cls.sock.close()