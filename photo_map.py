# from PIL import Image, ImageDraw
#
# karta = []
# f = open('data\lvl1.txt', 'w')
#
#
# # Free cells - rgb(40, 150, 40) - '='
# # Walls ---- rgb(200, 200, 16) - '#'
# # Another walls - rgb(255, 255, 0)
# # Wall cells - rgb(147, 112, 219) - '~'
# # Beween cells - rgb(255, 0, 127) - '|'
#
#
# def board():
#     global karta
#     im = Image.open("data\level1_1.png")
#     pixels = im.load()  # список с пикселями
#     x, y = im.size  # ширина (x) и высота (y) изображения
#     symb = ''
#     b = 0
#     c = 0
#
#     for j in range(0, y, 1):
#         karta.append([])
#         h = 0
#         for i in range(0, x, 1):
#             r, g, b = pixels[i, j][:-1]
#             if r == 40 and g == 150 and b == 40:
#                 symb = '='
#             elif r == 255 and g == 255 and b == 0:
#                 symb = '#'
#             elif r == 255 and g == 0 and b ==127:
#                 symb = '|'
#             elif r == 147 and g == 112 and b == 219:
#                 symb = '~'
#             else:
#                 symb = '~'
#             # karta[c].append(symb)
#             if h != 0:
#                 if karta[c][h - 1] != symb:
#                     karta[c].append(symb)
#                     h += 1
#             else:
#                 karta[c].append(symb)
#                 h += 1
#         c += 1
#     return karta
#
#
# a = board()
# # a = a[92:2210]
# for e in a:
#     # e = e[105:-95]
#     e = (''.join(e)).split('|')
#     if len(e) > 0:
#         f.write(''.join(e) + '\n')
# print(len(a))
# f.close()

from PIL import Image, ImageDraw

karta = []
f = open('data\lvl1.txt', 'w')


# Free cells - rgb(40, 150, 40) - '='
# Walls - rgb(200, 200, 16) - '#'
# Wall cells - rgb(147, 112, 219) - '~'


def board():
    global karta
    im = Image.open("data\level1.png")
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    c = 0

    for j in range(0, y, 10):
        karta.append([])
        for i in range(0, x, 9):
            r, g, b = pixels[i, j][:-1]
            if r == 40 and g == 150 and b == 40:
                karta[c].append('=')
            elif r == 200 and g == 200 and b == 16:
                karta[c].append('#')
            elif r == 147 and g == 112 and b == 219:
                karta[c].append('~')
            else:
                karta[c].append('~')
        c += 1
    return karta


a = board()
a = a[10:221]
for e in a:
    e = e[12:-11]
    f.write(''.join(e) + '\n')
print(len(a))
f.close()

