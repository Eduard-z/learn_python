
def error_handler(func):
    def wrapper(*args, **kwargs):
        ret = 0
        try:
            ret = func(*args, **kwargs)
        except:
            print('>> Ошибка в функции', func.__name__)
        return ret
    return wrapper


@error_handler
def div(a, b):
    return a / b


if __name__ == '__main__':
    print('старт')
    print(div(10, 2))
    print(div(10, 0))
    print('конец')
