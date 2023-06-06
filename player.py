import pygame
from settings import *
from support import import_folder
from testLevel import *
from chests import *

class Player(pygame.sprite.Sprite):

    def __init__(self, pos):
        super().__init__()

        #Player's attributes

        self.animations = {}
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15

        self.image = self.animations["Idle"][self.frame_index]

        self.offset = (-30, 0)
        self.rect = self.image.get_rect(topleft = pos)

        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 7
        self.jump_speed = -8

        self.status = "Idle"

        self.godMode = False

    def animate(self):
        #Animates the player
        animation = self.animations[self.status]

        self.frame_index += self.animation_speed
        if self.frame_index >=len(animation):
            self.frame_index = 0
        self.image = animation[int(self.frame_index)]

    def get_status(self):
        #Using the player's direction determines what animation to use

        if self.direction.y < 0 and self.status == "Idle":
            self.status = "Jump"
        elif self.direction.y < 0 and self.status == "Run":
            self.status = "Jump"

        elif self.direction.y < 0 and self.status == "IdleRight":
            self.status = "JumpRight"
        elif self.direction.y < 0 and self.status == "RunRight":
            self.status = "JumpRight"

        elif self.direction.y == 0 and self.status == "Jump":
            self.status = "Idle"
        elif self.direction.y == 0 and self.status == "JumpRight":
            self.status = "IdleRight"

        else:
            if self.direction.x < 0 and self.status!= "Jump":
                self.status = "Run"

            elif self.direction.x > 0 and self.status != "JumpRight":
                self.status = "RunRight"

            elif self.direction.x == 0 and self.status == "RunRight":
                self.status = "IdleRight"

            elif self.direction.x == 0 and self.status == "Run":
                self.status = "Idle"

    def get_input(self):
        #Creates the keys to cause movement

        key = pygame.key.get_pressed()

        if key[pygame.K_RIGHT]:
            self.direction.x = 1
        elif key[pygame.K_LEFT]:
            self.direction.x = -1
        elif key[pygame.K_g and pygame.K_o and pygame.K_d]:
            self.godMode = True
        elif key[pygame.K_1]:
            self.dead = False
        else:
            self.direction.x = 0

        if self.direction.y == 0.4 and not self.godMode:
            if key[pygame.K_SPACE]:
                self.jump()
        elif self.godMode == True:
            if key[pygame.K_SPACE]:
                self.direction.y = self.jump_speed

    def import_character_assets(self):
        #Finds the animation in the finder
        character_path = "/Users/anbrew22/PycharmProjects/PythonGame/graphics/player/"

        self.animations = {"Idle":[], "Run":[], "Jump":[], "RunRight":[], "IdleRight":[], "JumpRight":[]}

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def jump(self):
        #After being called when space is hit let's the player jump
        if self.status != "Jump":
            self.direction.y = self.jump_speed

    def horizontal_movement_collison(self, tiles, chests):
        #Stops the player from going inside blocks horizontally
        self.hitbox.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):

                if self.hitbox.left + 15 > tile.rect.right:
                    self.hitbox.left = tile.rect.right

                elif self.hitbox.right - 15 < tile.rect.left:
                    self.hitbox.right = tile.rect.left
        for treasure in chests.sprites():
            if treasure.rect.colliderect(self.hitbox):

                if self.hitbox.left + 10 > treasure.rect.right:
                    collided = True

                elif self.hitbox.right < treasure.rect.left + 10:
                    collided = True

    def vertical_movement_collison(self, tiles):
        #Stops the player from going inside blocks vertically
        global gravity

        self.apply_gravity()

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):

                if self.hitbox.top - 20 < tile.rect.top:
                    self.hitbox.bottom = tile.rect.top
                    self.direction.y = 0
                    #self.status = "Idle"
                    gravity = 0.4

                if self.hitbox.bottom - 20 > tile.rect.top:
                    gravity = 1
                    self.hitbox.top = tile.rect.bottom


    def apply_gravity(self):
        #makes the player constantly accelerate down
        self.direction.y += gravity
        self.hitbox.y += self.direction.y

    def update(self, tiles, chests):
        #Calls the functions so the player has what's previously established

        self.get_input()
        self.vertical_movement_collison(tiles)
        self.horizontal_movement_collison(tiles, chests)

        self.get_status()
        self.animate()

        self.rect = self.hitbox.inflate(self.offset[0] * -1, self.offset[1] * -1)

