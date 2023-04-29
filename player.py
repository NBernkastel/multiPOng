from settings import *


class Player:
    def __init__(self) -> None:
        self.score = 0
        self.x_pos = 0
        self.y_pos = 0
        self.speed = 1
        self.__color = (255, 255, 255)
        self.__R = 1
        self.__size = (10, 150)

    def update(self, dt: float) -> None:
        self.move(dt)
        self.draw()

    def move(self, dtime: float) -> None:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_s]:
            self.y_pos += self.speed * dtime
        if keys[pygame.K_w]:
            self.y_pos -= self.speed * dtime

    def draw(self) -> None:
        pygame.draw.rect(screen, self.__color, (self.x_pos, self.y_pos, self.__size[0], self.__size[1]), self.__R)

    @property
    def size(self) -> tuple[int, int]:
        return self.__size
