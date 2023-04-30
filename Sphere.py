from settings import *


class Sphere:
    def __init__(self, x: float, y: float, x_dir: int, y_dir: int) -> None:
        self.x = x
        self.y = y
        self.speed = 0.3
        self.x_dir = x_dir
        self.y_dir = y_dir
        self.__color = (255, 255, 255)
        self.__R = 10

    def update(self, y_pos1: float, y_pos2: float, dt: float, first_size: tuple, second_size: tuple) -> None:
        self.collision(first_size, second_size, y_pos1, y_pos2)
        self.x += self.speed * self.x_dir * dt
        self.y += self.speed * self.y_dir * dt
        self.draw()

    def collision(self, first_size: tuple, second_size: tuple, y_pos1: float, y_pos2: float) -> None:
        if pygame.Rect.collidepoint(
                pygame.Rect(10, y_pos1 - self.__R, first_size[0], first_size[1] + self.__R * 2), self.x, self.y):
            self.x_dir *= -1
        if pygame.Rect.collidepoint(
                pygame.Rect(WIDTH - 20, y_pos2 - self.__R, second_size[0], second_size[1] + self.__R * 2), self.x,
                self.y):
            self.x_dir *= -1
        if self.y < 0 or self.y > HEIGHT:
            self.y_dir *= -1
        if self.x < 0 or self.x > WIDTH:
            self.x = WIDTH / 2
            self.y = HEIGHT / 2

    def draw(self) -> None:
        pygame.draw.circle(screen, self.__color, (self.x, self.y), self.__R)
