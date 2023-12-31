import os
import random
import sys
from PIL import Image
import pygame

pygame.init()
# size = width, height = 945, 630
size = width, height = 1500, 890
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
    intro_text = [
        "Вы бегаете по лабиринту за пса",
        "и лопаете чупринчиков.",
        'Лопните как можно больше',
        "чупринчиков и не умрите."
    ]

    fon = pygame.transform.scale(load_image('fon1.jpg'), size)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 120)

    pygame.draw.rect(screen, 'PeachPuff', [1080, 750, 315, 112], border_radius=10)
    string_rendered = font.render('Level 2', 1, pygame.Color('black'))
    screen.blit(string_rendered, (1095, 772))

    pygame.draw.rect(screen, 'PeachPuff', [735, 750, 315, 112], border_radius=10)
    string_rendered = font.render('Level 1', 1, pygame.Color('black'))
    screen.blit(string_rendered, (750, 772))

    pygame.draw.rect(screen, 'PeachPuff', [735, 615, 660, 112], border_radius=10)
    string_rendered = font.render('Правила игры', 1, pygame.Color('black'))
    screen.blit(string_rendered, (772, 637))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 735 < event.pos[0] < 1050 and 750 < event.pos[1] < 862:
                    return 1  # start level 1
                if 1080 < event.pos[0] < 1395 and 750 < event.pos[1] < 862:
                    return 2  # start level 2

                if 735 < event.pos[0] < 1395 and 615 < event.pos[1] < 727:
                    text_font = pygame.font.Font(None, 45)
                    pygame.draw.rect(screen, 'PeachPuff', [75, 615, 600, 247], border_radius=10)
                    text_coord = 660
                    for line in intro_text:
                        string_rendered = text_font.render(line, 1, pygame.Color('black'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 15
                        intro_rect.top = text_coord
                        intro_rect.x = 112
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                    font = pygame.font.Font(None, 67)
                    pygame.draw.rect(screen, 'LightSalmon', [97, 592, 225, 60], border_radius=10)
                    string_rendered = font.render('Правила', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (112, 600))
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

proportions = 3
cell_size = 75 * proportions
delta = 25 * proportions

tile_images = {
    'Right_wall': load_image('3x_right_wall.png'),
    'Down_wall': load_image('3x_down_wall.png'),
    'free_cell': load_image('3x_road.png'),
    'free_right': load_image('3x_right_road.png'),
    'free_down': load_image('3x_down_road.png'),
    'close_cell': load_image('3x_wall.png'),
    'free_corner': load_image('3x_corner_road.png'),
    'corner_wall': load_image('3x_corner_wall.png')
}
player_image = load_image('Player_doge.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, tile_type, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        if tile_type in tile_images.keys():
            self.image = tile_images[tile_type]
            if tile_type == 'free_cell' or tile_type == 'close_cell':
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x // 2) + delta, cell_size * (pos_y // 2) + delta)
            elif tile_type == 'free_right' or tile_type == 'Right_wall':
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x - pos_x // 2) - delta + delta, cell_size * (pos_y // 2)+ delta)
            elif tile_type == 'free_down' or tile_type == 'Down_wall':
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x // 2) + delta, cell_size * (pos_y - pos_y // 2) - delta + delta)
            elif tile_type == 'corner_wall' or tile_type == 'free_corner':
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x - pos_x // 2) - delta + delta, cell_size * (pos_y - pos_y // 2) - delta + delta)
        else:
            if pos_y == -1:
                self.image = tile_images['Down_wall']
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x // 2), 0)
            elif pos_x == -1:
                self.image = tile_images['Right_wall']
                self.rect = self.image.get_rect().move(
                    0, cell_size * (pos_y // 2))
            elif pos_y == -105:
                self.image = tile_images['Down_wall']
                self.rect = self.image.get_rect().move(
                    cell_size * (pos_x // 2), 6300)
            elif pos_x == -105:
                self.image = tile_images['Right_wall']
                self.rect = self.image.get_rect().move(
                    6300, cell_size * (pos_y // 2))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            cell_size * (pos_x // 2) + delta, cell_size * (pos_y // 2) + delta)


player = None
tiles_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()


def generate_level(level):
    new_player, x, y = None, None, None
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
            elif level[y][x] == '@':
                Tile('free_cell', x, y)
                new_player = Player(x, y)
    for i in range(21):  # Горизонтальная граница Верхняя
        Tile('None', i, -1)
    for i in range(21):  # Вертикальная граница Левая
        Tile('None', -1, i)
    for i in range(21):  # Горизонтальная граница Нижняя
        Tile('None', i, -105)
    for i in range(21):  # Вертикальная граница Правая
        Tile('None', -105, i)
    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


player, level_x, level_y = generate_level(load_level(f'lvl{num}.txt'))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and level[(player.rect.y - 75) // 225 * 2][(player.rect.x - 75) // 225 * 2 - 1] not in ['Y', 'y']:
                player.rect.x -= 225
            elif event.key == pygame.K_RIGHT and level[(player.rect.y - 75) // 225 * 2][(player.rect.x - 75) // 225 * 2 + 1] not in ['Y', 'y']:
                player.rect.x += 225
            elif event.key == pygame.K_UP and level[(player.rect.y - 75) // 225 * 2 - 1][(player.rect.x - 75) // 225 * 2] not in ['Y', 'y']:
                player.rect.y -= 225
            elif event.key == pygame.K_DOWN and level[(player.rect.y - 75) // 225 * 2 + 1][(player.rect.x - 75) // 225 * 2] not in ['Y', 'y']:
                player.rect.y += 225

    screen.fill(pygame.Color("white"))
    all_sprites.draw(screen)
    tiles_group.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()
    clock.tick(10)

pygame.quit()