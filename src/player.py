import pygame

from ship import Ship

from window import WIDTH, HEIGHT

class Player(Ship):
    def __init__(self, x, y, health, ship_img, laser_img):
        super().__init__(x, y, health)
        self.ship_img      = ship_img
        self.laser_img     = laser_img
        self.mask          = pygame.mask.from_surface(self.ship_img)
        self.max_health    = 100
        self.velocity      = 5
        
    def draw(self, window: pygame.Surface):
        super().draw(window)
        self.health_bar(window)
        
    def move(self, keys: dict) -> None:
        if (keys[pygame.K_w] or keys[pygame.K_UP]) and (self.y - self.velocity > 0):
            self.y -= self.velocity
        if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and (self.y + self.velocity + self.get_height() + 15 < HEIGHT):
            self.y += self.velocity
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and (self.x - self.velocity > 0):
            self.x -= self.velocity
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and (self.x + self.velocity + self.get_width() < WIDTH):
            self.x += self.velocity
        if (keys[pygame.K_SPACE]):
            self.shoot()
            
    def move_lasers(self, velocity: float, objects) -> None:
        self.cooldown()
        for laser in self.lasers:
            laser.move(velocity)
            if laser.off_window_q():
                self.lasers.remove(laser)
            else:
                for obj in objects:
                    if laser.collision_q(obj):
                        objects.remove(obj)
                        if laser in self.lasers:
                            self.lasers.remove(laser)
                    
    def health_bar(self, window: pygame.Surface):        
        pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.get_height() + 10, self.get_width(), 10))
        pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.get_height() + 10, self.get_width() * (self.health / self.max_health), 10))
        
        
        