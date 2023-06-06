from os import walk
import pygame
from testLevel import *

def import_folder(path):

    surface_list = []
    for _, __, img_files in walk(path):
        if img_files[0] == ".DS_Store":
                del img_files[0]
        elif img_files[1] == ".DS_Store":
            del img_files[1]
        elif img_files[2] == ".DS_Store":
            del img_files[2]
        for file in img_files:

            full_path = path + "/" + file

            image = pygame.image.load(full_path)

            image = pygame.transform.scale(image, (128,128))

            #image = pygame.transform.flip(image,True,False)

            surface_list.append(image)
    return surface_list
