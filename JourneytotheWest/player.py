import pygame

pygame.init()

from os import path

img_dir = path.join(path.dirname(__file__), 'img')
#player_img = pygame.image.load(path.join(img_dir, "character.png")).convert()
player_img = pygame.image.load(path.join(img_dir, "monkey.png"))

class Player(pygame.sprite.Sprite):
    
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([80, 59])
        self.image.fill((255, 255, 255))
        self.image = player_img
        back = self.image.get_at((0, 0))
        self.image.set_colorkey(back)
        self.image = pygame.transform.scale(self.image, [80, 90])
        
        self.rect = self.image.get_rect(center=(1200 / 2, 600 - 34))

        self.x_speed = 0
        self.y_speed = 0
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y

    def update(self):
        keystate = pygame.key.get_pressed()
        self.y_speed = 0
        self.x_speed = 0

        if keystate[pygame.K_UP]:
            self.y_speed -= 20
        if keystate[pygame.K_DOWN]:
            self.y_speed += 20
        if keystate[pygame.K_LEFT]:
            
            self.x_speed -= 20
        if keystate[pygame.K_RIGHT]:
            
            self.x_speed += 20



        if self.rect.bottom != 1200:
            self.y_speed += 1
        self.x_speed *= 0.1
        self.y_speed *= 0.1

        self.exact_x += self.x_speed
        self.exact_y += self.y_speed

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)

        if self.rect.right > 1200:
            self.rect.right = 1200
            self.exact_x = self.rect.x
        if self.rect.left < 0:
            self.rect.left = 0
            self.exact_x = self.rect.x
        if self.rect.top < 0:
            self.rect.top = 0
            self.exact_y = self.rect.y
        if self.rect.bottom > 1200:
            self.rect.bottom = 1200
            self.exact_y = self.rect.y

    def get_loc(self):
        # return x,y -> players's x and the player's y

        return self.exact_x, self.exact_y
