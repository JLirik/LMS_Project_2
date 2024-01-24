import math
import os
import random
import sys
import pygame
import time
import math
import moviepy.editor

pygame.init()
prop = 0.9
# size = width, height = 945, 630
size = width, height = 1600 * prop, 890 * prop
screen = pygame.display.set_mode(size)
balls_count = 20
lives = 3



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
    font = pygame.font.Font(None, int(120 * prop))

    pygame.draw.rect(screen, 'PeachPuff', [1080 * prop, 750 * prop, int(315 * prop), int(112 * prop)], border_radius=10)
    string_rendered = font.render('Level 2', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(1095 * prop), int(772 * prop)))

    pygame.draw.rect(screen, 'PeachPuff', [int(735 * prop), int(750 * prop), int(315 * prop), int(112 * prop)], border_radius=10)
    string_rendered = font.render('Level 1', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(750 * prop), int(772 * prop)))

    pygame.draw.rect(screen, 'PeachPuff', [int(735 * prop), int(615 * prop), int(660 * prop), int(112 * prop)], border_radius=10)
    string_rendered = font.render('Правила игры', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(772 * prop), int(637 * prop)))

    pygame.draw.rect(screen, 'OliveDrab', [int(1420 * prop), int(615 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
    string_rendered = font.render('20', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(1448 * prop), int(637 * prop)))

    pygame.draw.rect(screen, 'Salmon', [int(1420 * prop), int(750 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
    string_rendered = font.render('40', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(1448 * prop), int(772 * prop)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if int(735 * prop) < event.pos[0] < int(1050 * prop) and int(750 * prop) < event.pos[1] < int(862 * prop):
                    return 1  # start level 1
                if int(1080 * prop) < event.pos[0] < int(1395 * prop) and int(750 * prop) < event.pos[1] < int(862 * prop):
                    return 2  # start level 2

                if int(1420 * prop) < event.pos[0] < int(1550 * prop) and int(615 * prop) < event.pos[1] < int(727 * prop):
                    pygame.draw.rect(screen, 'OliveDrab', [int(1420 * prop), int(615 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
                    string_rendered = font.render('20', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (int(1448 * prop), int(637 * prop)))

                    pygame.draw.rect(screen, 'Salmon', [int(1420 * prop), int(750 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
                    string_rendered = font.render('40', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (int(1448 * prop), int(772 * prop)))
                    balls_count = 20

                if int(1420 * prop) < event.pos[0] < int(1550 * prop) and int(750 * prop) < event.pos[1] < int(862 * prop):
                    pygame.draw.rect(screen, 'Salmon', [int(1420 * prop), int(615 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
                    string_rendered = font.render('20', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (int(1448 * prop), int(637 * prop)))

                    pygame.draw.rect(screen, 'OliveDrab', [int(1420 * prop), int(750 * prop), int(150 * prop), int(112 * prop)], border_radius=10)
                    string_rendered = font.render('40', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (int(1448 * prop), int(772 * prop)))
                    balls_count = 40

                if int(735 * prop) < event.pos[0] < int(1395 * prop) and int(615 * prop) < event.pos[1] < int(727 * prop):
                    text_font_2 = pygame.font.Font(None, int(45 * prop))
                    pygame.draw.rect(screen, 'PeachPuff', [int(75 * prop), int(615 * prop), int(600 * prop), int(247 * prop)], border_radius=10)
                    text_coord = int(660 * prop)
                    for line in intro_text:
                        string_rendered = text_font_2.render(line, 1, pygame.Color('black'))
                        intro_rect = string_rendered.get_rect()
                        text_coord += int(15 * prop)
                        intro_rect.top = text_coord
                        intro_rect.x = int(112 * prop)
                        text_coord += intro_rect.height
                        screen.blit(string_rendered, intro_rect)
                    font_3 = pygame.font.Font(None, int(67 * prop))
                    pygame.draw.rect(screen, 'LightSalmon', [int(97 * prop), int(592 * prop), int(225 * prop), int(60 * prop)], border_radius=10)
                    string_rendered = font_3.render('Правила', 1, pygame.Color('black'))
                    screen.blit(string_rendered, (int(112 * prop), int(600 * prop)))
        pygame.display.flip()
        clock.tick(FPS)


def chuprina_screen(result):
    if result == 'win':
        fon = pygame.transform.scale(load_image('fon2.jpg'), size)
        pygame.mixer.music.load("data/toothless.mp3")
        text = 'Вы победили!!!'
    else:
        fon = pygame.transform.scale(load_image('fon3.jpg'), size)
        pygame.mixer.music.load("data/sad_violin.mp3")
        text = 'Ты проиграл!!!!'
    pygame.mixer.music.play(-1)
    screen.blit(fon, (0, 0))
    font = pygame.font.Font(None, int(175 * prop))

    pygame.draw.rect(screen, 'PeachPuff', [320 * prop, 700 * prop, int(970 * prop), int(150 * prop)], border_radius=10)
    string_rendered = font.render(text, 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(340 * prop), int(720 * prop)))

    font = pygame.font.Font(None, int(80 * prop))
    pygame.draw.rect(screen, 'PeachPuff', [20 * prop, 700 * prop, int(280 * prop), int(150 * prop)], border_radius=10)
    string_rendered = font.render('Играть', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(70 * prop), int(720 * prop)))

    string_rendered = font.render('снова', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(80 * prop), int(780 * prop)))

    font = pygame.font.Font(None, int(120 * prop))
    pygame.draw.rect(screen, 'PeachPuff', [(1310 * prop), (700 * prop), int(280 * prop), int(150 * prop)], border_radius=10)
    string_rendered = font.render('Выйти', 1, pygame.Color('black'))
    screen.blit(string_rendered, (int(1320 * prop), int(740 * prop)))

    while True:
        for event_1 in pygame.event.get():
            if event_1.type == pygame.QUIT:
                terminate()
            elif event_1.type == pygame.MOUSEBUTTONDOWN:
                if int(1310 * prop) < event_1.pos[0] < int(1590 * prop) and int(700 * prop) < event_1.pos[1] < int(850 * prop):
                    terminate()
                if int(20 * prop) < event_1.pos[0] < int(300 * prop) and int(700 * prop) < event_1.pos[1] < int(850 * prop):
                    print(2)
                    pygame.mixer.music.stop()
                    return # start
                if int(320 * prop) < event_1.pos[0] < int(1290 * prop) and int(700 * prop) < event_1.pos[1] < int(850 * prop):
                    pass
                    # video = moviepy.editor.VideoFileClip("data/video-fon1.mp4")
                    # video.preview()
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
life_image = load_image('bonus_life.png')


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


class Life(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(life_group, all_sprites)
        self.image = life_image
        self.rect = self.image.get_rect().move(
            cell_size * pos_x + delta, cell_size * pos_y + delta)

    def update(self):
        if pygame.sprite.collide_mask(self, player):
            self.rect = self.rect.move(-1000000, -1000000)
            print_life(1)


class Balls(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(balls_group, all_sprites)
        self.image = ball_image
        self.rect = self.image.get_rect().move(
            cell_size * pos_x + delta, cell_size * pos_y + delta)
        self.sin_x = pos_x * cell_size + delta
        self.sin_y = pos_y * cell_size + delta
        self.x_ball = 0
        self.y_ball =0
        self.between_wall = False
        self.hero_x = ''
        self.hero_y = ''
        self.dukky_x = 0
        self.dukky_y = 0
        self.grib_x = 0
        self.grib_y = 0
        self.lst = ['L', 'R', 'U', 'D']
        self.direction = random.choice(self.lst)
        self.air = ''
        self.last_action = ''

    def runaway(self):
        if self.direction == 'D' and level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2] in ['Y', 'y', 's']:
            if level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 - 1] not in ['Y', 'y', 's']:
                self.direction = 'L'
            elif level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 + 1] not in ['Y', 'y', 's']:
                self.direction = 'R'

        if self.direction == 'U' and level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2] in ['Y', 'y', 's']:
            if level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 - 1] not in ['Y', 'y', 's']:
                self.direction = 'L'
            elif level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 + 1] not in ['Y', 'y', 's']:
                self.direction = 'R'


        if self.direction == 'L' and level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 - 1] in ['Y', 'y', 's']:
            if level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                self.direction = 'U'
            elif level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                self.direction = 'D'

        if self.direction == 'R' and level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 + 1] in ['Y', 'y', 's']:
            if level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                self.direction = 'U'
            elif level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                self.direction = 'D'

        if self.direction == 'R':
            self.last_action = 'L'
        elif self.direction == 'L':
            self.last_action = 'R'
        elif self.direction == 'U':
            self.last_action = 'D'
        elif self.direction == 'D':
            self.last_action = 'U'

        return self.direction
    def jump(self):
        print(1)
        if self.x_ball > 0:
            self.direction = 'D'
        if self.x_ball < 0:
            self.direction = 'U'
        if self.y_ball > 0:
            self.direction = 'L'
        if self.y_ball < 0:
            self.direction = 'R'

        if self.x_ball == 0 and self.y_ball == 0:
            self.air = random.choice(self.lst)
            f = 0
            while f != 1:
                if not(self.air == self.hero_x or self.air == self.hero_y):
                    if self.direction == 'D' and level[(self.sin_y - 75) // 225 * 2 + 1][
                        (self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                        f = 1
                        self.rect.move(0, 225)
                        self.sin_y += 225
                    if self.direction == 'U' and level[(self.sin_y - 75) // 225 * 2 - 1][
                        (self.sin_x - 75) // 225 * 2] not in ['Y', 'y', 's']:
                        f = 1
                        self.rect.move(0, -225)
                        self.sin_y -= 225
                    if self.direction == 'L' and level[(self.sin_y - 75) // 225 * 2][
                        (self.sin_x - 75) // 225 * 2 - 1] in ['Y', 'y', 's']:
                        f = 1
                        self.rect.move(-225, 0)
                        self.sin_x -= 225
                    if self.direction == 'R' and level[(self.sin_y - 75) // 225 * 2][
                        (self.sin_x - 75) // 225 * 2 + 1] in ['Y', 'y', 's']:
                        f = 1
                        self.rect.move(225, 0)
                        self.sin_x += 225




    def update(self):

        if self.x_ball == 0 and self.y_ball == 0:
            self.direction = random.choice(self.lst)
            while self.direction == self.last_action:
                self.direction = random.choice(self.lst)
        # if abs((self.sin_x - 75) // 225 - (kos_x - 75) // 225) <= 1 and abs((self.sin_y - 75) // 225 - (kos_y - 75) // 225) <= 1:
        #     self.jump()
        if abs((self.sin_x - 75) // 225 - (kos_x - 75) // 225) < 3 and abs((self.sin_y - 75) // 225 - (kos_y - 75) // 225) < 3:
            self.between_wall = False



            self.dukky_x = kos_x
            self.dukky_y = kos_y
            if to_x >= 5:
                self.dukky_x = kos_x + 225
            elif -4 <= to_x <= 4:
                self.dukky_x = kos_x
            elif to_x <= -5:
                self.dukky_x = kos_x - 225

            if to_y >= 5:
                self.dukky_y = kos_y + 225
            elif -4 <= to_y <= 4:
                self.dukky_y = kos_y
            elif to_y <= -5:
                self.dukky_y = kos_y - 225


            self.grib_x = self.sin_x
            self.grib_y = self.sin_y
            if self.x_ball >= 8:
                self.grib_x = self.sin_x + 225
            elif -7 <= self.x_ball <= 7:
                self.grib_x = self.sin_x
            elif self.x_ball <= -8:
                self.grib_x = self.sin_x - 225

            if self.y_ball >= 8:
                self.grib_y = self.sin_y + 225
            elif -7 <= self.y_ball <= 7:
                self.grib_y = self.sin_y
            elif self.y_ball <= -8:
                self.grib_y = self.sin_y - 225


            if (self.grib_x - 75) // 225 - (self.dukky_x - 75) // 225 < 0:
                self.hero_x = 'R'
            elif (self.grib_x - 75) // 225 - (self.dukky_x - 75) // 225 > 0:
                self.hero_x = 'L'
            else:
                self.hero_x = 'on_line'

            if (self.grib_y - 75) // 225 - (self.dukky_y - 75) // 225 < 0:
                self.hero_y = 'D'
            elif (self.grib_y - 75) // 225 - (self.dukky_y - 75) // 225 > 0:
                self.hero_y = 'U'
            else:
                self.hero_y = 'on_line'

            if self.hero_x == 'on_line':
                if self.hero_y == 'D':
                    for y_wall in range((self.grib_y - 75) // 225 * 2, (self.dukky_y - 75) // 225 * 2):
                        if level[y_wall][(self.grib_x - 75) // 225 * 2] in ['Y', 'y']:
                            self.between_wall = True
                            self.direction = 'D'
                            break
                    if self.between_wall is False:
                        self.direction = 'U'

                if self.hero_y == 'U':
                    for y_wall in range((self.dukky_y - 75) // 225 * 2, (self.grib_y - 75) // 225 * 2):
                        if level[y_wall][(self.grib_x - 75) // 225 * 2] in ['Y', 'y']:
                            self.between_wall = True
                            self.direction = 'U'
                            break
                    if self.between_wall is False:
                        self.direction = 'D'


            if self.hero_y == 'on_line':
                if self.hero_x == 'L':
                    for x_wall in range((self.dukky_x - 75) // 225 * 2, (self.grib_x - 75) // 225 * 2):
                        if level[(self.grib_y - 75) // 225 * 2][x_wall] in ['Y', 'y']:
                            self.between_wall = True
                            self.direction = 'L'
                            break
                    if self.between_wall is False:
                        self.direction = 'R'

                if self.hero_x == 'R':
                    for x_wall in range((self.grib_x - 75) // 225 * 2, (self.dukky_x - 75) // 225 * 2):
                        if level[(self.grib_y - 75) // 225 * 2][x_wall] in ['Y', 'y']:
                            self.between_wall = True
                            self.direction = 'R'
                            break
                    if self.between_wall is False:
                        self.direction = 'L'


            if self.between_wall is False:
                self.direction = self.runaway()
            else:
                if self.hero_x == 'R' and self.hero_y == 'on_line' and (self.dukky_x - 75) // 225 * 2 == (self.grib_x - 75) // 225 * 2 + 2 and level[(self.grib_y - 75) // 225 * 2][(self.grib_x - 75) // 225 * 2 + 1] in ['Y', 'y']:
                    self.rect.x -= 100000
                    self.sin_x -= 10000000
                    print('U were killed by CHUPRINA - right')
                    print_life(-1)
                if self.hero_x == 'L' and self.hero_y == 'on_line' and (self.dukky_x - 75) // 225 * 2 == (self.grib_x - 75) // 225 * 2 - 2 and level[(self.grib_y - 75) // 225 * 2][(self.grib_x - 75) // 225 * 2 - 1] in ['Y', 'y']:
                    self.rect.x -= 1000000
                    self.sin_x -= 1000000
                    print('U were killed by CHUPRINA - left')
                    print_life(-1)

                if self.hero_x == 'on_line' and self.hero_y == 'D' and (self.dukky_y - 75) // 225 * 2 == (self.grib_y - 75) // 225 * 2 + 2 and level[(self.grib_y - 75) // 225 * 2 + 1][(self.grib_x - 75) // 225 * 2] in ['Y', 'y']:
                    self.rect.x -= 100000
                    self.sin_x -= 1000000
                    print('U were killed by CHUPRINA - down')
                    print_life(-1)

                if self.hero_x == 'on_line' and self.hero_y == 'U' and (self.dukky_y - 75) // 225 * 2 == (self.grib_y - 75) // 225 * 2 - 2 and level[(self.grib_y - 75) // 225 * 2 - 1][(self.grib_x - 75) // 225 * 2] in ['Y', 'y']:
                    self.rect.x -= 1000000
                    self.sin_x -= 1000000
                    print('U were killed by CHUPRINA - up')
                    print_life(-1)

        if self.sin_x > 0:
            if self.direction == 'L' and (((level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 - 1] not in ['Y', 'y'] or self.x_ball != 0) and self.y_ball == 0) or ((level[(self.sin_y - 75) // 225 * 2 + int(math.copysign(1, self.y_ball))][(self.sin_x - 75) // 225 * 2 - 1] == 'p' or self.x_ball != 0) and self.y_ball != 0)):
                self.x_ball -= 1
                if self.x_ball == -15:
                    self.x_ball = 0
                    self.sin_x -= 225
                self.rect.x -= 15
            elif self.direction == 'R' and (((level[(self.sin_y - 75) // 225 * 2][(self.sin_x - 75) // 225 * 2 + 1] not in ['Y', 'y'] or self.x_ball != 0) and self.y_ball == 0) or ((level[(self.sin_y - 75) // 225 * 2 + int(math.copysign(1, self.y_ball))][(self.sin_x - 75) // 225 * 2 + 1] == 'p' or self.x_ball != 0) and self.y_ball != 0)):
                self.x_ball += 1
                if self.x_ball == 15:
                    self.x_ball = 0
                    self.sin_x += 225
                self.rect.x += 15
            elif self.direction == 'U' and (((level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y'] or self.y_ball != 0) and self.x_ball == 0) or ((level[(self.sin_y - 75) // 225 * 2 - 1][(self.sin_x - 75) // 225 * 2 + int(math.copysign(1, self.x_ball))] == 'p' or self.y_ball != 0) and self.x_ball != 0)):
                self.y_ball -= 1
                if self.y_ball == -15:
                    self.y_ball = 0
                    self.sin_y -= 225
                self.rect.y -= 15
            elif self.direction == 'D' and (((level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2] not in ['Y', 'y'] or self.y_ball != 0) and self.x_ball == 0) or ((level[(self.sin_y - 75) // 225 * 2 + 1][(self.sin_x - 75) // 225 * 2 + int(math.copysign(1, self.x_ball))] == 'p' or self.y_ball != 0) and self.x_ball != 0)):
                self.y_ball += 1
                if self.y_ball == 15:
                    self.y_ball = 0
                    self.sin_y += 225
                self.rect.y += 15



        if pygame.sprite.collide_mask(self, player):
            self.rect = self.rect.move(-1000000, -1000000)
            self.sin_x, self.sin_y = -10000000, -10000000
            print_kill(1)


def print_kill(n):
    global kills, balls_count
    kills += n
    font = pygame.font.Font(None, 100)
    string_rendered = font.render(f'Kills: {kills}/{balls_count}', 1, pygame.Color('Silver'))
    screen.blit(string_rendered, (10, 10))


def print_life(n):
    global lives
    lives += n
    font = pygame.font.Font(None, 100)
    string_rendered = font.render(f'Lives: {lives}', 1, pygame.Color('Silver'))
    screen.blit(string_rendered, (1130, 10))


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
    life_group = pygame.sprite.Group()

    for i in range(balls_count + int(balls_count * 0.5)):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        while level[y * 2][x * 2] != 'З':
            x = random.randint(0, 20)
            y = random.randint(0, 20)
        Balls(x, y)

    life_lst = []
    for i in range(balls_count // 20 * 6):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        while level[y * 2][x * 2] != 'З' and (x, y) not in life_lst:
            x = random.randint(0, 20)
            y = random.randint(0, 20)
        life_lst.append((x, y))
        Life(x, y)

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
        life_group.draw(screen)
        all_sprites.update()
        print_kill(0)
        print_life(0)
        if kills == balls_count:
            all_sprites.draw(screen)
            tiles_group.draw(screen)
            player_group.draw(screen)
            balls_group.draw(screen)
            all_sprites.update()
            pygame.display.flip()
            time.sleep(0.5)
            barboss = False

        if lives <= 0:
            barboss = False

        if camup == 1:
            camera.update(player)
            for sprite in all_sprites:
                camera.apply(sprite)
        pygame.display.flip()
        clock.tick(10)
    if kills == balls_count:
        chuprina_screen('win')
        kills = 0
    if lives == 0:
        chuprina_screen('lose')
        lives = 3

pygame.quit()