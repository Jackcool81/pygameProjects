from pickle import FALSE
import pygame
import random
from player_third import Player
from enemy_third import Enemy
from forth_pass_game import forth_pass
pygame.init()

from os import path
img_dir = path.join(path.dirname(__file__), 'img')
oldman_img = pygame.image.load(path.join(img_dir, "oldman.png"))
bluegirl_img = pygame.image.load(path.join(img_dir, "bluegirl.png"))
skullgirl_img = pygame.image.load(path.join(img_dir, "skullgirl.png"))

def draw_text(surface, text, size, x, y):
    font_name = pygame.font.get_default_font()
    font = pygame.font.Font(font_name, size)
    text_sruface = font.render(text, True, (0, 0, 0))
    txt_rect = text_sruface.get_rect()
    txt_rect.midtop = (x, y)
    surface.blit(text_sruface, txt_rect)
def third_pass(screen,screen_width,screen_height):

 
    white = (255, 255, 255)
    red = (255, 0, 0)

    player = Player()
    enemy = Enemy(screen,oldman_img,"I can't find my daughter,can you help me?",3,screen_width,screen_height)
    enemy2 = Enemy(screen,bluegirl_img,"I can't find my mom,can you help me?",3,screen_width,screen_height)
    enemy3 = Enemy(screen,skullgirl_img,"I can't find my way to home,can you help me?",3,screen_width,screen_height)
    img_dir = path.join(path.dirname(__file__), 'img')

    bg_img = pygame.image.load(path.join(img_dir, "background3.jpg"))
    bg_img = pygame.transform.scale(bg_img, [1200, 600])
    bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_enemies = pygame.sprite.Group()
    all_enemies.add(enemy)
    all_enemies.add(enemy2)
    oldman_group = pygame.sprite.Group()
    bluegirl_group = pygame.sprite.Group()
    skullgirl_group = pygame.sprite.Group()
    oldman_group.add(enemy)
    bluegirl_group.add(enemy2)
    skullgirl_group.add(enemy3)
    oldman_hit = False
    bluegirl_hit = False
    skullgirl_hit = False
    skullgirl_count = 0
    
    enemies_hit = 0
    do_not_update = False
    coinLabel = "hits = 0"
    while True:
        screen.fill((130, 233, 250))
        screen.blit(bg_img, bg_rect)
        all_sprites.draw(screen)
        oldman_group.draw(screen)
        all_sprites.update()
        if oldman_hit == False:
           oldman_group.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        hits = pygame.sprite.spritecollide(player, oldman_group, False)
        for hit in hits:
            oldman_hit = True 

        hits = pygame.sprite.spritecollide(player, bluegirl_group, False)
        for hit in hits:
           bluegirl_hit = True    
        
        hits = pygame.sprite.spritecollide(player, skullgirl_group, False)
        for hit in hits:
            do_not_update = True

            enemy3.move(random.randint(20,1180),random.randint(20,580)) 
            skullgirl_count += 1
            coinLabel = "hits = " + str(skullgirl_count)
            draw_text(screen, coinLabel, 24,65,50) 
                
        if skullgirl_count == 10:
            skullgirl_hit = True
            
        if oldman_hit == True:
            enemy.run_away()
            bluegirl_group.draw(screen)
            if bluegirl_hit == False:
               bluegirl_group.update()
        if bluegirl_hit == True:
            enemy2.run_away()
            skullgirl_group.draw(screen)
            if skullgirl_hit == False:
               draw_text(screen, coinLabel, 24,65,50) 
               if do_not_update == False:  
                    skullgirl_group.update()
               
        if skullgirl_hit == True:
            print("hi") 
            forth_pass(screen,screen_width,screen_height)

         
           
        pygame.display.update()
        pygame.display.flip()

    
     
   
       

