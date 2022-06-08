import pygame

pygame.font.init()

WIDTH, HEIGHT = 750, 750
WINDOW        = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")

lost       = False
lost_count = 0

main_font = pygame.font.SysFont("comicsans", 25)
lost_font = pygame.font.SysFont("comicsans", 50)
    
def render_pixels(background: pygame.image, resource: pygame.image = None):
    WINDOW.blit(background, (0, 0))
    if resource is not None:
        WINDOW.blit(resource, (0, 0))

def render_text(text: str, position: tuple, font: pygame.font.SysFont, centre: bool = False):
    text_surface = font.render(text, True, (255, 255, 255))
    if centre:
        position = (position[0] - text_surface.get_width() / 2, 
                    position[1] - text_surface.get_height() / 2)
    WINDOW.blit(text_surface, position)
    
    