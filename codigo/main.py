import pygame
from arena import arena_one
from collision import collision_tank_or_ball, collision_tank_ball
from config import *

pygame.init()

# screen
size = (900, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("combat tank")
screen.fill(orange)

exec(open("draw_tank.py").read())
exec(open("game_elements.py").read())

# objects draw
list_of_objects = arena_one(screen, yellow)

# wall
wall1 = pygame.draw.rect(screen, yellow, (0, 0, 900, 25))
wall2 = pygame.draw.rect(screen, yellow, (0, 625, 900, 25))
wall3 = pygame.draw.rect(screen, yellow, (0, 100, 25, 800))
wall4 = pygame.draw.rect(screen, yellow, (875, 100, 25, 800))

clock = pygame.time.Clock()

loop = True
recharge = False
respawn = False
no_animation = True
stop = False
victory1 = False
victory2 = False
time = 0

# game loop
while loop:

    exec(open("game.py").read())

pygame.quit()
