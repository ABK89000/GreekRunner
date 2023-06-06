import pygame, random
from testLevel import *


#creates a tile and makes it update faster than the y shift allowing it to continously rise
class Water(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("Red")

        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/threats/lava-halftone-modern-design-backdrop-hot-red-bright-pixel-camouflage-lava-halftone-modern-design-backdrop-red-bright-pixel-214928901 (1).png")

        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift - 2.5

