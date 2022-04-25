# -*- coding: utf-8 -*-

class DecoratorTest(object):
    """
    Тестируем обычный метод против @classmethod против @staticmethod
    """
    def __init__(self):
        """Конструктор"""
        pass
    
    def doubler(self, x):
        print("умножаем на 2")
        return x*2

    @classmethod
    def class_tripler(klass, x):
        print("умножаем на 3: %s" % klass)
        return x*3
    
    @staticmethod
    def static_quad(x):
        print("умножаем на 4")
        return x*4


if __name__ == "__main__":
    decor = DecoratorTest()
    print(decor.doubler(5))
    print(decor.class_tripler(3))
    print(DecoratorTest.class_tripler(3))
    print(decor.static_quad(3))
    print(DecoratorTest.static_quad(2))
    # print(DecoratorTest.doubler(2))  # TypeError: DecoratorTest.doubler() missing 1 required positional argument: 'x'

    print(decor.doubler)  # <bound method DecoratorTest.doubler of <__main__.DecoratorTest object at 0x000002761F76BA60>>
    print(decor.class_tripler)  # <bound method DecoratorTest.class_tripler of <class '__main__.DecoratorTest'>>
    print(decor.static_quad)  # <function DecoratorTest.static_quad at 0x000002761F7835B0>
                              # возвращает обычную функцию вместо связанного метода
