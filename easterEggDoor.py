import pygame
from player import *
from testLevel import *

class EasterEggDoor(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("red")
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/goal/escapedoor.png")


        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift
