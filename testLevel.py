import pygame
from settings import *
from tiles import Tile
from player import *
from lava import *
from chests import *
from winScreen import *
from background import Background
from BackgroundTest import backgroundTest
from lightBackground import LBackground
from goal import Goal
from spikes import *
from galanos import *
from fireWisp import *
from bonePile import *
from skeleton import *
from easterEggPhoto import *
from easterEggDoor import *
from winnerGoal import *

class Level:

    #creates initial background
    background = backgroundTest((0,0))
    backgroundGroup = pygame.sprite.GroupSingle()
    backgroundGroup.add(background)

    def __init__(self, level_data, surface, level_no):
        #attributes of a level from the various files created
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.background = pygame.sprite.Group()
        self.lighting = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.flood = pygame.sprite.Group()
        self.roofspikes = pygame.sprite.Group()
        self.floorspikes = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.goal = pygame.sprite.Group()
        self.galanos = pygame.sprite.Group()
        self.firewisp = pygame.sprite.Group()
        self.bonepile = pygame.sprite.Group()
        self.skeleton = pygame.sprite.Group()
        self.winDoor = pygame.sprite.Group()
        self.easterEggDoor2 = pygame.sprite.Group()
        self.world_shift = 0
        self.firstChest = False
        self.setup_level(level_data)
        self.music = 1
        self.level_no = level_no

        print(self.level_no)

        self.dead = False
        self.escaped = False
        self.winner = False
        self.easterEgg = False

    def setup_level(self, layout):
        #Checks every tile in the level layout for a specific letter and creates an object everytime and place it's on the layout
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size

                if cell == "x":
                    tile = Tile((x,y), tile_size)
                    self.tiles.add(tile)
                elif cell == "b":
                    backgrounds = Background((x,y), tile_size)
                    self.background.add(backgrounds)
                elif cell == "l":
                    lightBackgrounds = LBackground((x,y), tile_size)
                    self.lighting.add(lightBackgrounds)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                elif cell == "w":
                    water = Water((x,y), tile_size)
                    self.flood.add(water)
                elif cell == "c":
                    treasure = Chest((x,y), tile_size)
                    self.chests.add(treasure)
                elif cell == "g":
                    door = Goal((x,y), tile_size)
                    self.goal.add(door)
                elif cell == "v":
                    roofspike = RoofSpikes((x,y), tile_size)
                    self.roofspikes.add(roofspike)
                elif cell == "^":
                    floorspike = FloorSpikes((x,y), tile_size)
                    self.floorspikes.add(floorspike)
                elif cell == "0":
                    galanosfat = Galanos((x,y), tile_size)
                    self.galanos.add(galanosfat)
                elif cell == "f":
                    flamespirit = FireWisp((x,y), tile_size)
                    self.firewisp.add(flamespirit)
                elif cell == "~":
                    bones = BonePile((x,y), tile_size)
                    self.bonepile.add(bones)
                elif cell == "s":
                    skele = Skeleton((x,y), tile_size)
                    self.skeleton.add(skele)
                elif cell == "W":
                    winningGoal = WinnerGoal((x,y), tile_size)
                    self.winDoor.add(winningGoal)
                elif cell == "e":
                    eggDoor = EasterEggDoor((x,y), tile_size)
                    self.easterEggDoor2.add(eggDoor)

    def scroll_y(self):
        #creates a scroll in the level centered around the player
        player = self.player.sprite
        player_y = player.rect.y
        direction_y = player.direction.y

        if player_y < screen_height and direction_y < 0:
            self.world_shift = 15

        elif player_y > (screen_height / 2) +200 and direction_y > 0:
            self.world_shift = -player.speed - 50
        elif player_y > screen_height / 2 and direction_y > 0:
            self.world_shift = -player.speed - 12

        else:
            self.world_shift = 0

    def run(self):
        #If player is in the level and not escaped or dead

        if not self.dead and not self.escaped and not self.winner and not self.easterEgg or self.player.sprite.godMode == True and not self.escaped and not self.winner and not self.easterEgg:

            #Reloads music incase restart or start
            if self.music!= "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/2-07. Sawmill Thrill.mp3":
                self.music = "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/2-07. Sawmill Thrill.mp3"
                pygame.mixer.music.load(self.music)
                pygame.mixer.music.play(-1)

            #Updates the position of the object
            self.backgroundGroup.update()
            self.backgroundGroup.draw(self.display_surface)
            self.tiles.update(self.world_shift)
            self.firewisp.update(self.world_shift, self.tiles)
            self.flood.update(self.world_shift)
            self.background.update(self.world_shift)
            self.lighting.update(self.world_shift)
            self.chests.update(self.world_shift)
            self.goal.update(self.world_shift)
            self.winDoor.update(self.world_shift)
            self.roofspikes.update(self.world_shift)
            self.floorspikes.update(self.world_shift)
            self.galanos.update(self.world_shift)
            self.bonepile.update(self.world_shift)
            self.skeleton.update(self.world_shift, self.tiles)
            self.easterEggDoor2.update(self.world_shift)

            #Draws the object in the updated position
            self.tiles.draw(self.display_surface)
            self.background.draw(self.display_surface)
            self.lighting.draw(self.display_surface)
            self.chests.draw(self.display_surface)
            self.goal.draw(self.display_surface)
            self.roofspikes.draw(self.display_surface)
            self.skeleton.draw(self.display_surface)
            #for s in self.skeleton:
                #s.draw(self.display_surface)
            self.floorspikes.draw(self.display_surface)
            self.winDoor.draw(self.display_surface)
            self.galanos.draw(self.display_surface)
            self.firewisp.draw(self.display_surface)
            self.bonepile.draw(self.display_surface)
            self.flood.draw(self.display_surface)
            self.easterEggDoor2.draw(self.display_surface)
            self.scroll_y()

            self.player.update(self.tiles, self.chests)
            self.player.draw(self.display_surface)
            #self.player.sprite.draw(self.display_surface)

            #Variables for deadly collison. Makes list of all of the object that has been collided
            collided_lava = pygame.sprite.spritecollide(self.player.sprite, self.flood, False)

            collided_roofspike = pygame.sprite.spritecollide(self.player.sprite, self.roofspikes, False)

            collided_floorspike = pygame.sprite.spritecollide(self.player.sprite, self.floorspikes, False)

            collided_chest = pygame.sprite.spritecollide(self.player.sprite, self.chests, False)

            collided_goal = pygame.sprite.spritecollide(self.player.sprite, self.goal, False)

            collided_winGoal = pygame.sprite.spritecollide(self.player.sprite, self.winDoor, False)

            collided_easterEggGoal = pygame.sprite.spritecollide(self.player.sprite, self.easterEggDoor2, False)

            collided_galanos = pygame.sprite.spritecollide(self.player.sprite, self.galanos, False)

            collided_firewisp = pygame.sprite.spritecollide(self.player.sprite, self.firewisp, False)

            collided_skeleton = pygame.sprite.spritecollide(self.player.sprite, self.skeleton, False)


            #Checks if the players have collided with these deadly objects or chest
            if len(collided_roofspike) > 0:

                self.dead = True

            if len(collided_winGoal) > 0:

                self.winner = True
                self.escaped = True

            if len(collided_easterEggGoal) > 0:
                self.easterEgg = True

            if len(collided_floorspike) > 0 or len(collided_roofspike) > 0:

                self.dead = True
                self.reason = "You were impaled on a spike"

            if len(collided_lava) > 0:

                self.dead = True
                self.reason = "You were incinerated by the lava"

            if len(collided_galanos) > 0:

                self.dead = True
                self.reason = "Galanos is so fat he ate you"

            if len(collided_firewisp) > 0:

                self.dead = True
                self.reason = "The fire wisp burned you"

            if len(collided_skeleton) > 0:

                self.dead = True
                self.reason = "The skeleton eviscerated you"

            for chest in collided_chest:

                chest.image = pygame.image.load("/Users/anbrew22/PycharmProjects/PythonGame/graphics/chests/open-chest.png")
                self.player.sprite.speed = 9

            if len(collided_goal) > 0:

                self.escaped = True

        #If the player is dead loads death text and music instead
        if self.dead == True and self.player.sprite.godMode == False:

            if self.music == "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/2-07. Sawmill Thrill.mp3":
                pygame.mixer.music.stop
                self.music = "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/5-21 Game Over.mp3"
                pygame.mixer.music.load(self.music)
                pygame.mixer.music.play(-1)

            font = pygame.font.Font("freesansbold.ttf", 32)
            DeathText = font.render( "YOU'RE GREEK", True, (255,0,0))
            ReasonText = font.render(self.reason, True, (255,0,0))
            RestartText = font.render( "Press the 'r' key to retry", True, (255,0,0))

            self.display_surface.blit(DeathText, (600,300))
            self.display_surface.blit(RestartText, (540,500))
            self.display_surface.blit(ReasonText, (500,400))

        key = pygame.key.get_pressed()

        #If they escaped does not load level but escaped text
        if self.escaped == True and not self.winner:

            if self.music == "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/2-07. Sawmill Thrill.mp3":
                pygame.mixer.music.stop
                self.music = "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/KEerORa3kYb_final-fantasy-vii-victory-fanfare-hq.mp3"
                pygame.mixer.music.load(self.music)
                pygame.mixer.music.play(1)

            font = pygame.font.Font("freesansbold.ttf", 32)
            WinText = font.render( "YOU WON", True, (0,255,0))
            ContinueText = font.render( "Press the 'n' key to move to the next level", True, (0,255,0))
            self.display_surface.blit(WinText, (600,300))
            self.display_surface.blit(ContinueText, (400,400))

        #if escaped final level shows final win screen
        if self.winner == True:
            if self.music == "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/2-07. Sawmill Thrill.mp3":
                pygame.mixer.music.stop
                self.music = "/Users/anbrew22/PycharmProjects/PythonGame/sound/music/slow-motion-121841.mp3"
                pygame.mixer.music.load(self.music)
                pygame.mixer.music.play(-1)

            background = WinBackground((0,0))
            backgroundGroup = pygame.sprite.GroupSingle()
            backgroundGroup.add(background)
            backgroundGroup.update()
            backgroundGroup.draw(self.display_surface)

            font = pygame.font.Font("freesansbold.ttf", 48)
            endText = font.render( "Your journey is over", True, (0,255,0))
            self.display_surface.blit(endText, (220,200))

        elif self.easterEgg == True:
            background = EasterEggPhoto2((0,0))
            backgroundGroup = pygame.sprite.GroupSingle()
            backgroundGroup.add(background)
            backgroundGroup.update()
            backgroundGroup.draw(self.display_surface)



