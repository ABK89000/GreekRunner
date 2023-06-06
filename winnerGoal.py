import pygame
from player import *
from testLevel import *

#creates the tile that when collided with allows the player to win the game. Only creates attributes and updates it

class WinnerGoal(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("red")
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/goal/escapedoor.png")


        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift
