import os
import sys
import random

import pygame

sys.path.append(os.path.abspath("src"))

import load_assets
import window

from ship import Ship
from player import Player
from enemy import Enemy
from laser import collide

FPS = 60

ASSETS_DIR = "res"
ASSETS = load_assets.load(ASSETS_DIR)

# Resize the background to the window.
ASSETS["background-black"] = pygame.transform.scale(ASSETS["background-black"], (window.WIDTH, window.HEIGHT))

def main():
    run = True
    window.render_text("Press any button to play.", (50, 10), window.main_font, True)
    while run:
        window.render_pixels(ASSETS["background-black"])
        window.render_text("Press left mouse button.", (window.WIDTH / 2, window.HEIGHT / 2), window.main_font, True)
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game()
                
    pygame.quit()

def game():    
    run = True
    timer = pygame.time.Clock()
    
    level = 0
    lives = 5
    wave_length = 5
    enemy_velocity = 1
    laser_velocity = 4
    enemies = []
    player = Player(300, 630, 100, ASSETS["pixel_ship_yellow"], ASSETS["pixel_laser_yellow"])

    while run:
        timer.tick(FPS)
        
        window.render_pixels(ASSETS["background-black"])
        window.render_text(f"Level: {level}", (10, 10), window.main_font)
        window.render_text(f"Lives: {lives}", (10, 40), window.main_font)
        
        for enemy in enemies:
            enemy.draw(window.WINDOW)
            
        player.draw(window.WINDOW)
        
        if lives <= 0 or player.get_health() <= 0:
            window.lost = True
            window.lost_count += 1      
            window.render_text(f"Lost at level {level}", (window.WIDTH / 2, window.HEIGHT / 2), window.lost_font, True)
        
        pygame.display.update()
        
        if window.lost:
            if window.lost_count > FPS * 5:
                run = False
            else:
                continue
            
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            enemies = [Enemy(random.randrange(50, window.WIDTH - 50), 
                             random.randrange(-1000, -100), 100, 
                             random.choice(["red", "blue", "green"])) 
                       for _ in range(wave_length)]
            
        keys = pygame.key.get_pressed()
        
        player.move(keys)
        player.move_lasers(-laser_velocity, enemies)
        
        for enemy in enemies[:]:
            enemy.move(enemy_velocity)
            enemy.move_lasers(laser_velocity, player)
            
            if random.randrange(0, 4 * FPS) == 1:
                enemy.shoot()   
            elif collide(enemy, player):
                player.health -= 10
                enemies.remove(enemy)
                
            if enemy.y + enemy.get_height() > window.HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
    
if __name__ == "__main__":
    main()
    