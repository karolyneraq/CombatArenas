import pygame
from arena import draw_arena
from collision import collision_tank_or_ball, collision_tank_ball
from config import *

pygame.init()

# screen
size = (900, 650)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Combat Tank Pong")

exec(open("draw_tank.py").read())
exec(open("game_elements.py").read())

if stage_select == 0:

    background = pygame.image.load("assets/city_map.png")
    background.get_rect().center = (0, 0)
    screen.blit(background, background.get_rect())

else:

    background = pygame.image.load("assets/vegetation_map.png")
    background.get_rect().center = (0, 0)
    screen.blit(background, background.get_rect())

# objects draw
list_of_obstacles = draw_arena(screen, white, stage_select)

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
