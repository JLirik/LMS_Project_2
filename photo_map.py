from PIL import Image, ImageDraw

karta = [[]]


def board(num, size):
    im = Image.open("image.jpg")
    pixels = im.load()  # список с пикселями
    x, y = im.size  # ширина (x) и высота (y) изображения

    for j in range(0, y, 5):
        for i in range(0, x, 5):
            r, g, b = pixels[i, j]
            if r == 0 and g == 0 and b == 0:
                karta[j].append('#')
            else:
                karta[j].append('=')

