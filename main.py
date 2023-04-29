import asyncio
import time

from player import Player
from settings import *
from Sphere import Sphere
import random

from tcp import TcpConnect

pygame.init()
clock = pygame.time.Clock()
sphere = Sphere(random.randint(150, HEIGHT - 150), random.randint(150, WIDTH - 150), random.choice([-1, 1]),
                random.choice([-1, 1]))
running = True

player1 = Player()
player2 = Player()
player2.x_pos = WIDTH - 10

# Ask user if they want to start as host or client
host = input("Do you want to start as host? (y/n) ").lower() == 'y'

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
    if host:
        TcpConnect.senddata(str(player1.y_pos).encode('utf-8'))
        try:
            player2.y_pos = float(TcpConnect.getdata().decode())
        except:
            pass
    else:
        TcpConnect.senddata(str(player1.y_pos).encode('utf-8'))
        try:
            player2.y_pos = float(TcpConnect.getdata().decode())
        except:
            pass

    player1.update(dt)
    player2.update(dt)
    pygame.display.flip()
    clock.tick(60)  # Cap the frame rate at 60 FPS

# Close connection after the game loop
TcpConnect.close()

pygame.quit()
