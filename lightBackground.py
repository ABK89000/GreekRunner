import pygame

#creates the non solid closer background with a light as an uncollideable tile

class LBackground(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        #self.image = pygame.Surface((size, size))
        #self.image.fill("Grey")

        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/tiles/Backgroundlight (1).png")
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, y_shift):
        self.rect.y += y_shift
