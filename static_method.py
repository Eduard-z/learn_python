class Methods:
    def imeth(self, x):                     # Обычный метод экземпляра
        print(self, x)

    def smeth(x):                           # Статический метод: экземпляр не передается
        print(x)

    def cmeth(cls, x):                      # Метод класса: получает класс, но не экземпляр
        print(cls, x)

    smeth = staticmethod(smeth)             # Сделать smeth статическим методом
    cmeth = classmethod(cmeth)              # Сделать cmeth методом класса.

Methods.smeth(3)                            # Вызов статического метода, через имя класса
obj = Methods()                             # Создать экземпляр
obj.smeth(4)                                # Вызов статического метода, через экземпляр

Methods.cmeth(5)                            # Вызов метода класса, через имя класса
obj.cmeth(6)                                # Вызов метода класса, через экземпляр
