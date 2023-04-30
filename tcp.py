import socket

class UdpConnect:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    is_server = False
    server_address = None

    @classmethod
    def bind(cls, ip: str, port: int) -> None:
        """Work like a server, listen and get client socket"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.sock.bind((ip, port))
        cls.is_server = True

    @classmethod
    def connect(cls, ip: str, port: int) -> None:
        """Work like a client, will connect you to host"""
        cls.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        cls.server_address = (ip, port)
        cls.is_server = False

    @classmethod
    def getdata(cls) -> bytes:
        data, addr = cls.sock.recvfrom(32)
        if cls.is_server:
            cls.server_address = addr
        return data

    @classmethod
    def senddata(cls, data: bytes) -> None:
        cls.sock.sendto(data, cls.server_address)

    @classmethod
    def close(cls) -> None:
        cls.sock.close()