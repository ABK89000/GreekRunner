import pygame

#Creates the background for the final win screen
class WinBackground(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/ResizedEndingArt-castle (1).png")
        self.original_image = self.image
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 5
