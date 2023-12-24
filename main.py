import os
import random
import sys

import pygame

pygame.init()
size = width, height = 945, 630
screen = pygame.display.set_mode(size)


def load_image(name):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image


clock = pygame.time.Clock()
FPS = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():  # Создание экрана
    intro_text = [
        "Вы бегаете по лабиринту за пса",
        "и лопаете чупринчиков.",
        'Лопните как можно больше',
        "чупринчиков и не умрите."
    ]

    fon = pygame.transform.scale(load_image('fon1.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 80)

    pygame.draw.rect(screen, 'PeachPuff', [750, 500, 150, 75], border_radius=10)
    string_rendered = font.render('Play', 1, pygame.Color('black'))
    screen.blit(string_rendered, (770, 515))

    pygame.draw.rect(screen, 'PeachPuff', [550, 500, 175, 75], border_radius=10)
    string_rendered = font.render('Rules', 1, pygame.Color('black'))
    screen.blit(string_rendered, (560, 515))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 750 < event.pos[0] < 900 and 500 < event.pos[1] < 575:
                    return  # начинаем игру
                if 550 < event.pos[0] < 700 and 500 < event.pos[1] < 575:

                    text_font = pygame.font.Font(None, 30)
                    pygame.draw.rect(screen, 'PeachPuff', [105, 420, 400, 155], border_radius=10)
                    text_coord = 440
                    for line in intro_text:
                        string_rendered = text_font.render(line, 1, pygame.Color('black'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 10
                        intro_rect.top = text_coord
                        intro_rect.x = 125
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                    font = pygame.font.Font(None, 45)
                    pygame.draw.rect(screen, 'LightSalmon', [115, 405, 150, 40], border_radius=10)
                    string_rendered = font.render('Правила', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (125, 410))
        pygame.display.flip()
        clock.tick(FPS)


start_screen()
