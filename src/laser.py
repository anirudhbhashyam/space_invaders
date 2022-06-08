import pygame

from dataclasses import dataclass, field

from window import HEIGHT

def collide(obj1, obj2) -> bool:
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return (obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) is not None)

@dataclass
class Laser:
    x:      float
    y:      float
    img:    pygame.image
    mask:   pygame.mask = field(init = False)
    
    def __post_init__(self):
        self.mask = pygame.mask.from_surface(self.img)
        
    def draw(self, window: pygame.Surface) -> None:
        window.blit(self.img, (self.x, self.y))
        
    def move(self, velocity: float) -> None:
        self.y += velocity
        
    def off_window_q(self) -> bool:
        return not (self.y <= HEIGHT and self.y >= 0)
    
    def collision_q(self, obj) -> bool:
        return collide(obj, self)
