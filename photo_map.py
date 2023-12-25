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

    for j in range(0, y, 1):
        karta.append([])
        for i in range(0, x, 1):
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
for e in a:
    print(e)
    f.write(''.join(e) + '\n')
print(len(a))
f.close()
