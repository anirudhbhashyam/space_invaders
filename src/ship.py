import pygame

from abc import ABC, abstractmethod
from dataclasses import dataclass, field

from typing import ClassVar

from laser import Laser

@dataclass
class Ship(ABC):
    x:                   float
    y:                   float 
    health:              float         = 100
    ship_img:            pygame.image  = None
    laser_img:           pygame.image  = None
    lasers:              list          = field(init = False, default_factory = list)
    cooldown_counter:    int           = 0
    COOLDOWN:            ClassVar[int] = 30
    
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)
            
    def move_lasers(self, velocity: float, obj) -> None:
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_window_q():
                self.lasers.remove(laser)
            elif laser.collision_q(obj):
                obj.health -= 10
                self.lasers.remove(laser)
    
    def shoot(self) -> None:
        if self.cooldown_counter == 0:
            self.lasers.append(Laser(self.x + self.get_width() / 32, self.y + self.get_height() / 32, self.laser_img))
            self.cooldown_counter = 1
            
    def cooldown(self):
        if self.cooldown_counter >= self.COOLDOWN:
            self.cooldown_counter = 0
        elif self.cooldown_counter > 0:
            self.cooldown_counter += 1
    
    def get_width(self) -> float:
        return self.ship_img.get_width()
    
    def get_height(self) -> float:
        return self.ship_img.get_height()
    
    def get_health(self) -> float:
        return self.health
    
    @abstractmethod
    def move(keys: dict) -> None:
        pass
        
        
 

    
    