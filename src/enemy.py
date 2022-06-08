import pygame

from ship import Ship
import load_assets

ASSETS = load_assets.load("res")

class Enemy(Ship):
    COLOR_MAP = dict(zip(["red", "green", "blue"], 
                         [("pixel_ship_red_small", "pixel_laser_red"), ("pixel_ship_green_small", "pixel_laser_green"), ("pixel_ship_blue_small", "pixel_laser_blue")]
                         ))

    def __init__(self, x, y, health, color: str):
        super().__init__(x, y, health)
        asset_names                   = self.COLOR_MAP[color]
        self.ship_img                 = ASSETS[asset_names[0]]
        self.laser_img                = ASSETS[asset_names[1]]
        self.max_health               = 100
        self.velocity                 = 5
        self.mask                     = pygame.mask.from_surface(self.ship_img)
        
    def move(self, velocity: float) -> None:
        self.y += velocity
        