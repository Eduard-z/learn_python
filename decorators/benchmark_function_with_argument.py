def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло
    выполнение декорируемой функции.

    аргументы декорируемой функции передаются функции-обёртке"""
    import time

    def wrapper(*args, **kwargs):
        start = time.time()
        return_value = func(*args, **kwargs)
        end = time.time()
        print('[*] Время выполнения: {} секунд.'.format(end-start))
        return return_value
    return wrapper


@benchmark
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.status_code


if __name__ == '__main__':
    goog_req = fetch_webpage('https://google.com')
    print(goog_req)
