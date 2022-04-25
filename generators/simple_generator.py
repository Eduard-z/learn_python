# Простая программа на Python для демонстрации
# работы yield
  
# Функция-генератор, которая выдает 2 при
# первом обращении, 4 — при втором и
# 8 — при третьем
def simple_generator():
    yield 2
    yield 4
    yield 8
  
  
# Код для проверки simple_generator()
for value in simple_generator(): 
    print(value)
