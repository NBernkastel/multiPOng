from player import Player
from settings import *
from Sphere import Sphere
from tcp import TcpConnect


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.sphere = Sphere(150, 150, 1, 1)
        self.running = True
        self.player1 = Player()
        self.player2 = Player()
        self.player2.x_pos = WIDTH - 10

        # Ask user if they want to start as host or client
        self.host = input("Do you want to start as host? (y/n) ").lower() == 'y'
        if NET:
            if self.host:
                TcpConnect.bind(IP, PORT)
            else:
                TcpConnect.connect(IP, PORT)

    def network(self) -> bool:
        TcpConnect.senddata(f'{round(self.player1.y_pos, 2)}'
                            f' {round(self.sphere.x, 2)}'
                            f' {round(self.sphere.y, 2)}'
                            f' {round(self.sphere.x_dir, 2)}'
                            f' {round(self.sphere.y_dir, 2)}'.encode('utf-8'))
        try:
            data = TcpConnect.getdata().decode().split(' ')
            print(data)
            self.player2.y_pos = float(data[0])
            if not self.host:
                self.sphere.x = WIDTH - float(data[1])
                self.sphere.y = float(data[2])
                self.sphere.x_dir = float(data[3])
                self.sphere.y_dir = float(data[4])
        except:
            pass

    def run(self):
        while self.running:
            dtime = self.clock.get_time()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            # Screen clean
            screen.fill((0, 0, 0))
            # network work)
            if NET:
                self.network()
            # update part
            self.sphere.update(self.player1.y_pos, self.player2.y_pos, dtime, self.player1.size, self.player2.size)
            self.player1.update(dtime)
            self.player2.update(dtime)
            # end part
            pygame.display.flip()
            self.clock.tick(FPS)
        # if game closed
        TcpConnect.close()
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.run()
