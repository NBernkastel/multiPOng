import pygame

import settings


class Sphere:
    def __init__(self, x: float, y: float, x_dir: int, y_dir: int) -> None:
        self.x = x
        self.y = y
        self.speed = 0.5
        self.x_dir = x_dir
        self.y_dir = y_dir

    def update(self,y_pos) -> None:
        self.x += self.speed * self.x_dir
        self.y += self.speed * self.y_dir
        self.collision(y_pos)

    def collision(self,y_pos) -> None:
        if pygame.Rect.collidepoint(pygame.Rect(10, y_pos, 10, 150), self.x-10, self.y) or self.x > settings.WIDTH:
            self.x_dir *= -1
        if self.y < 0 or self.y > settings.HEIGHT:
            self.y_dir *= -1
