import pygame
import random

from pygame.mixer import stop

pygame.init()

from os import path

def draw_text(surface, text, size, x, y):
        font_name = pygame.font.get_default_font()
        font = pygame.font.Font(font_name, size)
        text_sruface = font.render(text, True, (0, 0, 0))
        txt_rect = text_sruface.get_rect()
        txt_rect.midtop = (x, y)
        surface.blit(text_sruface, txt_rect)
class Enemy(pygame.sprite.Sprite):

    def __init__(self,screen,img,words,speed,screen_width,screen_height):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.image = pygame.Surface([30, 40])
        self.image = img
        self.screen = screen
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [80, 100])
        self.screen_width=screen_width
        self.screen_height=screen_height
        # give it a location to put the surface
        self.words = words
        self.rect = self.image.get_rect(center=(self.screen_width, self.screen_height/2))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

        # give it a speed
        self.y_speed = 0.075
        self.x_speed = 0.1 * speed
    def move(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.exact_x = x
        self.exact_y = y

    def update(self):
    

        self.exact_x -= self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)
        #This make the enemy stop at the middle
        stop_enemy = 550
        if self.rect.left <= stop_enemy:
            self.y_speed = 0
            self.rect.left = stop_enemy
            draw_text(self.screen, self.words, 30,600,300)
    def run_away(self):
        up_speed = 0.1
        self.exact_x += self.x_speed
        self.exact_y -= up_speed
        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)
   

        
        



    
