import os

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

directory = os.path.dirname(__file__)

PIC = os.path.join(directory, 'pic1.jpg')
TEXT = u'Кто пёс?\nЯ пёс?\nА может ты пёс?'


with cbook.get_sample_data(PIC) as image_file:
    image = plt.imread(image_file)

fig = plt.figure()

ax_1 = fig.add_subplot(2, 3, 5)

ax_1.imshow(image)
ax_1.text(300, 50, TEXT, size='x-large')

fig.set_figwidth(7)
fig.set_figheight(7)

plt.show()