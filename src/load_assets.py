import os

import pygame

# IMAGES 
def load(dir: str) -> dict:
    images = {}
    for filename in os.listdir(os.path.abspath(dir)):
        name = filename.split(".")[0]
        img = pygame.image.load(os.path.join(dir, filename))
        images[name] = img
    return images


    