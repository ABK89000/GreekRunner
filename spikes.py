import pygame, random
from testLevel import *

class RoofSpikes(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #The roof spike's attributes

        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/threats/newRoofSpikes.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift

class FloorSpikes(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("Red")

        #The floor spike's attributes

        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/threats/newFloorSpikes.png")

        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift

