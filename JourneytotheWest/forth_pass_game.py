import pygame

import time
from player_forth import Player
#from enemy_third import Enemy
from finish import finalpass
pygame.init()

from os import path


img_dir = path.join(path.dirname(__file__), 'img')
pig_img = pygame.image.load(path.join(img_dir, "pig.png"))
turtle_img = pygame.image.load(path.join(img_dir, "turtle.png"))

class Turtle(pygame.sprite.Sprite):

    def __init__(self,screen,words,screen_width,screen_height):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.ride = 1
        self.image = pygame.Surface([30, 40])
        self.image = turtle_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [80, 100])
        self.screen_width=screen_width
        self.screen_height=screen_height
        # give it a location to put the surface
        self.words = words
        self.rect = self.image.get_rect(center=(1000, 400))
        self.exact_x = self.rect.x
        self.exact_y = self.rect.y
        self.screen = screen 
        # give it a speed
        speed = 5 
        self.y_speed = 0.075
        self.x_speed = 0.1 * speed
    def move(self,x,y):
        self.rect.x = x
        self.rect.y = y
        self.exact_x = x
        self.exact_y = y

    def update(self):
    

        self.exact_x -= self.x_speed
        

        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)
        #This make the enemy stop at the middle
        stop_enemy = 350
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
    def ride_turtle(self):
        self.exact_x += self.ride
        self.rect.x = int(self.exact_x)
        self.rect.y = int(self.exact_y)
        #This make the enemy stop at the middle
        stop_enemy = 800
        if self.rect.left >= stop_enemy:
            self.ride = 0
            self.rect.left = stop_enemy

class Pig(pygame.sprite.Sprite):

    def __init__(self):
        # make it a sprite
        pygame.sprite.Sprite.__init__(self)

        # tell it where to draw image can ge
        self.ride = 1
        self.image = pygame.Surface([80, 90])
        self.image.fill((255, 255, 255))
        self.image = pig_img
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, [80, 90])
        self.finish = False
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
        if keystate[pygame.K_w]:
            self.y_speed -= 20
        if keystate[pygame.K_s]:
            self.y_speed += 20
        if keystate[pygame.K_a]:
            self.x_speed -= 20
        if keystate[pygame.K_d]:
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
            self.finish = True
            self.rect.left = stop_enemy
    # print(self.exact_x)
  

def draw_text(surface, text, size, x, y):
    font_name = pygame.font.get_default_font()
    font = pygame.font.Font(font_name, size)
    text_sruface = font.render(text, True, (0, 0, 0))
    txt_rect = text_sruface.get_rect()
    txt_rect.midtop = (x, y)
    surface.blit(text_sruface, txt_rect)
def forth_pass(screen,screen_width,screen_height):
    player = Player()
    pig = Pig()
    turtle = Turtle(screen,"Come on!Get on me,I can help you to go to the other side!",screen_width,screen_height)


    bg_img = pygame.image.load(path.join(img_dir, "lake.jpg"))
    bg_img = pygame.transform.scale(bg_img, [1200, 600])
    bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(turtle)
    all_sprites.add(pig)
    all_sprites.add(player)
    all_players = pygame.sprite.Group()
    all_players.add(player)
    all_players.add(pig)
    all_turtles = pygame.sprite.Group()
    all_turtles.add(turtle)
    all_monkeys = pygame.sprite.Group()
    all_monkeys.add(player)
    all_pigs = pygame.sprite.Group()
    all_pigs.add(pig)
    pig_on_turtle = False
    monkey_on_turtle = False
    turtle_hit = True
    while True:
        screen.fill((130, 233, 250))
        screen.blit(bg_img, bg_rect)
        all_sprites.draw(screen)
        if not pig_on_turtle and not monkey_on_turtle:
            all_sprites.update()
        if pig_on_turtle and not monkey_on_turtle:
            all_monkeys.update()
            all_turtles.update()
        if not pig_on_turtle and monkey_on_turtle:
            all_pigs.update()
            all_turtles.update()
        if pig_on_turtle and monkey_on_turtle:
            if turtle_hit:
                turtle.exact_x = 350
                turtle.rect.x = 350
                
            turtle.ride_turtle()
            pig.ride_turtle()
            player.ride_turtle()
            turtle_hit = False
        if pig.finish == True:
            time.sleep(2)
            finalpass(screen,screen_width,screen_height)
        hits = pygame.sprite.spritecollide(turtle, all_pigs, False)
        for hit in hits:
            pig_on_turtle = True
        hits = pygame.sprite.spritecollide(turtle, all_monkeys, False)
        for hit in hits:
            monkey_on_turtle = True 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        pygame.display.update()
        pygame.display.flip()