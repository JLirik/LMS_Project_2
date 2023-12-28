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


def load_level(filename):
    filename = "data/" + filename
    # читаем уровень, убирая символы перевода строки
    with open(filename, 'r') as mapFile:
        level_map = [line.strip() for line in mapFile]

    # и подсчитываем максимальную длину
    # max_width = max(map(len, level_map))
    # print(max_width)

    # дополняем каждую строку пустыми клетками ('=') + убираем ненужные клетки
    # lvl_1 = list(map(lambda x: x.ljust(max_width, '='), level_map))

    return level_map


level = load_level('lvl1.txt')
# print(level)


tile_images = {
    'Right_wall': load_image('textura_1_stena.jpg'),
    'Down_wall': load_image('textura_1_stena.jpg'),
    'free_cell': load_image('textura_1_pol.jpg'),
    'free_right': load_image('textura_1_pol.jpg'),
    'free_down': load_image('textura_1_pol.jpg'),
    'close_cell': load_image('textura_1_V_stene.jpg'),
    'dog': load_image('fon.jpg'),
}
# player_image = load_image('mar.png')

tile_width_cell = tile_height_cell = 50
tile_width_wall_right = 25
tile_height_wall_right = 50
tile_width_wall_down = 75
tile_height_wall_down = 25


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        if tile_type == 'free_cell' or tile_type == 'close_cell':
            self.rect = self.image.get_rect().move(
                tile_width_cell * pos_x, tile_height_cell * pos_y)
        elif tile_type == 'free_right' or tile_type == 'Right_wall':
            self.rect = self.image.get_rect().move(
                tile_width_wall_right * pos_x, tile_height_wall_right * pos_y)
        elif tile_type == 'free_down' or tile_type == 'Down_wall':
            self.rect = self.image.get_rect().move(
                tile_width_wall_down * pos_x, tile_height_wall_down * pos_y)
        elif tile_type == 'dog':
            self.rect = self.image.get_rect().move(
                tile_width_cell * pos_x, tile_height_cell * pos_y)


def generate_level(level):
    # new_player, x, y = None, None, None
    for y in range(len(level)):
        for x in range(len(level[y])):
            if level[y][x] == 'З':
                Tile('free_cell', x, y)
            elif level[y][x] == 'Ф':
                Tile('close_cell', x, y)
            elif level[y][x] == 'G':
                Tile('free_right', x, y)
            elif level[y][x] == 'Y':
                Tile('Right_wall', x, y)
            elif level[y][x] == 'g':
                Tile('free_down', x, y)
            elif level[y][x] == 'y':
                Tile('Down_wall', x, y)
            elif level[y][x] == '@':
                Tile('dog', x, y)
            # elif level[y][x] == '@':
            #     Tile('empty', x, y)
            #     new_player = Player(x, y)
    # вернем игрока, а также размер поля в клетках
    # return new_player, x, y
    return x, y


tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
print(0)
level_x, level_y = generate_level(load_level('lvl1.txt'))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT and level[player.rect.y // 50][player.rect.x // 50 - 1] != '#':
        #         player.rect.x -= 50
        #     elif event.key == pygame.K_RIGHT and level[player.rect.y // 50][player.rect.x // 50 + 1] != '#':
        #         player.rect.x += 50
        #     elif event.key == pygame.K_UP and level[player.rect.y // 50 - 1][player.rect.x // 50] != '#':
        #         player.rect.y -= 50
        #     elif event.key == pygame.K_DOWN and level[player.rect.y // 50 + 1][player.rect.x // 50] != '#':
        #         player.rect.y += 50

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    # player_group.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()
