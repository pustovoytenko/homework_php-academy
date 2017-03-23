class Animal:
    __age = 0

    def __init__(self, name):
        self.__age = 2
        self.name = name

    def voice(self):
        raise NotImplementedError("Can't find that method")


class Cats(Animal):

    def voice(self):
        return "Meow"

    def get_age(self):
        self.__age = 3
        return "{} {} year(s) old.".format(self.name, self.__age)


class Dogs(Animal):

    def get_age(self):
        self.__age = 4
        return "{} {} year(s) old.".format(self.name, self.__age)

cat = Cats("Kot")
dog = Dogs("Pesik")

try:
    print(cat.__age)
    print(dog.__age)
except AttributeError:
    print("Class has no such attribute or method")

print(cat.get_age())
print(dog.get_age())

cat.__age = 10
print(cat.__age)
print(cat.get_age())

dog.__age = 10
print(dog.__age)
print(dog.get_age())

print(cat.voice())
print(dog.voice())
