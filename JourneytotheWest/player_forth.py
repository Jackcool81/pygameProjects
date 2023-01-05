import pygame

pygame.init()

from os import path

img_dir = path.join(path.dirname(__file__), 'img')
player_img = pygame.image.load(path.join(img_dir, "monkey2.png"))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.ride = 1
        self.image = pygame.Surface([80, 90])
        self.image.fill((255, 255, 255))
        self.image = player_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [80, 90])

        # give it a location to put the surface
        self.rect = self.image.get_rect(center=(100, 300))

        # give it a speed
        self.x_speed = 0
        self.y_speed = 0
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y
    def update(self):
        keystate = pygame.key.get_pressed()
        self.y_speed = 0
        self.x_speed = 0
        # keystate is dictionary where if a key is pressed, then that key is true
        if keystate[pygame.K_UP]:
            self.y_speed -= 20
        if keystate[pygame.K_DOWN]:
            self.y_speed += 20
        if keystate[pygame.K_LEFT]:
            self.x_speed -= 20
        if keystate[pygame.K_RIGHT]:
            self.x_speed += 20

        # it is on bottom when self.rect.bottom (bottom of rectangle) is at the bottom
        # we know it's not at the bottom when self.rect.bottom isn't at the bottom
        # when it's not at bottom it's in the air
        # we know that spirte is in the air when it's bottom is not at the bottom of the screen
      
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
        
    def ride_turtle(self):
        self.exact_x += self.ride
        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)
        #This make the enemy stop at the middle
        stop_enemy = 1100
        if self.rect.left >= stop_enemy:
            self.ride = 0
            self.rect.left = stop_enemy

            
    # print(self.exact_x)
  