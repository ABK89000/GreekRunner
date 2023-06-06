from os import walk
import pygame

#loads the image for that specific frame of the animation and displays it
def import_folder(path):

    surface_list = []
    for _, __, img_files in walk(path):
        if img_files[0] == ".DS_Store":
                del img_files[0]
        elif img_files[1] == ".DS_Store":
            del img_files[1]
        for file in img_files:

            full_path = path + "/" + file

            image = pygame.image.load(full_path)

            image = pygame.transform.scale(image, (64,64))

            #image = pygame.transform.flip(image,True,False)

            surface_list.append(image)
    return surface_list
