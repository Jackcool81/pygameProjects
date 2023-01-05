import pygame
import first_pass_game
from os import path
import sys
import os

def resource_path(relative_path):
    try:
    # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#hello this is a 
screen_width = 1200
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("西游记")
img_dir = path.join(path.dirname(__file__), 'img')
bg = pygame.image.load(path.join(img_dir, "begin_backgroup.png")).convert()
font_addr = pygame.font.get_default_font()
font = pygame.font.Font(font_addr, 18)


class Button(object):
    def __init__(self, text, color, x=None, y=None, **kwargs):
        self.surface = font.render(text, True, color)

        self.WIDTH = self.surface.get_width()
        self.HEIGHT = self.surface.get_height()

        if 'centered_x' in kwargs and kwargs['centered_x']:
            self.x = screen_width // 2 - self.WIDTH // 2
        else:
            self.x = x

        if 'centered_y' in kwargs and kwargs['cenntered_y']:
            self.y = screen_height // 2 - self.HEIGHT // 2
        else:
            self.y = y

    def display(self):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


def starting_screen():
    screen.blit(bg, (0, 0))

    game_title1 = font.render('In the beginning, Taizong, the president of the Tang dynasty, ', True, BLACK)
    game_title2 = font.render('sent the monk Tang to get the scripture from the Western Heave. ', True, BLACK)
    game_title3 = font.render('The program makes simple background changes from  a busy city to the desert, ', True,
                              BLACK)
    game_title4 = font.render('to the Gobi Desert, to Mount Wuxing. ', True, BLACK)
    game_title5 = font.render('The narrator points out someone needs to help Monk Tang', True, BLACK)
    game_title6 = font.render('get the scripture from the Western Heave.', True, BLACK)

    screen.blit(game_title1, (screen_width // 2 - game_title1.get_width() // 2, 50))
    screen.blit(game_title2, (screen_width // 2 - game_title2.get_width() // 2, 70))
    screen.blit(game_title3, (screen_width // 2 - game_title3.get_width() // 2, 90))
    screen.blit(game_title4, (screen_width // 2 - game_title4.get_width() // 2, 110))
    screen.blit(game_title5, (screen_width // 2 - game_title5.get_width() // 2, 130))
    screen.blit(game_title6, (screen_width // 2 - game_title6.get_width() // 2, 150))

    play_button = Button('Play', RED, None, 320, centered_x=True)
    exit_button = Button('Exit', BLACK, None, 350, centered_x=True)

    pygame.mixer.music.load('siaai aonf.wav')
    pygame.mixer.music.set_volume(0.65)
    pygame.mixer.music.play(-1) 
    
    play_button.display()
    exit_button.display()

    
    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Play', RED, None, 320, centered_x=True)
        else:
            play_button = Button('Play', BLACK, None, 320, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 350, centered_x=True)
        else:
            exit_button = Button('Exit', BLACK, None, 350, centered_x=True)

        play_button.display()
        exit_button.display()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit
        if pygame.mouse.get_pressed()[0]:
            if play_button.check_click(pygame.mouse.get_pos()):
                # 第一关
                first_pass_game.first_pass(screen,screen_width,screen_height,bg)
            if exit_button.check_click(pygame.mouse.get_pos()):
                break


starting_screen()


#font_name = pygame.font.match_font('arial')

#def score_writing(surf,text,size,x,y):
    #font = pygame.font.Font(font_name, size)
    #text_surface = font.render(text, True, black)
    #text_rect = text_surface.get_rect()
    #text_rect.midtop = (x, y)
    #surf.blit(text_surface, text_rect)
