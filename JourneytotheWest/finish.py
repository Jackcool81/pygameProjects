import pygame

pygame.init()
from os import path



img_dir = path.join(path.dirname(__file__), 'img')
bg = pygame.image.load(path.join(img_dir, "begin_backgroup.png"))
class Finish(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([80, 90])
        self.image.fill((255, 255, 255))

        self.rect = self.image.get_rect(center=(600, 0))
def draw_text(surface, text, size, x, y):
    font_name = pygame.font.get_default_font()
    font = pygame.font.Font(font_name, size)
    text_sruface = font.render(text, True, (0, 0, 0))
    txt_rect = text_sruface.get_rect()
    txt_rect.midtop = (x, y)
    surface.blit(text_sruface, txt_rect)
def finalpass(screen,screen_width,screen_height):
    
    bg_img = pygame.image.load(path.join(img_dir, "begin_backgroup.png"))
    bg_img = pygame.transform.scale(bg_img, [1200, 600])
    bg_rect = bg_img.get_rect(center=(1200 / 2, 600 / 2))
       
    while True:
        screen.fill((130, 233, 250))
        screen.blit(bg_img, bg_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        draw_text(screen,"Congratulation, you won the game!",30,600,300)

        pygame.display.update()
        pygame.display.flip()