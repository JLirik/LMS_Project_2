import math
import os
import random
import sys
import pygame
import time
import math

pygame.init()
# size = width, height = 945, 630
size = width, height = 1600, 890
screen = pygame.display.set_mode(size)
balls_count = 20


def load_image(name, w=-1, h=-1):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()

    image = pygame.image.load(fullname)
    return image


clock = pygame.time.Clock()
kills = 0
FPS = 60


def terminate():
    pygame.quit()
    sys.exit()


def start_screen():  # Создание экрана
    global balls_count
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

    pygame.draw.rect(screen, 'OliveDrab', [1420, 615, 150, 112], border_radius=10)
    string_rendered = font.render('20', 1, pygame.Color('black'))
    screen.blit(string_rendered, (1448, 637))

    pygame.draw.rect(screen, 'Salmon', [1420, 750, 150, 112], border_radius=10)
    string_rendered = font.render('40', 1, pygame.Color('black'))
    screen.blit(string_rendered, (1448, 772))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 735 < event.pos[0] < 1050 and 750 < event.pos[1] < 862:
                    return 1  # start level 1
                if 1080 < event.pos[0] < 1395 and 750 < event.pos[1] < 862:
                    return 2  # start level 2

                if 1420 < event.pos[0] < 1550 and 615 < event.pos[1] < 727:
                    pygame.draw.rect(screen, 'OliveDrab', [1420, 615, 150, 112], border_radius=10)
                    string_rendered = font.render('20', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (1448, 637))

                    pygame.draw.rect(screen, 'Salmon', [1420, 750, 150, 112], border_radius=10)
                    string_rendered = font.render('40', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (1448, 772))
                    balls_count = 20

                if 1420 < event.pos[0] < 1550 and 750 < event.pos[1] < 862:
                    pygame.draw.rect(screen, 'Salmon', [1420, 615, 150, 112], border_radius=10)
                    string_rendered = font.render('20', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (1448, 637))

                    pygame.draw.rect(screen, 'OliveDrab', [1420, 750, 150, 112], border_radius=10)
                    string_rendered = font.render('40', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (1448, 772))
                    balls_count = 40

                if 735 < event.pos[0] < 1395 and 615 < event.pos[1] < 727:
                    text_font_2 = pygame.font.Font(None, 45)
                    pygame.draw.rect(screen, 'PeachPuff', [75, 615, 600, 247], border_radius=10)
                    text_coord = 660
                    for line in intro_text:
                        string_rendered = text_font_2.render(line, 1, pygame.Color('black'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += 15
                        intro_rect.top = text_coord
                        intro_rect.x = 112
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                    font_3 = pygame.font.Font(None, 67)
                    pygame.draw.rect(screen, 'LightSalmon', [97, 592, 225, 60], border_radius=10)
                    string_rendered = font_3.render('Правила', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (112, 600))
        pygame.display.flip()
        clock.tick(FPS)


def chuprina_screen():
    intro_text = ['Вы выиграли']

    fon = pygame.transform.scale(load_image('fon2.jpg'), (1600, 890))
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, 30)
    text_coord = 50
    for line in intro_text:
        string_rendered = font.render(line, 1, pygame.Color('black'))
        intro_rect = string_rendered.get_rect()
        text_coord += 10
        intro_rect.top = text_coord
        intro_rect.x = 10
        text_coord += intro_rect.height
        screen.blit(string_rendered, intro_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.KEYDOWN or \
                    event.type == pygame.MOUSEBUTTONDOWN:
                return  # начинаем игру
        pygame.display.flip()
        clock.tick(FPS)


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
ball_image = load_image('apple-1.png')


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
                    cell_size * pos_x, 0)
            elif pos_x == -1:
                self.image = tile_images['Right_wall']
                self.rect = self.image.get_rect().move(
                    0, cell_size * pos_y)
            elif pos_y == -105:
                self.image = tile_images['Down_wall']
                self.rect = self.image.get_rect().move(
                    cell_size * pos_y, 4725)
            elif pos_x == -105:
                self.image = tile_images['Right_wall']
                self.rect = self.image.get_rect().move(
                    4725, cell_size * pos_y)
            elif pos_x == -1155 and pos_y == -1155:
                self.image = tile_images['corner_wall']
                self.rect = self.image.get_rect().move(
                    4725, 0)
            elif pos_x == -210 and pos_y == -210:
                self.image = tile_images['corner_wall']
                self.rect = self.image.get_rect().move(
                    0, 4725)


class Camera:
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.image = player_image
        self.rect = self.image.get_rect().move(
            cell_size * (pos_x // 2) + delta, cell_size * (pos_y // 2) + delta)


class Balls(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(balls_group, all_sprites)
        self.image = ball_image
        self.rect = self.image.get_rect().move(
            cell_size * pos_x + delta, cell_size * pos_y + delta)
        self.sin_x = pos_x * cell_size + delta
        self.sin_y = pos_y * cell_size + delta

    def update(self):
        lst = ['L', 'R', 'U', 'D']
        direction = random.choice(lst)
        if self.sin_x > 0:
            if direction == 'R' and level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 + 1] not in ['Y', 'y']:
                self.sin_x += 225
                self.rect = self.rect.move(225, 0)
            elif direction == 'L' and level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 - 1] not in ['Y', 'y']:
                self.sin_x -= 225
                self.rect = self.rect.move(-225, 0)
            elif direction == 'D' and level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y']:
                self.sin_y += 225
                self.rect = self.rect.move(0, 225)
            elif direction == 'U' and level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y']:
                self.sin_y -= 225
                self.rect = self.rect.move(0, -225)
        if pygame.sprite.collide_mask(self, player):
            self.rect = self.rect.move(-1000000, -1000000)
            print_kill(1)


def print_kill(n):
    global kills, balls_count
    kills += n
    font = pygame.font.Font(None, 120)
    string_rendered = font.render(f'Kills: {kills}/{balls_count}', 1, pygame.Color('Silver'))
    screen.blit(string_rendered, (10, 10))


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
    Tile('None', -210, -210)
    Tile('None', -1155, -1155)

    # вернем игрока, а также размер поля в клетках
    return new_player, x, y


running = True
while running:
    num = start_screen()
    level = load_level(f'lvl{num}.txt')
    player = None
    tiles_group = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    balls_group = pygame.sprite.Group()

    for i in range(balls_count + int(balls_count * 0.5)):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        while level[y * 2][x * 2] != 'З':
            x = random.randint(0, 20)
            y = random.randint(0, 20)
        Balls(x, y)

    barboss = True

    player, level_x, level_y = generate_level(load_level(f'lvl{num}.txt'))
    kos_x = player.rect.x
    kos_y = player.rect.y
    camera = Camera()
    camera.update(player)
    for sprite in all_sprites:
        camera.apply(sprite)
    pygame.display.flip()
    to_x, to_y = 0, 0

    while barboss:
        camup = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                barboss = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and (((level[(kos_y - 75) // 225 * 2][(kos_x - 75) // 225 * 2 - 1] not in ['Y', 'y'] or to_x != 0) and to_y == 0) or ((level[(kos_y - 75) // 225 * 2 + int(math.copysign(1, to_y))][(kos_x - 75) // 225 * 2 - 1] == 'p' or to_x != 0) and to_y != 0)):
                    to_x -= 1
                    if to_x == -9:
                        to_x = 0
                        kos_x -= 225
                    player.rect.x -= 25
                    camup = 1
                elif event.key == pygame.K_RIGHT and (((level[(kos_y - 75) // 225 * 2][(kos_x - 75) // 225 * 2 + 1] not in ['Y', 'y'] or to_x != 0) and to_y == 0) or ((level[(kos_y - 75) // 225 * 2 + int(math.copysign(1, to_y))][(kos_x - 75) // 225 * 2 + 1] == 'p' or to_x != 0) and to_y != 0)):
                    to_x += 1
                    if to_x == 9:
                        to_x = 0
                        kos_x += 225
                    player.rect.x += 25
                    camup = 1
                elif event.key == pygame.K_UP and (((level[(kos_y - 75) // 225 * 2 - 1][(kos_x - 75) // 225 * 2] not in ['Y', 'y'] or to_y != 0) and to_x == 0) or ((level[(kos_y - 75) // 225 * 2 - 1][(kos_x - 75) // 225 * 2 + int(math.copysign(1, to_x))] == 'p' or to_y != 0) and to_x != 0)):
                    to_y -= 1
                    if to_y == -9:
                        to_y = 0
                        kos_y -= 225
                    player.rect.y -= 25
                    camup = 1
                elif event.key == pygame.K_DOWN and (((level[(kos_y - 75) // 225 * 2 + 1][(kos_x - 75) // 225 * 2] not in ['Y', 'y'] or to_y != 0) and to_x == 0) or ((level[(kos_y - 75) // 225 * 2 + 1][(kos_x - 75) // 225 * 2 + int(math.copysign(1, to_x))] == 'p' or to_y != 0) and to_x != 0)):
                    to_y += 1
                    if to_y == 9:
                        to_y = 0
                        kos_y += 225
                    player.rect.y += 25
                    camup = 1

        screen.fill(pygame.Color("white"))
        all_sprites.draw(screen)
        tiles_group.draw(screen)
        player_group.draw(screen)
        balls_group.draw(screen)
        all_sprites.update()
        print_kill(0)
        if kills == balls_count:
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            balls_group.draw(screen)
            all_sprites.update()
            pygame.display.flip()
            time.sleep(0.5)
            barboss = False

        if camup == 1:
            print(to_x, to_y)
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
        pygame.display.flip()
        clock.tick(10)
    if kills == balls_count:
        chuprina_screen()
        kills = 0

pygame.quit()