def fibonacci():
    prev, cur = 0, 1
    while True:
        yield prev
        prev, cur = cur, prev + cur


for num, fib in enumerate(fibonacci()):
    print('{0}: {1}'.format(num, fib))
    if num > 9:
        break
