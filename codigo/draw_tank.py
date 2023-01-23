import pygame
from config import *


# Function that creates a tank (player)
def create_tank(tank_photo):
    photo = pygame.Surface((tank_photo.get_width(), tank_photo.get_height()))
    photo.set_colorkey(orange)
    pygame.draw.rect(photo, orange, (0, 0, *tank_photo.get_size()))
    photo.blit(tank_photo, (0, 0))
    tank_angle = 0
    vel = (speed_x_tanks, speed_y_tanks)
    speed_tank = pygame.math.Vector2(vel)
    recharge_time1 = 0 + 0
    balls_list = []
    tank_player = [
        photo, tank_angle, [False, False, False, False, False], recharge_time1,
        speed_tank, balls_list, 3]
    return tank_player


# tank 1
archive = pygame.image.load("assets/tank1.png")
tank1 = create_tank(archive)
tank1.insert(0, archive)
tank1.insert(2, spawn_x_tank_1)
tank1.insert(3, spawn_y_tank_1)
tank1.insert(4, spawn_x_tank_1)
tank1.insert(5, spawn_y_tank_1)
tank1.append(1)

# tank 2
archive = pygame.image.load("assets/tank2.png")
tank2 = create_tank(archive)
tank2.insert(0, archive)
tank2.insert(2, spawn_x_tank_2)
tank2.insert(3, spawn_y_tank_2)
tank2.insert(4, spawn_x_tank_2)
tank2.insert(5, spawn_y_tank_2)
tank2.append(2)

list_two_tank = [tank1, tank2]
