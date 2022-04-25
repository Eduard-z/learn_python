get_cube = lambda x : x ** 3
print(get_cube(4))

# Пример лямбда-функции, не возвращающей значение:
welcome = lambda username: print('Welcome, ' + username + '!')
welcome('Anon')

# Пример лямбда-функции с тремя параметрами:
get_prod = lambda a, b, c : a * b * c
print(get_prod(3, 5, 7))

# Ниже приведен пример лямбда-функции без параметров.
welcome = lambda : print('Welcome!')
welcome()

# Пример анонимной лямбда-функции:
print((lambda x: x**3)(10))


# Пример передачи лямбда-функции в качестве параметра:
def run_task(task):
    print('Before running the task')
    task()
    print('After running the task')


run_task(lambda : print('Task is complete!'))  # передача анонимной функции
important_task = lambda: print('Important task is complete!') 
run_task(important_task)  # передача лямбда-функции

# Пример передачи лямбда-функции в map():
prime_cube_list = map(lambda x: x**3, [2, 3, 5, 7, 11])  # передача анонимной функции
print(prime_cube_list)
print(next(prime_cube_list))
print(next(prime_cube_list))
print(next(prime_cube_list))
print(next(prime_cube_list))
