import pygame
import random

from os import path

pygame.init()

img_dir = path.join(path.dirname(__file__), 'img')
player_img = pygame.image.load(path.join(img_dir, "哪吒.png")).convert()


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50, 25])
        # self.image.fill((255,0,0))
        self.image = player_img
        back = self.image.get_at((0, 0))
        self.image.set_colorkey(back)
        # self.image = pygame.transform.scale(self.image, [80,90])

        self.image = pygame.transform.scale(self.image, [30, 25])

        self.rect = self.image.get_rect(center=(600, 0))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

        self.x_speed = .05 * random.randint(-9, 9)
        self.y_speed = 0

    def move_towards(self, x, y):
        # adjust the x_speed and y_speed
        # so that the enemy moves towwards the x and y
        self.x_speed = 0
        self.y_speed = .01

    def update(self):
        self.exact_x += self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)

        # self.rect.right = 500
        if self.rect.left <= 0:
            self.rect.left = 0
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= 1200:
            self.rect.bottom = 0

    # self.exact_x = random.randint(0, 500)

    def to_top(self):
        self.rect.bottom = 0
        self.rect.y = 0
        self.exact_y = 0

        self.exact_x = random.randint(0, 1200)

    def update_speed(self, p_x, p_y):
        if p_x < self.exact_x:
            self.x_speed = -.1
        if p_y > self.exact_y:
            self.y_speed = .1
        if p_x > self.exact_x:
            self.x_speed = .1
        if p_y < self.exact_y:
            self.y_speed = -.1
