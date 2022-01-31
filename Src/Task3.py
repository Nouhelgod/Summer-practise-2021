# Сурков Д. А. 8В01
# Летняя практика. Вариант 20

import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageOps


pic = plt.figure()

# 10

def task10(image):
    width, height = image.size
    img = image.load()

    block = width / 4
    for y in range(height):
        for x in range(width):            
            red = img[x, y][0]
            green = img[x, y][1]
            blue = img[x, y][2]

            gs = int(0.2125*red+0.7154*green+0.0721*blue)

            if x <= block:
                image.putpixel((x, y), (red, 0, 0))

            elif x >= block and x < block * 2:
                image.putpixel((x, y), (0, green, 0))

            elif x >= block * 2 and x < block * 3:
                image.putpixel((x, y), (0, 0, blue))

            else:
                image.putpixel((x, y), (gs, gs, gs))

    return image


# 11
    
def task11(image):
    width, height = image.size
    img = image.load()

    for y in range(height):
        for x in range(width):
            red = img[x, y][0]
            green = img[x, y][1]

            image.putpixel((x, y), (red, green, red))

    return image


# 12

def task12(image):
    width, height = image.size
    img = image.load()

    for y in range(height):
        for x in range(width):
            red = img[x, y][0]
            green = img[x, y][1]
            blue = img[x, y][2]
            gs = int(0.2125*red+0.7154*green+0.0721*blue)

            image.putpixel((x, y), (gs, gs, gs))

    return ImageOps.invert(image)


# 13

def task13(image):
    width, height = image.size
    img = image.load()

    br = int(input('Сколько добавить?\n'))
    for y in range(height):
        for x in range(width):

            red = img[x, y][0] + br
            green = img[x, y][1] + br
            blue = img[x, y][2] + br

            image.putpixel((x, y), (red, green, blue))

    return image


# 10
PIC_1 = Image.open('pic2.jpg')

ax_1_1 = pic.add_subplot(2, 4, 1)
ax_1_1.imshow(PIC_1)

ax_1_2 = pic.add_subplot(2, 4, 2)
ax_1_2.imshow(task10(PIC_1))

# 11
PIC_2 = Image.open('pic3.jpg')

ax_2_1 = pic.add_subplot(2, 4, 3)
ax_2_1.imshow(PIC_2)

ax_2_2 = pic.add_subplot(2, 4, 4)
ax_2_2.imshow(task11(PIC_2))

# 12
PIC_3 = Image.open('pic4.jpg')

ax_3_1 = pic.add_subplot(2, 4, 5)
ax_3_1.imshow(PIC_3)

ax_3_2 = pic.add_subplot(2, 4, 6)
ax_3_2.imshow(task12(PIC_3))

# 13
PIC_4 = Image.open('pic5.jpg')

ax_4_1 = pic.add_subplot(2, 4, 7)
ax_4_1.imshow(PIC_4)

ax_4_2 = pic.add_subplot(2, 4, 8)
ax_4_2.imshow(task13(PIC_4))

plt.show()