import socket
import time

class TcpConnect:
    client_sock = None
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 32)
    sock.setblocking(False)
    is_server = False
    @classmethod
    def bind(cls, ip: str, port: int) -> None:
        """Work like a server, listen and get client socket"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        cls.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 32)
        cls.sock.bind((ip, port))
        cls.sock.listen(1)
        cls.client_sock, cls.adr = cls.sock.accept()
        cls.is_server = True

    @classmethod
    def connect(cls, ip: str, port: int) -> None:
        """Work like a client, will connect you to host"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cls.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        cls.sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 32)
        cls.sock.connect((ip, port))
        cls.is_server = False

    @classmethod
    def getdata(cls) -> bytes:
        data = cls.client_sock.recv(32) if cls.is_server else cls.sock.recv(32)
        return data

    @classmethod
    def senddata(cls, data: any) -> None:
        if cls.is_server:
            cls.client_sock.send(data)
        else:
            cls.sock.send(data)

    @classmethod
    def close(cls) -> None:
        if cls.is_server:
            cls.client_sock.close()
        cls.sock.close()