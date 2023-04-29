import asyncio
import time

from player import Player
from settings import *
from Sphere import Sphere
import random

from tcp import TcpConnect

pygame.init()
clock = pygame.time.Clock()
sphere = Sphere(150, 150, 1, 1)
running = True

player1 = Player()
player2 = Player()
player2.x_pos = WIDTH - 10

# Ask user if they want to start as host or client
host = input("Do you want to start as host? (y/n) ").lower() == 'y'
time.sleep(10)
# Establish connection before the game loop
if host:
    TcpConnect.bind(IP, PORT)
else:
    TcpConnect.connect(IP, PORT)

while running:
    dt = clock.get_time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    # Screen clean
    sphere.update(player1.y_pos, player2.y_pos, dt, player1.size, player2.size)
    TcpConnect.senddata(f'{round(player1.y_pos, 6)} {round(sphere.x, 6)} {round(sphere.y, 6)}'.encode('utf-8'))
    try:
        data = TcpConnect.getdata().decode().split(' ')
        player2.y_pos = float(data[0])
        if not host:
            sphere.x = WIDTH - float(data[1])
            sphere.y = float(data[2])
    except:
        pass
    player1.update(dt)
    player2.update(dt)
    pygame.display.flip()
    clock.tick(120)  # Cap the frame rate at 60 FPS

# Close connection after the game loop
TcpConnect.close()

pygame.quit()
