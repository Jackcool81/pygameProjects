import pygame
import first_pass_game
from os import path

screen_width = 1200
screen_height = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

#screen = pygame.display.set_mode((screen_width, screen_height))
#pygame.display.set_caption("西游记")
img_dir = path.join(path.dirname(__file__), 'img')
#bg = pygame.image.load(path.join(img_dir, "begin_backgroup.png")).convert()
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

    def display(self, screen):
        screen.blit(self.surface, (self.x, self.y))

    def check_click(self, position):
        x_match = position[0] > self.x and position[0] < self.x + self.WIDTH
        y_match = position[1] > self.y and position[1] < self.y + self.HEIGHT

        if x_match and y_match:
            return True
        else:
            return False


def gameover_screen(screen,screen_width,screen_height,bg):
    screen.blit(bg, (0, 0))
    print("hello")
    game_title1 = font.render('Game Over ', True, BLACK)
    screen.blit(game_title1, (screen_width // 2 - game_title1.get_width() // 50, 100))

    play_button = Button('Restart', RED, None, 320, centered_x=True)
    exit_button = Button('Exit', BLACK, None, 350, centered_x=True)

    play_button.display(screen)
    exit_button.display(screen)

    pygame.display.update()

    while True:

        if play_button.check_click(pygame.mouse.get_pos()):
            play_button = Button('Restart', RED, None, 320, centered_x=True)
        else:
            play_button = Button('Restart', BLACK, None, 320, centered_x=True)

        if exit_button.check_click(pygame.mouse.get_pos()):
            exit_button = Button('Exit', RED, None, 350, centered_x=True)
        else:
            exit_button = Button('Exit', BLACK, None, 350, centered_x=True)

        play_button.display(screen)
        exit_button.display(screen)
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
                pygame.quit()
                quit()
    


#gameover_screen()


#font_name = pygame.font.match_font('arial')

#def score_writing(surf,text,size,x,y):
    #font = pygame.font.Font(font_name, size)
    #text_surface = font.render(text, True, black)
    #text_rect = text_surface.get_rect()
    #text_rect.midtop = (x, y)
    #surf.blit(text_surface, text_rect)
