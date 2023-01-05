import pygame
#import gameover
import  time
from os import path
from gameover import gameover_screen
from second_pass_game import second_pass
from third_pass_game import third_pass
pygame.init()


def first_pass(screen,screen_width,screen_height,bg):
    from player import Player
    from enemy import Enemy
    from finish import Finish
    start_time = time.time()
    def draw_text(surface, text, size, x, y):
        font_name = pygame.font.get_default_font()
        font = pygame.font.Font(font_name, size)
        text_sruface = font.render(text, True, (0, 0, 0))
        txt_rect = text_sruface.get_rect()
        txt_rect.midtop = (x, y)
        surface.blit(text_sruface, txt_rect)

    player = Player()
    finish = Finish()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)
    all_sprites.add(finish)
    pass_sprites = pygame.sprite.Group()
    pass_sprites.add(finish)
    all_enemies = pygame.sprite.Group()


    img_dir = path.join(path.dirname(__file__), 'img')
    bg_img = pygame.image.load(path.join(img_dir, "firstbg.png"))
    bg_img = pygame.transform.scale(bg_img, [1200, 600])
    bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))


    for i in range(5):
        enemy = Enemy()
        all_sprites.add(enemy)
        all_enemies.add(enemy)
    enemies_hit = 0
    pygame.display.update()

    while True:
        current_time = time.time()
        delta_time = current_time-start_time
        screen.fill((130, 233, 250))
        screen.blit(bg_img, bg_rect)
        draw_text(screen, "first pass begin!", 20, 100, 30)
        all_sprites.draw(screen)
        all_sprites.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        hits = pygame.sprite.spritecollide(player, all_enemies, False)
        for hit in hits:
            hit.to_top()
            enemies_hit += 1
        while pygame.sprite.spritecollide(player, pass_sprites, False):
            # 第二关
            #print("You win! then Second pass game!")
            #second_pass(screen,screen_width,screen_height)
            second_pass(screen,screen_width,screen_height,bg)
        #print(enemies_hit)
        x, y = player.get_loc()
        for enemy in all_enemies:
            enemy.update_speed(x, y)
        if enemies_hit >= 3:
            print("You lose! Game over!")
            #draw_text(screen, "you lose!", 20, 70, 50)
            gameover_screen(screen,screen_width,screen_height,bg)
        elif delta_time >= 10:  
            print("You win! then Second pass game!")
            second_pass(screen,screen_width,screen_height,bg)
        pygame.display.flip()
