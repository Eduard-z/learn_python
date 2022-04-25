# -*- coding: utf-8 -*-
import logging


def log_dec(func):
    """
    Логируем какая функция вызывается
    """
    
    def wrap_log(*args, **kwargs):
        name = func.__name__
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
    
        # Открываем файл логов для записи.
        fh = logging.FileHandler(f"{name}.log_dec")
        fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(fmt)
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        
        logger.info("Call function: %s" % name)
        result = func(*args, **kwargs)
        logger.info("Result: %s" % result)
        return func
    
    return wrap_log


@log_dec
def double_function(a):
    """
    Умножаем полученный параметр.
    """
    return a*2


if __name__ == "__main__":
    value = double_function(3)
