import numpy
import seaborn
import matplotlib.pyplot as plt

# создаем колодцы, куда будут падать шарики после прохождения препятствий
a = {-5:0, -4:0, -3:0, -2:0, -1:0, 0:0, +1:0, +2:0, +3:0, +4:0, +5:0}

# кидаем 100 шариков
for i in range(100):
    # первоначально шарик летит по центру
    x = 0
    # первое препятствие - шарик отскочит либо налево (-1), либо направо (+1)
    # random.choice в numpy с равной вероятностью выдает один из элементов массива
    x += numpy.random.choice([-1, 1])
    # второй ряд препятствий - шарик полетит либо в центр, либо еще дальше от центра
    x += numpy.random.choice([-1, 1])
    # Добавим еще 2 уровня
    x += numpy.random.choice([-1, 1])
    # x += numpy.random.choice([-1, 1])
    # приземляем шарик к колодец, в зависимости от того, куда она отскочил
    a[x] += 1

    print(x)
    print(a[x])

seaborn.set()
# по х - покажем индексы наших колодцев,
# по оси y - сколько шариков в них оказалось
seaborn.barplot(x=list(a.keys()), y=list(a.values()))

plt.show()