import pygame, sys
from settings import *
from testLevel import Level
from player import *

#Creates initial level and makes parameters such as fps
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
level = Level(level1_map, screen, 1)

current_level = 1

#continously loads and updates the level
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        key = pygame.key.get_pressed()

        #Finds out what level it is to restart or head to next level
        if key[pygame.K_r] and current_level == 1 and not level.escaped and not level.winner:
            level = Level(level1_map, screen, 1)

        elif key[pygame.K_r] and current_level == 2 and not level.escaped:
            level = Level(level2_map, screen, 2)

        elif key[pygame.K_r] and current_level == 3 and not level.escaped:
            level = Level(level3_map, screen, 3)

        elif key[pygame.K_r] and current_level == 4 and not level.escaped:
            level = Level(level4_map, screen, 4)

        if key[pygame.K_n] and level.escaped == True and current_level == 1:
            current_level = 2
            level = Level(level2_map, screen, 2)

        elif key[pygame.K_n] and level.escaped == True and current_level == 2:
            current_level = 3
            level = Level(level3_map, screen, 3)

        elif key[pygame.K_n] and level.escaped == True and current_level == 3:
            current_level = 4
            level = Level(level4_map, screen, 4)

    screen.fill("black")

    level.run()

    pygame.display.update()

    clock.tick(fps)

