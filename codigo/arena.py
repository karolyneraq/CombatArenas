import pygame

# opening the files of the arenas
arena_difficult_file = open("assets/arena_dif.txt", "r")
arena_easy_file = open("assets/arena_easy.txt", "r")

# Reading the arenas
data_hard = arena_difficult_file.read()
data_easy = arena_easy_file.read()

# Converting each line in an element of the lists
arena_difficulties = [data_hard.split('\n'), data_easy.split('\n')]

# Closing the files
arena_difficult_file.close()
arena_easy_file.close()


def draw_arena(screen, color, stage):

    lista = []

    if stage == 0:

        for i in range(25):

            for j in range(36):

                if arena_difficulties[stage][i][j] == '1':

                    obstacle_face = pygame.image.load("assets/city_obstacle.png")
                    x = (j * 25)
                    y = (i * 22) + 100
                    position = (x, y)
                    size = obstacle_face.get_size()
                    obstacle_rect = pygame.draw.rect(screen, color, (position[0], position[1],
                                                                     obstacle_face.get_width(), obstacle_face.get_height()))
                    element = (obstacle_face, obstacle_rect, position, size)
                    lista.append(element)

    else:

        for i in range(25):

            for j in range(36):

                if arena_difficulties[stage][i][j] == '1':
                    obstacle_face = pygame.image.load("assets/vegetation_obstacle1.png")
                    x = (j * 25)
                    y = (i * 22) + 100
                    position = (x, y)
                    size = obstacle_face.get_size()
                    obstacle_rect = pygame.draw.rect(screen, color, (position[0], position[1],
                                                                     obstacle_face.get_width(),
                                                                     obstacle_face.get_height()))
                    element = (obstacle_face, obstacle_rect, position, size)
                    lista.append(element)

    return lista
