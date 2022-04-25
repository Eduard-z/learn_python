class Website:
    def __init__(self,title):
        self.title = title

        self.notification()

    def showTitle(self):
        print(self.title)

    def notification(self):
    	print('object created')

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    @staticmethod
    def static_method():
    	print('static')

obj = Website('pythonbasics.org')
obj.showTitle()
obj.set_name('py site')
print(obj.name)

Website.static_method()

d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 }
iterable = d.keys()
iterator = iter(iterable)
print( next(iterator) )
print( next(iterator) )

print(iterable)
print(type(iterable))

print(iterator)
print(type(iterator))


class Fruit:
    name = 'Fruitas'

    @classmethod
    def printName(cls):
        print('The name is:', cls.name)

Fruit.printName()
apple = Fruit()
apple.printName()
berry = Fruit()
berry.printName()
