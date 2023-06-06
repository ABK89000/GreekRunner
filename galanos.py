import pygame
import random

class Galanos(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("Grey")

        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/tiles/GalanosFix.png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift
        self.rect.x += random.randint(-3, 3)
