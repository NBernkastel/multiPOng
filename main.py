import pygame
from player import y_pos
from settings import *
from Sphere import Sphere
import random

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])
clock = pygame.time.Clock()
sphere = Sphere(random.randint(150, HEIGHT - 150), random.randint(150, WIDTH - 150), random.choice([-1, 1]), random.choice([-1, 1]))
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        y_pos += 5
    if keys[pygame.K_w]:
        y_pos -= 5
    sphere.update()
    pygame.draw.rect(screen, (255, 255, 255), (10, y_pos, 10, 150), 1)
    pygame.draw.circle(screen, (255, 255, 255), (sphere.x, sphere.y), 10)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
