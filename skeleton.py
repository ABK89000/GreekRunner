import pygame
from supportSkeleton import import_folder

class Skeleton(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()

        #Skeleton attributes
        self.animations = {}
        self.import_character_assets()
        self.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/skeleton/walkLeft/skeletonLeftwalk1cut (1).png")
        self.frame_index = 0
        self.animation_speed = 0.1
        self.status = "walkLeft"

        self.offset = (-64, -64)
        self.rect = self.image.get_rect(topleft = pos)

        self.image = self.animations[self.status][self.frame_index]
        self.direction = pygame.math.Vector2(0,0)

        #Hit box being added here
        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])

        self.speed = 2


    def animate(self):
        #Animates the skeleton
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >=len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def import_character_assets(self):
        #Finds the animation in the finder in the graphics folder
        character_path = "/Users/anbrew22/PycharmProjects/PythonGame/graphics/skeleton/"

        self.animations = {"walkLeft":[], "walkRight":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def horizontal_movement_collison(self, tiles):
        #Stops the skeleton from going inside blocks horizontally. Skeleton simply moves left and right and turns if hits a block
        self.hitbox.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):

                if self.hitbox.left + 10 > tile.rect.right:
                    self.hitbox.left = tile.rect.right

                    self.status = "walkRight"
                    self.offset = (-40, -64)

                elif self.hitbox.right < tile.rect.left + 30:

                    self.hitbox.right = tile.rect.left
                    self.status = "walkLeft"
                    self.offset = (16, -64)


    def vertical_movement_collison(self, tiles):
         #Stops the skeleton from going inside blocks vertically

        self.hitbox.y += self.direction.y * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):

                if self.hitbox.top + 30 > tile.rect.bottom:
                    self.hitbox.top = tile.rect.bottom

                elif self.hitbox.bottom < tile.rect.top+30:
                    self.hitbox.bottom = tile.rect.top


    def update(self, y_shift, tiles):
        #Calls the functions so the skeleton has what's previously established

        self.hitbox.y += y_shift
        self.horizontal_movement_collison(tiles)
        self.vertical_movement_collison(tiles)

        self.rect = self.hitbox.inflate(self.offset[0] * -1, self.offset[1] * -1)

        if self.status == "walkRight":
            self.direction.x = 1
        elif self.status == "walkLeft":
            self.direction.x = -1

        self.animate()

    #def draw(self, screen):
        #pygame.draw.rect(screen,(0,255,0), self.hitbox, 1)

