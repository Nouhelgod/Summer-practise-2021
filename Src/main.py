import os

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

directory = os.path.dirname(__file__)
pic = os.path.join(directory, 'pic1.jpg')


with cbook.get_sample_data(pic) as image_file:
    image = plt.imread(image_file)

fig, ax = plt.subplots()

ax.imshow(image)
ax.text(300, 50, u'Кто пёс?\nЯ пёс?\nА может ты пёс?', size='x-large')

fig.set_figwidth(7)
fig.set_figheight(7)

plt.show()