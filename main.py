import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5, 5, 40)             # от 0.05 до 1 сделать 100 точек
y1 = (np.sin(x))**5+(np.cos(x))**5  # первая функция
fig, ab = plt.subplots()                 # создаем полотно
ab.plot(x, y1, color="blue", label="y1)")      # функция y1(x), синий, надпись y1(x)
ab.set_xlabel("x")                       # подпись у горизонтальной оси х
ab.set_ylabel("y")                       # подпись у вертикальной оси y
ab.legend()                              # показывать условные обозначения
plt.show()                               # показать рисунок
fig.savefig('1.png')                     # сохранить в файл 1.png
