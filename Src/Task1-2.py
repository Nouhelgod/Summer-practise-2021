# Сурков Д. А. 8В01
# Летняя практика. Вариант 20

import os
import math

import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import numpy as np

directory = os.path.dirname(__file__)

pic = plt.figure()
# 1
PIC = os.path.join(directory, 'pic1.jpg')

with cbook.get_sample_data(PIC) as image_file:
    image = plt.imread(image_file)


ax_1 = pic.add_subplot(2, 3, 1)
ax_1.imshow(image)
ax_1.text(300, 50, 'Пёс', size='x-large')
pic.set_figwidth(7)
pic.set_figheight(7)


# 2
data=[]
with open('task1.txt') as file:
    for line in file:
        data.append([float(x) for x in line.split()])

x1, y1, x2, y2, i = [], [], [], [], 0
while i < 27:
    if data[19][i] < 0:
        x1.append(data[0][i])
        y1.append(data[19][i])
            
    else:
        x2.append(data[0][i])
        y2.append(data[19][i])

    i += 1;    

ax_2 = pic.add_subplot(2, 3, 2)
ax_2.fill_between(x1, y1, color = (0.2, 0.4, 0.6, 0.5))
ax_2.fill_between(x2, y2, color = (0.2, 0.8, 0.4, 0.5))
ax_2.grid(True)

ax_2.set_title('Вариант №20', fontsize=16, fontweight='light', style='italic', font='Times New Roman')
ax_2.set_xlabel('t, c')
ax_2.set_ylabel('T, K')
plt.xticks(rotation=45, fontsize=15, font='Arial')
plt.yticks(rotation=45, fontsize=15, font='Arial')

# 3
data=[]
with open('task2.txt') as file:
    for line in file:
        data.append([x for x in line.split()])

x = np.arange(int(data[38][0]), int(data[38][1] ) + 1)
y = [int(i) for i in data[39]]

ax_3 = pic.add_subplot(2, 3, 3)
ax_3.bar(x, y, color='black')

arrowprops = {'arrowstyle': '->',
              'color': 'green',}

selected_x, selected_y = 501, 11
ax_3.annotate(u'Тут', xy=(selected_x, selected_y), 
    xytext = (selected_x - 0.5, selected_y + 2), 
    arrowprops = arrowprops, 
    color='green', 
    font='Comic Sans MS', 
    size=15, 
    fontweight='bold',
    alpha =0.3)


# 4
y1, y2 = 0, 0
k = np.poly([-1.8, -1, -0.13, 0.5, 1.9])
x = np.linspace(0, 2, 40)
y1 = np.sin(4 * x) - np.cos(6 * x) ** 2
y2 = 0.12*(k[0] * (x**4) + k[1] * (x**3) + k[2] * (x**2) + k[3] * x + k[4])

ax_4 = pic.add_subplot(2, 3, 4)
ax_4.plot(x, y1, linestyle='dashdot', label='y1', color='red')
ax_4.plot(x, y2, linestyle='dotted', label='y2', color='black')
leg = ax_4.legend(loc = 'lower right')
plt.setp(leg.texts, fontname='Courier', 
        color='darkgray', 
        fontsize=16, 
        fontweight='light')
plt.xticks(rotation=15)
plt.yticks(rotation=15)


# 5 
N = 300
alpha = 5.2

x = np.random.rand(N)
y = np.random.pareto(alpha, size=N)

ax_5 = pic.add_subplot(2, 3, 5)
ax_5.scatter(x-1, y, color='orange', s=4)

y = np.random.uniform(low=-5, high=5, size=N)
ax_5.scatter(x, y, color=(0.0, 1.0, 0.0), s=3)

y = np.random.gamma(shape=2, scale=1.5, size=N)
ax_5.scatter(x+1, y, color='#add8e6', s=2)
ax_5.set_facecolor('black')


# 6
A, B, a, b, sigma = 10, 7.5, 3, 7.5, np.pi/4
t = np.linspace(0, np.pi * 4, 2000)
x = A * np.sin(a * t + sigma)
y = B * np.sin(b * t)


ax_6 = pic.add_subplot(2, 3, 6)
ax_6.fill_between(x, y, color = (0.8, 0.4, 0.9, 0.7))
ax_6.plot(x, y, color=(0.8, 0.4, 0.9, 1.0))
plt.grid(True, color='gray')

plt.show()