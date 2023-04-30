import socket


class UdpConnect:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    is_server = False
    @classmethod
    def bind(cls, ip: str, port: int) -> None:
        """Work like a server, listen and get client socket"""
        cls.sock.bind((ip, port))
        cls.is_server = True

    @classmethod
    def connect(cls, ip: str, port: int) -> None:
        """Work like a client, will connect you to host"""
        cls.is_server = False

    @classmethod
    def getdata(cls) -> bytes:
        data, address = cls.sock.recvfrom(32)
        return data

    @classmethod
    def senddata(cls, data: any , ip: str, port: int) -> None:
        cls.sock.sendto(data, (ip,port))

    @classmethod
    def close(cls) -> None:
        cls.sock.close()