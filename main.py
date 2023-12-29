import os
import random
import sys
from PIL import Image
import pygame

pygame.init()
size = width, height = 945, 630
screen = pygame.display.set_mode(size)


def load_image(name, w=-1, h=-1):
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
    num = 0
    intro_text = [
        "Вы бегаете по лабиринту за пса",
        "и лопаете чупринчиков.",
        'Лопните как можно больше',
        "чупринчиков и не умрите."
    ]

    fon = pygame.transform.scale(load_image('fon1.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 80)

    pygame.draw.rect(screen, 'PeachPuff', [720, 500, 210, 75], border_radius=10)
    string_rendered = font.render('Level 2', 1, pygame.Color('black'))
    screen.blit(string_rendered, (730, 515))

    pygame.draw.rect(screen, 'PeachPuff', [490, 500, 210, 75], border_radius=10)
    string_rendered = font.render('Level 1', 1, pygame.Color('black'))
    screen.blit(string_rendered, (500, 515))

    pygame.draw.rect(screen, 'PeachPuff', [490, 410, 440, 75], border_radius=10)
    string_rendered = font.render('Правила игры', 1, pygame.Color('black'))
    screen.blit(string_rendered, (515, 425))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 490 < event.pos[0] < 700 and 500 < event.pos[1] < 575:
                    return 1  # start level 1
                if 720 < event.pos[0] < 930 and 500 < event.pos[1] < 575:
                    return 2  # start level 2

                if 490 < event.pos[0] < 930 and 410 < event.pos[1] < 485:
                    text_font = pygame.font.Font(None, 30)
                    pygame.draw.rect(screen, 'PeachPuff', [50, 410, 400, 165], border_radius=10)
                    text_coord = 440
                    for line in intro_text:
                        string_rendered = text_font.render(line, 1, pygame.Color('black'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 10
                        intro_rect.top = text_coord
                        intro_rect.x = 75
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                    font = pygame.font.Font(None, 45)
                    pygame.draw.rect(screen, 'LightSalmon', [65, 395, 150, 40], border_radius=10)
                    string_rendered = font.render('Правила', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (75, 400))
        pygame.display.flip()
        clock.tick(FPS)


num = start_screen()


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


level = load_level(f'lvl{num}.txt')
# print(level)

cell_size = 75
delta = 25


tile_images = {
    'Right_wall': load_image('right_wall.png'),
    'Down_wall': load_image('down_wall.png'),
    'free_cell': load_image('road.png'),
    'free_right': load_image('right_road.png'),
    'free_down': load_image('down_road.png'),
    'close_cell': load_image('wall.png'),
    'free_corner': load_image('corner_road.png'),
    'corner_wall': load_image('corner_wall.png')
}
# player_image = load_image('mar.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.image = tile_images[tile_type]
        if tile_type == 'free_cell' or tile_type == 'close_cell':
            self.rect = self.image.get_rect().move(
                cell_size * (pos_x // 2), cell_size * (pos_y // 2))
        elif tile_type == 'free_right' or tile_type == 'Right_wall':
            self.rect = self.image.get_rect().move(
                cell_size * (pos_x - pos_x // 2) - 25, cell_size * (pos_y // 2))
        elif tile_type == 'free_down' or tile_type == 'Down_wall':
            self.rect = self.image.get_rect().move(
                cell_size * (pos_x // 2), cell_size * (pos_y - pos_y // 2) - 25)
        elif tile_type == 'corner_wall' or tile_type == 'free_corner':
            self.rect = self.image.get_rect().move(
                cell_size * (pos_x - pos_x // 2) - 25, cell_size * (pos_y - pos_y // 2) - 25)


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
            elif level[y][x] == 'p':
                Tile('free_corner', x, y)
            elif level[y][x] == 's':
                Tile('corner_wall', x, y)
    # вернем игрока, а также размер поля в клетках
    # return new_player, x, y
    return x, y


tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
print(0)
level_x, level_y = generate_level(load_level(f'lvl{num}.txt'))
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