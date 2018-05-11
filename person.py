from classtools import AttrDisplay              # Импортирует обобщенный инструмент


class Person(AttrDisplay):
    """
    Создает и обрабатывает записи с информацией о людях
    """
    def __init__(self, name, job=None, pay=0):  # Конструктор принимает 3 аргумента
        self.name = name                        # Заполняет поля при создании
        self.job = job                          # self – новый экземпляр класса
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]            # self – подразумеваемый экземпляр
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    # def __str__(self):                        # AttrDisplay извлекает имя класса непосредственно из экземпляра
    #     return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):                          # Наследует атрибута класса Person
    """
    Версия класса Person, адаптированная в соответствии
    со специальными требованиями
    """
    def __init__(self, name, pay):              # Переопределенный конструктор
        Person.__init__(self, name, 'mgr', pay)

    def giveRaise(self, percent, bonus=.10):    # Переопределить для адаптации
        # self.pay = int(self.pay * (1 + percent + bonus))  # Неправильно: копирование
        Person.giveRaise(self, percent+bonus)   # Правильно: дополняет оригинал

if __name__ == '__main__':                      # Только когда файл запускается для тестирования
    # реализация самотестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)

    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob)
    print(sue)

    print(bob.name.split()[-1])                 # Извлечь фамилию
    print(bob.lastName(), sue.lastName())

    sue.pay *= 1.10                             # Повысить зарплату
    print(sue.pay)
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)

    tom = Manager('Tom Jones', 50000)           # Экземпляр Manager: __init__
    tom.giveRaise(.10)                          # Вызов адаптированной версии
    print(tom.lastName())                       # Вызов унаследованного метода
    print(tom)                                  # Вызов унаследованного __str__

    print('--All three--')
    for object in (bob, sue, tom):              # Обработка объектов обобщенным способом
        object.giveRaise(.10)                   # Вызовет метод giveRaise этого объекта
        print(object)                           # Вызовет общий метод __str__
