import pygame

class FireWisp(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()

        self.direction = "down"
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/threats/fireWisp (1).png")
        self.rect = self.image.get_rect(topleft=pos)


    def vertical_movement_collison(self, tiles):
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.rect):

                if self.rect.top < tile.rect.top + 50:
                    #self.rect.bottom = tile.rect.top
                    self.direction = "up"

                if self.rect.top > tile.rect.bottom - 50:
                    #self.rect.top = tile.rect.bottom
                    self.direction = "down"



    def update(self, y_shift, tiles):

        self.vertical_movement_collison(tiles)

        if self.direction == "down":
            self.rect.y += y_shift + 4.5

        elif self.direction == "up":
            self.rect.y += y_shift - 4.5
