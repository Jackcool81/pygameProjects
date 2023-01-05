import pygame
import random

pygame.init()

from os import path

img_dir = path.join(path.dirname(__file__), 'img')
Enemy_img = pygame.image.load(path.join(img_dir, "Tiger.png"))
Heart_img = pygame.image.load(path.join(img_dir, "heart.png"))
Coins_img = pygame.image.load(path.join(img_dir, "coin.png"))

class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.image = pygame.Surface([30, 40])
        self.image = Enemy_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [30, 40])

        # give it a location to put the surface

        self.rect = self.image.get_rect(center=(random.randint(0, 1200), 0))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

        # give it a speed
        self.x_speed = 0
        self.y_speed = 0.1 * random.randint(5, 15)

    def update(self):
        # it is on bottom when self.rect.bottom (bottom of rectangle) is at the bottom
        # we know it's not at the bottom when self.rect.bottom isn't at the bottom
        # when it's not at bottom it's in the air
        # we know that spirte is in the air when it's bottom is not at the bottom of the screen

        # self.y_speed = .1

        self.exact_x += self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)

        if self.rect.right >= 1200:
            self.rect.right = 1200
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 1200:
            # print("here")
            # print(self.rect.bottom)
            # print(self.rect.top)
            # print(self.rect.y)
            self.rect.bottom = 0
            self.rect.y = 0
            self.exact_y = 00
            # self.y_speed = .1
            self.exact_x = random.randint(0, 1200)

    def to_top(self):
        self.rect.bottom = 0
        self.rect.y = 0
        self.exact_y = 0
        # self.y_speed = .1
        self.exact_x = random.randint(0, 1200)

class Hearts(pygame.sprite.Sprite):

    def __init__(self):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.image = pygame.Surface([30, 40])
        self.image = Heart_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [30, 40])

        # give it a location to put the surface

        self.rect = self.image.get_rect(center=(random.randint(0, 1200), 0))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

        # give it a speed
        self.x_speed = 0
        self.y_speed = 1 * random.randint(1, 2)

    def update(self):
        # it is on bottom when self.rect.bottom (bottom of rectangle) is at the bottom
        # we know it's not at the bottom when self.rect.bottom isn't at the bottom
        # when it's not at bottom it's in the air
        # we know that spirte is in the air when it's bottom is not at the bottom of the screen

        # self.y_speed = .1

        self.exact_x += self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)

        if self.rect.right >= 1200:
            self.rect.right = 1200
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 1200:
            # print("here")
            # print(self.rect.bottom)
            # print(self.rect.top)
            # print(self.rect.y)
            self.rect.bottom = 0
            self.rect.y = 0
            self.exact_y = 00
            # self.y_speed = .1
            self.exact_x = random.randint(0, 1200)

    def to_top(self):
        self.rect.bottom = 0
        self.rect.y = 0
        self.exact_y = 0
        # self.y_speed = .1
        self.exact_x = random.randint(0, 1200)

class Coins(pygame.sprite.Sprite):

    def __init__(self):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.image = pygame.Surface([30, 40])
        self.image = Coins_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [30, 40])

        # give it a location to put the surface

        self.rect = self.image.get_rect(center=(random.randint(0, 1200), 0))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

        # give it a speed
        self.x_speed = 0
        self.y_speed = 0.1 * random.randint(4, 9)

    def update(self):
        # it is on bottom when self.rect.bottom (bottom of rectangle) is at the bottom
        # we know it's not at the bottom when self.rect.bottom isn't at the bottom
        # when it's not at bottom it's in the air
        # we know that spirte is in the air when it's bottom is not at the bottom of the screen

        # self.y_speed = .1

        self.exact_x += self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)

        if self.rect.right >= 1200:
            self.rect.right = 1200
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 1200:
            # print("here")
            # print(self.rect.bottom)
            # print(self.rect.top)
            # print(self.rect.y)
            self.rect.bottom = 0
            self.rect.y = 0
            self.exact_y = 00
            # self.y_speed = .1
            self.exact_x = random.randint(0, 1200)

    def to_top(self):
        self.rect.bottom = 0
        self.rect.y = 0
        self.exact_y = 0
        # self.y_speed = .1
        self.exact_x = random.randint(0, 1200)
    
