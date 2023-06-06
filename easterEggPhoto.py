import pygame

class EasterEggPhoto2(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/coolEasterEgg.png")
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
