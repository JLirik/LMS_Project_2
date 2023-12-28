from PIL import Image

karta = []
f = open('data\lvl1.txt', 'w')


# rgb(200, 200, 16) - yellow


def board():
    global karta
    im = Image.open("data\level1.png")
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения
    c = 0

    for j in range(194 - 43, 2210, 100):
        karta.append([])
        karta.append([])
        for i in range(206 -  43, 2223, 100):
            r, g, b = pixels[i, j][:-1]
            # Встаём в центр клетки и смотрим цвет
            if (r, g, b) == (40, 150, 40):
                karta[c].append('З')
            # elif (r, g, b) == (200, 200, 16):
            #     karta[c].append('Ж')
            elif (r, g, b) == (147, 112, 219) or (r, g, b) == (211, 211, 211):
                karta[c].append('Ф')

            right = tuple(pixels[i + 43, j][:-1])
            down = tuple(pixels[i, j + 43][:-1])
            # if right == (40, 150, 40):
            #     karta[c].append('G')
            # elif right == (200, 200, 16):
            #     karta[c].append('Y')

            if down == (40, 150, 40):
                karta[c + 1].append('g')
            elif down == (200, 200, 16):
                karta[c + 1].append('y')
        c += 2
    return karta


a = board()
for e in a:
    f.write(''.join(e) + '\n')
print(len(a))
f.close()