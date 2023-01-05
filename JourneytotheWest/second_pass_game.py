from os import path

import pygame
import time
from third_pass_game import third_pass
from finish import Finish

pygame.init()

# def draw_text(surface, text, size, x, y):
#     font_name = pygame.font.get_default_font()
#     font = pygame.font.Font(font_name, size)
#     text_sruface = font.render(text, True, (0, 0, 0))
#     txt_rect = text_sruface.get_rect()
#     txt_rect.midtop = (x, y)
#     surface.blit(text_sruface, txt_rect)


# def second_pass(screen):
#     from player_second import Player
#     from enemy_second import Enemy
#     from enemy_second import Hearts
#     from enemy_second import Coins
#     white = (255, 255, 255)
#     red = (255, 0, 0)

#     player = Player()
#     img_dir = path.join(path.dirname(__file__), 'img')

#     # bg_img = pygame.image.load(path.join(img_dir, "background3.jpg"))
#     # bg_img = pygame.transform.scale(bg_img, [1200, 600])
#     # bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))

#     all_sprites = pygame.sprite.Group()
#     all_sprites.add(player)

#     all_enemies = pygame.sprite.Group()
#     all_hearts = pygame.sprite.Group()
#     all_coins = pygame.sprite.Group()

#     finish = Finish()
#     pass_sprites = pygame.sprite.Group()
#     pass_sprites.add(finish)

    # for i in range(5):
    #     enemy = Enemy()
    #     all_sprites.add(enemy)
    #     all_enemies.add(enemy)
    # enemies_hit = 0
    # for i in range(1):
    #     heart = Hearts()
    #     all_sprites.add(heart)
    #     all_hearts.add(heart)
    # lives = 3
    # for i in range(3):
    #     coin = Coins()
    #     all_sprites.add(coin)
    #     all_coins.add(coin)
    # coins = 0
   
#     pygame.display.update()
#     # game loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()

#         all_sprites.update()
#         # takes all the events and updates the sprites accordingly

        # # checking for sprite collisions
        # hits = pygame.sprite.spritecollide(player, all_enemies, False)
        # for hit in hits:
        #     hit.to_top()
        #     lives -= 1
        # hits = pygame.sprite.spritecollide(player, all_hearts, False)
        # for hit in hits:
        #     hit.to_top()
        #     lives += 1
        # hits = pygame.sprite.spritecollide(player, all_coins, False)
        # for hit in hits:
        #     hit.to_top()
        #     coins += 1 
        #     print("you got a coin！")

#         # drawing
        # screen.fill((130, 233, 250))
        # screen.blit(bg_img, bg_rect)

        # coinLabel = "Coins = " + str(coins)
        # liveLabel = "Lives = " + str(lives)
        # draw_text(screen, coinLabel, 24,65,50)
        # draw_text(screen, liveLabel, 24,65,25)
        # all_sprites.draw(screen)
        # pygame.display.flip()

       
        
        # if lives == 0:
        #     draw_text(screen, "Game over", 30,600,300)
        #     pygame.display.update()
        #     time.sleep(5)
        #     pygame.quit()
        #     quit()

        # if coins == 2:
        #     while pygame.sprite.spritecollide(player, pass_sprites, False):
        #         print ("You win let's go yo the third pass game")
        #         third_pass(screen)
              
            
            
import pygame
import gameover
#from second_pass_game import second_pass
from third_pass_game import third_pass
pygame.init()


def second_pass(screen,screen_width,screen_height, bg):
    from player_second import Player
    from enemy_second import Enemy
    from enemy_second import Hearts
    from enemy_second import Coins
    from finish import Finish

    def draw_text(surface, text, size, x, y):
        font_name = pygame.font.get_default_font()
        font = pygame.font.Font(font_name, size)
        text_sruface = font.render(text, True, (0, 0, 0))
        txt_rect = text_sruface.get_rect()
        txt_rect.midtop = (x, y)
        surface.blit(text_sruface, txt_rect)

    player = Player()
    img_dir = path.join(path.dirname(__file__), 'img')

    bg_img = pygame.image.load(path.join(img_dir, "超级玛丽奥背景.jpg"))
    bg_img = pygame.transform.scale(bg_img, [1200, 600])
    bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))

    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    all_enemies = pygame.sprite.Group()
    all_hearts = pygame.sprite.Group()
    all_coins = pygame.sprite.Group()
    
    # finish = Finish()
  
    # all_sprites.add(finish)
    # pass_sprites = pygame.sprite.Group()
    # pass_sprites.add(finish)
   

    for i in range(5):
        enemy = Enemy()
        all_sprites.add(enemy)
        all_enemies.add(enemy)
    enemies_hit = 0
    for i in range(1):
        heart = Hearts()
        all_sprites.add(heart)
        all_hearts.add(heart)
    lives = 3
    for i in range(3):
        coin = Coins()
        all_sprites.add(coin)
        all_coins.add(coin)
    coins = 0
    pygame.display.update()

    while True:
        screen.fill((130, 233, 250))
        screen.blit(bg_img, bg_rect)
        all_sprites.draw(screen)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
    # checking for sprite collisions
        hits = pygame.sprite.spritecollide(player, all_enemies, False)
        for hit in hits:
            hit.to_top()
            lives -= 1
        hits = pygame.sprite.spritecollide(player, all_hearts, False)
        for hit in hits:
            hit.to_top()
            lives += 1
        hits = pygame.sprite.spritecollide(player, all_coins, False)
        for hit in hits:
            hit.to_top()
            coins += 1 
            print("you got a coin！")
        # while pygame.sprite.spritecollide(player, pass_sprites, False):
       
      
        coinLabel = "Coins = " + str(coins)
        liveLabel = "Lives = " + str(lives)
        draw_text(screen, coinLabel, 24,65,50)
        draw_text(screen, liveLabel, 24,65,25)
        if coins == 10:
            print("You win! then third_pass_game!")
            third_pass(screen,screen_width,screen_height)

       

        if lives == 0:
            draw_text(screen, "Game over", 30,600,300)
            gameover.gameover_screen(screen,screen_width,screen_height,bg)
            pygame.display.update()
            time.sleep(5)
            pygame.quit()
            quit()

      
              
        pygame.display.flip()
   
        

