def benchmark(iters):
    def actual_decorator(func):
        '''декоратор, который принимает аргументы'''
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total/iters))
            return return_value

        return wrapper
    return actual_decorator


@benchmark(iters=3)  # тут вызывается функция benchmark()
def fetch_webpage(url):
    import requests
    webpage = requests.get(url)
    return webpage.status_code


if __name__ == '__main__':
    goog_req = fetch_webpage('https://google.com')
    print(goog_req)
